import cv2

imageData = cv2.imread("img1.jpg")
for r in range(imageData.shape[0]):
    for c in range(imageData.shape[1]):
        rgb = imageData[r][c];
        red = rgb[0]
        green = rgb[1]
        blue = rgb[2]
        if red < green: clr = red
        else : clr = green
        if blue < clr : clr = blue
        imageData[r][c] = (clr,clr,clr)
cv2.imwrite("tmp2.jpg",imageData)
