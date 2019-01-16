#This script will download static files (images, .pdfs...) from existing list of URLs from an URLs.txt file in the same directory.
#The script will create a folder and add downloaded files there with filenames stripped of URLs and folder structure (as on the web server)

import urllib.request as req
import os
import time

urls = []

with open('URLs.txt') as fwurls:
    for line in fwurls:
        urls.append(line.strip())

#for testing-splitting
#file_name = urls[4].split('/')[-1]
#print(file_name)

def create_directory():
    """ Checks if there's an existing directory for Downloaded Files. If not, creates one."""
    global dirName
    dirName = 'Downloaded Files'
    global folder_path
    if os.path.isdir(dirName) == True:
        print("This folder already exists, path:", os.path.abspath(dirName))
    else:
        os.mkdir(dirName)
        global folder_path
        folder_path = os.path.abspath(dirName)
        print("Directory " , dirName ,  " Created ")

create_directory()

#for testing dir creation
#print(os.path.abspath(dirName))
#print(folder_path)


def download_file():
    "Goes through the list of URLs and downloades each one in pre-created folder with a specific (URL folder strucute stripped) file name"
    for lines in urls:
        try:
            req.urlretrieve(lines, '{0}/{1}'.format(folder_path, lines.split('/')[-1]))
            time.sleep(1)
            print ('File - {} - downloaded successfully'.format(lines.split('/')[-1]))
        except urllib.error.HTTPError:
            print('File is missing or not reachable')
    print('Download Complete & Successful!')

download_file()
