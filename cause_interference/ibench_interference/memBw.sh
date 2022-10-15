#! /bin/bash
date +%s.%N
for ((i=0;i<128;i++))
do
        taskset -c $i ./memBw 100 &
done
wait
date +%s.%N
