import math
import time
from datetime import *


def toswatch(a):
    t = tostr(a)
    tot = 0
    (h, m, s) = t.split(":")
    tot += int(h) * 3600
    tot += int(m) * 60
    tot += int(s)
    tot /= 86.4
    return tot


def gettime():
    return datetime.now().time()


def tostr(a):
    return a.strftime("%H:%M:%S")

def getdate():
    return datetime.now().date()

def toWorld(a):
    d = a.strftime("%Y-%j")
    (y,d) = d.split("-")
    d = int(d)
    year = int(y) + 9700
    month = ""
    if 1 <= d <= 31:
        month = "Ianuarius"
        day = d
    elif 32 <= d <= 61:
        month = "Februarius"
        day = d - 31
    elif 62 <= d <= 91:
        month = "Martius"
        day = d - 61
    elif 92 <= d <= 121:
        month = "Aprilis"
        day = d - 91
    elif 122 <= d <= 152:
        if d == 122 and year % 4 == 0 and year % 1000 != 0:
            month = "Leapyear day"
            day = ""
            d -= 1
        else:
            month = "Maius"
            day = d - 121
    elif 153 <= d <= 182:
        month = "Iunius"
        day = d - 152
    elif 183 <= d <= 213:
        month = "Iulius"
        day = d - 182
    elif 214 <= d <= 243:
        month = "Augustus"
        day = d - 213
    elif 244 <= d <= 273:
        month = "September"
        day = d - 243
    elif 274 <= d <= 304:
        month = "October"
        day = d - 273
    elif 305 <= d <= 334:
        month = "November"
        day = d - 304
    elif 335 <= d <= 364:
        month = "December"
        day = d - 334
    elif d == 365:
        month = "Worldsday"
        day = ""
    
    return "{} {} {}".format(year, month, day)