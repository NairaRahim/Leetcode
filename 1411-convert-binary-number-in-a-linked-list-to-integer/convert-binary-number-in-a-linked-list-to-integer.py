# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        length = 0
        temp = head
        while(temp):
            length+=1
            temp=temp.next
        
        result=0
        length -=1
        while(head):
            result += (2**length)* head.val
            length-=1
            head = head.next
        
        return result


        