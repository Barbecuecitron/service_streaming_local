from flask import Flask, render_template, send_from_directory
from config.config import Config
from utils.thumbnail_generator import build_video_previews
from utils.folder_utility import get_video_filenames

app = Flask(__name__, static_folder="static")
app.config.from_object(Config)

@app.route("/")
def home():
    # Get a list of files in the VIDEO_FOLDER directory
    videos_filenames = get_video_filenames(Config.VIDEO_FOLDER)
    thumbnail_folder = "static"
    videos = build_video_previews(videos_filenames, Config.VIDEO_FOLDER, thumbnail_folder)
    return render_template("video_list.html", videos=videos)

@app.route("/play/<video_url>")
def play_video(video_url=None):
    if video_url is None:
        return render_template("video_list.html")
    else:
        return render_template("video_player.html", video_url=video_url)

@app.route("/list")
def list_videos():
    return render_template("video_list.html")

@app.route('/image/<path:filename>')
def serve_image(filename):
    root_dir = "static"
    return send_from_directory(root_dir, filename)

@app.route("/<path:filename>")
def serve_video(filename):
    root_dir = Config.VIDEO_FOLDER
    return send_from_directory(root_dir, filename)

if __name__ == "__main__":
    app.run(debug=True)
