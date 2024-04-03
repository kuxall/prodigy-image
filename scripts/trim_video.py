from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
video = VideoFileClip("D:/liquor/videos/strawberry_lemonade.avi")
start_time = 3
# end_time = 46
# ffmpeg_extract_subclip("C:/Users/Admin/OneDrive/Documents/Image_annotation/25data/Black_cherry.avi", start_time, end_time, targetname="C:/Users/Admin/OneDrive/Documents/changed.avi")
trimmed_video = video.subclip(start_time)
trimmed_video.write_videofile("D:/liquor/videos/strawberry_lemonade(trimmed).avi",codec='libx264')
