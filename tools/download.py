from pytube import YouTube
import argparse
import os

parser = argparse.ArgumentParser(description='Download YouTube videos')
parser.add_argument('--videolist', default='./configs/videolist.txt')
parser.add_argument('--videopath', default='videos')

args = parser.parse_args()
if __name__ == '__main__':
  if not os.path.exists(args.videopath):
    os.mkdir(args.videopath)
  count=0
  with open(args.videolist,"r") as f:
    urls = f.readlines()
  urls = [url.replace('\n','') for url in urls]

  for url in urls:
    try:
      video = YouTube(r"https://www.youtube.com/watch?v=" + url)
      video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download(args.videopath,filename=url)
      count += 1
    except:
      continue
  print(f"download: {count} videos || total: {len(urls)} videos")