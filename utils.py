import sys
import random
import zipfile
import os
import secrets
import string
import time
import json
import logging

logging.basicConfig(
	format="%(filename)s[LINE:%(lineno)d] - %(message)s",
	level=logging.INFO,
)

class Color:
	Red="\033[31m"
	Blue="\033[34m"
	Green = "\033[32m"
	Yellow = "\033[33m"
	Clear="\033[0m"

	def setup_windows(self=None):
		import ctypes
		kernel32 = ctypes.windll.kernel32
		kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

if sys.platform == 'win32' or sys.platform == 'win64':
	splitter = '\\'
	cmd = 'cls'
	Color.setup_windows()
else:
	splitter = '/'
	config_dir = '~/.config/py_compressor'
	os.mkdir(config_dir)
	cmd = 'clear'

class ScreenConfig():
	def __init__(self):
		self.screen = 0
		self.screen_comprs = 0
	
	def render(self):
		os.system(cmd)
		if self.screen == 0:
			print("""
	Please entry number configuration:
		1.Type compression
		2.Type arhivator to default
		0.Exit
""")
		elif self.screen == 1:
			print("""
	Arhivator:
		1.Zip
		2.Tar
		0.Exit
""")
		elif self.screen == 3:
			if self.screen_comprs == 1:
				print("""
	Zip compressions:
		1.BZIP2
		2.ZIP_DEFLATED
		3.ZIP_LZMA
		4.ZIP_STORED
		0.Exit
""")
			elif self.screen_comprs == 2:
				print("""
	Tar compressions:
		1.Gzip compressions
		2.bzip2 compressions
		3.lzma compressions
		4.Without compression
		0.Exit
""")
		elif self.screen == 2:
			print("""
	Default arhivator:
		1.Zip
		2.Tar
		0.Exit
""")
		while True:
			logging.info(f"State: {self.screen}")
			self.new_screen = input("\n>> ")
			try:
				self.new_screen = int(self.new_screen)
			except:
				print("Try integer.")
				time.sleep(0.5)
				self.render()
			if self.new_screen == 0:
				sys.exit(0)
			if self.new_screen > 4 or self.new_screen < 0:
				self.render()

			if self.screen == 0:
				if self.checkScreen(1,2):
					self.screen = self.new_screen
					self.render()
					break
				else:
					continue
			elif self.screen == 1:
				if self.checkScreen(1,2):
					self.screen_comprs = self.new_screen
					self.screen = 3
					break
				else:
					continue
			elif self.screen == 2:
				if self.checkScreen(1,2):
					print("Ok")
					sys.exit(0)
				else:
					continue
			elif self.screen == 3:
				if self.checkScreen(1,4):
					if self.screen_comprs == 1: # ZIP
						arhivator = 'zip'
						if self.new_screen == 1:
							cs = BZIP2
						elif self.new_screen == 2:
							cs = zipfile.ZIP_DEFLATED
						elif self.new_screen == 3:
							cs = zipfile.ZIP_LZMA
						elif self.new_screen == 4:
							cs = zipfile.ZIP_STORED
					elif self.screen_comprs == 2: # TAR
						arhivator = 'tar'
						if self.new_screen == 1:
							cs = 'gz'
						elif self.new_screen == 2:
							cs = 'bz2'
						elif self.new_screen == 3:
							cs = 'xz'
						elif self.new_screen == 4:
							cs = 'None'
					self.dump_config(var="compressions", value=cs, t_arc=arhivator)
					self.screen = 0
					break
				else:
					continue
		self.render()

	def dump_config(self, var, value, t_arc):
		path = os.path.join(config_dir, 'config.json')
		with open(path, 'r') as j_file:
			current_config = json.load(j_file)
		current_config[t_arc][var] = value
		with open(path, 'w') as j_file:
			json.dump(current_config, j_file)

	def checkScreen(self, min_screen, max_screen):
		if self.new_screen < max_screen and self.new_screen > min_screen:
			print(f"{min_screen}{max_screen}")
			return False
		else:
			return True
	
	def clear(self):
		self.screen = 0
		self.screen_comprs = 0


def rand_pwd():
	name = string.ascii_letters + string.digits

	password = "".join([secrets.SystemRandom().choice(name) for i in range(secrets.SystemRandom().randrange(8, 10))])
	return password

