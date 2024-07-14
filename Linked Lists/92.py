"""
92. Reverse Linked List II
(Medium)

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]

Time Complexity = O(n)
Space Complexity = O(1)
"""

def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    
        if not head or left == right:
            return head
            
        dummy = ListNode(0, head)
        before_node = dummy

        # Move the pointer to the node just before the sub list to reverse
        for _ in range(left - 1):
            before_node = before_node.next

        prev = before_node
        curr = before_node.next

        # Reverse the list from the left upto right
        for _ in range(right-left + 1):
            new_node = curr.next
            curr.next = prev
            prev = curr
            curr = new_node

        # Point the node at the left pointer to new_node
        left_node = before_node.next
        left_node.next = curr

        # Point the node just before left to the node at the right pointer
        before_node.next = prev

        return dummy.next