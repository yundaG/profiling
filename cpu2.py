#! /usr/bin/python
import os
import commands
import time

def run():
    id=commands.getoutput("docker run --name ibench_cpu --cpuset-cpus 64-99 -d mirrors.tencent.com/cloudns/cloudrepo:cpu ./cpu 60 ")
    time.sleep(60)
    os.system("docker container stop ibench_cpu > /dev/null")
    os.system("docker container rm ibench_cpu > /dev/null")

os.system("date")
for i in range(1):
    run()
    print("ibench run times: "+str(i))
os.system("date")
