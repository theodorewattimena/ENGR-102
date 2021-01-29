# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		THEODORE FREDERIK WATTIMENA
# Section:		554
# Assignment:	Lab 11B
# Date:		5/11/2019
import numpy as np

filename = str(input('Input file name:'))
xuser = float(input('Input X-value:'))
userinput = open(filename,'r')
data = np.loadtxt(userinput,skiprows=0)
xsorted = np.argsort(data[:,0])
sortedlist = data[xsorted]

#Interpolating Formula
if float(xuser) < (3.141592653589793):
    def interpolation():
        for i in range (len(sortedlist)):
            while sortedlist[i+1][0]>(xuser) and sortedlist[i][0]<(xuser):
                yy1 = (((sortedlist[i+1][1])-(sortedlist[i][1]))/((sortedlist[i+1][0])-(sortedlist[i][0])))*(xuser-sortedlist[i][0])+sortedlist[i][1]
                yy2 = (((sortedlist[i+1][2])-(sortedlist[i][2]))/((sortedlist[i+1][0])-(sortedlist[i][0])))*(xuser-sortedlist[i][0])+sortedlist[i][2]
                yy3 = (((sortedlist[i+1][3])-(sortedlist[i][3]))/((sortedlist[i+1][0])-(sortedlist[i][0])))*(xuser-sortedlist[i][0])+sortedlist[i][3]
                i+=1
                print(yy1,yy2,yy3)
                return(yy1,yy2,yy3)
interpolation()

#Extrapolation
if float(xuser) > (float(3.141592653589793)):
    x = []
    y1 = []
    y2 = []
    y3 = []
    xy1 = []
    xy2 = []
    xy3 = []
    dslope = []

    for i in range (len(data)):
        x.append(data[i][0])
        y1.append(data[i][1])
        y2.append(data[i][2])
        y3.append(data[i][3])

#Mean of X and Y Values
    xaverage = sum(x)/(len(x))
    y1average = sum(y1)/(len(y1))
    y2average = sum(y2)/(len(y2))
    y3average = sum(y3)/(len(y3))

#Finding the slope of the best fit line
    for i in range (len(data)):
        xy1val = ((x[i]-xaverage)*(y1[i]-y1average))
        xy1.append(xy1val)
        dslopeval = ((x[i]-xaverage)**2)
        dslope.append(dslopeval)
        xy2val = ((x[i]-xaverage)*(y2[i]-y2average))
        xy2.append(xy2val)
        xy3val = ((x[i]-xaverage)*(y3[i]-y3average))
        xy3.append(xy3val)
    
#Finding the Y Intercept
    b1 = y1average - (sum(xy1)/sum(dslope))*xaverage
    b2 = y2average - (sum(xy2)/sum(dslope))*xaverage
    b3 = y3average - (sum(xy3)/sum(dslope))*xaverage

#Best Fit Line
    bestfitline1 = ((sum(xy1))/(sum(dslope)))*xuser + b1
    bestfitline2 = ((sum(xy2))/(sum(dslope)))*xuser + b2
    bestfitline3 = ((sum(xy3))/(sum(dslope)))*xuser + b3
    print(bestfitline1,',',bestfitline2,',',bestfitline3)
