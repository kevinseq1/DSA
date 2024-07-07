"""
Given a string s, determine if all characters have the same frequency.

Example 1: 
Given s = "abacbc"
return true.  All characters appear twice. 

Example 2:
Given s = "aaabb", return false. "a" appears 3 times, "b" appears 2 times. 3 != 2.

Time Complexity = O(n)
Space Complexity = O(k) k is the number of characters that could be in the input, which happens to be 26 in this problem
"""

def areOccurencesEqual(self, s: str) -> bool:
    counts = defaultdict(int)
    for c in s:
        counts[s[c]] += 1
    
    frequencies = counts.values()
    return len(set(frequencies)) == 1


"""
Alternate one liner solution
"""

def areOccurencesEqual(self, s: str) -> bool:
    return len(set(counter(s).values())) == 1