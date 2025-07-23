
process_num = int(input("Enter total number of processes: "))
process_data = {}

for i in range(process_num):
    process_id = f"Task{i+1}"
    arrival = int(input(f"Enter Arrival Time for {process_id}: "))
    burst = int(input(f"Enter Burst Time for {process_id}: "))
    process_data[process_id] = [arrival, burst]

sorted_processes = sorted(process_data.items(), key=lambda x: x[1][0])

completion_times = []
for index, (pid, (arrival, burst)) in enumerate(sorted_processes):
    if index == 0:
        completion_times.append(arrival + burst)
    else:
        prev_ct = completion_times[index - 1]
        start_time = max(prev_ct, arrival)
        completion_times.append(start_time + burst)

turnaround_times = []
waiting_times = []
for idx, (pid, (arrival, burst)) in enumerate(sorted_processes):
    tat = completion_times[idx] - arrival
    wt = tat - burst
    turnaround_times.append(tat)
    waiting_times.append(wt)

avg_wait = sum(waiting_times) / process_num

print("| PID | Arrival Time | Burst Time| Completion Time | Turnaround | Waiting Time|")

for i in range(process_num):
    pid = sorted_processes[i][0]
    arrival = sorted_processes[i][1][0]
    burst = sorted_processes[i][1][1]
    ct = completion_times[i]
    tat = turnaround_times[i]
    wt = waiting_times[i]

    print("| {:<10} | {:<7} | {:<5} | {:<10} | {:<10} | {:<7} |".format(
        pid, arrival, burst, ct, tat, wt
    ))

print(f"\nAverage Waiting Time: {avg_wait:.2f}")


