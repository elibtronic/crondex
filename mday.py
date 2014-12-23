
#
# Create skeleton of text file for today
#
#

from datetime import date
from os import path
from settings import *

def make_today():
    print "creating...",
    fname = str(date.today().month) + "_"+ str(date.today().day)+".txt"
    if path.exists(fname):
        print "file exist"
        return False
    else:
        f = open(fname, "w")
        f.write("#\n" + str(date.today().month) + "\n" + str(date.today().day) + "\n#\n\n") 
        f.write("## Today ##\n\n")
        f.write("## ETC ##\n\n")
        f.write("## Stuff ##\n\n")
        f.close()
        print "done"
        return True

if __name__ == "__main__":
    make_today()
