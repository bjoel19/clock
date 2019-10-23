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
    return round(tot, 2)


def gettime():
    return datetime.now(timezone.utc).time()


def tostr(a):
    return a.strftime("%H:%M:%S")
