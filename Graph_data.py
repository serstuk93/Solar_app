from datetime import time, timedelta, datetime
import numpy as np


startday= time(hour=0,minute=0,second=0)
acttday= time(hour=0,minute=0,second=0)
acttday2= time(hour=0,minute=6,second=0)
print(startday)
print(type(startday))
endday= time(hour=23,minute=59,second=59)
n=6
x,y=[],[]

date_and_timeS = datetime(2020, 2, 19, 0, 0, 0)
date_and_timeAC = datetime(2020, 2, 19, 0, 0, 0)
date_and_timeE = datetime(2020, 2, 19, 23, 59, 59)
# while date_and_timeAC<date_and_timeE:
#     date_and_timeAC= date_and_timeAC + timedelta(minutes=6)
#     xt = str(date_and_timeAC)
#     print(xt)
#     xt2= xt[-8:]
#  #   xt= str(date_and_timeAC[-8:])
#     x.append(xt2)
  #  print(date_and_timeAC)

for i in np.arange(0, 240, 1):
    y.append(i)
for i in np.arange(0, 240, 1):
    x.append(i)
print(x)
print(y)
print(len(x))
print(len(y))
print(type(y[58]))
print(type(x[58]))
jj= np.datetime64('2005-02-25T03:30')
jj=jj  + np.timedelta64(12, 'm')
print(jj)