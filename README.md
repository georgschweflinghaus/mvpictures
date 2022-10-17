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

### Run the script
```
python3 mvpictures.py
```

## Sorting into different date ranges
By default the script will sort pictures into daily folders that have the name YEAR-MONTH-DAY.
The parameter --dst_format describes the template used for the folders applied per picture. The template allows placholders for date specific name creation. The placholders are those of the python strftime() function.
Examples are:

| dst_format | Example folder name result | Comment |
| --- | --- | --- |
| "%W" | 28 | will sort per week and assign each folder the week number (Monday as first day of a week) |
| "CW%W" | CW28 | will sort per week and assign each folder a prefix CW and the week number |
| "%Y-%m"| 2022-10 | will sort per month|
| "%Y-%m-%d" | 2022-10-17 |will sort per day |
