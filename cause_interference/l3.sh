#! /bin/bash
cores=`cat /proc/cpuinfo| grep "processor"| wc -l`
date +%s.%N
for ((i=0;i<${cores};i++))
do
        taskset -c $i ./l3 10 &
done
wait
date +%s.%N
