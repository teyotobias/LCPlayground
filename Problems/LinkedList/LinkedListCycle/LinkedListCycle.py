#have not done yet

def hasCycle(head):
    if not head or not head.next: return False        
    slow, fast = head, head.next
    while slow != fast:
        if not fast or not fast.next: return False
        slow, fast = slow.next, fast.next.next
    return True
