# Leetcode Question 494 [Medium]
# Target Sum

# You are given an integer array nums and an integer target. 

# You want to build an expression out of nums by adding one of the symbols '+' 
# and '-' before each integer in nums and then concatenate all the integers. 
#   - For example, if nums = [2, 1], you can add a '+' before 2 and a '-' 
#     before 1 and concatenate them to build the expression "+2-1". 

# Return the number of different expressions that you can build, which 
# evaluates to target. 

# Example 1: 
# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be 
# target 3. 
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3

# Example 2: 
# Input: nums = [1], target = 1
# Output: 1

# 0/1 Knapsack DP problem
# Our 'capacity' is the target, we want to reach target (or S). Our 'items' are
# the numbers in the input subset and the 'weights' of the items are the values
# of the numbers itself. This question follows 0/1 and not unbounded knapsack 
# because we can use each number ONCE. 

# Brute Force Recursive Approach

class Solution(object):
    def findTargetSumWays(self, nums, target):
        index = len(nums) - 1
        curr_sum = 0
        return self.calculate(nums, target, index, curr_sum)
    def calculate(self, nums, target, index, curr_sum):
        # Base Cases
        if index < 0 and curr_sum == target:
            return 1
        if index < 0:
            return 0
        
        # Decisions
        positive = self.calculate(nums, target, index - 1, curr_sum + nums[index])
        negative = self.calculate(nums, target, index - 1, curr_sum - nums[index])

        # diff = target
        # positive - negative = target
        return positive + negative

# Memoization solution optimization approach
class Solution2(object):
    def findTargetSumWays(self, nums, target):
        index = len(nums) - 1
        curr_sum = 0
        self.memo = {}
        return self.calculate(nums, target, index, curr_sum)

    def calculate(self, nums, target, index, curr_sum):
        if (index, curr_sum) in self.memo:
            return self.memo[(index, curr_sum)]

        if index < 0 and curr_sum == target:
            return 1
        if index < 0: 
            return 0

        positive = self.calculate(nums, target, index-1, curr_sum + nums[index])
        negative = self.calculate(nums, target, index-1, curr_sum - nums[index])

        self.memo[(index, curr_sum)] = positive + negative
        return self.memo[(index, curr_sum)] 