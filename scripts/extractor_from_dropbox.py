import cv2
import multiprocessing as mp
from concurrent.futures import ProcessPoolExecutor
from typing import List
import os
from time import perf_counter
from itertools import islice
from functools import partial

DATA_DUMP_PATH = '/home/darshan/Dropbox/neeroxdrive/nx-datasets/nx-ds-liquor/dumps/videos/'
# DTA_RAW_PATH = '/home/darshan/Documents/anyproimage/liquid'

# - get list of files in a directory
# - get image frames from the video file

# %%


def get_filepaths(dir: str) -> List[str]:
    """Returns a list of filepaths in a directory"""
    for root, dirs, files in os.walk(dir):
        for file in files:
            filepath = os.path.join(root, file)
            yield filepath


# %%
data_dump_filepaths: List[str] = get_filepaths(DATA_DUMP_PATH)

# %%


def get_iframes(filepath: str, frame_size: int) -> List[bytes]:
    """Returns a list of frames from a file"""
    with open(filepath, 'rb') as f:
        while True:
            frame = f.read(frame_size)
            if not frame:
                break
            yield frame

# %%


def get_frames(filepath: str, frame_size: int) -> List[bytes]:
    frames = get_iframes(filepath, frame_size)
    return [*frames]


get_frames_partial = partial(get_frames, frame_size=30*15*500)
# with ProcessPoolExecutor() as executor:
images = mp.Pool().imap(get_frames_partial, data_dump_filepaths)
# print("22")
# print(images)

sample = islice(images, 1)
# print("33333")
# print(sample)


def get_images(video_filepath: str):

    suffix = video_filepath.split('.')[-2]
    # Open the video file
    video = cv2.VideoCapture(video_filepath)

    # Get the total number of frames in the video
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    # Loop over each frame and save it as an image
    for i in range(total_frames):
        # Read the next frame
        ret, frame = video.read()

        # Break the loop if the video has ended
        if not ret:
            break

        # Save the frame as an image
        cv2.imwrite(f'/home/darshan/Documents/anyproimage/acheck/img{suffix}_frame_{i}.jpg', frame)

    # Release the video capture object
    video.release()
    return total_frames



if __name__ == '__main__':
    start = perf_counter()
    with ProcessPoolExecutor() as executor:
        total = executor.map(get_images, get_filepaths(DATA_DUMP_PATH))
        print(*total)

    print(f'Finished in {perf_counter() - start} seconds')
