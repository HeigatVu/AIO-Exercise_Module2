import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


# ----------------------------Question 12----------------------------
plt.imshow(mpimg.imread('dog.jpeg'))

img = plt.imread('dog.jpeg')
grey_lightness_img = (np.max(img, axis=2) + np.min(img, axis=2))/2

plt.imshow(grey_lightness_img, cmap="gray")

grey_lightness_img[0, 0]

# ----------------------------Question 13----------------------------
img = plt.imread('dog.jpeg')
grey_average_img = np.sum(img, axis=2, keepdims=True)/3

plt.imshow(grey_average_img, cmap="gray")

grey_average_img[0, 0]

# ----------------------------Question 14----------------------------
img = plt.imread('dog.jpeg')
grey_luminosity_img = 0.21*img[:, :, 0] + 0.72*img[:, :, 1] + 0.07*img[:, :, 2]
plt.imshow(grey_average_img, cmap="gray")

grey_luminosity_img[0, 0]
