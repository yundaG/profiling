#! /bin/bash
for ((i=0;i<=29;i+=1))
do
        cat llc/llc.yaml.template | sed 's/?/'$i'/g' > llc/llc_${i}.yaml
done
for ((i=0;i<=29;i+=1))
do
        kubectl create -f llc/llc_${i}.yaml
done
