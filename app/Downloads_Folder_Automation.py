import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from time import sleep
from datetime import datetime

from app.utils.file_extension_handler import file_extension_handler


class FileSystemEventHandlerCustom(FileSystemEventHandler):
    def on_created(self, event):
        print(datetime.now(), "A fost creat un fisier/director.")
        print(event.src_path, event.is_directory)
        self.run_handler(event)


    @staticmethod
    def run_handler(event):
        sleep(5)
        if not event.is_directory:
            all_files = (f for f in os.listdir(path_to_track) if os.path.isfile(os.path.join(path_to_track, f)))
            for file in all_files:
                file_full_path = os.path.join(path_to_track, file)
                file_extension_handler(file_full_path)


if __name__ == "__main__":
    # defining the path
    path_to_track = r"C:\Users\edarosr\Downloads"
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