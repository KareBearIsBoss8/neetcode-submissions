# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node1 = head
        node2 = head
        
        while node2 and node2.next:
            node1 = node1.next
            node2 = node2.next.next
            if node1 == node2:
                return True
        
        return False