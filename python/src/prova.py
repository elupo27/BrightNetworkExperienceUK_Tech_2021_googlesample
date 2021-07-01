"""try a bit the functions"""

from .video import Video
from pathlib import Path
import csv


# Helper Wrapper around CSV reader to strip whitespace from around
# each item.
def something(reader):
    yield from ((item.strip() for item in line) for line in reader)

videosL = {}
videosL2=[]
with open(Path(__file__).parent / "videos.txt") as video_file:
    reader = something(csv.reader(video_file, delimiter="|"))
    for video_info in reader:
        title, url, tags = video_info
        videosL[url] = Video(
            title,
            url,
            [tag.strip() for tag in tags.split(",")] if tags else [],
        )
        videosL2.append(Video(
            title,
            url,
            [tag.strip() for tag in tags.split(",")] if tags else []
        ))

print(videosL)
print(videosL["funny_dogs_video_id"])
print(list(videosL))

print('Hello!')