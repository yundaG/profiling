#! /usr/bin/python3
import argparse
import re
import time

example=""

parser=argparse.ArgumentParser(description="report latest average speed",epilog=example)
parser.add_argument('-r','--resize',help="resize output file",metavar="",default="normal.log")
parser.add_argument('-s','--scale',help="scale output file",metavar="",default="nospeedup.log")
parser.add_argument('-i','--interval',type=int,help="the interval seconds between two calculate",default=10,metavar="")
parser.add_argument('-n','--number',type=int,help="the number of latest requests used to calculate",default=-1,metavar="")

log_group = parser.add_mutually_exclusive_group()
log_group.add_argument("--nolog",help="do not write log file",action="store_true")
log_group.add_argument('-l','--log',help="log file name",default="avg_speed.log",metavar="")

args=parser.parse_args()
if args.resize is None and args.scale is None:
    print("at least one file is required")
    exit(1)

pattern = re.compile(r'(?<=spend: )[0-9]+')

def calculate(file_name,num):
    f=open(file_name,"r")
    content=f.read()
    f.close()
    data = pattern.findall(content)
    if num != -1 and len(data)>num:
        data = data[-num:]
    total_time = 0
    for i in data:
        total_time += int(i)
    return total_time/len(data),len(data)

if  not args.nolog:
    logfile = open(args.log,"w+")
    
while 1:
    time.sleep(args.interval)
    if args.resize != None:
        resize_avg,resize_num = calculate(args.resize,args.number)
        curtime = time.strftime("%H:%M:%S",time.localtime())
        cout = curtime + ", average resize speed: " + "%.2f" % resize_avg + ", data amount: "+ str(resize_num)
        if not args.nolog:
            logfile.write(cout+"\n")
        print(cout)
    if args.scale != None:
        scale_avg,scale_num = calculate(args.scale,args.number)
        curtime = time.strftime("%H:%M:%S",time.localtime())
        cout = curtime + ", average scale speed: " + "%.2f" % scale_avg + ", data amount: "+ str(scale_num)
        if not args.nolog:
            logfile.write(cout+"\n")
        print(cout)
    print()

