import os
from PIL import Image
from pathlib import Path


DEFAULT_WH_WEIGHT = 2.2

def image_to_ascii(image_path, save_path, width=None, height=None, wh_weight=DEFAULT_WH_WEIGHT):
    # Open image and resize
    image = Image.open(image_path)
    raw_width, raw_height = image.size
    ratio_wh= raw_width / raw_height * wh_weight

    if width is None:
        if height is None:
            height = 80
        width = int(height * ratio_wh)
    elif width is not None and height is None:
        height = int(width / ratio_wh)
    
    image = image.resize((width,height))

    # Create ASCII character set
    ascii_chars = [' ', '.', ',', ':', ';', '+', '*', '#', '@']

    # Map each pixel to an ASCII character
    ascii_image = []
    for y in range(image.size[1]):
        ascii_row = []
        for x in range(image.size[0]):
            pixel = image.getpixel((x,y))
            pixel_brightness = sum(pixel) / len(pixel)
            ascii_index = int(pixel_brightness / 256 * len(ascii_chars))
            ascii_row.append(ascii_chars[ascii_index])
        ascii_image.append(ascii_row)

    # Save ASCII image to text file    
    ASCII_file = "ita_" + Path(image_path).stem + ".txt"
    ASCII_path = os.path.join(save_path, ASCII_file)

    with open(ASCII_path, "w") as f:
        for row in ascii_image:
            f.write(''.join(row) + '\n')