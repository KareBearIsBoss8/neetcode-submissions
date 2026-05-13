# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return None
        
        node1 = head
        node2 = head
        node_mid = head
        
        while node2 and node2.next:
            node_mid = node1
            node1 = node1.next
            node2 = node2.next.next
        
        node_mid.next = None

        prev = None
        curr = node1

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        dummy = ListNode()
        new = dummy
        counter = 0
        
        while head and prev:
            if counter == 0:
                new.next = head
                head = head.next
                counter = 1
            else:
                new.next = prev
                prev = prev.next
                counter = 0
            new = new.next
        
        new.next = head or prev