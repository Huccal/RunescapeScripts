import pyautogui as pauto
import numpy as np
import cv2
import os
from PIL import ImageGrab

LH = 86
LS = 234
LV = 202
UH = 111
US = 255
UV = 255
PATH = 'tempscrnshot.png'
RES_IMG = [1214, 803]
RES_SCRN = [2256, 1504]

# Return HSV format of screenshot of what is highlighted with given HSV
def shoot():
	'''
	image = pauto.screenshot(PATH, region=(0, 0, 1214, 803))
	frame = cv2.imread(PATH)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	os.remove(PATH)
	'''
	
	image = pauto.screenshot(region=(0, 0, 1214, 803))
	image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
	frame = np.array(image)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	'''
	img = ImageGrab.grab(bbox=(0, 0, 1214, 803)).convert('RGB')
	img_np = np.array(img)
	img_resize = cv2.resize(img_np, (1214, 803))
	hsv = cv2.cvtColor(img_resize, cv2.COLOR_BGR2HSV)
	'''
	return hsv

def shot_coords(lh, ls, lv, uh, us, uv, hsv):
	lb = np.array([lh, ls, lv])
	ub = np.array([uh, us, us])

	mask = cv2.inRange(hsv, lb, ub)

	points = cv2.findNonZero(mask)

	#print(points)
	#print(points.size)
	'''
	if points.any() == None:
		return [None]
	'''
	try:
		if points.size < 500:
			return [None]
	except AttributeError:
		return [None]

	avg = np.mean(points, axis=0)

	return avg
	

if __name__ == '__main__':
	hsv = shoot()
	#coords = shot_coords(LH, LS, LV, UH, US, UV, hsv)
	coords = shot_coords(86, 255, 200, 255, 255, 251, hsv)
	#x = coords[0, 0]
	#y = coords[0, 1]
	print(coords, type(coords))
	#print(coords[0, 0], coords[0, 1])
	#pauto.moveTo((RES_SCRN[0] / RES_IMG[0]) * x,(RES_SCRN[1] / RES_IMG[1]) * y, 0.2)
	#pauto.moveTo((RES_IMG[0] / RES_SCRN[0]) * x,(RES_IMG[1] / RES_SCRN[1]) * y, 0.2)
	#pauto.moveTo(x, y, 0.2)