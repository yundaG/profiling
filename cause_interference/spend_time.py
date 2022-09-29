import sys

def stoi(s):
    length = len(s)
    idx = 0
    for i in range(length):
        if s[i]=='0':
            idx += 1
        else:
            break
    s = s[idx:]
    if len(s) == 0:
        return 0
    else:
        return eval(s)

file_name = sys.argv[1]
with open(file_name, 'r') as f:
    content = f.readlines()
    start = content[0]
    end = content[1]
    lt1 = start.split(".")
    lt2 = end.split(".")
    start_s = eval(lt1[0])
    start_ns = stoi(lt1[1])
    end_s = eval(lt2[0])
    end_ns = stoi(lt2[1])
    spend = (end_s-start_s)*1000000000 + end_ns-start_ns
    #print("spend_time(ns): ",spend)
    #print("spend_time(us): ",spend/1000.0)
    print("spend_time(ms): ",spend/1000000.0)
