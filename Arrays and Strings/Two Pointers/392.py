"""
392. Is Subsequence
(Easy)

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false

Time Complexity = O(n)
Space Complexity = O(1)
"""

def isSubsequence(self, s: str, t: str) -> bool:

    # If lenght of s is greater than lenght of t it cannot be a sub string
    if len(s) > len(t):
        return False

    i = 0
    j = 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1

    return i == len(s)
