
processes = ["P1", "P2", "P3", "P4"]
arrival_time = [0, 2, 4, 5]
burst_time = [7, 4, 1, 4]

n = len(processes)
remaining = list(range(n))
completed = [False] * n

completion_time = [0] * n
waiting_time = [0] * n
turnaround_time = [0] * n

gantt_processes = []
gantt_start = []
gantt_end = []

current_time = 0
completed_count = 0

while completed_count < n:

    available = []

    for i in range(n):
        if arrival_time[i] <= current_time and not completed[i]:
            available.append(i)

    if not available:
        current_time += 1
        continue

    selected = min(
        available,
        key=lambda i: (burst_time[i], arrival_time[i])
    )

    start = current_time

    current_time += burst_time[selected]

    end = current_time

    completion_time[selected] = end

    turnaround_time[selected] = (
        completion_time[selected] - arrival_time[selected]
    )

    waiting_time[selected] = (
        turnaround_time[selected] - burst_time[selected]
    )

    completed[selected] = True
    completed_count += 1

    gantt_processes.append(processes[selected])
    gantt_start.append(start)
    gantt_end.append(end)


average_waiting = sum(waiting_time) / n
average_turnaround = sum(turnaround_time) / n



print("NON-PREEMPTIVE SJF SCHEDULING")
print("-" * 70)

print("Process\tArrival\tBurst\tCompletion\tWaiting\tTurnaround")

for i in range(n):
    print(
        f"{processes[i]}\t"
        f"{arrival_time[i]}\t"
        f"{burst_time[i]}\t"
        f"{completion_time[i]}\t\t"
        f"{waiting_time[i]}\t"
        f"{turnaround_time[i]}"
    )

print("-" * 70)
print(f"Average Waiting Time    = {average_waiting:.2f} ms")
print(f"Average Turnaround Time = {average_turnaround:.2f} ms")



import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 3))

for i in range(n):
    start = gantt_start[i]
    end = gantt_end[i]

    ax.barh(
        0,
        end - start,
        left=start,
        height=0.5,
        edgecolor="black"
    )

    ax.text(
        (start + end) / 2,
        0,
        gantt_processes[i],
        ha="center",
        va="center",
        fontsize=12
    )

    ax.text(
        start,
        -0.35,
        str(start),
        ha="center"
    )

ax.text(
    gantt_end[-1],
    -0.35,
    str(gantt_end[-1]),
    ha="center"
)

ax.set_xlim(0, gantt_end[-1])
ax.set_ylim(-0.7, 0.7)
ax.set_yticks([])
ax.set_xlabel("Time (ms)")
ax.set_title("Non-Preemptive SJF Gantt Chart")

plt.tight_layout()
plt.show()
