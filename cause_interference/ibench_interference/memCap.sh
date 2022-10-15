#! /bin/bash
date +%s.%N
for ((i=0;i<10;i++))
do
        ./memCap 1 &
done
wait
date +%s.%N
