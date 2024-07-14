"""
206. Reverse Linked List
(Easy)

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []


Time Complexity = O(n)
Space Complexity = O(1)
"""

def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
    prev = None
    curr = head

    while curr:
        next_node = curr.next # First, make sure we do not lose the next node
        curr.next = prev      # Reverse the direction of the pointer
        prev = curr           # Set the current node to prev for next_node
        curr = next_node      # Set current as the next node

    return prev

"""
Recrusive Method
Time Complexity = O(n)
Space Complexity = O(n)
"""
def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:

    # Handles empty linked list and a linked list with one node
    if not head or not head.next:
        return head
    
    reversed_list_head = reverseLinkedList(head.next)
    
    # Get the last node after the list is reversed
    last_node = head.next

    # Set the current node as the last_node's next element
    last_node.next = head
    head.next = None

    return reversed_list_head
    

    