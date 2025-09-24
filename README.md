YouTube HD Downloader

🚀 A modern, snappy web app for downloading high-quality YouTube videos (up to 8K), audio-only tracks, and even 360° videos — built with Flask, yt-dlp, and a sleek Tailwind CSS frontend.

✨ Features

High-Resolution Video Downloads – Supports 4K and 8K

Audio-Only Mode – Extract the best available audio in MP3 format

360° Video Detection – Automatically detects and labels 360° videos

Clean UI/UX – Minimalist, modern, and mobile-friendly design

Progress Tracking – Real-time progress bar with percentage updates

Auto-Download on Completion – Browser automatically downloads when ready

One-Click Simplicity – Just paste the URL and hit download

Snappy Flow – Options disappear when downloading to keep UI clean

📂 Project Structure
youtube-hd-downloader/
│
├── templates/                  # HTML templates
│   └── index.html               # Main UI template
│
├── static/                      # (Optional) Static files like CSS/JS
│
├── downloads/                   # Saved videos/audio
│
├── youtube_downloader_app.py    # Main Flask application
│
├── requirements.txt             # Python dependencies
│
└── Procfile                      # For cloud deployment

🚀 Getting Started

Follow these steps to run the app locally:

1. Clone the Repository
git clone https://github.com/your-username/youtube-hd-downloader.git
cd youtube-hd-downloader

2. Create Virtual Environment
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

3. Install Dependencies
pip install -r requirements.txt

🛠 Requirements

Your requirements.txt should include:

Flask
yt-dlp


Additionally, make sure FFmpeg is installed:

Download FFmpeg

Verify installation:

ffmpeg -version

▶ Running the App

Start the Flask server:

python youtube_downloader_app.py


Open your browser and navigate to:

http://127.0.0.1:5000

🌍 Public Hosting
Option 1: Render (Recommended)

Push this repo to GitHub.

Create a free Render
 account.

New → Web Service → Connect GitHub repo.

Use these settings:

Build Command:

pip install -r requirements.txt


Start Command:

python youtube_downloader_app.py


Deploy → Get a free public URL!

💻 Technologies Used
Tech	Purpose
Flask	Backend web framework
yt-dlp	YouTube downloading engine
Tailwind CSS	Modern, responsive styling
Alpine.js	Lightweight interactivity
FFmpeg	Media processing & merging
📸 Features in Action
High-Quality Video Downloads

Easily grab 4K/8K YouTube videos with a single click.

Audio-Only Downloads

Extract clean MP3 audio files from any video.

Real-Time Progress

Track download progress with a modern progress bar.

🤝 Contributing

Contributions are welcome!
To get started:

Fork the repo

Create a feature branch (git checkout -b feature/amazing-feature)

Commit changes (git commit -m 'Add amazing feature')

Push to branch (git push origin feature/amazing-feature)

Open a Pull Request

⚡ Quick Git Commands
git add .
git commit -m "feat: initial version with high-quality downloads and modern UI"
git push origin main

📜 License

This project is licensed under the MIT License.
Feel free to use and modify for personal or commercial projects.

💡 Credits

Written by Robust
 ❤️
Powered by yt-dlp, Flask, and open-source technologies.
