"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

Time Complexity = O(n)
Space Complexity = O(n)
"""
def subarraySum(self, nums: List[int], k: int) -> int:
    counts = defaultdict(int)
    counts[0] = 1
    current = 0 
    ans = 0

    for num in nums:
        current += num
        ans += counts[current - k]
        counts[current] += 1
    
    return ans