"""
49. Anagram Groups
(Medium)

Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:
Input: strs = ["x"]
Output: [["x"]]

Example 3:
Input: strs = [""]
Output: [[""]]

Constraints:
1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.

Time Complexity = O(m n log n)
Space Complexity = O(m n)
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = defaultdict(list)

        for w in strs:
            key = "".join(sorted(w))
            ans[key].append(w)
        
        return ans.values()


"""
Alternate Solution

Time Complexity = O(m n)
Space Complexity = O(m n)
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26                      # Since its lower case character a - z (26)
            for c in s:
                count[ord(c) - ord("a")] += 1     # Current character - a   
            ans[tuple(count)].append(s)           # Since lists cannot be keys in Python
        
        return ans.values()