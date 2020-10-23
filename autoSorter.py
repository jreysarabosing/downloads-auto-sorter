import os
import shutil
import fnmatch
from dotenv import load_dotenv
from pathlib import Path

# Setting folder paths from .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

for file in os.listdir(os.environ['DOWNLOADS_PATH']):
	if fnmatch.fnmatch(file, '*.jpg'): #TODO other picture file types
		shutil.move(file, os.environ['PICTURES_PATH']) 
	#TODO Other folders sorting
	