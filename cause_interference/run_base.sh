sh l1d.sh > l1d.log
echo "l1d:"
python3 spend_time.py l1d.log
echo "--------------------"
sleep 1
sh l1i.sh > l1i.log
echo "l1i:"
python3 spend_time.py l1i.log
echo "--------------------"
sleep 1
sh l2.sh > l2.log
echo "l2:"
python3 spend_time.py l2.log
echo "--------------------"
sleep 1
sh l3.sh > l3.log
echo "l3:"
python3 spend_time.py l3.log
echo "--------------------"
sleep 1
sh memBw.sh > memBw.log
echo "memBw:"
python3 spend_time.py memBw.log
echo "--------------------"
sleep 1
sh memCap.sh > memCap.log
echo "memCap:"
python3 spend_time.py memCap.log
