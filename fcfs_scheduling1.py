def fcfs(bt):
    print("Process      Burst Time     Waiting Time     Turnaround Time")
    i = 0
    wt = 0
    tat = 0
    waiting_time = []
    turnaround_time = []

    while(i < len(bt)):
        tat += bt[i]
        print("  P"+str(i+1)+"\t\t"+str(bt[i])+"\t\t"+str(wt)+"\t\t"+str(tat))
        waiting_time.append(wt)
        turnaround_time.append(tat)
        wt += bt[i]
        i+=1
    return (waiting_time,turnaround_time)

process = int(input("Enter the number of processes you want: "))
bt = [] # burst_time list 
for i in range(process):
    bt.append(int(input(f"Enter the burst times for {process}: ")))
func = fcfs(bt)
print("Average waiting time: "+str(sum(func[0])/len(func[0])))
print("Average turnaround time: "+str(sum(func[1])/len(func[1])))
