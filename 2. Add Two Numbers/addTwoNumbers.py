# URL: https://leetcode.com/problems/add-two-numbers/
# Logic:

# 1. Iterate through both linked lists: Start by iterating through both linked lists simultaneously, 
#    adding the digits from corresponding nodes, and handling the carry-over if the sum exceeds 9 (since each node is a single digit).
# 2. Handle carry and uneven lists: We need to take care of cases where one list is longer than the other and still has digits left to process. 
#    Also, if there's a carry left after the last addition, we need to add an extra node to the result list to accommodate it.
# 3. Create a new list for the result: The sum of two digits (and possibly a carry from the previous addition) will be stored in a new node in the result list. 
#    We'll maintain a pointer to the current node in the result list and update it as we proceed.
# 4. Use a dummy head for ease: To simplify list manipulation, we can use a dummy head node for the result list. 
#    This way, we avoid handling special cases for the head of the result list. 

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            total = x + y + carry
            
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        if carry > 0:
            current.next = ListNode(carry)
        
        return dummy_head.next