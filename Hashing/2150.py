"""
2150. Find All Lonely Numbers in the Array
(Medium)

You are given an integer array nums. A number x is lonely when it appears only once, and no adjacent numbers (i.e. x + 1 and x - 1) appear in the array.

Return all lonely numbers in nums. You may return the answer in any order.

Example 1:

Input: nums = [10,6,5,8]
Output: [10,8]
Explanation: 
- 10 is a lonely number since it appears exactly once and 9 and 11 does not appear in nums.
- 8 is a lonely number since it appears exactly once and 7 and 9 does not appear in nums.
- 5 is not a lonely number since 6 appears in nums and vice versa.
Hence, the lonely numbers in nums are [10, 8].
Note that [8, 10] may also be returned.

Example 2:
Input: nums = [1,3,5,3]
Output: [1,5]
Explanation: 
- 1 is a lonely number since it appears exactly once and 0 and 2 does not appear in nums.
- 5 is a lonely number since it appears exactly once and 4 and 6 does not appear in nums.
- 3 is not a lonely number since it appears twice.
Hence, the lonely numbers in nums are [1, 5].
Note that [5, 1] may also be returned.

Solution using defaultdict function
Time Complexity = O(n)
Space Complexity = O(n)
"""

def findLonely(self, nums: List[int]) -> List[int]:
    ans = []
    hashmap = defaultdict(int) # Initialize a hashmap with the default value 0

    for element in nums:
        hashmap[element] += 1
    
    for num in nums:
        if (hashmap[num] == 1) and (hashmap[num + 1] == 0) and (hashmap[num - 1] == 0):
            ans.append(num)
    
    return ans

"""
Alternate solution using the Counter function
Time Complexity = O(n)
Space Complexity = O(n)
"""

def findLonely(self, nums: List[int]) -> List[int]:
    ans = []

    hashmap = Counter(nums)
    
    for num in nums:
        if (hashmap[num] == 1) and (hashmap[num + 1] == 0) and (hashmap[num - 1] == 0):
            ans.append(num)
    
    return ans