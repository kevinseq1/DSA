# Time Complexity: O(N)
# Space Complexity: O(1)

import re

def is_palindrome(s):

    # Replace all the characters not in this set to ''
    s = re.sub(r'[^a-z0-9]', '', s.lower())

    left = 0
    right = len(s) - 1

    while left < right:
        
        if s[left] != s[right]:
            return False
        
        left += 1
        right -= 1

    return True



def is_palindrome(s):

    left = 0
    right = len(s) - 1

    while left < right:

        while left < right and not s[left].isalnum():
            left += 1
        
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False


        left += 1
        right -= 1

    return True

