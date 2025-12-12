import argparse
import os
import shutil
import numpy as np

parser = argparse.ArgumentParser(description='Select YouTube-GDD images')
parser.add_argument('--imagelist', default='./configs/imagelist.npy')
parser.add_argument('--framepath', default='frames')
parser.add_argument('--imagepath', default='images')

args = parser.parse_args()
if __name__ == '__main__':
  dic = np.load(args.imagelist,allow_pickle=True).item()
  for set in ["train","val","test"]:
    if not os.path.exists(os.path.join(args.imagepath,set)):
      os.mkdir(os.path.join(args.imagepath,set))
  for set in ["train", "val", "test"]:
    dist_root = os.path.join(args.imagepath,set)
    for image in dic[set]:
      source_path = os.path.join(args.framepath,image)
      if os.path.exists(source_path):
        shutil.copy(source_path,os.path.join(dist_root,image))