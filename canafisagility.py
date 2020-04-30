import pyautogui as pauto
import time
import random
import sys
import numpy as np
import cv2
import winsound

from modules import setup
from modules import Mouse
from modules import Keyboard
from modules import RandomTime
from modules import Screenshot
import login


# 8 total states

lh = 88#165
ls = 223#199
lv = 151#192
uh = 116#172
us = 255#255
uv = 255#255

lh1 = 162
ls1 = 200
lv1 = 157
uh1 = 185
us1 = 255
uv1 = 255


w = setup.Window()

def alert_mark_found():
	winsound.PlaySound("*", winsound.SND_ALIAS)
	pauto.alert(text='Mark was found. Please find it and go to the next state before clicking "CONTINUE"', title="Mark Found!", button="CONTINUE")

def alert_fell_state():
	winsound.PlaySound("*", winsound.SND_ALIAS)
	pauto.alert(text='Fell from course. Please go to State 1 before clicking "CONTINUE".', title='Fell State!', button='CONTINUE')

def get_state():
	#image = pauto.screenshot(region=(0, 0, 1214, 803))
	image = pauto.screenshot(region=(9, 46, 770, 500))#(9, 779, 46, 546))
	image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
	frame = np.array(image)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lb = np.array([lh, ls, lv])
	ub = np.array([uh, us, us])

	mask = cv2.inRange(hsv, lb, ub)

	try:
		points = cv2.findNonZero(mask)
		print(points.size)
		return(points.size)
	except AttributeError:
		lb1 = np.array([lh1, ls1, lv1])
		ub1 = np.array([uh1, us1, us1])

		mask = cv2.inRange(hsv, lb1, ub1)
		try:
			points = cv2.findNonZero(mask)
			print(points.size)
			points = [1]
			return len(points)
		except AttributeError:
			points = []
			return len(points)

	#print(points.size)

	#return points.size

def give_state(size):
	if size >= 835 and size <= 865:
		return 0
	elif (size >= 1180 and size <= 1195) or (size >= 1094 and size <= 1096):
		return 1
	elif size >= 1156 and size <= 1176:
		return 2
	elif size >= 1196 and size <= 1270:
		return 3
	elif size >= 386 and size <= 406:
		return 4
	elif size >= 656 and size <= 676:
		return 5
	elif size >= 328 and size <= 348 or size == 728:
		return 6
	elif size >= 296 and size <= 316:
		return 7
	elif size == 1:
		return -1
	else:
		return None

def click_state_0():
	# 842
	Mouse.moveClick(random.randint(274, 338), random.randint(209, 222), 1)

def click_state_1():
	# 1190, 1096, 1094
	Mouse.moveClick(random.randint(375, 399), random.randint(188, 207), 1)

def click_state_2():
	# 1166
	Mouse.moveClick(random.randint(299, 310), random.randint(286, 309), 1)

def click_state_3():
	# 1200, 1264
	Mouse.moveClick(random.randint(280, 294), random.randint(365, 393), 1)

def click_state_4():
	# 396
	Mouse.moveClick(random.randint(372, 381), random.randint(402, 431), 1)

def click_state_5():
	# 666
	Mouse.moveClick(random.randint(419, 428), random.randint(338, 346), 1)

def click_state_6():
	# 338
	Mouse.moveClick(random.randint(623, 639), random.randint(286, 312), 1)

def click_state_7():
	# 306
	Mouse.moveClick(random.randint(389, 398), random.randint(173, 192), 1)


while True:
	size = get_state()
	state = give_state(size)

	if state == 0:
		click_state_0()
		time.sleep(random.randint(7100, 7500)/1000)
	elif state == 1:
		click_state_1()
		time.sleep(random.randint(5200, 5600)/1000)
	elif state == 2:
		click_state_2()
		time.sleep(random.randint(5550, 5950)/1000)
	elif state == 3:
		click_state_3()
		time.sleep(random.randint(6100, 6500)/1000)
	elif state == 4:
		click_state_4()
		time.sleep(random.randint(5700, 6100)/1000)
	elif state == 5:
		click_state_5()
		time.sleep(random.randint(7900, 8300)/1000)
	elif state == 6:
		click_state_6()
		time.sleep(random.randint(8400, 8900)/1000)
	elif state == 7:
		click_state_7()
		time.sleep(random.randint(5650, 6050)/1000)
	else:
		if state == -1:
			alert_mark_found()
		else:
			#pauto.alert(text='Error. Cannot determine state.', title='Error State!', button='END PROGRAM')
			#break
			alert_fell_state()
'''
while True:
	get_state()
'''