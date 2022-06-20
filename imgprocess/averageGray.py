import cv2
imageData = cv2.imread("img1.jpg")
for r in range(imageData.shape[0]):
    for c in range(imageData.shape[1]):
        rgb = imageData[r][c]
        red = int(rgb[0])
        green = int(rgb[1])
        blue = int(rgb[2])
        avg = int((red+green+blue)/3)
        imageData[r][c]=(avg,avg,avg)  #image file data is being manipulated

cv2.imwrite("tmp.jpg",imageData)
