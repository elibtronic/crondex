
#
# Create skeleton of text file for today
#
#

from datetime import date
from os import path
from settings import *

def make_today():

    if len(str(date.today().month)) == 1:
        t_month = "0" + str(date.today().month)
    else:
        t_month = str(date.today().month)

    if len(str(date.today().day)) == 1:
        t_day = "0" + str(date.today().day)
    else:
        t_day = str(date.today().day)

    
    print "creating...",
    fname = t_month + "_" + t_day +".txt"
    if path.exists(fname):
        print "file exist"
        return False
    else:
        f = open(fname, "w")
        f.write("#\n" + t_month + "\n" + t_day + "\n#\n\n") 
        f.write("## Today ##\n\n")
        f.write("## ETC ##\n\n")
        f.write("## Stuff ##\n\n")
        f.close()
        print "done"
        return True

if __name__ == "__main__":
    make_today()
