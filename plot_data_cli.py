import csv
import sys


#net_speed test
def speed_test():
    file = open('stats/net_speed.csv')
    csvreader = csv.reader(file)
    rows = []
    for row in csvreader:
        r =  str(row)
        rows.append(r.split())

    x = len(rows)
    speed = []
    for i in range(x):
        speed.insert(i,rows[i][1])
        print(speed[i])

    f = open('speed_test.txt','w')
    f.write(speed[0])
    f.close
#hard disk used
    file.close()

def hdused():
    file = open('stats/hard_used.csv')
    csvreader = csv.reader(file)
    rows=[]
    for row in csvreader:
        r = str(row)
        rows.append(r.split())

    x = len(rows) -1
    disk_used = 0
    for i in range(x):
        rows[i][5]=rows[i][5].replace("'","")
        rows[i][5]=rows[i][5].replace("]","")
        if(rows[i][5]=="/"):
            rows[i][4]=rows[i][4].replace("%","")
            disk_used = rows[i][4]

    print(disk_used)
    f = open('stats/hdused.txt','w')
    f.write(disk_used)
    f.close

    file.close()

# memory used

def memoryused():
    file = open('stats/mem1_used.csv')

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
    x = len(rows) -1
    for i in range(x):
        sumi+=float(rows[i][5])
        #print(sumi)

    avg = sumi/x
    print(sumi)
    print(avg)
    not_used = 100-avg
    plot_data.insert(0,not_used)
    plot_data.insert(1,avg)

    #pie chart for memory used
    #y = np.array([not_used,avg])
    #mem_used_label = ['Not used', 'Used']
    #plt.pie(y)    #labels= mem_used_label)
    #plt.show()

    #plt.savefig(sys.stdout.buffer)
    #sys.stdout.flush()

    f = open('stats/memory_used.txt','w')
    f.write(avg)
    f.close

    file.close()
#swapused
def swapused():
    file = open('stats/swap.csv')

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
    x = len(rows)-1
    for i in range(x):
        sumi+=float(rows[i][4])

    avg = sumi/x
    print(sumi)
    print(avg)

    not_used= 100 - avg
    f = open('stats/swap_used.txt','w')
    f.write(avg)
    f.close
    
    file.close()



#cpu used
def cpuused():
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
    x = len(rows)-1
    for i in range(x):
        rows[i][8]=rows[i][8].replace("'","")
        rows[i][8]=rows[i][8].replace("]","")
        sumi+=float(rows[i][8])
    avg = sumi/x;
    print(sumi)
    print(avg)
    
    f = open('stats/cpu_used.txt','w')
    f.write(avg)
    f.close
    

    file.close()




#function call
speed_test()
memoryused()
swapused()
cpuused()
hdused()
