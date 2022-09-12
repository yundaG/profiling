import sys
file_name = sys.argv[1]
f = open(file_name,"r")
lines = f.readlines()
f.close()
dic = {}
times = []
for line in lines[2:]:
    lt =line.strip().split()
    if len(lt) != 9:
        continue
    dport = eval(lt[-1])
    tcp_type = lt[1]
    if tcp_type == "A":
        if dport not in dic:
            dic[dport] = eval(lt[0])
    elif tcp_type =="X":
        if dport in dic:
            interval = eval(lt[0]) - dic[dport]
            dic.pop(dport)
            times.append(interval)
print(len(times))
print(sum(times)/len(times) * 1000)
        