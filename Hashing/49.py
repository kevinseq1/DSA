"""
49. Group Anagrams
(Medium)

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]

Time Complexity = O(n m log m)
Space Complexity = O(n m)
"""

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
    hashmap = defaultdict(list)
    for s in strs:
        key = "".join(sorted(s))
        hashmap[key].append(s)
    
    return hashmap.values()

"""
Alternate Solution

Time Complexity = O(n m)
Space Complexity = O(n m)
"""

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
    hashmap = defaultdict(list)

    for s in strs:
        count = [0] * 26

        for c in s:
            count[ord(c) - ord("a")] += 1

        hashmap[tuple(count)].append(s)

    return hashmap.values()