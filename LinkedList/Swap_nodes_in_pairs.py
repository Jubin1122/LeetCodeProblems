'''

Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        
        while curr and curr.next:
            #save pts
            nxtpair = curr.next.next
            second = curr.next
            
            #reverse the pair
            second.next = curr
            curr.next =  nxtpair
            prev.next = second
            
            #update ptrs
            prev  = curr
            curr = nxtpair            
            
        return dummy.next
