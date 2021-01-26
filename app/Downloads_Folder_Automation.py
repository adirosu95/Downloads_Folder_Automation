import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class FileSystemEventHandlerCustom(FileSystemEventHandler):
    def on_moved(self, event):
        print("A fost mutat un fisier/director.")
        print(event.src_path)
        print(event.is_directory)

    def on_created(self, event):
        print("A fost creat un fisier/director.")
        print(event.src_path)
        print(event.is_directory)

    def on_deleted(self, event):
        print("A fost sters un fisier/director.")
        print(event.src_path)
        print(event.is_directory)

    def on_modified(self, event):
        print("A fost modificat un fisier/director.")
        print(event.src_path)
        print(event.is_directory)


if __name__ == "__main__":
    # defining the path
    path_to_track = r"C:\Users\edarosr\Downloads"
    # initialize
    event_handler = FileSystemEventHandlerCustom()
    # initialize observer
    observer = Observer()
    # recursive=True - looks for events also on subfoders,
    # if recursive=False - looks just for the main folder
    observer.schedule(event_handler, path_to_track, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()