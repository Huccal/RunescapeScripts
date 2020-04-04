import os
import subprocess
import win32gui as wgui
import pyautogui as pauto

from modules import WindowMgr

class Window():
	def __init__(self):
		self.window_ID = self.window_selection()
		self.position = None
		if self.position == None:
			#self.center_window()
			self.default_position()
			self.window_stats()

	def window_selection(self, window_n = None):
		w = WindowMgr.WindowMgr()
		w.find_window_wildcard("RuneLite")
		w.set_foreground()
		return w._handle

	def window_stats(self):
		win_geometry = wgui.GetWindowRect(self.window_ID)
		x = win_geometry[0]
		y = win_geometry[1]
		w = win_geometry[2] - x
		h = win_geometry[3] - y
		self.position = (x, y)
		return [x, y, w , h]

	def center_window(self):
		screen_width, screen_height = pauto.size()
		win_geometry = self.window_stats()
		wgui.MoveWindow(self.window_ID, int(screen_width/3), int(screen_height/3), win_geometry[2], win_geometry[3], True)

	def default_position(self):
		win_geometry = self.window_stats()
		wgui.MoveWindow(self.window_ID, 0, 0, win_geometry[2], win_geometry[3], True)

if __name__ == '__main__':
	w = Window()