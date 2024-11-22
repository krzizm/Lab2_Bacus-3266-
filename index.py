from dataclasses import dataclass
from typing import List, Optional
import time
from collections import deque

@dataclass
class Process:
    pid: int                    # Process ID
    arrival_time: int           # When the process arrives
    burst_time: int            # How long it needs to run
    priority: Optional[int]     # Priority level (lower number = higher priority)
    remaining_time: int = None  # Time left to complete
    start_time: int = None     # When process first started
    completion_time: int = None # When process finished
    
    def __post_init__(self):
        if self.remaining_time is None:
            self.remaining_time = self.burst_time

class CPUScheduler:
    def __init__(self, processes: List[Process]):
        # Make a copy so we don't modify the original
        self.processes = [Process(
            pid=p.pid,
            arrival_time=p.arrival_time,
            burst_time=p.burst_time,
            priority=p.priority,
            remaining_time=p.burst_time
        ) for p in processes]
        self.gantt_chart = []
        self.current_time = 0

    def fcfs(self):
        """First Come First Serve - The simplest scheduling algorithm"""
        # Sort by arrival time
        self.processes.sort(key=lambda p: p.arrival_time)
        
        for process in self.processes:
            # If we need to wait for the process to arrive, update current time
            if self.current_time < process.arrival_time:
                self.current_time = process.arrival_time
            
            process.start_time = self.current_time
            # Add to Gantt chart - (pid, start_time, end_time)
            self.gantt_chart.append((process.pid, self.current_time, 
                                   self.current_time + process.burst_time))
            
            self.current_time += process.burst_time
            process.completion_time = self.current_time

    def sjf(self):
        """Shortest Job First - Non-preemptive scheduling by shortest burst time"""
        ready_queue = []
        remaining_processes = self.processes.copy()
        
        while remaining_processes or ready_queue:
            # Add all processes that have arrived to ready queue
            while remaining_processes and remaining_processes[0].arrival_time <= self.current_time:
                ready_queue.append(remaining_processes.pop(0))
            
            if not ready_queue:
                # Jump to next process arrival if nothing is ready
                self.current_time = remaining_processes[0].arrival_time
                continue
                
            # Sort ready queue by burst time
            ready_queue.sort(key=lambda p: p.burst_time)
            process = ready_queue.pop(0)
            
            process.start_time = self.current_time
            self.gantt_chart.append((process.pid, self.current_time, 
                                   self.current_time + process.burst_time))
            
            self.current_time += process.burst_time
            process.completion_time = self.current_time

    def priority_scheduling(self):
        """Non-preemptive Priority Scheduling"""
        ready_queue = []
        remaining_processes = sorted(self.processes, key=lambda p: p.arrival_time)
        
        while remaining_processes or ready_queue:
            # Add arrived processes to ready queue
            while remaining_processes and remaining_processes[0].arrival_time <= self.current_time:
                ready_queue.append(remaining_processes.pop(0))
            
            if not ready_queue:
                self.current_time = remaining_processes[0].arrival_time
                continue
                
            # Sort by priority (lower number = higher priority)
            ready_queue.sort(key=lambda p: p.priority)
            process = ready_queue.pop(0)
            
            process.start_time = self.current_time
            self.gantt_chart.append((process.pid, self.current_time, 
                                   self.current_time + process.burst_time))
            
            self.current_time += process.burst_time
            process.completion_time = self.current_time

    def round_robin(self, time_quantum: int):
        """Round Robin - Preemptive scheduling with time slices"""
        ready_queue = deque()
        remaining_processes = sorted(self.processes, key=lambda p: p.arrival_time)
        
        while remaining_processes or ready_queue:
            # Add newly arrived processes
            while remaining_processes and remaining_processes[0].arrival_time <= self.current_time:
                ready_queue.append(remaining_processes.pop(0))
            
            if not ready_queue:
                self.current_time = remaining_processes[0].arrival_time
                continue
            
            process = ready_queue.popleft()
            time_slice = min(time_quantum, process.remaining_time)
            
            # Execute for time quantum or until completion
            self.gantt_chart.append((process.pid, self.current_time, 
                                   self.current_time + time_slice))
            
            process.remaining_time -= time_slice
            self.current_time += time_slice
            
            # Add back to queue if not finished
            if process.remaining_time > 0:
                ready_queue.append(process)
            else:
                process.completion_time = self.current_time

    def srtf(self):
        """Shortest Remaining Time First - Preemptive version of SJF"""
        ready_queue = []
        remaining_processes = sorted(self.processes, key=lambda p: p.arrival_time)
        
        while remaining_processes or ready_queue:
            # Add newly arrived processes
            while remaining_processes and remaining_processes[0].arrival_time <= self.current_time:
                ready_queue.append(remaining_processes.pop(0))
            
            if not ready_queue:
                self.current_time = remaining_processes[0].arrival_time
                continue
            
            # Choose process with shortest remaining time
            ready_queue.sort(key=lambda p: p.remaining_time)
            process = ready_queue.pop(0)
            
            # Find how long we can run this process
            next_arrival = float('inf')
            if remaining_processes:
                next_arrival = remaining_processes[0].arrival_time
            
            run_time = min(process.remaining_time, 
                          next_arrival - self.current_time if next_arrival != float('inf') else process.remaining_time)
            
            self.gantt_chart.append((process.pid, self.current_time, 
                                   self.current_time + run_time))
            
            process.remaining_time -= run_time
            self.current_time += run_time
            
            if process.remaining_time > 0:
                ready_queue.append(process)
            else:
                process.completion_time = self.current_time

    def get_metrics(self):
        """Calculate and return the scheduling metrics"""
        total_tat = 0
        total_wt = 0
        
        for process in self.processes:
            # Turnaround Time = Completion Time - Arrival Time
            tat = process.completion_time - process.arrival_time
            # Waiting Time = Turnaround Time - Burst Time
            wt = tat - process.burst_time
            
            total_tat += tat
            total_wt += wt
            
            print(f"Process {process.pid}:")
            print(f"  Turnaround Time: {tat}")
            print(f"  Waiting Time: {wt}")
        
        avg_tat = total_tat / len(self.processes)
        avg_wt = total_wt / len(self.processes)
        
        print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
        print(f"Average Waiting Time: {avg_wt:.2f}")

    def display_gantt_chart(self):
        """Display a simple ASCII Gantt chart"""
        print("\nGantt Chart:")
        print("-" * 50)
        
        for pid, start, end in self.gantt_chart:
            print(f"|P{pid}({start}-{end})", end="")
        print("|")
        print("-" * 50)

