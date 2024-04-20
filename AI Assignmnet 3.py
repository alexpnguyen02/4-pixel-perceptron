from PIL import Image
import numpy as np

#Convert the image to an array
def image_to_array(image_path):
    image = Image.open(image_path)
    image_array = np.array(image)
    return image_array

#Check if the pixel is white and count white pixels in image
def count_white_pixels(image_array):
    white_pixels = np.sum(np.all(image_array[:, :, :3] == [255, 255, 255], axis=-1))
    return white_pixels

#If more than 2 white pixels return bright
def classify_brightness(image_path):
    image_array = image_to_array(image_path)
    white_pixels = count_white_pixels(image_array)
    if white_pixels >= 2:
        return "bright"
    else:
        return "dark"

#main method
image_path = "bwTest4-dark.png"  
classification = classify_brightness(image_path)
print("Classification:", classification)