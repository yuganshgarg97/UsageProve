import os
if(os.path.exists("stats")):
    
    os.system(" rm -rf stats")
os.mkdir("stats")
os.system("sar -r 1 5 >> stats/mem1_used.csv | sar -S 1 5 >> stats/swap.csv | sar -u 1 5 >> stats/cpu.csv | df -h|grep sda >> stats/hard_used.csv | speedtest --secure|grep -E 'Download:|Upload:' >>stats/net_speed.csv")

