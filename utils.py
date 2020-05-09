
class Color:
	Red="\033[31m"
	Blue="\033[34m"
	Green = "\033[32m"
	Yellow = "\033[33m"
	Clear="\033[0m"

	def setup_windows():
		import ctypes
		kernel32 = ctypes.windll.kernel32
		kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)


