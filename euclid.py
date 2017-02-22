#!/usr/bin/python
import sys
def euclid(a,b):
    if(b==0):
        return a
    return euclid(b,a % b)
if(len(sys.argv)<2):
    x = input("Erste Zahl eingeben: ")
    y = input("Zweite Zahl eingeben: ")
else:
    x=int(sys.argv[1])
    y=int(sys.argv[2])
print 'Der groesste gemeinsame Teiler lautet %i.' % (euclid(x,y))
