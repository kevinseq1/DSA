"""
1832. Check if the Sentence Is Pangram
(Easy)

A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

Example 1:
Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.

Example 2:
Input: sentence = "leetcode"
Output: false

Time Complexity = O(n)
Space Complexity = O(1)
"""

def checkIfPangram(self, sentence: str) -> bool:
    
    seen = set(sentence)
    return len(seen) == 26