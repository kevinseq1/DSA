"""
1. Top k elements in a list
(Medium)

Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:
Input: nums = [1,2,2,3,3,3,3,3], k = 2
Output: [2,3]

Example 2:
Input: nums = [7,7], k = 1
Output: [7]

Constraints:
1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.

Time Complexity = O(n)
Space Complexity = O(n)
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hm = Counter(nums)                                # Num -> Count
        freq = [[] for i in range(len(nums) + 1)]         #  0    1    2    3    4    5    6   7   8    How many times each element occurs
                                                          # [[]  [1]  [2]  [ ]  [ ]  [3]  [ ] [ ] [ ]]  Element is add to the corresponding subarray

        for num, count in hm.items():
            freq[count].append(num)
        
        res = []

        for i in range(len(freq) - 1, -1, -1):        # From the end go until the first element one element at a time
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res


        