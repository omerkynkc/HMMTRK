#fix which days error
import time
from math import floor
#work in progres.. the program that shows how many minutes to next coming rk for Sarıtepe Campus

weekday = ("07.00", "08.00", "09.00", "09.55", "10.35", "12.15", "13.05", "13.50", "14.55", "15.35", "16.15", "17.30", "18.35", "19.15", "20.35", "21.15", "22.00", "23.55")
saturday = ("07.20", "08.45", "10.00", "11.10", "12.25", "13.40", "15.00", "16.15", "17.45", "19.15", "20.35", "21.50", "23.55")
sunday = ("08.45", "11.15", "13.45", "16.15", "19.15", "19.45", "21.50","22.15", "23.55")
mekik = ("17.00")
def calc():
    cd = time.strftime("%c")
    if cd == "Sun":
        day = sunday
    elif cd == "Sat":
        day = saturday
    else:
        day = weekday
    cm = time.strftime("%M")
    ch = time.strftime("%H")
    cs = time.strftime("%S") 
    currentL = (2000,1,1,int(ch),int(cm),int(cs),1,1,1)
    currentT = time.mktime(currentL)    
    timedelta = 0 # bus time - current time
    count = 0 #bus number from 0 to how many buses on that day
    while timedelta <= 0: #I am trying to find when is the next bus
        bh, bm = day[count].split(".")
        busL = (2000,1,1,int(bh),int(bm),0,1,1,1)
        busT = time.mktime(busL)
        sub = busT - currentT
        if sub > 0:
            break
        count += 1
    return ("Remaining to 59RK: {}.{}".format(round(sub//3600),floor(sub/60%60)))

