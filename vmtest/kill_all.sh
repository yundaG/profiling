#! /bin/bash
pids=`ps -ef |grep test_ | grep -v grep |awk '{print $2}'`
for i in $pids
do
    kill $i
done