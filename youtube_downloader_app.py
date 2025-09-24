from flask import Flask, request, render_template, send_from_directory, jsonify, url_for
import os, threading, uuid
import yt_dlp

app = Flask(__name__, static_folder="static")
DOWNLOAD_FOLDER = "downloads"

if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

progress_data = {}

def progress_hook(d, task_id):
    if d['status'] == 'downloading':
        total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate')
        downloaded_bytes = d.get('downloaded_bytes', 0)
        if total_bytes:
            progress_data[task_id]['progress'] = int(downloaded_bytes / total_bytes * 100)
        else:
            progress_data[task_id]['progress'] = 0
    elif d['status'] == 'finished':
        progress_data[task_id]['progress'] = 100
        progress_data[task_id]['status'] = 'finished'
        filename = f"{d['filename'].split(os.sep)[-1]}"
        progress_data[task_id]['files'] = [filename]

def download_video(url, ydl_opts, task_id):
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        progress_data[task_id]['status'] = 'finished'
    except Exception as e:
        progress_data[task_id]['status'] = 'error'
        progress_data[task_id]['error'] = str(e)

def get_video_info(url):
    ydl_opts = {'quiet': True, 'skip_download': True}
    info = {}
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            if 'entries' in info:
                info = info['entries'][0]
    except Exception as e:
        print("Error fetching video info:", e)
    return info

@app.route("/", methods=["GET", "POST"])
def index():
    task_id = None
    video_info = None
    show_options = True

    if request.method == "POST":
        url = request.form.get("url")
        media_type = request.form.get("media_type")  # 'video' or 'audio'

        task_id = str(uuid.uuid4())
        progress_data[task_id] = {'status': 'starting', 'progress': 0, 'files': []}

        video_info = get_video_info(url)
        is_360 = video_info.get('is_360') if video_info else False
        formats = video_info.get('formats') if video_info else []

        # Select best quality automatically
        best_format = None
        if media_type == 'video':
            video_formats = [f for f in formats if f.get('vcodec') != 'none']
            if video_formats:
                best_format = sorted(video_formats, key=lambda x: int(x.get('height') or 0), reverse=True)[0]['format_id']
        else:  # audio
            audio_formats = [f for f in formats if f.get('acodec') != 'none' and f.get('vcodec') == 'none']
            if audio_formats:
                best_format = sorted(audio_formats, key=lambda x: int(x.get('abr') or 0), reverse=True)[0]['format_id']

        ydl_opts = {
            'format': best_format or 'best',
            'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',
            'progress_hooks': [lambda d: progress_hook(d, task_id)]
        }

        if media_type == 'audio':
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]

        threading.Thread(target=download_video, args=(url, ydl_opts, task_id)).start()
        show_options = False  # hide options once download starts

    return render_template("index.html", task_id=task_id, show_options=show_options, video_info=video_info)

@app.route("/progress/<task_id>")
def get_progress(task_id):
    task = progress_data.get(task_id, {'status':'notfound', 'progress':0, 'files':[]})
    if task.get('status') == 'finished' and task.get('files'):
        task['url'] = url_for('download_file', filename=task['files'][0])
    return jsonify(task)

@app.route("/downloads/<path:filename>")
def download_file(filename):
    return send_from_directory(DOWNLOAD_FOLDER, filename, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
