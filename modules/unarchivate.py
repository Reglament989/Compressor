import tarfile
import zipfile
import logging

class UnCompress():
	def __init__(self, root_pwd, archive_name):
		real_name = archive_name.split('.', maxsplit=1)[-1]
		if real_name == 'zip':
			self.unzip(root_pwd, archive_name)
		elif real_name == 'tar.xz':
			self.untar(root_pwd, archive_name, 'r:xz')
		elif real_name == 'tar.gz':
			self.untar(root_pwd, archive_name, 'r:gz')
		elif real_name == '':
			pass
		else:
			raise Exception('Cant unarhivate this.')
	
	def unzip(self, root_pwd, archive_name):
		with zipfile.ZipFile(root_pwd, 'r') as zip:
			test = zip.testzip()
			if test:
				logging.error(test)
			else:
				zip.extractall(root_pwd)

	def untar(self, root_pwd, archive_name, method_tar):
		pass
	