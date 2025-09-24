✨ Features
- 🎥 Download videos in **4K and 8K** quality  
- 🎵 **Audio-only mode** for MP3 extraction  
- 🌀 **360° video detection** and support  
- ⚡ Clean, **snappy**, and modern UI  
- 📊 Real-time progress updates  
- ⬇ **Automatic browser download** when complete  
- 🖱 One-click simplicity — paste URL and go!

📂 Folder Structure


youtube-hd-downloader/
│
├── templates/
│ └── index.html # Main UI
│
├── downloads/ # Where downloads are saved
│
├── youtube_downloader_app.py # Flask backend
│
├── requirements.txt # Dependencies
│
└── Procfile # For free hosting

🚀 Setup Instructions

1. Clone the project
```bash
git clone https://github.com/your-username/youtube-hd-downloader.git
cd youtube-hd-downloader

2. Create a virtual environment
python -m venv venv
# macOS/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

🛠 Requirements

Your requirements.txt should include:

Flask
yt-dlp


Also install FFmpeg:

Download FFmpeg

Verify installation:

ffmpeg -version

▶ Running the App
python youtube_downloader_app.py


Open in your browser:

http://127.0.0.1:5000

🌍 Free Hosting on Render

Push the project to GitHub.

Create an account at Render
.

Select New → Web Service → Connect to GitHub Repo.

Use these settings:

Build Command:

pip install -r requirements.txt

Start Command:

python youtube_downloader_app.py

Deploy and get a free public URL.

💻 Tech Stack
Tech	Use Case
Flask	Backend framework
yt-dlp	Download engine
TailwindCSS	Modern UI styling
FFmpeg	Video & audio merging
⚡ Git Commands
git add .
git commit -m "feat: first release with HD download support"
git push origin main

📜 License
Licensed under the MIT License — free to use and modify.
💡 Credits
Written by Robust
 ❤️
