#have not done yet
# Runtime: 55 ms, faster than 73.02% of Python3 online submissions for Linked List Cycle.
# Memory Usage: 20.5 MB, less than 67.99% of Python3 online submissions for Linked List Cycle.
def hasCycle(head):
    if not head or not head.next: return False        
    slow, fast = head, head.next
    while slow != fast:
        if not fast or not fast.next: return False
        slow, fast = slow.next, fast.next.next
    return True
