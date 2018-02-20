import os
import time

hour = 3600 
multiplier = 2
startTime = time.time()
finishTime = startTime + (hour * multiplier)

print ("Computer will shut down in:")

while time.time() < finishTime:
    print (time.strftime("%H:%M:%S", time.gmtime(finishTime - time.time())))
    time.sleep(1)

print ("done")
os.system("shutdown.exe /s")

