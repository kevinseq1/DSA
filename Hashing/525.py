"""
525. Contiguous Array
(Medium)

Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Time Complexity = O(n)
Space Complexity = O(n)
"""

def findMaxLength(self, nums: List[int]) -> int:
    
    zero = 0 
    one = 0
    res = 0
    diff = {} # count[1] - count[0] -> index

    for i, n in enumerate(nums):
        if n == 0:
            zero += 1
        else:
            one += 1
        
        if one - zero not in diff:
            diff[one - zero] = i
        
        if one == zero:
            res = one + zero
        else:
            index = diff[one - zero]
            res = max(res, i - index)

        
    return res

