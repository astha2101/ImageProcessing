import cv2

imageData = cv2.imread("img1.jpg")
print(imageData)
print(type(imageData))
print(imageData.shape)
print(imageData[0][0])

def hello():
	print("Hello world!!!")

hello()
