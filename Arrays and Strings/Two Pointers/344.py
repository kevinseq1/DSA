"""
344. Reverse String
(Easy)

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Time Complexity = O(n)
Space Complexity = O(1)
"""

def reverseString(self, s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """

    left = 0
    right = len(s) - 1

    while left < right:
        tmp = s[right]
        s[right] = s[left]
        s[left] = tmp

        left += 1
        right -= 1
    
    return
