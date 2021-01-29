# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		THEODORE FREDERIK WATTIMENA
# Section:		554
# Assignment:	Lab 10B
# Date:		3/11/2019
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('WeatherDataWindows.csv')
dataf = pd.DataFrame({'Date':data['Date'], 'Temp Avg':data['Temp Avg'], 'Pressure Avg':data['Pressure Avg'], 'Precipitation (in.)':data['Precipitation (in.)'], 'Dew Point Avg':data['Dew Point Avg']})
print(dataf)

#Line Graph
fig, ax1 = plt.subplots()
#plt.plot('Date','Temp Avg', data = dataf)


color = 'red'
ax1.set_xlabel('Date')
ax1.set_ylabel('Temp Avg', color = color)
ax1.plot('Date','Temp Avg',color=color, data=dataf)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  

color = 'blue'
ax2.set_ylabel('Pressure Avg', color=color)  
ax2.plot('Date','Pressure Avg', color=color, data=dataf)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout() 
plt.suptitle('Line Graph')
plt.legend('Pressure Avg',loc=2)
plt.show()

#Histrogram
#print(dataf2)
mask = (dataf['Precipitation (in.)']>0) & (dataf['Precipitation (in.)'])
x = dataf[mask]
plt.hist(x['Precipitation (in.)'], normed=True, bins=30)
plt.suptitle('Histogram')
plt.legend('Precipitation (in.)',loc=2)
plt.show()

#Scatterplot
plt.scatter('Temp Avg','Dew Point Avg', data = dataf)
plt.xlabel('Temp Avg')
plt.ylabel('Dew Point Avg')
plt.suptitle('Scatter Plot')
plt.legend('Dew Point Avg',loc=2)
plt.show()

#Bar Graph
month1 = dataf.loc[dataf['Date'].str.startswith('1/')]
month2 = dataf.loc[dataf['Date'].str.startswith('2/')]
month3 = dataf.loc[dataf['Date'].str.startswith('3/')]
month4 = dataf.loc[dataf['Date'].str.startswith('4/')]
month5 = dataf.loc[dataf['Date'].str.startswith('5/')]
month6 = dataf.loc[dataf['Date'].str.startswith('6/')]
month7 = dataf.loc[dataf['Date'].str.startswith('7/')]
month8 = dataf.loc[dataf['Date'].str.startswith('8/')]
month9 = dataf.loc[dataf['Date'].str.startswith('9/')]
month10 = dataf.loc[dataf['Date'].str.startswith('10/')]
month11 = dataf.loc[dataf['Date'].str.startswith('11/')]
month12 = dataf.loc[dataf['Date'].str.startswith('12/')]

month1a = month1['Temp Avg']
list1 = month1a.values.tolist()
month1average = (sum(list1))/(len(list1))

month2a = month2['Temp Avg']
list2 = month2a.values.tolist()
month2average = (sum(list2))/(len(list2))

month3a = month3['Temp Avg']
list3 = month3a.values.tolist()
month3average = (sum(list3))/(len(list3))

month4a = month4['Temp Avg']
list4 = month4a.values.tolist()
month4average = (sum(list4))/(len(list4))

month5a = month5['Temp Avg']
list5 = month5a.values.tolist()
month5average = (sum(list5))/(len(list5))

month6a = month6['Temp Avg']
list6 = month6a.values.tolist()
month6average = (sum(list6))/(len(list6))

month7a = month7['Temp Avg']
list7 = month7a.values.tolist()
month7average = (sum(list7))/(len(list7))

month8a = month8['Temp Avg']
list8 = month8a.values.tolist()
month8average= (sum(list8))/(len(list8))

month9a = month9['Temp Avg']
list9 = month9a.values.tolist()
month9average = (sum(list9))/(len(list9))

month10a = month10['Temp Avg']
list10 = month10a.values.tolist()
month10average = (sum(list10))/(len(list10))

month11a = month11['Temp Avg']
list11 = month11a.values.tolist()
month11average = (sum(list11))/(len(list11))

month12a = month12['Temp Avg']
list12 = month12a.values.tolist()
month12average = (sum(list12))/(len(list12))

x = [1,2,3,4,5,6,7,8,9,10,11,12]
y = [month1average,month2average,month3average,month4average,month5average,month6average,month7average,month8average,month9average,month10average,month11average,month12average]

#Error Bar
month1high = max(list1)
month1low = min(list1)
month2high = max(list2)
month2low = min(list2)
month3high = max(list3)
month3low = min(list3)
month4high = max(list4)
month4low = min(list4)
month5high = max(list5)
month5low = min(list5)
month6high = max(list6)
month6low = min(list6)
month7high = max(list7)
month7low = min(list7)
month8high = max(list8)
month8low = min(list8)
month9high = max(list9)
month9low = min(list9)
month10high = max(list10)
month10low = min(list10)
month11high = max(list11)
month11low = min(list11)
month12high = max(list12)
month12low = min(list12)

monthhigh = [month1high,month2high,month3high,month4high,month5high,month6high,month7high,month8high,month9high,month10high,month11high,month12high]
monthlow = [month1low,month2low,month3low,month4low,month5low,month6low,month7low,month8low,month9low,month10low,month11low,month12low]
listupper = []
listlower = []
for i in range(12):
    diffhigh = monthhigh[i] - y[i]
    difflow = y[i]-monthlow[i]
    listupper.append(diffhigh)
    listlower.append(difflow)
    
#Plot
plt.bar(x,y,yerr=[listlower,listupper])
plt.ylabel('Avg Temperature')
plt.xlabel('Month')
plt.suptitle('Bar Graph')
plt.legend('Temperature Avg''Pressure Avg',loc = 2)
plt.show()