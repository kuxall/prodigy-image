import cv2
import os
from time import perf_counter


def get_mainfolder(main_folder):
    for sub_folder in os.listdir(main_folder):
        sub_folder_path = os.path.join(main_folder, sub_folder)
        if os.path.isdir(sub_folder_path):
            print(sub_folder_path)
            # Loop over all MP4 files within the sub-folder
            for video_file in os.listdir(sub_folder_path):
                if video_file.endswith(".avi"):
                    # Load the video
                    video = cv2.VideoCapture(os.path.join(sub_folder_path, video_file))

                    # Get the number of frames in the video
                    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

                    output_folder = os.path.join("liquidframe", sub_folder)
                    if not os.path.exists(output_folder):
                        os.makedirs(output_folder) 

                    # Set the starting frame number
                    current_frame = 0
                    
                    while True:
                        # Read the next frame
                        ret, frame = video.read()

                        # Break the loop if we've reached the end of the video
                        if not ret:
                            break

                        # Save the current frame as a JPG image
                        cv2.imwrite(os.path.join(output_folder, "frame_{}.jpg".format(current_frame)), frame)

                        # Increment the frame number
                        current_frame += 1

                    # Release the video capture object
                video.release()
                    



if __name__ == '__main__':
    start = perf_counter()
    mainfolder = "/home/darshan/Documents/anyproimage/videos"
    extract = get_mainfolder(mainfolder)
    print(f'Finished in {perf_counter() - start} seconds')
