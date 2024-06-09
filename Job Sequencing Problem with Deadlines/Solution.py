#A class to store job details.
class Job:
    def __init__(self, jobID, deadline, profit):
        self.jobID = jobID
        self.deadline = deadline
        self.profit = profit




#____________________________________________________________________________________________________________



#Function to schedule jobs to maximize profit
def job_sequencing(jobs):
 
    #stores the maximum profit that can be earned
    profit = 0

    #As there is no maximum deadline so we will use 24 hour as a day
    time = 24
 
    #list to store used and unused slots for our variable time
    slot = [0] * time
    """ print(slot) """
 
    #sort the jobs according to decreasing order of their profits
    jobs.sort(key=lambda x: x.profit, reverse=True)
 
    #consider every job
    for job in jobs:
        #search for the next free slot and map the task to that slot
        #we used reversed order to schedule the job in the latest possible slot (nearest to the deadline)
        for j in reversed(range(job.deadline)):
            if slot[j] == 0:
                slot[j] = job.jobID
                profit += job.profit
                break
 
    #print the scheduled jobs and remove the empty slots
    print('The scheduled jobs are', list(filter(lambda x: x != 0, slot)))
 
    #print total profit that can be earned
    print('The total profit earned is', profit)




#____________________________________________________________________________________________________________
 
 

if __name__ == '__main__':
 
    #List of given jobs
    jobs = [
        Job(1, 4, 20),
        Job(2, 1, 10),
        Job(3, 1, 40),
        Job(4, 1, 30)
    ]
 
    #schedule jobs and calculate the maximum profit
    job_sequencing(jobs)
