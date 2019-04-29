# Design a Python script to determine the difference in date for given two dates in YYYY:MM:DD format

# import datetime Module
from datetime import datetime as dtm
dt1=input('enter date in YY-MM-DD:').strip()
dt2=input('enter date in YY-MM-DD:').strip()
format= "%Y-%m-%d" # date format

def datedifference(date1, date2): 
        try:
                dt1 = dtm .strptime(date1,format)
                dt2 = dtm.strptime(date2, format)
        except Exception as e:
                print(e)
                return e
        return (dt2 - dt1)
print(datedifference(dt1,dt2))
