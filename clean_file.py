#!/usr/bin/python
import os

dir = "/Library/WebServer/Documents/htdocs/sooc_new"

def clean_file(dir, name):
    list = os.listdir(dir)
    for v in list:
        file = dir + os.path.sep + v
        if os.path.isdir(file):
            clean_file(file, name)
        else:
            if os.path.isfile(file) and v == name:
                print file
                os.remove(file)

if __name__ == '__main__':
    clean_file(dir, '.DS_Store')
