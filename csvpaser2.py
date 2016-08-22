import csv


jinjjang = []
ip = {}


f = open('logons_redacted_fixed20160520_fakeIP.csv','r')
csvReader = csv.reader(f)
p = open ('resylt33.csv','w')
for row in csvReader:
    jinjjang.append(row)
    jinsejjang = row[1]

    if jinsejjang in ip:
        ip[jinsejjang] += 1
    else:
        ip[jinsejjang] = 1
print ip
for i in ip.keys() :
    p.write(i + ", " + `ip[i]` + "\n")

f.close()