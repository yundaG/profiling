#! /bin/bash
for ((i=0;i<=2;i++))
do
        cat l1d/l1d.yaml.template | sed 's/?/'$i'/g' > l1d/l1d${i}.yaml
done
for ((i=0;i<=2;i++))
do
        kubectl create -f l1d/l1d${i}.yaml
done
