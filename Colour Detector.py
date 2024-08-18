import cv2
import os
import numpy as np


def crop_image(image, percentage):
    height, width = image.shape[:2]

    crop_top = int(height * percentage)
    crop_bottom = int(height * (1 - percentage))
    crop_left = int(width * percentage)
    crop_right = int(width * (1 - percentage))

    cropped_image = image[crop_top:crop_bottom, crop_left:crop_right]

    return cropped_image


# Rest of your existing code
image_directory = 'all'
output_directory = 'cars'
# define range wanted color in HSV
lower_val = np.array([37, 42, 0])
upper_val = np.array([84, 255, 255])
# Load YOLO
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

filename='cars.jpg'
filenameSplit = filename.split('.')
image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
img = cv2.resize(image, None, fx=0.4, fy=0.4)

blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
net.setInput(blob)
outs = net.forward(output_layers)
numberofCar=1
for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5 and classes[class_id] == 'car':
                    scale_factor = 0.8
                    car_image = crop_image(img, 1 - scale_factor)
                    hsv = cv2.cvtColor(car_image, cv2.COLOR_BGR2HSV)
                    # Threshold the HSV image - any green color will show up as white
                    mask = cv2.inRange(hsv, lower_val, upper_val)

                    # if there are any white pixels on mask, sum will be > 0
                    hasGreen = np.sum(mask)
                    if hasGreen > 0:
                        print('Green detected!')
                        cv2.imwrite('./output/'+filenameSplit[0]+str(numberofCar)+'.'+filenameSplit[1], car_image)
                        numberofCar=numberofCar+1



