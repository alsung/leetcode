# Leetcode Question 206

# Given the head of a singly linked list, reverse the list, and return the reversed list. 

# input: head = [1, 2, 3, 4, 5]
# output: [5, 4, 3, 2, 1]

# input: head = [1, 2]
# output: [2, 1]

# input: head = []
# output: []


# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # print head: 
        # ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, 
        # next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}

        curr_node = head
        prev_node = None
        while curr_node != None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        
        head = prev_node
        
        return head

    def append(self, head, data):
        new_node = ListNode(data)
        curr_node = head
        while curr_node.next != None:
            curr_node = curr_node.next
        curr_node.next = new_node




