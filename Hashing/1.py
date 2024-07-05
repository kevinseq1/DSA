"""
Given an array of integers nums and an integer target, return indices of two numbers such that they add up to target. You cannot use the same index twice.

Time Complexity = O(n)
Space Complexity = O(n)
"""

def twoSum(self, nums: List[int], target: int) -> List[int]:
    dic = {}
    for i in range(len(nums)):
      num = nums[i]
      complement = target - num
      if complement in dic:
        return [dic[complement], i]
    
      dic[num] = i

    return [-1,1]