def main():
    while True:
        print("\nCPU Scheduling Simulator")
        print("1. First Come First Serve (FCFS)")
        print("2. Shortest Job First (SJF)")
        print("3. Priority Scheduling")
        print("4. Round Robin (RR)")
        print("5. Shortest Remaining Time First (SRTF)")
        print("6. Exit")
        
        choice = input("Choose an algorithm (1-6): ")
        
        if choice == '6':
            break
            
        n = int(input("Enter number of processes: "))
        processes = []
        
        for i in range(n):
            print(f"\nProcess {i+1}:")
            arrival = int(input("Arrival time: "))
            burst = int(input("Burst time: "))
            priority = None
            
            if choice == '3':  # Priority Scheduling
                priority = int(input("Priority (lower number = higher priority): "))
                
            processes.append(Process(i+1, arrival, burst, priority))
            
        scheduler = CPUScheduler(processes)
        
        if choice == '1':
            scheduler.fcfs()
        elif choice == '2':
            scheduler.sjf()
        elif choice == '3':
            scheduler.priority_scheduling()
        elif choice == '4':
            quantum = int(input("Enter time quantum: "))
            scheduler.round_robin(quantum)
        elif choice == '5':
            scheduler.srtf()
            
        scheduler.display_gantt_chart()
        scheduler.get_metrics()

if __name__ == "__main__":
    main()