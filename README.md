# mvpictures
This is a small tool which is capable to move (sort) picures based on exif data into directories.
EXIF data is meta data available in many pictures, specifically if they were taken by any sort of camera.
The sorting is date based, so that images taken e.g. on 1st of January 2022 may be sorted into a folder named 2022-01-01 or 2022-January.

## How to setup
### Optional, use a virutal environment
It is best to setup a virtual environment.
```
python3 -m venv .
source bin/activate
```
In case the above will fail and you are on Ubuntu you may miss the venv module. This command will then help.
```
sudo apt-get install python3.10-venv
```
### Install dependencies
```
pip3 install -r requirements.txt
```
