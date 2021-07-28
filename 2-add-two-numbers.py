# Leetcode Question 2

# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a 
# single digit. Add the two numbers and return the sum as a linked list. 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself. 

# Example 1:
# l1 = 2 -> 4 -> 3
# l2 = 5 -> 6 -> 4
#      7 -> 0 -> 8

# input: l1 = [2,4,3], l2 = [5,6,4]
# output: [7,0,8]

# input: l1 = [0], l2 = [0]
# output: [0]

# input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# output: [8,9,9,9,0,0,0,1]

# Approach:
# keep track of carry using a variable and simulate digit-by-digit sum starting
# from head of list (least significant digit). We will build the returning list 
# by doing digit-by-digit calculations to evaluate the correct digit value 
# starting with least significant digit. 

# Pseudocode:
# - initialize current node to dummy head of return list
# - initialize carry to 0
# - initialize p and q to head of l1 and l2 respectively
# - loop through l1 and l2 until reach both ends
#   - set x to node p's value. if p has reached end of l1, set to 0
#   - set y to node q's value. if q has reached end of l2, set to 0
#   - set sum = x + y + carry
#   - update carry = sum/10
#   - create a new node with the digit value of (sum mod 10) and set it to
#     current node's next, then advance current node to next. 
#   - advance p and q
# - check if carry = 1, if so append new node with digit 1 to return list
# - return dummy head's next node (head of return list)

class ListNode(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        dummy = ListNode(None)
        p = l1 # head of l1
        q = l2 # head of l2
        curr = dummy
        carry = 0

        while p is not None or q is not None:
            if p is not None:
                x = p.val
            else:
                x = 0
            if q is not None:
                y = q.val
            else:
                y = 0
            
            sum = x + y + carry
            carry = sum / 10
            curr.next = ListNode(sum % 10) # place non-carry digit value
            curr = curr.next
            if p is not None:
                p = p.next
            if q is not None:
                q = q.next
        
        if carry > 0:
            curr.next = ListNode(carry)
        
        return dummy.next
