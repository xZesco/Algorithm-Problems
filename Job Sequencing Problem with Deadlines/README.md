# Job Sequencing Problem

## Introduction

The Job Sequencing Problem involves scheduling jobs with deadlines and associated profits to maximize the total profit earned. Each job has a deadline by which it must be completed and a profit associated with it.

## Problem Description

Given a list of jobs with deadlines and total profit earned on completing a task, the Job Sequencing Problem aims to find the maximum profit earned by executing the tasks within the specified deadlines. Each task takes one unit of time to complete, and a task can't execute beyond its deadline. Only a single task will be executed at a time.

## Implementation

### Python Implementation

```python
# A class to store job details.
class Job:
    def __init__(self, jobID, deadline, profit):
        self.jobID = jobID
        self.deadline = deadline
        self.profit = profit

# Function to schedule jobs to maximize profit
def job_sequencing(jobs):
    # stores the maximum profit that can be earned
    profit = 0

    # As there is no maximum deadline so we will use 24 hours as a day
    time = 24
 
    # list to store used and unused slots for our variable time
    slot = [0] * time
 
    # sort the jobs according to decreasing order of their profits
    jobs.sort(key=lambda x: x.profit, reverse=True)
 
    # consider every job
    for job in jobs:
        # search for the next free slot and map the task to that slot
        # we used reversed order to schedule the job in the latest possible slot (nearest to the deadline)
        for j in reversed(range(job.deadline)):
            if slot[j] == 0:
                slot[j] = job.jobID
                profit += job.profit
                break
 
    # print the scheduled jobs and remove the empty slots
    print('The scheduled jobs are', list(filter(lambda x: x != 0, slot)))
 
    # print total profit that can be earned
    print('The total profit earned is', profit)

if __name__ == '__main__':
    # List of given jobs
    jobs = [
        Job(1, 4, 20),
        Job(2, 1, 10),
        Job(3, 1, 40),
        Job(4, 1, 30)
    ]
 
    # schedule jobs and calculate the maximum profit
    job_sequencing(jobs)

```

## Usage

The provided Python code can be used to solve the Job Sequencing Problem. It defines a `Job` class to store job details and a `job_sequencing` function to schedule jobs and maximize profit.

To use the code, simply create a list of `Job` objects representing the jobs to be scheduled, and then call the `job_sequencing` function with this list as an argument.

## Contributions

Contributions to this repository are welcome! If you have an improvement or a new solution to the Job Sequencing Problem, feel free to open a pull request. Please ensure that your code is well-documented and follows the repository's coding standards.

## License

This project is licensed under the MIT License.
