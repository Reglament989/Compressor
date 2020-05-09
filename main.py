import tarfile
import os
import sys
# import argparser

ParentDir = os.getcwd()
MOD = 'TAR'
PLATFORM = sys.platform
OVER_SIZE = 1572864000 # 1,5 GB

if PLATFORM == 'win32' or PLATFORM == 'win64':
	splitter = '\\'
else:
	splitter = '/'


def main():
	print("ParentDir: ", ParentDir)
	dirs = [x[0] for x in os.walk(ParentDir)]
	for directory in dirs:
		print("Start selecting for directory - ", directory)
		Compress(directory)
		print("Successffull compress, ", directory)

def Compress(directory):
	name_archive = os.path.join(os.getcwd(), directory.split(splitter)[-1]) 
	files = os.listdir(directory)
	tar = tarfile.open(name_archive, 'x:xz')
	archives = [tar]
	memory = 0
	count = 0
	# try:
	for file in files:
		if os.isdir(file):
			continue
		absolute_path_file = os.path.join(directory, file)
		file_size = os.getsize(absolute_path_file)
		memory + file_size
		if memory > OVER_SIZE:
			count += 1
			name_archive = os.path.join(os.getcwd(), directory.split(splitter)[-1] + f'_{count}') 
			archives[-1].close()
			archives.append(tarfile.open(name_archive))
		archives[-1].add(absolute_path_file)
	# except Exception as e:
	# 	raise e
	# finally:
	# 	try:
	# 		for archive in archives:
	# 			archive.close()
	# 	except:
	# 		pass
		

# def main():
# 	get_dirs()