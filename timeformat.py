# Design a Python Script to determine the time difference between two given times in HH:MM:SS format
    
# import date time Module
from datetime import datetime as dtm  
t1=input('enter time in HH:MM:SS:')
t2=input('enter time in HH:MM:SS:')
format= "%H:%M:%S"  # format Time

def timedifference(time1, time2):
        try:
                t1 = dtm .strptime(time2,format)-dtm.strptime(time1, format)
                return t1
        except Exception as e:
                print(e)
                return e
        return (t2 - t1)
print(timedifference(t1,t2))
