# Leetcode Question 382

# Given a singly linked list, return a random node's value from the linked 
# list. Each node must have the same probability of being chosen. 

# Example 1: 
# 1 --> 2 --> 3

# input: 
# ["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
# [[[1, 2, 3]], [], [], [], [], []]
# output: 
# [null, 1, 3, 2, 2, 3]

# explanation:
# Solution solution = new Solution([1, 2, 3]);
# solution.getRandom(); // return 1
# solution.getRandom(); // return 3
# solution.getRandom(); // return 2
# solution.getRandom(); // return 2
# solution.getRandom(); // return 3
# getRandom() should return either 1, 2, or 3 randomly. Each element should have
# equal probability of returning. 

#========================================================================================

# Approach #1: Fixed-Range Sampling

# convert linked list to a simple list and calculate length of linked list in init
# then when getRandom is called, randomly choose index to return value from list. 

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import random

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        curr = head
        self.total = 0
        self.node_list = []
        
        while curr is not None:
            self.total+=1
            self.node_list.append(curr.val)
            curr = curr.next
        
    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        index = int(random.random() * self.total)
        return self.node_list[index]
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

# Caveats:
# - requires some space to keep pool of elements for sampling
# - cannot cope with list of ever-growing elements. say we have a stream of numbers, 
#   we have to keep all values in memory, not scalable. 

# Time Complexity: O(N)
# Space Complexity: O(N), need to keep track of separate pool of values 

#========================================================================================

# Approach #2: Reservoir Sampling
# - to do random sampling over a population of unknown size with constant space. 

