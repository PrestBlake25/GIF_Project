import imageio.v3 as iio
from PIL import Image
import numpy as np

filenames = ['OtherGIF1.jpg', 'OtherGIF2.jpg','OtherGIF3.jpg', 'OtherGIF4.jpg', 'OtherGIF5.jpg', 'OtherGIF6.jpg', 'Othergif7.jpg', 'OtherGIF8.jpg']
images = []

for filename in filenames:
    # Read image
    image = iio.imread(filename)
    
    # Convert to PIL Image for rotation
    pil_image = Image.fromarray(image)
    
    # Rotate the image by 90 degrees
    rotated_image = pil_image.rotate(270, expand=True)
    
    # Convert back to numpy array
    rotated_image_array = np.array(rotated_image)
    
    # Append to images list
    images.append(rotated_image_array)

# Write the rotated images to a GIF
iio.imwrite('Prest.gif', images, duration=500, loop=0)
