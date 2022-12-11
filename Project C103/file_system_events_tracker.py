import os
import shutil
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/sywon/OneDrive/Desktop/Coding/Python/Byjus python/Project C103/Watch"

# event handler
class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"{event.from_dir} has been created")

    def on_deleted(self, event):
        print(f"{event.from_dir} has been deleted")

    def on_moved(self, event):
        print(f"{event.from_dir} has been moved or renamed")

    def on_modified(self, event):
        print(f"{event.from_dir} has been modified")

# initialize event handler
event_handler = FileEventHandler()

# initialize observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)

# start the observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()