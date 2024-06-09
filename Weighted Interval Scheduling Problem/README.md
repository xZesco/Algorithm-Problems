# Weighted Interval Scheduling Problem

## Introduction

The Weighted Interval Scheduling Problem deals with scheduling jobs with start and finish times and associated profits. The objective is to select a subset of non-overlapping jobs that maximizes total profit. Each job has a start time, a finish time, and a profit associated with it.

## Problem Description

Given a list of jobs with start and finish times and associated profits, this problem aims to find a subset of non-overlapping jobs that maximizes the total profit. Each job has a start time, a finish time, and a profit. The goal is to determine which jobs to execute to achieve the highest total profit without overlapping in their time intervals.

## Implementation

### Python Implementation

```python
#class to store the Job
class Job:
    def __init__(self, start, finish, profit):
        self.start = start
        self.finish = finish
        self.profit = profit

    #representation for printing the jobs involved in the maximum profit
    def __repr__(self):
        return str((self.start, self.finish, self.profit))

#Function to print the non-overlapping jobs involved in maximum profit
def MaxProfitJobs(jobs):
    #base case
    if not jobs:
        return 0

    #sort the jobs according to increasing order of their start time
    jobs.sort(key=lambda x: x.start)

    #get the number of jobs
    n = len(jobs)

    #'tasks[i]' stores the index of non-conflicting jobs involved in the maximum profit
    tasks = [[] for _ in range(n)]

    #'maxProfit[i]' stores the total profit of jobs in 'tasks[i]'
    maxProfit = [0] * n

    #considering every job
    for i in range(n):
        #considering each 'j' less than 'i'
        for j in range(i):
            #update if the j'th job is not conflicting with the i'th job and is leading to the maximum profit
            if jobs[j].finish <= jobs[i].start and maxProfit[i] < maxProfit[j]:
                tasks[i] = tasks[j].copy()
                maxProfit[i] = maxProfit[j]

        #end the current task with i'th job
        tasks[i].append(i)
        maxProfit[i] += jobs[i].profit

    # find an index with the maximum profit
    index = 0
    for i in range(1, n):
        if maxProfit[i] > maxProfit[index]:
            index = i

    #Printing the maximum profit
    print('The maximum profit is', max(maxProfit))

    #Printing jobs involved in the maximum profit
    print('The jobs involved in the maximum profit are ', end='')
    for i in tasks[index]:
        print(jobs[i], end=' ')


if __name__ == '__main__':
    # Example usage
    jobs = [
        Job(1, 6, 6),
        Job(2, 5, 5),
        Job(5, 7, 5),
        Job(6, 8, 3)
    ]
    MaxProfitJobs(jobs)

```

# Usage

The provided Python code can be used to solve the Weighted Interval Scheduling Problem. It defines a `Job` class to store job details and a `MaxProfitJobs` function to print the non-overlapping jobs involved in the maximum profit.

To use the code, simply create a list of `Job` objects representing the jobs to be scheduled, and then call the `MaxProfitJobs` function with this list as an argument.

# Contributions

Contributions to this repository are welcome! If you have an improvement or a new solution to the Weighted Interval Scheduling Problem, feel free to open a pull request. Please ensure that your code is well-documented and follows the repository's coding standards.

# License

This project is licensed under the MIT License.
