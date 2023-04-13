from utils import os

def get_video_filenames(video_folder):
    videos_filenames = [x for x in os.listdir(video_folder) if x.endswith(".mp4")]
    return videos_filenames