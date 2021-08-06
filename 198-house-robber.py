# Leetcode Question 198 [Medium]
# House Robber

# You are a professional robber planning to rob houses along a street. Each 
# house has a certain amount of money stashed, the only constraint stopping 
# you from robbing each of them is that adjacent houses have security systems 
# connected and it will automatically contact the police if two adjacent 
# houses were broken into on the same night. 

# Given an integer array nums representing the amount of money of each house, 
# return the maximum amount of money you can rob tonight without alerting the 
# police. 

# Example 1: 
# input: nums = [1,2,3,1]
# output: 4
# explanation: rob house 1 (money = 1) then rob house 3 (money = 3). 1 + 3 = 4

# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400

# =============================================================================
# Simple Dynamic Programming Approach
class Solution(object):
    def rob(self, nums):
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

# Time: O(n)
# Space: O(1)

# =============================================================================
# Approach 1: Recursion with Memoization

# The easiest approach is to try all possible combinations of house choices and
# then use the combination that gives the maximum amount of money. We do this 
# bc there is no plausible greedy strategy we can use to decide if the robber 
# should rob a particular house or not. 

# We rely on recursion whenever we have choices involved in solving a problem. 
# Technically, a robber can come back and rob a house that they previously 
# rejected. However, since we are trying all options, we will not go back and 
# rob an unrobbed house since that scenario with be covered in a different 
# recursive path. 

# The basic choice that we make is whether to rob the current house or not. 
# If the robber decides to rob the current house, they have to skip the next 
# house. Otherwise, they can evaluate the same choice on the next house i.e. 
# to rob or not to rob. 

# Subproblems:
# To approach a problem recursively, we need to make sure that it can be 
# broken down into sub-problems. Additionally, we need to ensure that the 
# optimal solution to these sub-problems can be used to form the solution to 
# the main problem. Let's see how we can divide this problem into smaller 
# recursive problems. 

# Let's say that we have a function called robFrom() which we will use to 
# solve this rpblem. The only input this function takes is an index, position. 
# This position essentially represents a suffix in the array which we, the 
# robber, have yet to scan. Essentially, the position indicates that the 
# robber has yet to scan houses [position, ..., N] where N represents the 
# total number of houses. 

# Naturally, the answer to our problem would be the function call robFrom(0) 
# which means scan all the houses and return the maximum profit. Now let's 
# think about robFrom(i) for a moment. This simply represents a sub-array or 
# a suffix from the main array. We can think about this as a smaller 
# max-profit problem in itself, can't we? 

# A suffix of the initial set of houses simply means a smaller set of houses 
# that the robber has to consider. We will be working with the assumption that 
# in the function call robFrom(i), the robber has to maximize their profit from 
# i..N houses. 

# At each step, the robber has two options. If he chooses to rob the current 
# house, he will have to skip the next house on the list by moving two steps 
# forward. If he chooses not to rob the current house, he can simply move on 
# to the next house in the list. Mathematically: 

# robFrom(i) = max( robFrom(i + 1), robFrom(i + 2) + nums(i) )

# Recursion tree and memoization: 
# Now that we have an idea about the recursive structure of our problem, let's 
# look at the recursion tree which will be formed. This is important so that 
# we can determine if we have repeating sub-problems, in which case we can use 
# memoization or caching to reduce the overall solution complexity. 

#                  robFrom(0)
#              /              \   
#       robFrom(1)           robFrom(2)
#       /        \          /         \
# robFrom(2) robFrom(3) robFrom(3) robFrom(4)
#
#           0
#          / \
#         1   2
#        / \ / \
#       2  3 3  4
#
# As we can see from the recursion tree, we have repeating sub-problems (nodes)
# marked the same. A repeating node in the tree represents an entire subtree 
# calcuation that has to be repeated which is computationally expensive. Hence,
# we cache the already computed results so we don't need to re-calculate the 
# maximum profit for previously seen sub-problems. 

# Algorithm: 
#   1. Define a function called robFrom() which takes the index of the house 
#      that the robber currently has to examine. Also, this function takes the 
#      nums array which is required during the calculations. 
#   2. At each step of recursive call, robber has two options. rob current 
#      house or not. 
#       1. If robber chooses to rob current house, then have to skip next house
#          i.e. robFrom(i+2, nums). The answer here would be what is returned
#          by robFrom(i+2, nums) in addition to the amount that robber will get
#          by robbing the current house nums[i]
#       2. Otherwise, can move onto next house and return whatever profit he 
#          will make in sub-problem i.e. robFrom(i+1, nums)
#   3. We need to find, cache, and return maximum of two options at each step.
#   4. robFrom(0, nums) will give us answer to entire problem. 

class Solution1(object):
    def __init__(self):
        self.mem = {}

    def rob(self, nums):
        self.mem = {}
        return self.robFrom(0, nums)

    def robFrom(self, i, nums):
        # if no more houses left to examine
        # base case
        if i >= len(nums):
            return 0

        # return cached value
        if i in self.mem:
            return self.mem[i]

        # recursion relation evaluation to get optimal answer
        ans = max(self.robFrom(i + 1, nums), self.robFrom(i + 2, nums) + nums[i])

        # cache for future use
        self.mem[i] = ans

        return ans

# =============================================================================
# Approach 2: Dynamic Programming

