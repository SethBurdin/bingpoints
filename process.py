import psutil
import os
import time
import signal
##Pending Feature to enable custom browser selections
def processID():
    for proc in psutil.process_iter():
        if proc.name() == 'msedge.exe':
            EdgeID = proc.pid
            return EdgeID

def taskkill(processID):
   #signal.pthread_kill(processID)

#taskkill(processID)
