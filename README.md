# NYU-NYC-StreetScene

The NYU-NYC StreetScene dataset is a high-resolution, high-quality video dataset with accurate bounding box annotations. The dataset consists of stereo videos captured using a ZED-mini camera on the streets of NYC. Portions of each video were manually annotated with bounding boxes across 15 classes of objects of interest. Objects of interest were selected based on relevance to pedestrian navigation and obstacle avoidance. The videos were all captured in 2.2K resolution (4416x1242) at 15 fps and the bitrate used to encode the videos was 50Mbps, which ensures that compression artifacts are minimal.

There are 9 videos with IDs 78-86. 
To download all 9 videos:
```
python download_dataset.py
```

Optionally, to download a single video with an ID number:

```
python download_dataset.py --video_id ID
```

The bounding box labels will be downloaded automatically if you download any video.
You can also download only the bounding box labels by:
```
python download_dataset.py --bbox_only
```
