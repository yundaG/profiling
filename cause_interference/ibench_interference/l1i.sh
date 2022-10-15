#! /bin/bash
date +%s.%N
for ((i=0;i<128;i++))
do
        taskset -c $i ./l1i 10 0 &
done
wait
date +%s.%N
