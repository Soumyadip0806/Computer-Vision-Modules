import math


def height_ratio(x1, y1, x2, y2, x3, y3):
    actual_height = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    changed_height = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
    current_height = (changed_height*3)/ actual_height

    return current_height

# Here (X1,Y1)is the top edge coordinate (X2,Y2) is the bottom edge coordinate, when there is no waterlogging issue
#(X3,Y3)is the bottom edge coordinate when there is waterlogging issue
# So EUC distance between the top(X1,Y1) and bottom(X2,Y2) is 3ft distance
# After Waterlogging, the distance between the top(X1,Y1) and bottom(X3,Y3) is current height(ratio)

x1, y1 = 244, 272
x2, y2 = 244, 323
x3, y3 = 244, 293

Height = height_ratio(x1, y1, x2, y2, x3, y3)
print("Current Height:", Height)
