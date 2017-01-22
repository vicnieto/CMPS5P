#!/usr/bin/python3
# Assignment 1
# CMPS 5P, Fall 2016
# Victor Nieto
# vnieto@ucsc.edu
#Now using python 3
l = float(input("what is the straightaway length (in yards): "))
r = float(input("What is the turn radius of the track (in yards): "))
w = float(input("What is the track width (in feet): "))
d = float(input("What is the track depth (in inches): "))

#converting length to meters.
# Conversion from google query: Yards to meters
l = l * 0.9144

#converting radius to meters
# Conversion from google query: Yards to meters
r = r * .9144

#convert width to meters
# Conversion from google query: feet to meters
w = w * .3048

#convert depth to meters
# Conversion from google query: inches to meters
d = d * 0.0254

#Value of pi found on google
#Query: pi
pi = 3.14159265359

#volume is l*w*d
#multiply by 2 because there are 2 straightaways
volumeStraight = l*w*d*2

areaSmall = (r**2) * pi

areaBig= ((r + w)**2) * pi

areaTurn = areaBig - areaSmall

volumeTurn = areaTurn * d

totalVolume = volumeStraight + volumeTurn

print("Total volume of dirt (in cubic meters) is " + str(totalVolume))

#it worked



