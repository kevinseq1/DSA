"""
242. Valid Anagram
(Easy)

Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: s = "racecar", t = "carrace"
Output: true

Example 2:
Input: s = "jar", t = "jam"
Output: false

Constraints:
s and t consist of lowercase English letters.

Time Complexity = O(s + t)
Space Complexity = O(s + t)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        count_s = defaultdict(int)
        count_t = defaultdict(int)

        for i in range(len(s)):
            count_s[s[i]] += 1
            count_t[t[i]] += 1
        
        return count_s == count_t


"""
Alternate Solution

Time Complexity = O(n log n)
Space Complexity = O(1)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        if sorted(s) == sorted(t):
            return True
        
        return False