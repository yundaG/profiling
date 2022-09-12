#! /bin/bash
for ((i=0;i<=29;i++))
do
        cat l2/l2.yaml.template | sed 's/?/'$i'/g' > l2/l2_${i}.yaml
done
for ((i=0;i<=29;i++))
do
        kubectl create -f l2/l2_${i}.yaml
done
