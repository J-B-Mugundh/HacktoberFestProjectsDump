class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.priority = priority
        self.start_time = None
        self.finish_time = None  # Changed from 'exit' to 'finish_time'
        self.waiting_time = None
        self.turnaround_time = None

    def tat(self, exit_time):  # Changed from 'exit' to 'exit_time'
        self.finish_time = exit_time  # Changed from 'exit' to 'finish_time'
        self.turnaround_time = self.finish_time - self.arrival_time
        return self.turnaround_time

    def wt(self):
        self.waiting_time = self.turnaround_time - self.burst_time
        return self.waiting_time

def priority(processes):
    processes = sorted(processes, key=lambda p: p.arrival_time)
    queue = []
    current_time = 0
    completed = []

    while processes or queue:
        if processes and processes[0].arrival_time <= current_time:
            queue.append(processes.pop(0))

        if queue:
            queue = sorted(queue, key=lambda p: p.priority, reverse=True)
            process = queue.pop(0)

            process.start_time = current_time
            process.remaining_time -= 1

            if process.remaining_time == 0:
                process.turnaround_time = process.tat(current_time + 1)
                process.waiting_time = process.wt()

                completed.append((process.pid, process.start_time, process.finish_time,
                                  process.waiting_time, process.turnaround_time))
            else:
                if not completed or process.pid != completed[-1][0]:
                    completed.append((process.pid, process.start_time, current_time + 1, None, None))

                queue.append(process)
        current_time += 1

    return completed


if __name__ == '__main__':
    processes_list = [
        Process('A', 0, 4, 3),
        Process('B', 1, 3, 4),
        Process('C', 2, 3, 6),
        Process('D', 3, 5, 5)
    ]

    processes = priority(processes_list)
    # print(processes)

    wt = 0
    for process in processes:
        if process[3] is not None:
            wt += process[3]
    print("Process\tArrival time\tBurst Time\tTurnaround Time\tWaiting Time")

    for i in range(len(processes_list)):
        print(f"{processes_list[i].pid}\t\t{processes_list[i].arrival_time}\t\t{processes_list[i].burst_time}\t\t{processes_list[i].turnaround_time}\t\t{processes_list[i].waiting_time}")

    gantt_chart = ''
    for i in range(len(processes)):
        if i != 0:
            if processes[i][0] == processes[i - 1][0]:
                gantt_chart += str(processes[i][2]) + "|"
            else:
                gantt_chart += str(processes[i][1]) + " " + str(processes[i][0]) + " "
        else:
            gantt_chart += "|" + str(processes[i][1]) + " " + str(processes[i][0]) + " " + str(
                processes[i][2]) + "|"

    print("Gantt Chart:\n", gantt_chart)
    print("Average Waiting Time: ", wt / 4)
    print("Throughput: ", processes[-1][2] / 4)
