class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
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

def srtf(processes):
    processes = sorted(processes, key=lambda p: p.arrival_time)
    queue = []
    current_time = 0
    completed = []

    while processes or queue:
        if processes and processes[0].arrival_time <= current_time:
            queue.append(processes.pop(0))

        if queue:
            queue = sorted(queue, key=lambda p: p.remaining_time)
            process = queue.pop(0)

            process.start_time = current_time
            process.remaining_time -= 1

            if process.remaining_time == 0:
                process.finish_time = current_time + 1
                process.turnaround_time = process.tat(process.finish_time)
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
    processes = [
        Process(1, 0, 8),
        Process(2, 1, 4),
        Process(3, 2, 9),
        Process(4, 3, 5)
    ]

    processes = srtf(processes)
    print(processes)

    wt = 0
    for process in processes:
        if process[3] is not None:
            wt += process[3]
        print(f'Process {process[0]}:')
        print(f'Waiting time: {process[3]}')
        print(f'Turnaround time: {process[4]}')
        print(f'Start time: {process[1]}')
        print(f'Finish time: {process[2]}')  # Changed from 'Exit time' to 'Finish time'
        print()

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
