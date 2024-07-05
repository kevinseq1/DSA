"""
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
Space Complexity = O(n)
"""

def checkIfPangram(self, sentence: str) -> bool:
    x = set(sentence)
    if len(x) == 26:
        return True
    else:
        return False