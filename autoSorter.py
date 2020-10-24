import os
import shutil
from fnmatch import fnmatch
from dotenv import load_dotenv
from pathlib import Path

# Setting folder paths from .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
downloads_path = os.environ['DOWNLOADS_PATH']

for file in os.listdir(os.environ['DOWNLOADS_PATH']):
	try:
		# PICTURES
		if fnmatch(file, '*.jpg') or fnmatch(file, '*.png'):
			shutil.move(downloads_path + file, os.environ['PICTURES_PATH'])
		# DOCUMENTS
		elif fnmatch(file, '*.docx') or fnmatch(file, '*.xlsx') or fnmatch(file, '*.pdf') or fnmatch(file, '*.pptx'):
			shutil.move(downloads_path + file, os.environ['DOCUMENTS_PATH'])
		# MUSIC
		elif fnmatch(file, '*.mp3'):
			shutil.move(downloads_path + file, os.environ['MUSIC_PATH'])
		# VIDEOS
		elif fnmatch(file, '*.mp4') or fnmatch(file, '*.avi'):
			shutil.move(downloads_path + file, os.environ['MUSIC_PATH'])
		# ALL OTHER FILES
		else:
			print('FILE: ' + file + ' file type not supported.')
	except(shutil.Error):
		#TODO PLACEHOLDER TEXT
		print("Wow")