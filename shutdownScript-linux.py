import os
import time
import sys

hour = 3600
multiplier = 2

if len(sys.argv) > 1:
    if sys.argv[1].isnumeric():
        multiplier = int(sys.argv[1])

startTime = time.time()
finishTime = startTime + (hour * multiplier)

print("Type a number after the name of the script to specify how many hours you wish to wait before the computer turns off. For example, \"shutdownScript.py 3\". By default, this is set to two.")
print("")
print("Computer will shut down in " + str(multiplier) + " hours")

while time.time() < finishTime:
    print (time.strftime("%H:%M:%S", time.gmtime(finishTime - time.time())))
    time.sleep(1)

print ("done")
os.system("shutdown now -h")
