class Process:
    def __init__(self, process_id, arrival, burst):
        self.process_id = process_id
        self.arrival = arrival
        self.burst = burst
        self.completion = 0
        self.turnaround = 0
        self.waiting = 0

def sjf_non_preemptive(processes):
    time = 0
    completed = 0
    total = len(processes)
    processes.sort(key=lambda p: p.arrival)
    ready_queue = []

    while completed < total:
        for p in processes:
            if p.arrival <= time and p not in ready_queue and p.completion == 0:
                ready_queue.append(p)

        ready_queue.sort(key=lambda p: p.burst)

        if not ready_queue:
            time += 1
            continue

        current = ready_queue.pop(0)
        time += current.burst
        current.completion = time
        current.turnaround = current.completion - current.arrival
        current.waiting = current.turnaround - current.burst
        completed += 1

    total_waiting = sum(p.waiting for p in processes)

    
    print("| Process ID | Arrival | Burst | Completion | Turnaround | Waiting Time |")
  
    for p in processes:
        print("| {:<10} | {:<7} | {:<5} | {:<10} | {:<10} | {:<12} |".format(
            f'P{p.process_id}', p.arrival, p.burst, p.completion, p.turnaround, p.waiting
        ))
  
    print(f"\nAverage Waiting Time: {total_waiting / total:.2f}")

if __name__ == "__main__":
    num = int(input("Enter number of processes: "))
    process_list = []

    for i in range(num):
        print(f"\nEnter details for Process P{i+1}:")
        arrival_time = int(input("Arrival Time: "))
        burst_time = int(input("Burst Time: "))
        process_list.append(Process(i+1, arrival_time, burst_time))

    sjf_non_preemptive(process_list)
