# Organize Media Files by Year

## Description

This program organizes image and video files by copying them from a source directory to a destination directory based on their last modification year.

The program recursively scans the source directory, identifies supported media files, creates the required directory structure, and copies each file without modifying the original files.

Only supported image and video formats are processed. All other files are ignored.

## How It Works

The program receives the source and destination directories as command-line arguments.

It then performs the following steps:

* Recursively traverses the source directory using `os.walk()`.
* Determines the type of each file based on its extension.
* Retrieves the file's last modification year.
* Creates the required destination directories when necessary.
* Copies image files into a `photos` directory.
* Copies video files into a `videos` directory.
* Preserves the original file names while leaving the source directory unchanged.

## Example

Suppose the source directory contains the following files:

```text
src_folder/
├── IMG_2235.jpg
├── travel_photos/
│   ├── 2018-11-09_11-27-14.3gp
│   ├── IMG_20171017_052418.jpg
│   ├── 20180311_214539.JPG
│   ├── IMG_2237.jpg
│   └── note.txt
└── vid1/
    ├── images/
    │   └── IMG_2014-01-12.JPG
    └── VID_20170425_184731.mp4
```

Running:

```bash
python organize.py src_folder dst_folder
```

Produces the following destination structure:

```text
dst_folder/
├── 2014/
│   └── photos/
│       └── IMG_2014-01-12.JPG
├── 2017/
│   ├── photos/
│   │   └── IMG_20171017_052418.jpg
│   └── videos/
│       └── VID_20170425_184731.mp4
└── 2018/
    ├── photos/
    │   ├── 20180311_214539.JPG
    │   ├── IMG_2235.jpg
    │   └── IMG_2237.jpg
    └── videos/
        └── 2018-11-09_11-27-14.3gp
```

## Code

The complete implementation is available in **5_organize_media_files.py**.

---

**Author:** AiPixelCode
