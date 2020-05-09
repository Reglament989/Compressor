import tarfile
import os
import sys
# import argparser

ParentDir = os.getcwd()
GitDirs = [x[0] for x in os.walk(os.path.join(ParentDir, '.git'))]
MOD = 'TAR'
PLATFORM = sys.platform
OVER_SIZE = 1048576000 # 1 GB

if PLATFORM == 'win32' or PLATFORM == 'win64':
	splitter = '\\'
else:
	splitter = '/'


def main():
	print("ParentDir: ", ParentDir)
	dirs = [x[0] for x in os.walk(ParentDir)]
	for directory in dirs:
		if directory == ParentDir or directory in GitDirs:
			continue
		print("Start selecting for directory - ", directory)
		Compress(directory)
		print("Successffull compress, ", directory)

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
			print(f"Append {absolute_path_file} to {archives[-1]}\n\tSize: {tarinfo.size}\n")
			archives[-1].addfile(tarinfo, fileobj)
	except Exception as e:
		raise e
	finally:
		try:
			for archive in archives:
				archive.close()
		except:
			pass
		

# def main():
# 	get_dirs()

if __name__ == '__main__':
	main()
