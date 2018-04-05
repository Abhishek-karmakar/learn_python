import random
import sys
import os

# functions : Reuse the code. 

def addnumber(fnum, lnum):
	snum = fnum + lnum
	return snum

print(addnumber(1,4))


def getinputfromuser():
	print("Please enter your name")
	name = sys.stdin.readline()
	print ('Helo' , name)

getinputfromuser()

