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
# - initially, fill array of reservoir R[] with the heading elements from the pool of samples
#   S[]. At the end of the algo, the reservoir will contain the final elements we sample from 
#   the pool. 
# - then iterate through rest of elements in the pool. For each element, we need to decide if
#   we want to include it in the reservoir or not. If so, we will replace an existing element
#   in reservoir with current element. 

# - proof that each element scanned so far has equal chance to be selected into reservoir: 

# - suppose that we have an element at index of i (i > k), when we reach the element, the chance
#   it will be selected into the reservoir would be k/i. 
# - later, there is a chance any chosen element in the reservoir might be replaced with a subsequent
#   element. more specifically, when we reach element j (j > i), there would be chance of 1/j for any 
#   specific element in reservoir is replaced. Bc for any specific position in reservoir, there is 1/j
#   chance that it might be chosen by random number generator. On the other hand, there is (j-1)/j 
#   probability for any specific element in reservoir to stay in reservoir at moment of sampling. 
# - to sum up, in order for any element in pool to be chosen in final reservoir, a series of independent
#   events need to occur: 
#       - first, element needs to be chosen in reservoir when we reach the element
#       - second, in the following sampling, element should remain in reservoir, not be replaced
# - therefore, for a sequence of length n, the chance any element ends up in final reservoir represented by:
#   k/i * i/(i+1) * (i+1)/(i+2) * ... * (n-1)/n = k/n 

# Pseudo:
# __init__: simply keep head of linked list, rather than convert to array
# getRandom(): do reservoir sampling starting from head of linked list. More specifically, we scan the 
#   element one by one and decide whether we should put it into the reservoir (which in our case happens to
#   be of size one).

class Solution:
    def __init__(self, head):
        """
        @param head: linked list's head
        Note the head is guaranteed to not be null, so it contains at least one node
        """
        self.head = head