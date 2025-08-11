# Time Complexity: O(N)
# Space Complexity: O(1)

def remove_nth_last_node(head, n):

    right = head
    left = head

    # Move the right pointer n nodes
    for i in range(n):
        right = right.next
    
    # If right does not exist return the next node form head
    if not right:
        return head.next
    
    # Keep moving the pointers forward as long as right.next exists
    while right.next:
        right = right.next
        left = left.next
    
    # Left points to the next of the node that needs to be removed
    left.next = left.next.next

    return head