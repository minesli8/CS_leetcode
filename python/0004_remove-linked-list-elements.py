# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        output = []
        
        if head is None:
            return output
        
        value = head.val
        if value!=val:
            output.append(value)
            
        temp = head.next
        while temp is not None:
            value = temp.val
            if value!=val:
                output.append(value)

                
            temp = temp.next
            
        return output
    
