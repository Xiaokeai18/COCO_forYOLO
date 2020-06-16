import argparse
import os
from random import shuffle
import shutil
import subprocess
import sys
import shutil

train_image_subsets = "/media/wp/HDD/dataset/COCO/train2017"
val_image_subsets = "media/wp/HDD/dataset/COCO/val2017"
#test_image_subsets = "media/wp/HDD/dataset/COCO/test2017"
dst_image_dir = "media/wp/HDD/dataset/COCO/JPEGImages"

def change(path, path1):
    for f in os.listdir(path):
        if os.path.isfile(path + os.path.sep + f):
            a, b = os.path.splitext(f)
            if b != '.py':
                shutil.copy(path + os.sep + f, path1)
        elif os.path.isdir(path + os.path.sep + f):
            change(path + os.sep + f, path1)

# Copy annotations from subset to labels.
change(train_image_subsets, dst_image_dir)
change(val_image_subsets, dst_image_dir)
#change(test_image_subsets, dst_image_dir)
