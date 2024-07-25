"""
1941. Check if All Characters Have Equal Number of Occurrences
(Easy)

Given a string s, return true if s is a good string, or false otherwise.

A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).

Example 1:

Input: s = "abacbc"
Output: true
Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.

Example 2:

Input: s = "aaabb"
Output: false
Explanation: The characters that appear in s are 'a' and 'b'.
'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.

Time Complexity = O(n)
Space Complexity = O(k) # Is the number of characters that could be in the input, which happens to be 26 in this problem
"""

def areOccurrencesEqual(self, s: str) -> bool:

    frequency = Counter(s)
    frequency_values = frequency.values()
    return len(set(frequency_values)) == 1
    