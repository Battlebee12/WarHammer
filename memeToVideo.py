from moviepy.editor import *
import os

folder_path = "C:\\Users\\sarab\\OneDrive\\Documents\\GitHub\\WarHammer\\automated videos"

video_clips = []

for file in os.listdir(folder_path):
    if file.endswith(".png") or file.endswith(".jpg"):
        # Construct the full path to the image file
        image_path = os.path.join(folder_path, file)

        # Load the image
        image = ImageClip(image_path, duration=4)

        # Create a unique output video path based on the image file name
        output_video_path = os.path.splitext(file)[0] + '.mp4'

        # Write the video
        image.write_videofile(output_video_path, fps=24)
        
        # Append the video clip to the list
        video_clips.append(VideoFileClip(output_video_path))

# Concatenate all video clips into a single video
final_video = concatenate_videoclips(video_clips, method="compose")

# Export the final video
final_video.write_videofile("final_output.mp4", fps=24)

# very cool


