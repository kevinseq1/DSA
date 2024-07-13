"""
19. Remove Nth Node From End of List
(Medium)

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]


Time Complexity = O(n)
Space Complexity = O(1)
"""

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

    dummyNode = ListNode(0, head)
    slow = dummyNode
    fast = head

    for _ in range(n):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next
    
    slow.next = slow.next.next

    return dummyNode.next