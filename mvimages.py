import os
import shutil
import argparse
from PIL import UnidentifiedImageError
from DirReader import DirReader
from ImageInfo import ImageInfo, ExifImageInfoNotFound


def build_dst_dirpath(dst_dir: str, imginf: ImageInfo, format: str):
    dst_date = imginf.get_datetime().strftime(format)
    return os.path.join(dst_dir, dst_date)

def build_dst_filepath(dst_dir_path: str, imginf: ImageInfo):
    dst_filename = os.path.basename(imginf.get_filename())
    return os.path.join(dst_dir_path, dst_filename)

def move_file(imginf: ImageInfo, dst_dir: str, format: str):
    """Move a file to a destination directory.

        The function will assure that directories missing will be created.
        The image described by imginf will be moved to the destination
        directory which will get a name as specified by the format. """
    src_file = imginf.get_filename()
    dst_dir_path = build_dst_dirpath(dst_dir, imginf, format)
    dst_file_path = build_dst_filepath(dst_dir_path, imginf)
    assure_dir_exists(dst_dir_path)
    shutil.move(src_file, dst_file_path)

def assure_dir_exists(path: str):
    if not os.path.exists(path):
        os.mkdir(path)

def main():
#files = find_all_files(startdir)
#files_and_dates = read_dates_from_files(files)
#create_date_directories(files_and_dates)
#move_files_into_directories(files_and_dates)
    parser = argparse.ArgumentParser(
        description='Move images based on their embeded exif meta data into directories baed on day of photo taken.')
    parser.add_argument('--src', nargs='?', type=str, default='.', help='Folder with the source images to be moved. (default ".")')
    parser.add_argument('--dst', nargs=1, required=True, type=str, help='Folder where directories are created and images will be moved into.')
    parser.add_argument('--dst_format', type=str, default="%Y-%m-%d", help='Defines how destination folder name is built from date. Default is (%%Y-%%m-%%d)')
    args = parser.parse_args()

    files = DirReader().read(args.src)
    assure_dir_exists(args.dst[0])
    for file in files:
        try:
            imginf = ImageInfo()
            imginf.read(file)
            move_file(imginf, args.dst[0], args.dst_format)
        except UnidentifiedImageError as err:
            print(f"Warning: \"{file}\" may not be an image. It will not be moved!")
        except ExifImageInfoNotFound as err:
            print(f"warning: \"{file}\" has no exif data. It will not be moved!")


if __name__ == "__main__":
    main()
