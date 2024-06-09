# function to schedule the jobs take 2 arguments array and no of jobs to schedule

def printJobScheduling(arr, t):
 
    # length of array
    n = len(arr)
 
    # Sort all jobs according to
    # decreasing order of profit
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
 
    # To keep track of free time slots
    result = [False] * t
 
    # To store result (Sequence of jobs)
    job = ['-1'] * t
    number_of_jobs_done=0
    max_profit=0
    no_of_jops_unabled_to_be_done=0
    jobs_unabled_to_be_done=[]
 
    # Iterate through all given jobs
    for i in range(len(arr)):
 
        # Find a free slot for this job (Note that we start from the last possible slot)

        for j in range(arr[i][1] - 1, -1, -1):
 
            # Free slot found
            if result[j] is False:
                result[j] = True
                job[j] = arr[i][0]
                number_of_jobs_done=number_of_jobs_done+1
                max_profit=arr[i][2]+max_profit
                break
     
    for k in range (len(arr)):
        if not arr[k][0] in job:
            jobs_unabled_to_be_done.append(arr[k][0])
            
    no_of_jops_unabled_to_be_done=len(jobs_unabled_to_be_done)
    job = [ele for ele in job if ele != '-1']
    # print the sequence
    print(job)
    print("Number of jobs done: ",number_of_jobs_done)
    print("Max profit: ",max_profit)
    print("jobs unabled to be done: ",jobs_unabled_to_be_done)
    print("Number of jobs cannot be done: ",no_of_jops_unabled_to_be_done)


# Driver's Code
if __name__ == '__main__':
    arr = [[1, 4, 20],  # Job Array
              [2, 1, 10],
              [3, 1, 40],
              [4, 1, 30]]
 
 
    print("Following is maximum profit sequence of jobs")
 
    # Function Call
    printJobScheduling(arr, 4)
