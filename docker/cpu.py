#! /usr/bin/python
import os
import commands
import time

request=8
cores=commands.getoutput('cat /proc/cpuinfo| grep "processor"| wc -l')
cores=eval(cores)
#print(cores)
quota=int((cores-request)*100000)
#print(quota)

def run():
    id=commands.getoutput("docker run --name ibench_cpu --cpuset-cpus 0-"+str(cores-1)+" --cpu-quota "+str(quota)+" -d mirrors.tencent.com/cloudns/cloudrepo:cpu ./cpu 60 ")
    time.sleep(60)
    os.system("docker container stop ibench_cpu > /dev/null")
    os.system("docker container rm ibench_cpu > /dev/null")

os.system("date")
for i in range(8):
    run()
    print("ibench run times: "+str(i))
os.system("date")
