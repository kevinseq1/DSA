"""
Given a string s, return the first character to appear twice. It is guaranteed that the input will have a duplicate character.

Time Complexity = O(n)
Space Complexity = O(m) m is the number of allowable characters in the input
"""

def repeatedCharacter(self, s: str) -> str:
    seen = set()
    for c in s:
        if c in seen:
            return c
        seen.add(c)
    return " "