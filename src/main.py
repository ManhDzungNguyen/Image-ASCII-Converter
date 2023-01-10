import img_to_ASCII
from img_to_ASCII import image_to_ascii
from utils import input_val, input_path

if __name__ == "__main__":
    image_path = input_path("image_path: ")
    save_path = input_path("save_path: ")
    width = input_val("width: ")
    height = input_val("height: ")
    wh_weight = input_val("wh_weight: ", type=float, default=img_to_ASCII.DEFAULT_WH_WEIGHT)

    image_to_ascii(image_path, save_path, width, height, wh_weight)
