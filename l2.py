#! /usr/bin/python
import os
import commands
import time

request=8
cores=commands.getoutput('cat /proc/cpuinfo| grep "processor"| wc -l')
cores=eval(cores)
#print(cores)
quota=int((cores-request)*1.0/cores*100000)
#print(quota)

def run():
    #containers=[]
    for i in range(cores):
        id=commands.getoutput("docker run --name ibench_l2_"+str(i)+" --cpuset-cpus "+str(i)+" --cpu-quota "+str(quota)+" -d mirrors.tencent.com/cloudns/cloudrepo:l2 ./l2 300")
        #containers.append(id)
        #path=commands.getoutput("find /sys/fs/cgroup/cpu/ -name "+id+"*")
    time.sleep(300)
    os.system("date")
    for i in range(cores):
        os.system("docker container stop ibench_l2_"+str(i)+" > /dev/null")
        os.system("docker container rm ibench_l2_"+str(i)+" > /dev/null")

os.system("date")
run()
os.system("date")
