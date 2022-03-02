"""
Check if file extension is in extensions directories, if it is it will move the file to the corresponding directory,
if not it will do nothing
"""
import os
import shutil
from utils.directory_validator import directory_validator

documents = {'.key', '.odp', '.pps', '.ppt', '.pptx', '.ods', '.xls', '.xlsm', '.xlsx',
             '.doc', '.docx', '.odt', '.pdf', '.rtf', '.tex', '.txt', '.wpd', '.csv', '.xml'}
audios = {'.aif', '.cda', '.mid', '.midi', '.mp3', '.mpa', '.ogg', '.wav', '.wma', 'wpl'}
videos = {'.3g2', '.3gp', '.avi', '.flv', '.h264', '.m4v', '.mkv', '.mov', '.mp4', '.mpg',
         '.mpeg', '.rm', '.swf', '.vob', '.wmv'}
images = {'.ai', '.bmp', '.gif', '.ico', '.jpeg', '.jpg', '.png', '.ps', '.psd', '.svg', '.tif', '.tiff', '.jfif'}
archives = {'.7z', '.arj', '.deb', '.pkg', '.rar', '.rpm', '.tar', '.gz', '.zip'}


def file_extension_handler(file):
    """

        file (str): file path to be checked

    Returns:

    """
    parent_dir, file_name = os.path.split(file)
    file_extension = os.path.splitext(file_name)[1].lower()
    for dir_name, extensions in zip(['Documents', 'Audios', 'Videos', 'Images', 'Archives'],
                                    [documents, audios, videos, images, archives ]):
        if file_extension in extensions:
            directory_validator(parent_dir, dir_name)
            new_path_file = os.path.join(parent_dir, dir_name, file_name)
            shutil.move(file, new_path_file)
            break
