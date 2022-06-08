# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        lis = ListNode()
        head = lis
        c = 0
        
        while l1 or l2 or c:
            a1=a2=0
            
            if l1:
                a1 = l1.val
                l1 = l1.next
            if l2:
                a2 = l2.val
                l2 = l2.next
                
            total = a1+a2+c
            
            if total > 9:
                c = 1
                total = total % 10
            else:
                c=0
            
            non = ListNode(total)
            lis.next = non
            lis = lis.next
            
        return head.next