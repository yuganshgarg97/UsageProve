import csv
def cpu_d
file = open('stats/cpu.csv')
type(file)
csvreader = csv.reader(file)
next(csvreader)
next(csvreader)
header = []
header = next(csvreader)
#print(header)

rows=[]
for row in csvreader:
    r = str(row)
    rows.append(r.split())
#print(rows)
sumi=0
for i in range(len(rows)):
    ##rows[i][5]=rows[i][5].replace("'","")
    ##rows[i][5]=rows[i][5].replace("]","")
    sumi+=float(rows[i][3])
average = sumi/float(len(rows))
print("stats/average load on processor:",average)
file.close()
x = open("cpu_average.txt",'w')
x.write(str(average))
x.close()

