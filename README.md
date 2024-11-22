# CPU Scheduler Simulator with Enhanced Visualization

A command-line based CPU scheduling simulator that brings scheduling algorithms to life with detailed visualizations. Perfect for learning OS concepts, testing different scheduling scenarios, and understanding process execution patterns.

## Features 🚀

### Scheduling Algorithms
The simulator implements five key CPU scheduling algorithms:

#### Non-preemptive Algorithms
- **First Come First Serve (FCFS)**: Simple queue-based processing
- **Shortest Job First (SJF)**: Optimizes for shortest execution time
- **Priority Scheduling**: Process execution based on priority levels

#### Preemptive Algorithms
- **Round Robin (RR)**: Fair execution with time quantum
- **Shortest Remaining Time First (SRTF)**: Dynamic version of SJF

### Visualization Features
- **Enhanced Gantt Chart**:
  - Clear process execution blocks
  - Timeline markers for precise timing
  - Visual representation of idle time
  - Detailed process execution table
- **Comprehensive Metrics**:
  - Individual process statistics
  - Average turnaround times
  - Average waiting times

## Quick Start Guide 🎯

### Prerequisites
- Python 3.7 or newer installed on your system

### Installation
1. Save the code as `cpu_scheduler.py`
2. Open your terminal/command prompt
3. Navigate to the file location
4. Run: `python cpu_scheduler.py`

### Basic Usage
1. Choose a scheduling algorithm (1-5)
2. Enter the number of processes
3. For each process, provide:
   - Arrival time
   - Burst time
   - Priority (if using Priority Scheduling)
   - Time quantum (for Round Robin only)

## Understanding the Output 📊

### Gantt Chart
```
====================================
--P1----P2--P3-----P4--
------------------------
0 1  4  6  8   12  15
```
- Each block shows when a process runs
- Numbers below show exact timings
- Dashes indicate process boundaries

### Process Details
```
Process Execution Details:
--------------------------
Process | Start | End | Duration
P1     |   0   |  4  |    4
P2     |   4   |  7  |    3
```
- Shows exact timing for each process
- Helps track process execution order
- Makes it easy to verify scheduling decisions

## Code Structure 🔧

### Key Components

#### Process Class
```python
@dataclass
class Process:
    pid: int                    # Process ID
    arrival_time: int           # Arrival time
    burst_time: int             # Execution time needed
    priority: Optional[int]     # Priority level
```

#### Scheduler Class
- Implements all scheduling algorithms
- Handles process management
- Generates visualizations
- Calculates metrics

## Example Usage 💡

Here's a simple FCFS example:
```
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

[Gantt chart and metrics will be displayed]
```

## Testing Tips 🎓

1. **Start Simple**
   - Try FCFS first with 2-3 processes
   - Make sure arrival times make sense

2. **Explore Algorithms**
   - Compare same processes across different algorithms
   - Notice how metrics change

3. **Round Robin Testing**
   - Try different time quantum values
   - Watch how it affects fairness

4. **Priority Scheduling**
   - Test with mixed priorities
   - See how priority affects order

## Troubleshooting 🔍

Common issues and solutions:

1. **Invalid Input**
   - Use only positive integers
   - Arrival times can be 0 or positive
   - Burst times must be positive

2. **Unexpected Results**
   - Double-check process parameters
   - Verify algorithm selection
   - Make sure priorities are properly set

## Contributing 🤝

Feel free to:
- Report bugs
- Suggest improvements
- Add new features
- Enhance visualizations

## Future Enhancements 🚀

Planned improvements:
- Additional scheduling algorithms
- More detailed process statistics
- Enhanced visualization options
- Performance metrics
- Process priority changes over time

## Need Help? 💭

If you encounter issues:
1. Verify your Python version
2. Check input values
3. Follow the example usage
4. Try simpler process configurations first

Happy Scheduling! 🎉
