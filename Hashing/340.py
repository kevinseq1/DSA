"""
340. Longest Substring with At Most K Distinct Characters
(Medium)

Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.

Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.

Time Complexity = O(n)
Space Complexity = O(k) # Since the hashmap will delete elements from the hash map once it grows beyond k space
"""

def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

    counts = defaultdict(int)
    left = 0
    ans = 0
    for right in range(len(s)):
        counts[s[right]] += 1
        while len(counts) > k:
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1
        
        ans = max(ans, right-left+1)

    return ans