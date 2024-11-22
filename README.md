# CPU Scheduler Simulator

A friendly Python-based CPU scheduling simulator that helps you understand how different scheduling algorithms work. This tool simulates both preemptive and non-preemptive scheduling algorithms, perfect for learning OS concepts or testing different scheduling scenarios.

## What's Inside? 🚀

This simulator implements five popular CPU scheduling algorithms:

### Non-preemptive Algorithms
- **First Come First Serve (FCFS)**: The simplest one - first process to arrive gets to run first
- **Shortest Job First (SJF)**: Picks the process with the shortest execution time
- **Priority Scheduling**: Processes with higher priority (lower number) get to run first

### Preemptive Algorithms
- **Round Robin (RR)**: Gives each process a fair time slice to run
- **Shortest Remaining Time First (SRTF)**: Like SJF, but can switch to a shorter process that arrives

## Getting Started 🎯

### Requirements
- Python 3.7 or newer (we use some cool features like dataclasses)

### Running the Simulator
1. Save the code as `cpu_scheduler.py`
2. Open your terminal
3. Navigate to where you saved the file
4. Run it with: `python cpu_scheduler.py`

That's it! The menu will guide you through the rest.

## How to Use 📝

1. When you run the program, you'll see a menu with options 1-6
2. Choose your scheduling algorithm
3. Enter the number of processes you want to simulate
4. For each process, you'll need to provide:
   - Arrival time (when the process shows up)
   - Burst time (how long it needs to run)
   - Priority (only for Priority Scheduling)
   - Time quantum (only for Round Robin)

## What You'll Get 📊

The simulator shows you:
- A Gantt chart showing when each process runs
- Turnaround Time (TAT) for each process
- Waiting Time (WT) for each process
- Average TAT and WT for all processes

## Understanding the Code 🔍

### Key Components

#### Process Class
Handles all the info about each process:
```python
@dataclass
class Process:
    pid: int                    # Process ID
    arrival_time: int           # When it arrives
    burst_time: int             # How long it needs
    priority: Optional[int]     # Its priority level
    remaining_time: int = None  # Time left to finish
```

#### CPUScheduler Class
The brain of the operation! Contains:
- Methods for each scheduling algorithm
- Gantt chart generation
- Metric calculations

### Cool Features

- **Menu-driven interface**: No need to modify code, just follow the prompts
- **Visual Gantt chart**: See exactly when each process runs
- **Detailed metrics**: Get insights into how efficiently processes are running
- **Flexible input**: Test different scenarios easily

## Example Usage 💡

Here's a quick example with 3 processes using FCFS:

```
Choose an algorithm (1-6): 1
Enter number of processes: 3

Process 1:
Arrival time: 0
Burst time: 4

Process 2:
Arrival time: 1
Burst time: 3

Process 3:
Arrival time: 2
Burst time: 1

Gantt Chart:
--------------------------------------------------
|P1(0-4)|P2(4-7)|P3(7-8)|
--------------------------------------------------
```

## Tips for Testing 🎓

- Start with FCFS - it's the easiest to understand
- Try the same processes with different algorithms to see how performance changes
- Round Robin is great for seeing how time quantum affects fairness
- SRTF usually gives the best average waiting times

## Need Help? 🤔

If something's not clear or you find a bug:
1. Double-check your input values
2. Make sure arrival times make sense
3. For Priority Scheduling, remember lower numbers = higher priority

## Technical Details (for the curious) 🔧

The simulator uses:
- Python's dataclasses for clean process management
- Deque for efficient queue operations in Round Robin
- Simple but effective ASCII art for Gantt charts

That's it! Have fun exploring different scheduling scenarios! 🎉
