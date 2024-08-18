# import required libraries
import numpy as np
import cv2
# define a numpy.ndarray for the color
# here insert the bgr values which you want to convert to hsv
green = np.uint8([[[0, 255, 0]]])

# convert the color to HSV
hsvGreen = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)

# display the color values
print("BGR of Green:", green)
print("HSV of Green:", hsvGreen)

# Compute the lower and upper limits
lowerLimit = hsvGreen[0][0][0] - 10, 100, 100
upperLimit = hsvGreen[0][0][0] + 10, 255, 255

# display the lower and upper limits
print("Lower Limit:",lowerLimit)
print("Upper Limit", upperLimit)