# Leetcode Question 234 Palindrome Linked List

# Given the head of a singly linked list, return true if it is a palindrome

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Example 1: 
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
"""

"""
Approach 1: Copy into ArrayList and use Two Pointer Technique

Intuition: 
There are 2 commonly used List implementations, ArrayList and Linked List. 
    - an Array List uses an underlying Array to store value. We can access 
        the value at any position in the list in O(1) time, as long as we
        know the index. Based on underlying memory addressing. 
    - Linked List uses Objects commonly called Nodes. Each Node holds a 
        value and a next pointer to the next node. Accessing a node at a 
        particular index would take O(N) time because we have to go down
        the list using next pointers. 

Determining whether or not an Array List is a palindrome is straight-forward.
We can simply use the two-pointer technique to compare indexes at either end,
moving in towards the middle. One pointer starts at the start and goes up, 
and the other starts at the end and goes down. This would take O(N) because 
each index access is O(1) and there are n index accesses in total. 

However, its not so straightforward for Linked List. Accessing the values in 
any order other than forward, sequentially, is not O(1). Unfortunately, this 
includes (iteratively) accessing the values in reverse. We will need a diff 
approach. 

On the plus side, making a copy of a Linked List values into an Array List is 
O(N). Therefore, the simplest solution is to copy the values of the Linked List
into an Array List. 

Algorithm:
1. Copy the Linked List into an Array. 
2. Checking whether or not the Array is a palindrome. 

To do the first step, we need to iterate through the Linked List, adding each 
value to an array. We do this by using a variable currentNode to point at the 
current Node we're looking at, and at each iteration, adding currentNode.val 
to the array and updating currentNode to point to currentNode.next. Stop 
looping when currentNode points to null node. 
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]

# Time Complexity: O(N)
# Space Complexity: O(N)

"""
Approach 2: Reverse Second Half In-Place

Intuition:
In order to avoid using O(N) extra space, we have to modify the input in-place.

We can reverse the second half of the LinkedList in-place, and then comparing 
it with the first half. Afterwards, we should re-reverse the second half and 
put the list back together. While you don't need to restore the list to pass 
the test cases, it is still good programming practice because the function 
could be a part of a bigger program that doesn't want the LinkedList broken. 

Algorithm:
1. Find the end of the first half.
2. Reverse the second half. 
3. Determine whether or not there is a palindrome.
4. Restore the list.
5. Return the result.

Two runners pointer technique:
Imagine we have 2 runners one fast and one slow, running down the nodes of the 
Linked List. In each second, the fast runner moves down 2 nodes, and the slow 
runner just 1 node. By the time the fast runner gets to the end of the list, 
the slow runner will be half way. By representing the runners as pointers, 
and moving them down the list at the corresponding speeds, we can use this 
trick to find the middle of the list, and then split the list into two halves. 

If there is an odd-number of nodes, then the "middle" node should remain attached to the first half. 
"""

class Solution2:
    def isPalindrome(self, head):
        if head is None:
            return True
        
        # find end of first half and reverse second half
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # check whether or not palindrome
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # restore list and return result
        first_half_end.next = self.reverse_list(second_half_start)
        return result

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def reverse_list(self, head):
        prev = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
        return prev

# Time Complexity: O(N)
# Space Complexity: O(1)