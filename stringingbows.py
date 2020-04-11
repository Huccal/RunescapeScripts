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


reps = input('How many times do you want to repeat?: ')

w = setup.Window()
geometry = w.window_stats()
screen = pauto.size()

def click_bank():
	#Mouse.moveClick(random.randint(298, 430), random.randint(223, 325), 1)
	'''
	# SURFACE LAPTOP
	Mouse.moveClick(random.randint(279, 449), random.randint(262, 315), 1)
	'''
	# MOMMY'S LAPTOP
	Mouse.moveClick(random.randint(201, 292), random.randint(40, 131), 1)

def click_deposit_inventory():
	'''
	# SURFACE LAPTOP
	Mouse.moveClick(random.randint(650, 691), random.randint(490, 530), 1)
	'''
	# MOMMY's LAPTOP
	Mouse.moveClick(random.randint(435, 461), random.randint(327, 353), 1)

def withdraw_items():
	'''
	# SURFACE LAPTOP
	Mouse.moveClick(random.randint(119, 154), random.randint(265, 298), 1)
	#Mouse.moveClick(random.randint(195, 228), random.randint(273, 304), 1)
	Mouse.moveFast(random.randint(195, 228), random.randint(273, 304))
	Mouse.click('left')
	Mouse.moveClick(random.randint(724, 748), random.randint(69, 87), 1)
	'''
	# MOMMY's LAPTOP
	Mouse.moveClick(random.randint(81, 100), random.randint(180, 195), 1)
	Mouse.moveFast(random.randint(130, 151), random.randint(179, 197))
	Mouse.click('left')
	Mouse.moveClick(random.randint(482, 498), random.randint(43, 57), 1)

def string_bows():
	'''
	# SURFACE LAPTOP
	Mouse.moveClick(random.randint(919, 950), random.randint(535, 562), 1)
	#Mouse.moveClick(random.randint(986, 1015), random.randint(527, 565), 1)
	Mouse.moveFast(random.randint(986, 1015), random.randint(527, 565))
	Mouse.click('left')
	time.sleep(random.randint(240, 290)/1000)
	#Mouse.moveClick(random.randint(331, 459), random.randint(636, 725), 1)
	'''
	# MOMMY's LAPTOP
	Mouse.moveClick(random.randint(614, 636), random.randint(355, 373), 1)
	Mouse.moveFast(random.randint(657, 677), random.randint(351, 373))
	Mouse.click('left')
	time.sleep(random.randint(240, 290)/1000)

	hold = random.randint(800, 1000)/1000
	start = time.time()
	while time.time() - start < hold:
		Keyboard.press('space')

def wait_stringing(x1, y1, x2, y2, v, z):
	chance = random.randint(1, 100)
	if chance < 30:
		# Move mouse out of screen
		Mouse.moveTo(random.randint(x2 + 50, v - 150), random.randint(y2 + 50, z - 150))
		time.sleep(random.randint(8000, 8500)/1000)
		Mouse.moveTo(random.randint(x1 + 19, x2 - 150), random.randint(y1 + 19, y2 - 150))
		time.sleep(random.randint(8000, 8500)/1000)
	elif chance >= 30:
		Mouse.moveTo(random.randint(x1 + 19, x2 - 150), random.randint(y1 + 19, y2 - 150))
		time.sleep(random.randint(16500, 17100)/1000)


for i in range(int(reps)):
	print('Doing repetition ' + str(i+1) + ' of '+ str(reps))

	click_bank()
	time.sleep(random.randint(250, 300)/1000)
	click_deposit_inventory()
	withdraw_items()
	string_bows()
	wait_stringing(geometry[0], geometry[1], geometry[2], geometry[3], screen[0], screen[1])

print('Finished all ' + str(reps) + ' repetition')
