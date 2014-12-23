#
# compiles a week worth
#
#

import os
from datetime import date
from settings import *

def make_week():
    num = 0
    print "compiling week...",
    #next week to do
    for f in os.listdir(os.getcwd()):
        if f[0:4] == "week":
            if (int(f[5:6]) > num):
                num = int(f[5:6])

    fname = "week0" + str(num+1) + ".txt"
    f = open(fname,"w")
    for ff in os.listdir("0"+str(num+1)):
        if ff[0:3] == str(date.today().month)+"_":
            tf = open("0"+str(num+1)+SEP+ff)
            for t in tf:
                f.write(t)
    print "done"
                

if __name__ == "__main__":
    make_week()
