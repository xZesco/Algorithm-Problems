#class to store the Job
class Job:
    def __init__(self, start, finish, profit):
        self.start = start
        self.finish = finish
        self.profit = profit

    #representation for printing the jobs involved in the maximum profit
    def __repr__(self):
        return str((self.start, self.finish, self.profit))
 



#____________________________________________________________________________________________________________



#Function to print the non-overlapping jobs involved in maximum profit
def MaxProfitJobs(jobs):
 
    #base case
    if not jobs:
        return 0
 
    #sort the jobs according to increasing order of their start time
    jobs.sort(key=lambda x: x.start)
 
    #get the number of jobs
    n = len(jobs)
    """ print(n) """
 
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
                """ print(tasks) """
                maxProfit[i] = maxProfit[j]
                """ print(maxProfit) """
                
 
        #end the current task with i'th job
        tasks[i].append(i)
        """ print(tasks) """
        maxProfit[i] += jobs[i].profit
        """ print(maxProfit) """
 

    # find an index with the maximum profit
    index = 0
    for i in range(1, n):
        if maxProfit[i] > maxProfit[index]:
            index = i


    #Printing the maximum profit
    print('The maximum profit is',max(maxProfit))
 

    #Printing jobs involved in the maximum profit
    print('The jobs involved in the maximum profit are ', end='')
    for i in tasks[index]:
        print(jobs[i], end=' ')



#____________________________________________________________________________________________________________


 
 
if __name__ == '__main__':
 
    jobs = [
        Job(1, 6, 6),
        Job(2, 5, 5),
        Job(5, 7, 5),
        Job(6, 8, 3)
    ]
    MaxProfitJobs(jobs)