import numpy as np
import argparse
import cv2

'''
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

boundaries = [([235, 235, 0], [255, 255, 10])]

for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)
	# show the images
	cv2.imshow("images", np.hstack([image, output]))
	cv2.waitKey(0)
'''

def nothing(x):
	pass

cv2.namedWindow('Tracking')
cv2.createTrackbar('LH', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('LS', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('LV', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('UH', 'Tracking', 255, 255, nothing)
cv2.createTrackbar('US', 'Tracking', 255, 255, nothing)
cv2.createTrackbar('UV', 'Tracking', 255, 255, nothing)


while True:
	frame = cv2.imread('testimg.png')

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	'''
	l_h = 55
	l_s = 205
	l_v = 0
	u_h = 100
	u_s = 255
	u_v = 255
	'''
	
	l_h = cv2.getTrackbarPos('LH', 'Tracking')
	l_s = cv2.getTrackbarPos('LS', 'Tracking')
	l_v = cv2.getTrackbarPos('LV', 'Tracking')

	u_h = cv2.getTrackbarPos('UH', 'Tracking')
	u_s = cv2.getTrackbarPos('US', 'Tracking')
	u_v = cv2.getTrackbarPos('UV', 'Tracking')
	

	l_b = np.array([l_h, l_s, l_v])
	u_b = np.array([u_h, u_s, u_v])
	

	mask = cv2.inRange(hsv, l_b, u_b)

	res = cv2.bitwise_and(frame, frame, mask=mask)

	cv2.imshow('frame', frame)
	cv2.imshow('mask', mask)
	cv2.imshow('res', res)	

	# code that gives coordinates
	#points = cv2.findNonZero(mask)

	#avg = np.mean(points, axis=0)

	#pointInScreen = ()
	#print(avg)

	key = cv2.waitKey(1)
	if key == 27:
		break

cv2.destroyAllWindows()