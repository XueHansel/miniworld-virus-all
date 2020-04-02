import psutil
import os
import getpass
import time
import subprocess


def judgeprocess(processname):
    ret = 'none'
    pl = psutil.pids()
    for pid in pl:
        if psutil.Process(pid).name() == processname:
            ret = pid
            break
    return ret


while(True):
    if judgeprocess('v2.exe') == 0:
        path = 'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\v2.exe'
        os.popen(path)
    cmd = 'taskkill /F /IM MicroMiniNew.exe'
    res = subprocess.call(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(1)
