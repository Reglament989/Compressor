import tarfile
import os
import sys
import argparse
from utils import Color

parser = argparse.ArgumentParser(description='Easy arhivate your data with this script')
parser.add_argument("-cb", action='store_true', help="Contribute https://gihub.com/Reglament989/Compressor")
parser.add_argument("-zip", action='store_true', help="Pass this option for use zip, default tar")
parser.add_argument("-debug", action='store_true', help="More info on shell")
parser.add_argument("-passwd", type=str, help="Add for archives password", metavar='<Password>')
parser.add_argument('-max_size', type=int, help="Max size for one archive", metavar='<int>')



if sys.platform == 'win32' or sys.platform == 'win64':
	splitter = '\\'
	Color.setup_windows()
else:
	splitter = '/'


ParentDir = os.getcwd()
try:
	GitDirs = [x[0] for x in os.walk(os.path.join(ParentDir, '.git'))]
except:
	GitDirs = []
MOD = 'TAR'
OVER_SIZE = 1048576000 # 1 GB


def get_dirs():
	print(f"{Color.Red}ParentDir: {ParentDir}{Color.Clear}")
	dirs = [x[0] for x in os.walk(ParentDir)]
	for directory in dirs:
		if directory == ParentDir or directory in GitDirs:
			continue
		print(f"{Color.Yellow}Start selecting for directory - {directory}{Color.Clear}")
		Compress(directory)
		print(f"{Color.Blue}Successffull compress, {directory}{Color.Clear}")

def Compress(directory):
	name_archive = os.path.join(os.getcwd(), directory.split(splitter)[-1] + '.tar.xz') 
	files = os.listdir(directory)
	tar = tarfile.open(name_archive, 'x:xz')
	archives = [tar]
	memory = 0
	count = 0
	try:
		for file in files:
			if os.path.isdir(file):
				continue
		else:
			absolute_path_file = os.path.join(directory, file)
			file_size = os.path.getsize(absolute_path_file)
			memory + file_size
			if memory > OVER_SIZE:
				count += 1
				name_archive = os.path.join(os.getcwd(), directory.split(splitter)[-1] + f'_{count}' + '.tar.xz') 
				archives[-1].close()
				archives.append(tarfile.open(name_archive))
			with open(absolute_path_file, 'rb') as f:
				fileobj = f.read()
			tarinfo = tarfile.TarInfo(file)
			print(f"{Color.Green}Append {file} to {archives[-1].name}, Size - will be soon {Color.Clear}")
			archives[-1].addfile(tarinfo, fileobj)
	except Exception as e:
		raise e
	finally:
		try:
			for archive in archives:
				archive.close()
		except:
			pass
		
def started_cli():
	if sys.platform == 'win64' or sys.platform == 'win32':
		os.system('cls')
	else:
		os.system('clear')
	print(f"""
{Color.Yellow}Hello this app arhivate all directory for parrent dir of script.{Color.Clear}
{Color.Green}Run script with options -h for more help{Color.Clear}
{Color.Blue}Author - Reglament989{Color.Clear}\n\n""")
	get_dirs()

def main():
	args = parser.parse_args()
	print(args)
	if args.cb:
		print(Color.Blue, 'My github: https://github.com/Reglament989', Color.Clear)
		sys.exit(0)
	if args.debug:
		DEBUG = True
	if args.zip:
		print(Color.Red, 'Coming soon, please use tar', Color.Clear)
	if args.passwd:
		print(Color.Red, 'Coming soon', Color.Clear)
	started_cli()

if __name__ == '__main__':
	main()
