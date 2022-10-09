from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime

class ExifImageInfoNotFound(Exception):
    pass

class ImageInfo(object):

    def __init__(self):
        self.image_info_dict = {}

    def read(self, imagename: str):
        """Read meta data of an image."""
        image = Image.open(imagename)
        self.extract_basic_data(image)
        # extract EXIF data
        exifdata = image.getexif()
        if not exifdata:
            raise ExifImageInfoNotFound
        # iterating over all EXIF data fields
        for tag_id in exifdata:
            # get the tag name, instead of human unreadable tag id
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)
            if isinstance(data, bytes):
                data = data.decode()
            self.image_info_dict[tag] = data
        return self.image_info_dict

    def extract_basic_data(self, image: Image):
        """Extract basic metadata."""
        info_dict = {
            "filename": image.filename,
            "size": image.size,
            "height": image.height,
            "width": image.width,
            "format": image.format,
            "mode": image.mode,
            "is_animated": getattr(image, "is_animated", False),
            "n_frames": getattr(image, "n_frames", 1)
        }
        for label,value in info_dict.items():
            self.image_info_dict[label] = value

    def get_datetime(self):
        date_str = self.image_info_dict['DateTime']
        return datetime.strptime(date_str, '%Y:%m:%d %H:%M:%S')

    def get_filename(self):
        return self.image_info_dict['filename']


if __name__ == "__main__":
    # path to the image or video
    imagename = "./data/20220722_101404.jpg"
    # read the image data using PIL
    img_info = ImageInfo()
    for tag, data in img_info.read(imagename).items():
        print(f"{tag:25}: {data}")
    print(img_info.get_datetime().strftime("%Y-%m-%d"))
