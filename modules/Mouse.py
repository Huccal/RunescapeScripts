from pyclick import HumanClicker
import random
import time
import pyautogui as pauto

from modules import RandomTime

hc = HumanClicker()

def moveTo(x, y):
	#start_coords = pauto.position()
	end_coords = (x, y)
	#delay = RandomTime.randTime(400, 0, 0, 1200, 9, 9)/1000
	#print(delay)
	#hc.move((start_coords[0], start_coords[1]), RandomTime.randTime(200, 0, 0, 500, 9, 9)/1000)
	hc.move((end_coords[0], end_coords[1]), RandomTime.randTime(400, 0, 0, 1200, 9, 9)/1000)

def relMove(px, py):
	coords = pauto.position()
	px = coords[0] + px
	py = coords[1] + py
	#hc.move((px, py), RandomTime.randTime(400, 0, 0, 1200, 9, 9)/1000)
	#pauto.moveTo(px, py, RandomTime.randTime(0, 2, 2, 0, 5, 5))
	#pauto.moveTo(px, py, random.randint(100, 250)/1000)
	pauto.moveTo(px, py, 0.1)

def moveFast(x, y):
	hc.move((x, y), random.randint(100, 250)/1000)

def click(btn):
	pauto.mouseDown(button=btn)
	time.sleep(RandomTime.randTime(0, 0, 0, 0, 3, 9))
	pauto.mouseUp(button=btn)

def moveClick(x, y, btn):
	moveTo(x, y)
	if btn == 1:
		pauto.mouseDown(button='left')
		time.sleep(RandomTime.randTime(0, 1, 0, 0, 2, 9))
		pauto.mouseUp(button='left')
	elif btn == 2:
		pauto.mouseDown(button='right')
		time.sleep(RandomTime.randTime(0, 1, 0, 0, 2, 9))
		pauto.mouseUp(button='right')
	time.sleep(RandomTime.randTime(0, 1, 0, 0, 2, 9))

def randCoord(pt, w, h):
    """Takes a top-left point as pt, and width and height of template
        returns a pair of coordinates within the the size of the template, to be used with inventory bag items only"""
    w = pt[0]+w
    h = pt[1]+h

    x = random.randint(pt[0],w)
    y = random.randint(pt[1],h)
    return x,y

def genCoords(x1, y1, x2, y2):
    """Returns random coords of passed coordinates, not relative to RS window"""
    x = random.randint(x1, x2)
    y = random.randint(y1, y2)
    return x, y

def randMove(x1, y1, x2, y2, btn):
    x, y = genCoords(x1, y1, x2, y2)
    if btn == 1:
        moveClick(x,y,1)
    elif btn == 2:
        moveClick(x,y,3)
    else:
        moveTo(x,y)

def mouse_loc():
	return pauto.position()