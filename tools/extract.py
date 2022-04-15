import argparse
import os
import cv2
import math

parser = argparse.ArgumentParser(description='Extract YouTube frames')
parser.add_argument('--videopath', default='videos')
parser.add_argument('--framepath', default='frames')


def extract_frames(video_path, dst_folder, extract_frequency, abstract_name, frame_rate, index):
  video = cv2.VideoCapture()
  if not video.open(video_path):
    print("can not open the video")
    exit(1)
  count = 1
  while True:
    _, frame = video.read()
    if frame is None:
      break
    if count % extract_frequency == 0:
      save_path = "{}/{}_{:2d}_{:2d}_{:>06d}.jpg".format(dst_folder, abstract_name, frame_rate, extract_frequency,
                                                         index)
      cv2.imwrite(save_path, frame)
      index += 1
    count += 1
  video.release()

args = parser.parse_args()
if __name__ == '__main__':
  if not os.path.exists(args.framepath):
    os.mkdir(args.framepath)
  video_names = os.listdir(args.videopath)
  for video_name in video_names:
    video_path = os.path.join(args.videopath, video_name)
    abstract_name = video_name.split('.')[0]
    video_capture = cv2.VideoCapture(video_path)
    frame_rate = math.ceil(video_capture.get(5))
    extract_rate = frame_rate * 2
    extract_frames(video_path, args.framepath, extract_rate, abstract_name, frame_rate, 1)