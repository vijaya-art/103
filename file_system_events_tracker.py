import os
import shutil
import random
import time
import sys
import logging

from watchdog.observers import observer
from watchdog.events import filesystemeventhandler

from_dir='c:users/singh'

class FileEventHandler(filesystemeventhandler):
	def on_created(self,event):
		print(f"{event.src_path}has been created")

	def on_deleted(self,event):
		print(f"{event.src_path}has been deleted")

	def on_modified(self,event):
		print(f"{event.src_path}has been modified")

	def on_moved(self,event):
		print(f"{event.src_path}has been moved")

event_handler=FileEventHandler()
observer=observer()
observer.schedule(event_handler,from_dir,recursive=true)
observer.start()

try:
	while True:
		time.sleep(2)
	except keyboardInterrupt:
		observer.stop()
