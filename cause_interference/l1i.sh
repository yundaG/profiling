#! /bin/bash
cores=`cat /proc/cpuinfo| grep "processor"| wc -l`
date +%s.%N
for ((i=0;i<${cores};i++))
do
        taskset -c $i ./l1i 1 0 &
done
wait
date +%s.%N
