import csv
import sys
import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

plot_data = []

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

    print(speed[0])
    print(speed[1])
    plot_data.insert(8,speed[0])
    plot_data.insert(9,speed[1])
#hard disk used

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
    not_used = 100-int(disk_used)
    plot_data.insert(6,not_used)
    plot_data.insert(7,disk_used)    


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
    plot_data.insert(2,not_used)
    plot_data.insert(3,avg)
    #y = np.array([not_used,avg])
    #plt.pie(y)
    #plt.show()

    #plt.savefig(sys.stdout.buffer)
    #sys.stdout.flush()
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
    not_used = 100-avg

    plot_data.insert(4,not_used)
    plot_data.insert(5,avg)

    file.close()

#Graph plotting function

def plot_graph(plot_data):
    a = np.array([plot_data[0],plot_data[1]])
    mylabels = ["Unused Memory","Used Memory"]
    plt.subplot(3,2,1)
    plt.pie(a, labels = mylabels)

    b = np.array([plot_data[2],plot_data[3]])
    mylabels1 = ["Free Swap","Swap Used"]
    plt.subplot(3,2,2)
    plt.pie(b, labels = mylabels1)

    c = np.array([plot_data[4],plot_data[5]])
    mylabels2 = ["Free CPU","CPU Used"]
    plt.subplot(3,2,3)
    plt.pie(c , labels = mylabels2)

    d = np.array([plot_data[6],plot_data[7]])
    mylabels3 = ["Free Space","Used Space"]
    plt.subplot(3,2,4)
    plt.pie(d, labels = mylabels3)

    e = np.array([plot_data[8],plot_data[9]])
    mylabels4 = ["Download","Upload"]
    plt.subplot(3,2,5)
    plt.bar(mylabels4,e)

    plt.show()


#function call
speed_test()
memoryused()
swapused()
cpuused()
hdused()
plot_graph(plot_data)
