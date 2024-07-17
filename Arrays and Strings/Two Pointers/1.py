"""
1. Two Sum
(Easy)

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]


Soluton for sorted array (Time Complexity is n log n if you had to first sort the array)
Time Complexity = O(n)
Space Complexity = O(1)
"""

def twoSum(self, nums: List[int], target: int) -> List[int]:

    left = 0
    right = len(nums) -  1

    while left < right:
        total_sum = nums[left] + nums[right]
        if total_sum == target:
            return [left, right]
        elif total_sum > target:
            right -= 1
        else:
            left += 1
    
    return

"""
Solution using a Hashmap
Time Complexity = O(n)
Space Complexity = O(n)
"""

def twoSum(self, nums: List[int], target: int) -> List[int]:
    
    hashmap = {}

    for index, value in enumerate(nums):

        complement = target - value

        if complement in hashmap:
            return [hashmap [complement], index]
        
        hashmap[value] = index
    
    return []
