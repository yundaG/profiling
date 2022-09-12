#! /bin/bash
for ((i=0;i<=127;i++))
do
        cat l1i/l1i.yaml.template | sed 's/?/'$i'/g' > l1i/l1i${i}.yaml
done
for ((i=0;i<=127;i++))
do
        kubectl create -f l1i/l1i${i}.yaml
done
