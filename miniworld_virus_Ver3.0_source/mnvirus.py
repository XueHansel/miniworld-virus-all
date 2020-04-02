# -*- coding:utf-8 -*-

import time
import subprocess


while(1):
    try:
        cmd = 'taskkill /F /IM MicroMiniNew.exe'
        res = subprocess.call(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(1)
    except:
        continue