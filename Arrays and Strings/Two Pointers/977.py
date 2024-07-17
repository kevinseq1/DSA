"""
977. Squares of a Sorted Array
(Easy)

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?

Time Complexity = O(n)
Space Complexity = O(n)
"""

def sortedSquares(self, nums: List[int]) -> List[int]:

    n = len(nums)
    left = 0
    right = n - 1

    ans = [0] * n
    
    # Iterate from the last location in ans
    for i in range(n-1, -1, -1):
        if abs(nums[left]) < abs(nums[right]):
            ans[i] = nums[right] ** 2
            right -= 1
        else:
            ans[i] = nums[left] ** 2
            left += 1
    
    return ans

