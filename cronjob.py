import os
from time import time

files = os.listdir(".\media")
for file in files:
    timefive = round(time(), 0) - 300
    timecreated = (round(os.path.getmtime("media\\" + file), 0))
    if timefive >= timecreated:
        os.remove("media\\" + file)
    else:
        pass

