from PIL import Image
import os
from pathlib import Path


def prepocess_image(image_to_crop):
    box = (115, 210, 350, 445)
    newsize = (116, 116)
    im_cropped = image_to_crop.crop(box)
    im_resized = im_cropped.resize(newsize)
    return im_resized

# create local directory for frames
par_dir = r"C:\Users\Admin\Documents\video capture"
path_frame = r"C:\Users\Admin\Documents\video capture\frames\\"


# create local directory for cropped images
path_new = os.path.join(par_dir, "cropped", "")
if not os.path.exists(path_new):
    os.makedirs(path_new)

# preprocess and save images
images = Path(path_frame).glob('*.jpg')
for image in images:
    im = Image.open(image)
    im_new = prepocess_image(im)
    name = os.path.split(image)
    file_path = os.path.join(path_new, "cropped_" + name[1].split("_")[1])
    im_new.save(file_path, quality=95)