# Intuition:
# The idea here is same as before except instead of recursive approach, we go 
# with tabular approach. The recursive approach may run into trouble when the 
# recusion stack grows too large. It may also run into trouble because, for 
# each recursive, the compiler must additional work to maintain the call stack 
# (function variables, etc.) which results in unwanted overhead. The dynamic 
# programming approach is simply a tabular formulation of ideas presented 
# above. 

# The cache we had before will still exist in this approach but instead of 
# calling it a cache, we will refer to it as our dynamic programming table. 
# Every DP solution has a table that we ppulate starting with the base case or 
# the simplest of cases for which we already know the answer. E.g. for our 
# problem, we know that in the absence of houses, the robber will make 0 
# profit. Similarly, if there is just one house left to rob, the robber will 
# rob that house, and that will be maximum profit. 

# We start by populating the dynamic programming table with these initial 
# values and then build the table in a bottom-up fashion which is the essence 
# of this solution. 

# Algorithm Pseudocode

#   1. We define a table which we will use to store the results of our 
#      sub-problems. Let's call this table maxRobbedAmount where 
#      maxRobbedAmount[i] is the same value that would be returned by 
#      recursive solution.  
#   2. We set maxRobbedAmount[N] to 0 since this means the robber doesn't 
#      have any houses left to rob, thus zero profit. Additionally, we set 
#      maxRobbedAmount[N - 1] to nums[N - 1] because in this case, there is 
#      only one house to rob which is the last house. Robbing it will yield 
#      the maximum profit. 
#   3. We iterate from N - 2 down to 0 and set 
#      maxRobbedAmount[i] = max(maxRobbedAmount[i + 1], maxRobbedAmount[i + 2] 
#      + nums[i])). Note that this is the same as the recursive formulation in 
#      the previous solution. The only difference is that we have already 
#      calculated the solutions to the sub-problems and we simple reuse the 
#      solutions in O(1) time when calculating the solution to the main problem
#   4. We return the value in maxRobbedAmount[0]

class Solution2:
    def rob(self, nums):
        # special handling for empty case
        if not nums:
            return 0

        maxRobbedamount = [None for _ in range(len(nums) + 1)]
        N = len(nums)

        # Base case initialization
        maxRobbedamount[N], maxRobbedamount[N-1] = 0, nums[N - 1]

        # DP table calculation
        for i in range(N-2, -1, -1):

            # same as recursive solution
            maxRobbedamount[i] = max(maxRobbedamount[i + 1], \
                maxRobbedamount[i + 2] + nums[i])

        return maxRobbedamount[0]

# Time: O(N) since we loop from N-2...0
# Space: O(N) is used by table. When number of houses is large, a recursion 
# stack can become a serious limitation, because the recursion stack size will 
# be huge and the compiler will eventually run into stack-overflow problems. 

# =============================================================================
# Approach 3: Optimized Dynamic Programming

# Intuition
# This is the exact same solution as previous one with exception that we will 
# be optimizing the space complexity here. Let's look at the recursive relation
# again to see where we can reduce the amount of space used. 

# robFrom(i) = max(robFrom(i + 1), robFrom(i + 2) + nums[i])

# To calculate the current value, we just need to rely on the next two 
# consecutive values/recursive calls. 

# Porting this idea over to our dynamic programming solution we see that in 
# order to calculate the value at a current index in the dynamic programming 
# table, we simply need to know the next two values i.e. maxRobbedAmount[I + 1]
# and maxRobbedAmount[i + 2]. In the end, we will return the value of 
# maxRobbedAmount[0]. 

# Instead of keeping an entire table for storing these cached values, we can 
# get by with simply keeping track of the "next" two values. 

# Algorithm Pseudocode

#   1. We will make two variables robNext and robNextPlusOne which at any point
#      will represent the optimal solution for maxRobbedAmount[i + 1] and 
#      maxRobbedAmount[i + 2]. These are the two values we need to calculate 
#      the current value. 
#   2. We set robNextPlusOne to 0 since this means the robber doesn't have any 
#      houses left to rub, thus zero profit. Additionally, we set robNext to 
#      nums[N - 1] because in this case there is only one house to rob which is 
#      the last house. Robbing it will yield the maximum profit. 
#       - Note: We are assuming that robNextPlusOne is the value of 
#           maxRobbedAmount[N] and robNext is maxRobbedAmount[N - 1] initially.
#   3. We iterate from N - 2 down to 0 and set current = 
#      max(robNext, robNextPlusOne + nums[i]). Note that this is same solution
#      except that we are making use of our variables and not table entries. 
#   4. Set robNextPlusOne = robNext
#   5. Set robNext = current. Updating the two variables is important as we 
#      iterate down to 0. 
#   6. Return value in robNext

class Solution3(object):
    def rob(self, nums):

        # special handling for empty case
        if not nums:
            return 0

        N = len(nums)

        rob_next_plus_one = 0
        rob_next = nums[N - 1]

        # DP table calculations
        for i in range(N - 2, -1, -1):

            # Same as recursive solution
            current = max(rob_next, rob_next_plus_one + nums[i])

            # Update variables
            rob_next_plus_one = rob_next
            rob_next = current
        return rob_next

# Time: O(N) since we loop from N-2 ... 0
# Space: O(1) since we arent using a table to store values. We maintain 
#       two variables  

