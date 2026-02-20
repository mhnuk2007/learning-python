""" url-errors.py - Trying to Download Things That Don't Exist """

import urllib.request

try:
    webpage = urllib.request.urlopen('http://www.godogle.com')
except urllib.error.URLError:
    print('Could not access webpage!')
else:
    for line in webpage:
        print(line)