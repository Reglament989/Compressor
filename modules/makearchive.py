import tarfile
import zipfile
import os
import sys
from threading import Thread
import logging

if sys.platform == 'win32' or sys.platform == 'win64':
	splitter = '\\'
else:
	splitter = '/'

def join_thread(fn):
    def wrapper(*args, **kwargs):
        print(fn)
        th = Thread(target=fn, args=(args, kwargs),)
        th.start()
        th.join()
    return wrapper


class Compress:
    # @join_thread 

    def make_zip(root_dir=os.getcwd(), name, compression=zipfile.ZIP_LZMA):
        logging.debug(name)
        if name != "archive.zip":
            if name.endswith('.zip'):
                pass
            else:
                name += ".zip"
        with zipfile.ZipFile(file=name, mode='w', compression=compression) as zip:
            files = os.listdir()
            for file in files:
                if (os.path.isdir(file) or file == '.gitignore'
                 or file.endswith('.zip')
                 or file.endswith('.tar.*')
                 or file.split(splitter)[-1] == __file__):
                    continue
                else:
                    logging.debug(f"Archivate - {file}")
                    path = os.path.join(root_dir, file)
                    zip.write(path, arcname=file)
                    
            # logging.debug(__file__)
                    

    # @join_thread
    def make_tar(root_dir, mode='xz', arc_name="archive.tar."):
        name = f"{arc_name}{mode}"
        files = os.listdir(root_dir)
        for file in files:
            if os.path.isdir(file):
                continue
            else:
                tarinfo = tarfile.TarInfo(file)
                with open(os.path.join(root_dir, file), 'rb') as f:
                    fileobj = f.read()
                    with tarfile.open(name=name, mode=f"x:{mode}") as tar:
                        tar.addfile(tarinfo, fileobj)

    