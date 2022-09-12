a=0
for i in `ps aux |grep stress|grep -v grep | awk '{print $3}'`;do
echo $a,$i
a=`echo "$a + $i" | bc`
done
echo $a
