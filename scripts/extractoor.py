import os
import sys
import cv2
import argparse



parser = argparse.ArgumentParser(description="Script to extract frames from video.")

# Add arguments
parser.add_argument('-f','--file_name', type=str, required=True, help = "file name of the video.")
parser.add_argument('-i','--info', action='store_true',help = "display the number of frames, height, width and fps information of given file")
parser.add_argument('-s','--save_images', type=str, required=True,help = "location to save the extracted images")

# Parse the argument
args = parser.parse_args()

#display formatting
cstr = "#"
info = "Information"

#read video file
cap = cv2.VideoCapture(args.file_name)

length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH )
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT )
fps =  cap.get(cv2.CAP_PROP_FPS)

frame_skip = 0

#print information related to the video
if args.info:
    print (info.center(40, '#'))
    print( "Number of frames:",length )
    print("width:",width,"\nheight:",height,"\nfps:",fps)
    print (cstr.ljust(40, '#'))

outdir = args.save_images

def write():
    global frame_skip
    frame_count = 0
    i = 1
    filename = ""
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("{} images has been written".format(frame_count))
            break
        if i % frame_skip == 0:
            frame_count += 1
            filename = outdir + '/%d.jpg' % frame_count
            cv2.imwrite(filename, frame)
        i += 1    
    print("Operation completed")

if __name__ == '__main__': 
    while True:
        frame_skip = int(input("\nEnter how many frames to skip:"))
        saved_frames = int(length//frame_skip)
        print(saved_frames,"images will be saved")
        answer = input("Perform extraction! Press y to continue, n to decline:")
        if answer.lower() in ["y","yes"]:
            write()
            exit(0)

        elif answer.lower() in ["n","no"]:
            continue
