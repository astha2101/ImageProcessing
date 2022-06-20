import cv2

imageData = cv2.imread("img1.jpg")
for r in range(imageData.shape[0]):
    for c in range(imageData.shape[1]):
        rgb = imageData[r][c]
        red = int(int(rgb[0])*0.3)
        green = int(int(rgb[1])*.59)
        blue = int(int(rgb[2])*.11)
        total = red+green+blue
        imageData[r][c] = (total,total,total)
cv2.imwrite("tmp3.jpg",imageData)
