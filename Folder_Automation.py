import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from time import sleep
from datetime import datetime

# from app.utils import file_extension_handler
from utils import file_extension_handler


class FileSystemEventHandlerCustom(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print(datetime.now().strftime('%Y-%d-%m %H:%M:%S'), "A new file was created.")
            print(event.src_path)
            sleep(5)
            self.run_handler()

    @staticmethod
    def run_handler():
        all_files = (f for f in os.listdir(path_to_track) if os.path.isfile(os.path.join(path_to_track, f)))
        for file in all_files:
            file_full_path = os.path.join(path_to_track, file)
            file_extension_handler(file_full_path)


if __name__ == "__main__":
    # defining the path to be tracked
    # change here the path with your path
    path_to_track = r"C:\Users\...\Downloads"
    # initialize
    event_handler = FileSystemEventHandlerCustom()
    # initialize observer
    observer = Observer()
    # recursive=True - looks for events also on subfoders,
    # if recursive=False - looks just for the main folder
    observer.schedule(event_handler, path_to_track, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()
