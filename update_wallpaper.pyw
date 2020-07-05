import ctypes
import requests
import json
import os
import shutil
import numpy as np
from PIL import Image

def main():
    try:
        with open('config.json') as f:
            config = json.load(f)
    except:
        print("Config file could not be opened")

    get_latest(config['url_base'], config['satellite'], config['band'], config['quality'])

    # Max quality does not have anything added to the image, otherwise remove watermark and metadata
    if config['quality'] != "10848x10848":
        crop_watermark("fulldisk.jpg")

    # Set desktop
    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.dirname(os.path.realpath(__file__))+r"\\fulldisk.jpg", 3)

# Removes watermark and metadata from image
def crop_watermark(image_path):
    # Open the input image as numpy array
    image = np.array(Image.open(image_path))

    # Calculate location of bottom left ~10% of image
    height = int(image.shape[0] * 0.9)
    width = int(image.shape[1] * 0.1)

    # Black out bottom left of image (watermark)
    for i in range(height, image.shape[0]):
        for j in range(width):
            image[i, j] = [1,1,1]

    # Black out bottom row of image (metadata)
    for i in range(int(image.shape[0]*0.991), image.shape[0]):
        for j in range(image.shape[1]):
            image[i, j] = [1,1,1]

    im = Image.fromarray(image)
    im.save("fulldisk.jpg")


# Fetches the latest available picture from the given satellite, band type, and quality. 
# Writes image to temp.jpg and returns nothing
def get_latest(url_base, satellite, band, quality):
    # Lastest images are stored as 'quality'.jpg, eg. 1808x1808.jpg
    url = url_base + satellite + band + quality + ".jpg"

    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open('fulldisk.jpg', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
    else:
        print("Error, recieved status code {}".format(response.status_code))


if __name__ == "__main__":
    main()