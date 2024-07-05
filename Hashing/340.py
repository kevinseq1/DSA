"""
You are given a string s and an integer k. Find the length of the longest substring that contains at most k distinct characters.

Example 1:
Given s = "eceba" and k = 2, return 3. 
The longest substring with at most 2 distinct characters is "ece".

Time Complexity = O(n)
Space Complexity = O(k)
"""

def find_longest_substring(self, s: str, k: int) -> int:
    counts = defaultdict(int)
    left = 0
    ans = 0
    for right in range(len(s)):
        count[s[right]] += 1
        while len(counts) > k:
            counts[s[left]] -= 1
            if counts[s[left]] == 0
                del counts[s[left]]
            left += 1
        ans = max(ans, right - left + 1)
    return ans