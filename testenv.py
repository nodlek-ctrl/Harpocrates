import os
import signal
import psutil
print("BCUA Soft Kill Started.")

process_name = "Taskmgr"
pid = None

for proc in psutil.process_iter():
    if process_name in proc.name():
       pid = proc.pid
       break

os.kill(pid, signal.SIGILL)