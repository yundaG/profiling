#! /usr/bin/python
import os
import commands
import time

request=8
cores=commands.getoutput('cat /proc/cpuinfo| grep "processor"| wc -l')
cores=eval(cores)
#quota=int((cores-request)*1.0/cores*100000)

quota= (cores-request)*100000

memTotal = 500
memRequest = 16


def run():
    id=commands.getoutput("docker run --name ibench_memCap --cpu-quota "+str(quota)+" -m "+str(memTotal-memRequest)+"G -d mirrors.tencent.com/cloudns/cloudrepo:memCap ./memCap 300")
    time.sleep(300)
    os.system("date")
    os.system("docker container stop ibench_memCap > /dev/null")
    os.system("docker container rm ibench_memCap > /dev/null")

os.system("date")
run()
os.system("date")
