#---------------------------------------------------------------------------
"""2. Add Two Numbers: You are given two non-empty linked lists representing 
two non-negative integers. The digits are stored in reverse order, and each 
of their nodes contains a single digit. Add the two numbers and return the 
sum as a linked list. You may assume the two numbers do not contain any 
leading zero, except the number 0 itself.."""
#---------------------------------------------------------------------------
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head, tmp, carry = None, None, 0
        while l1 is not None or l2 is not None:
            sums = carry  
            if l1 is not None:
                sums += l1.val
                l1 = l1.next
            if l2 is not None:
                sums += l2.val
                l2 = l2.next        
            node = ListNode(sums % 10)
        
            carry = sums // 10
        
            if tmp is None:
                tmp = head = node        
            else:
                tmp.next = node
                tmp = tmp.next                 
        if carry > 0:
            tmp.next = ListNode(carry)
        return head

#---------------------------------------------------------------------------
# Convert LinkedList to List
def toList(l):
    lst = []
    while(l):
        lst.append(l.val)
        l = l.next
    return lst
#---------------------------------------------------------------------------
if __name__ == '__main__':
    inst2 = Solution()
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))    
    print(toList(inst2.addTwoNumbers(l1, l2)))
#---------------------------------------------------------------------------
# Location: cd /home/alem/0_Alem/alemprojects/FinalNotes/4_Algorithms/LeetCode/
#---------------------------------------------------------------------------