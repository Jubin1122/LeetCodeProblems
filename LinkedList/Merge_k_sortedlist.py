'''
Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if lists == []:
            return ListNode().next
        
        if not(lists[0]):
            return ListNode().next
            
        l1 = lists[0]
        l2 = lists[1]
        l3 = lists[2]
        
        l_dumm = ListNode()
        l_final = ListNode()
        tail_1 = l_dumm
        tail_2 = l_final
        
        
        while l1 and l2:
            if l1.val < l2.val:
                tail_1.next = l1 
                l1 = l1.next
                
            else:
                tail_1.next = l2
                l2 = l2.next
                
            tail_1 = tail_1.next
            
        if l1:
            tail_1.next = l1
            
        elif l2:
            tail_1.next = l2
            
        temp = l_dumm.next
        
        while temp and l3:
            if temp.val < l3.val:
                tail_2.next = temp
                temp = temp.next
                
            else:
                tail_2.next = l3
                l3 = l3.next
                
            tail_2 = tail_2.next
            
        if temp:
            tail_2.next = temp
            
        elif l3:
            tail_2.next = l3
        
        
        return l_final.next