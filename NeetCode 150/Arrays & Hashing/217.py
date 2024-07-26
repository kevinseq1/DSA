"""
217. Contains Duplicate
(Easy)

Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:
Input: nums = [1, 2, 3, 3]
Output: true

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false

Time Complexity = O(n)
Space Complexity = O(n)
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
        hs = set()
        
        for n in nums:
            if n in hs:
                return True
            hs.add(n)

        return False

         