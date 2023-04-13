from utils import Image, VideoFileClip, os

def build_video_previews(video_filenames, video_folder, thumbnail_folder):
    # Load the video file
    videos_and_previews = []

    for video_name in video_filenames:
        img_output_path = f"static/{video_name}".replace("mp4", "jpg")
        vignette_name = video_name.replace("mp4", "jpg")

        if vignette_name in os.listdir(thumbnail_folder):
            print(f"The file {vignette_name} exists in {thumbnail_folder}")
            print(f"Its full path is {img_output_path}")
            video_plus_thumb = {
            "name": video_name,
            "preview": vignette_name
            }
            videos_and_previews.append(video_plus_thumb)
        else:
            print(f"The file {vignette_name} does not exist in {thumbnail_folder}")

            clips = VideoFileClip(os.path.join(video_folder, video_name))
            duration = clips.duration # seconds

            max_duration = int(duration)+1

            i = max_duration//10  # 1 / 10th of the video

            frame = clips.get_frame(i)

            new_img_file = os.path.join(thumbnail_folder, vignette_name)

            new_img = Image.fromarray(frame)
            new_img.save(new_img_file)

            video_plus_thumb = {
                "name": video_name,
                "preview": vignette_name
            }
            videos_and_previews.append(video_plus_thumb)
    return videos_and_previews