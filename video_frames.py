import cv2
import os


# create local directory for frames
path_video = r"C:\Users\Admin\Documents\video capture\Camera 3_20220526_003249.mp4"
par_dir = r"C:\Users\Admin\Documents\video capture"
path = os.path.join(par_dir, "frames", "")
if not os.path.exists(path):
    os.makedirs(path)

vidcap = cv2.VideoCapture(path_video)
success, image = vidcap.read()
count = 0

# number of frames to skip
numFrameToSave = 15

print("I am in success")
while success:  # check success here might break your program
    success, image = vidcap.read()  # success might be false and image might be None
    # check success here
    if not success:
        break
    # on every numFrameToSave
    if count % numFrameToSave == 0:
        cv2.imwrite(path + "\\" + f"frame_{count}.jpg", image)
    if cv2.waitKey(10) == 27:  # waitKey(10) - wait for 10 ms, 27 - the ASCII value for “ESC”
        break
    count += 1
