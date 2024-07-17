"""
643. Maximum Average Subarray I
(Easy)

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000

Time Complexity = O(n)
Space Complexity = O(1)
"""

def findMaxAverage(self, nums: List[int], k: int) -> float:

    # If the length of the substring is less than 1 return 0
    if k < 1:
        return 0
    
    n = len(nums)
    curr_sum = 0

    # Get the sum of the first window
    for i in range(k):
        curr_sum += nums[i]

    # Get the max_avg of the first window
    max_avg = curr_sum / k

    # Get the max_avg for the rest of the windows
    for i in range(k, n):
        curr_sum += nums[i]      # We add an element to the window
        curr_sum -= nums[i-k]    # We remove an element from the window

        avg = curr_sum / k 
        max_avg = max(max_avg, avg)

    return max_avg