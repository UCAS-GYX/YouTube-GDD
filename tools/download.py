import argparse
import os
from yt_dlp import YoutubeDL

parser = argparse.ArgumentParser(description="Download YouTube videos with yt-dlp")
parser.add_argument("--videolist", default="./configs/videolist.txt")
parser.add_argument("--videopath", default="videos")

args = parser.parse_args()

def load_entries(path):
    with open(path, "r") as f:
        return [line.strip() for line in f if line.strip()]

if __name__ == "__main__":
    os.makedirs(args.videopath, exist_ok=True)

    entries = load_entries(args.videolist)
    print(f"Found {len(entries)} entries in {args.videolist}")
    print(f"Saving videos to: {os.path.abspath(args.videopath)}")

    # yt-dlp options
    ydl_opts = {
        "format": "bv*+ba/b",  # best video+audio, fallback to best
        "outtmpl": os.path.join(args.videopath, "%(id)s.%(ext)s"),
        "noplaylist": True,
    }

    success = 0
    with YoutubeDL(ydl_opts) as ydl:
        for i, entry in enumerate(entries, start=1):
            # allow IDs or full URLs
            if entry.startswith("http://") or entry.startswith("https://"):
                url = entry
            else:
                url = f"https://www.youtube.com/watch?v={entry}"

            print(f"\n[{i}/{len(entries)}] Downloading: {url!r}")
            try:
                ydl.download([url])
                success += 1
            except Exception as e:
                print(f"  ❌ Error downloading {url}: {e}")

    print(f"\nFinished. Successfully downloaded: {success} / {len(entries)} videos.")
