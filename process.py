import psutil
import os
import time
import signal



def taskkill():
    for proc in psutil.process_iter():
        if proc.name() == 'msedge.exe':
            processID = proc.pid
            signal.pthread_kill(processID)
            
taskkill()    
