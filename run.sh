#classify
cd /home/clouda/classify-stable && locust -f img_classify_cpu_1_0_19.py --headless -u100 -r100 -t300 2> /home/clouda/data/classify-stable.log &
cd /home/clouda/classify-growing && locust -f img_classify_cpu_1_0_19.py --headless -u100 -r0.33 -t300  2> /home/clouda/data/classify-growing.log &
cd /home/clouda/classify-cycle && sh run.sh 2> /home/clouda/data/classify-cycle.log &
cd /home/clouda/classify-onoff && sh run.sh 2> /home/clouda/data/classify-onoff.log &

#face
cd /home/clouda/face-stable && locust -f face-recognition_161.py --headless -u100 -r100 -t300 2> /home/clouda/data/face-stable.log &
cd /home/clouda/face-growing && locust -f face-recognition_161.py --headless -u100 -r0.33 -t300 2> /home/clouda/data/face-growing.log &
cd /home/clouda/face-cycle && sh run.sh 2> /home/clouda/data/face-cycle.log &
cd /home/clouda/face-onoff && sh run.sh 2> /home/clouda/data/face-onoff.log &

#ocr
cd /home/clouda/ocr-stable && locust -f locust_flid.py --headless -u30 -r30 -t300 2> /home/clouda/data/ocr-stable.log &
cd /home/clouda/ocr-growing && locust -f locust_flid.py --headless -u30 -r0.1 -t300 2> /home/clouda/data/ocr-growing.log &
cd /home/clouda/ocr-cycle && sh run.sh 2> /home/clouda/data/ocr-cycle.log &

#logo
cd /home/clouda/logo-stable && locust -f locust_logo_detection.py --headless -u100 -r100 -t300 2> /home/clouda/data/logo-stable.log &
cd /home/clouda/logo-growing && locust -f locust_logo_detection.py --headless -u100 -r0.33 -t300 2> /home/clouda/data/logo-growing.log &
cd /home/clouda/logo-cycle && sh run.sh 2> /home/clouda/data/logo-cycle.log &

#jiaping
cd /home/clouda/jiaping-stable && sh run.sh > /home/clouda/data/jiaping-stable.log &
cd /home/clouda/jiaping-growing && python run.py > /home/clouda/data/jiaping-growing.log &
cd /home/clouda/jiaping-cycle && python run.py > /home/clouda/data/jiaping-cycle.log &

sleep 300
for pid in `ps -ef |grep run.py | grep -v grep | awk '{print $2}'`
do
    kill $pid
done
