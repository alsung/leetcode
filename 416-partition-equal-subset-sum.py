# Leetcode Question 416 [Medium]
# Partition Equal Subset Sum

# Given a non-empty array nums containing only positive integer, find if the 
# array can be partitioned into two subsets such that the sum of elements in 
# both subsets is equal. 

# Example: 
# Input: nums = [1,5,11,5]
# Output: True
# Explanation: The array can be partitioned as [1,5,5] and [11]. 

# Input: nums = [1,2,3,5]
# Output: False
# Explanation: The array cannot be partitioned into equal sum subsets. 

# Constraints: 
#   1 <= nums.length <= 200
#   1 <= nums[i] <= 100

class Solution(object):
    def canPartition(self, nums):
        if sum(nums) % 2: 
            return False
        
        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return True if target in dp else False

# bottom-up DP approach

# Time: O(n * sum(nums))
# Space: O(sum(nums))

