#! /bin/bash
date +%s.%N
for ((i=0;i<128;i++))
do
        taskset -c $i ./l2 50000 &
done
wait
date +%s.%N
