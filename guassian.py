import skimage
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
import skimage.data as data
import skimage.segmentation as seg
import skimage.filters as filters
import skimage.draw as draw
import cv2 as cv
import skimage.color as color
image = io.imread('/image5.jpg')
plt.imshow(image);

ddepth = cv.CV_16S
kernel_size = 3
# [variables]
# [load]
image = cv.imread(r'/image5.jpg', cv.IMREAD_COLOR) # Load an image
# Check if image is loaded fine
# [load]
# [reduce_noise]
# Remove noise by blurring with a Gaussian filter
image = cv.GaussianBlur(image, (3, 3), 0)
# [reduce_noise]
# [convert_to_gray]
# Convert the image to grayscale
image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# [convert_to_gray]
# Create Window
# [laplacian]
# Apply Laplace function
dst = cv.Laplacian(image_gray, ddepth, kernel_size)
# [laplacian]
# [convert]
# converting back to uint8
abs_dst = cv.convertScaleAbs(dst)
# [convert]
# [display]
plt.subplot(121),plt.imshow(image, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(abs_dst, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()
