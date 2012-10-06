#!/usr/bin/env python

import sys
import os
import html5lib
import requests
import getopt
from bs4 import BeautifulSoup

DESTINATION = "images"
SOURCE = None # TODO: make this accept a directory and do all files, including CSS
SOUP = None

def replace_originals():
    original_file = open(SOURCE, 'rw')
    original_file.read()
    new_images = os.listdir(DESTINATION)

def replace_images(images):
    global SOUP
    for image in images:
        src = image.attrs['src']
        try:
            r = requests.get(src)
            if r.status_code != 200:
                print 'nope'
                continue
    
            # a reasonably good approximation of most online image names
            name = src.split('.')[-2].split('/')[-1] + '.' + src.split('.')[-1]
            new_image_src = DESTINATION + '/' + name
            with open(new_image_src, 'w+') as f:
                f.write(r.content)
                f.close()

            image.attrs['src'] = new_image_src
        except:
            # TODO: account for local images already present.
            pass

    with open(SOURCE, 'w') as f:
        f.write(str(SOUP))

def open_file():
    global SOUP
    try:
        SOUP = BeautifulSoup(open(SOURCE))
        images = SOUP.find_all('img')
        replace_images(images)

    except:
        print "You crazy? Gimme a real file, man,"
        sys.exit(0)

def usage():
    print "usage: pic [-s FILE] [-d OPTIONAL IMAGE DIRECTORY - DEFAULTS TO IMAGES/]"

if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hd:s:", ["help", "destination=", "source="])
    except getopt.GetoptError, err:
        print str(err)
        usage()
        sys.exit(2)

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-d", "--destination"):
            DESTINATION = a.replace('/', '')
        elif o in ("-s", "--source"):
            SOURCE = a
        else:
            usage()
            sys.exit()
    
    if SOURCE == None:
        usage()
        sys.exit()

    if not os.path.exists(DESTINATION):
        os.makedirs(DESTINATION)

    open_file()

# TODO: rewrite in node.
