# Leetcode Question 1670 [Medium]
# Design Front Middle Back Queue

# Design a queue that supports push and pop operations in the front, middle, and back.

# Implement the FrontMiddleBack class:
# - FrontMiddleBack(): initializes the queue
# - void pushFront(int val): Adds val to the front of the queue
# - void pushMiddle(int val): Adds val to the middle of the queue
# - void pushBack(int val): Adds val to the back of the queue
# - int popFront(): Removes the front element of the queue and returns it. If the 
#   queue is empty, return -1. 
# - int popMiddle(): Removes the middle element of the queue and returns it. If 
#   the queue is empty, return -1. 
# - int popBack(): Removes the back element of the queue and returns it. If the 
#   queue is empty, return -1. 

# Notice that when there are two middle position choices, the operation is performed
# on the FRONTMOST middle position choice. For example:

# - pushing 6 into the middle of [1,2,3,4,5] results in [1,2,6,3,4,5]
# - popping the middle from [1,2,3,4,5,6] results in [1,2,4,5,6]

# Example 1:
# Input: ["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
#        [[], [1], [2], [3], [4], [], [], [], [], []]
# Output: [null, null, null, null, null, 1, 3, 4, 2, -1]

# Explanation:
# FrontMiddleBackQueue q = new FrontMiddleBackQueue();
# q.pushFront(1);   // [1]
# q.pushBack(2);    // [1, 2]
# q.pushMiddle(3);  // [1, 3, 2]
# q.pushMiddle(4);  // [1, 4, 3, 2]
# q.popFront();     // return 1 -> [4, 3, 2]
# q.popMiddle();    // return 3 -> [4, 2]
# q.popMiddle();    // return 4 -> [2]
# q.popBack();      // return 2 -> []
# q.popFront();     // return -1 -> [] (Queue is empty)

# Approach 1: Brute force, single array approach

# Approach 2: Use 2 double-ended queues (deque)

class FrontMiddleBackQueue(object):
    
    def __init__(self):
        self.q = []

    def pushFront(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.q.insert(0, val) # insert val into position 0 of list
        

    def pushMiddle(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.q.insert(len(self.q) / 2, val)

    def pushBack(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.q.append(val)

    def popFront(self):
        """
        :rtype: int
        """
        return (self.q or [-1]).pop(0)

    def popMiddle(self):
        """
        :rtype: int
        """
        return (self.q or [-1]).pop((len(self.q) - 1) / 2)

    def popBack(self):
        """
        :rtype: int
        """
        return (self.q or [-1]).pop()


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()

# Approach 2: 

import collections
class FrontMiddleBackQueue2(object):
    
    def __init__(self):
        self.first, self.second = collections.deque(), collections.deque()

    def pushFront(self, val):
        self.first.appendleft(val)
        self.balance()
    
    def pushMiddle(self, val):
        if len(self.first) > len(self.second):
            self.second.appendleft(self.first.pop())
        self.first.append(val)
    
    def pushBack(self, val):
        self.second.append(val)
        self.balance()
    
    def popFront(self):
        val = self.first.popleft() if self.first else -1
        self.balance()
        return val
    
    def popMiddle(self):
        val = (self.first or [-1]).pop()
        self.balance()
        return val

    def popBack(self):
        # if second half queue is empty, pop first half
        val = (self.second or self.first or [-1]).pop() 
        self.balance()
        return val

    # keep len(first) >= len(second)
    def balance(self):
        if len(self.front) > len(self.back) + 1:
            self.back.appendleft(self.front.pop())
        if len(self.front) < len(self.back):
            self.front.append(self.back.popleft())

    