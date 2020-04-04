import pyautogui as pauto
import time
import random
import sys

from modules import setup
from modules import Mouse
from modules import Keyboard
from modules import RandomTime
from modules import Screenshot
import login

LH = 86
LS = 234
LV = 202
UH = 111
US = 255
UV = 255

LH1 = 86
LS1 = 255
LV1 = 200
UH1 = 255
US1 = 255
UV1 = 251

def setup_settings():
	Mouse.moveClick(random.randint(1000, 1039), random.randint(745, 785), 1)
	Mouse.moveClick(random.randint(912, 920), random.randint(445, 455), 1)
	Mouse.moveClick(random.randint(949, 990), random.randint(295, 341), 1)

# Finds Gerrant, moves mouse to him, right-clicks        #, press trade, buys feathers, closes store
def find_gerrant():
	#tries = 0
	try:
		hsv = Screenshot.shoot()
		coords = Screenshot.shot_coords(LH, LS, LV, UH, US, UV, hsv)
		Mouse.moveFast(int(coords[0, 0]), int(coords[0, 1]))
		return True
	except TypeError:
		print('Gerrent was not located, trying again.')
		#move_camera()
		#tries += 1
		return False
		#sys.exit()
	'''
	Mouse.click('right')
	time.sleep(random.randint(300, 800)/1000)
	'''


	'''
	time.sleep(RandomTime.randTime(0, 2, 2, 0, 3, 3))
	Mouse.relMove(0, random.randint(62, 68))
	time.sleep(RandomTime.randTime(0, 2, 2, 0, 3, 3))
	Mouse.click('left')
	time.sleep(random.randint(5000, 8000)/1000)
	Mouse.moveClick(random.randint(129, 155), random.randint(212, 243), 2)
	Mouse.relMove(0, random.randint(103, 109))
	Mouse.click('left')
	Mouse.moveClick(random.randint(724, 747), random.randint(92, 116), 1)
	'''

def found_gerrant(flag):
	if flag:
		Mouse.click('right')
		time.sleep(random.randint(100, 400)/1000)
	else:
		pass

def click_featherpack():
	Mouse.moveClick(random.randint(981, 1016), random.randint(365, 407), 1)
	time.sleep(random.randint(350, 650)/1000)

def wait_featherpack():
	Mouse.moveTo(random.randint(1220, 2200), random.randint(810, 1300))
	time.sleep(random.randint(7500, 10000)/1000)
	Mouse.moveTo(random.randint(19, 1100), random.randint(19, 730))
	time.sleep(random.randint(2000, 3000)/1000)

# Checks if find_gerrant right click is valid
def click_check():#lh, ls, lv, uh, us, uv):
	#Mouse.click('right')
	#time.sleep(random.randint(100, 400)/1000)
	hsv = Screenshot.shoot()
	coords = Screenshot.shot_coords(LH1, LS1, LV1, UH1, US1, UV1, hsv)
	if None not in coords:
		return True
	else:
		return False

## If click was valid, press trade
def click_valid():
	time.sleep(RandomTime.randTime(0, 2, 2, 0, 3, 3))
	Mouse.relMove(0, random.randint(62, 68))
	time.sleep(RandomTime.randTime(0, 2, 2, 0, 3, 3))
	Mouse.click('left')
	time.sleep(random.randint(4000, 6000)/1000)

# Buys featherpack and closes store window
def buy_featherpack():
	Mouse.moveClick(random.randint(129, 155), random.randint(212, 243), 2)
	Mouse.relMove(0, random.randint(103, 109))
	Mouse.click('left')
	Mouse.moveClick(random.randint(724, 747), random.randint(92, 116), 1)

def move_camera():
	dir = random.randint(0, 1)
	if dir == 0:
		Keyboard.pressDef('left', random.randint(1000, 1200)/1000)
	elif dir == 1:
		Keyboard.pressDef('right', random.randint(1000, 1200)/1000)


# Actual program loop starts here
'''
print('Setting up window environment.')
w = setup.Window()
login.logging()
print('Setting up settings.')
setup_settings()
'''

try:
	#found = False
	#setup_settings()
	start = time.time()
	
	w = setup.Window()
	#login.logging()
	time.sleep(2)
	

	reps = 30
	for i in range(reps):
		print('Finding Gerrant.')
		while True:
			gerrant = find_gerrant()
			if gerrant:
				found_gerrant(gerrant)

				found = click_check()

				if found:
					break

				continue
			time.sleep(1.2)
			move_camera()
			#time.sleep(1.2)

			'''
			found = click_check()
			if found == True:
				print('Gerrant found.')
				break
			print('Not found, trying again.')
			move_camera()'''

		click_valid()
		print('Buying featherpack.')
		buy_featherpack()
		click_featherpack()
		wait_featherpack()
		print('Finished repetition ' + str(i+1) + ' of ' + str(reps) + '.')
	print('Finished script.')
	end = time.time() - start
	print('Ran for ' + str(end) + ' seconds.')
except (KeyboardInterrupt, pauto.FailSafeException):
	sys.exit()

