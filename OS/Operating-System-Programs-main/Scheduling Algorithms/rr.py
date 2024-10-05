class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.start_time = None
        self.exit_time = None
        self.waiting_time = None
        self.turnaround_time = None

    def tat(self, exit_time):
        self.exit_time = exit_time
        self.turnaround_time = self.exit_time - self.arrival_time
        return self.turnaround_time

    def wt(self):
        self.waiting_time = self.turnaround_time - self.burst_time
        return self.waiting_time

def round_robin(processes, time_quantum):
    processes = sorted(processes, key=lambda p: p.arrival_time)
    queue = []
    current_time = 0
    completed = []

    while processes or queue:
        if processes and processes[0].arrival_time <= current_time:
            queue.append(processes.pop(0))

        if queue:
            queue = sorted(queue,key=lambda p: p.arrival_time)
            process = queue.pop(0)

            #if process.start_time is None:
            process.start_time = current_time
 

            if process.remaining_time <= time_quantum:
                print(process.pid,process.start_time)
                current_time += process.remaining_time
                process.remaining_time = 0
                process.exit_time = current_time
                
                process.turnaround_time = process.tat(process.exit_time)
                process.waiting_time = process.wt()
                
                completed.append((process.pid, process.start_time, process.exit_time, process.waiting_time, process.turnaround_time))
            else:
                current_time += time_quantum
                process.remaining_time -= time_quantum
                completed.append((process.pid, process.start_time, current_time, None, None))
                
                process.arrival_time = current_time
                queue.append(process)
    
    return completed

if __name__ == '__main__':
    processes = [
        Process('A', 0, 3),
        Process('B', 1, 6),
        Process('C', 4, 4),
        Process('D', 6, 2)
    ]

    time_quantum = 2

    processes = round_robin(processes, time_quantum)
    print(processes)

    wt = 0
    for process in processes:
        if process[3] is not None:
            wt += process[3]
        print()
    print("Process\tStart Time\tExit Time\tTurnaround Time\tWaiting Time")

    for process in processes:
        print(f"{process[0]}\t\t{process[1]}\t\t{process[2]}\t\t{process[4]}\t\t{process[3]}")

    gantt_chart = ''
    for i in range(len(processes)):
        if i != 0:
            if processes[i][0] == processes[i - 1][0]:
                gantt_chart += str(processes[i][2]) + "|"
            else:
                gantt_chart += str(processes[i][1]) + " " + str(processes[i][0]) + " "
        else:
            gantt_chart += "|" + str(processes[i][1]) + " " + str(processes[i][0]) + " " + str(processes[i][2]) + "|"

    print("Gantt Chart:\n", gantt_chart)
    print("Average Waiting Time: ", wt / len(processes))

