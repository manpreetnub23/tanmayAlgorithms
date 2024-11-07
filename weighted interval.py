# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 19:06:40 2024

@author: TANMAY
"""

class Job:
    def __init__(self, start, finish, weight):
        self.start = start
        self.finish = finish
        self.weight = weight

def binary_search(jobs, index):
    low = 0
    high = index - 1

    while low <= high:
        mid = (low + high) // 2
        if jobs[mid].finish <= jobs[index].start:
            if mid + 1 < index and jobs[mid + 1].finish <= jobs[index].start:
                low = mid + 1
            else:
                return mid
        else:
            high = mid - 1
    return -1

# Bottom-Up Approach
def weighted_job_scheduling_bottom_up(jobs):
    jobs.sort(key=lambda job: job.finish)
    n = len(jobs)
    dp = [0] * n

    dp[0] = jobs[0].weight

    for i in range(1, n):
        incl_weight = jobs[i].weight
        l = binary_search(jobs, i)
        if l != -1:
            incl_weight += dp[l]
        
        dp[i] = max(incl_weight, dp[i - 1])

    return dp

# Top-Down Approach
# def weighted_job_scheduling_top_down(jobs, index, dp):
#     if index < 0:
#         return 0
#     if dp[index] != -1:
#         return dp[index]
    
#     # Include current job
#     incl_weight = jobs[index].weight
#     l = binary_search(jobs, index)
#     if l != -1:
#         incl_weight += weighted_job_scheduling_top_down(jobs, l, dp)

#     # Exclude current job
#     excl_weight = weighted_job_scheduling_top_down(jobs, index - 1, dp)
    
#     # Store the result
#     dp[index] = max(incl_weight, excl_weight)
#     return dp[index]

def main():
    n = int(input("Enter the number of jobs: "))
    jobs = []

    for _ in range(n):
        start = int(input("Enter start time of job: "))
        finish = int(input("Enter finish time of job: "))
        while(finish<start):
            print("finish cannot be smaller than start")
            finish = int(input("Enter finish time of job: "))
        weight = int(input("Enter weight of job: "))
        jobs.append(Job(start, finish, weight))

    # Using Bottom-Up Approach
    dp_bottom_up = weighted_job_scheduling_bottom_up(jobs)
    print("Maximum weight of non-overlapping jobs (Bottom-Up):", dp_bottom_up[-1])
    print("DP Table (Bottom-Up):", dp_bottom_up)

    # Using Top-Down Approach
    # dp_top_down = [-1] * n
    # max_weight_top_down = weighted_job_scheduling_top_down(jobs, n - 1, dp_top_down)
    # print("Maximum weight of non-overlapping jobs (Top-Down):", max_weight_top_down)
    # print("DP Table (Top-Down):", dp_top_down)


main()
