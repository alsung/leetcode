# Leetcode Question 322 [Medium]
# Coin Change

# You are given an integer array coins representing coins of different 
# denominations and an integer amount representing a total amount of money. 

# Return the fewest number of coins that you need to make up that amount. If 
# that amount of money cannot be made up by any combination of coins, 
# return -1. 

# You may assume that you have an infinite number of each kind of coin. 

# Example 1:
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# Example 2: 
# Input: coins = [2], amount = 3
# Output: -1

# Example 3: 
# Input: coins = [1], amount = 0
# Output: 0

# Example 4: 
# Input: coins = [1], amount = 1
# Output: 1

# Example 5: 
# Input: coins = [1], amount = 2
# Output: 2

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount + 1] * (amount + 1) # 0,...,amount
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
                    
        return dp[amount] if dp[amount] != amount + 1 else -1
    
# Time Complexity: O(amount * len(coins))
# Space Complexity: O(amount)


# =============================================================================
# Neetcode Approach 2/24/2022

class Solution1:
    # O(amount * len(coins)) time | O(amount) space
    def coinChange(self, coins, amount):
        # amount + 1 or any max int value will work for starting value of dp
        dp = [amount + 1] * (amount + 1) # we go from 0 --> amount, so amount + 1 length
        dp[0] = 0 # base case

        # going from bottom-up
        for am in range(1, amount + 1):
            for coin in coins:
                if am - coin >= 0:
                    # possibly found solution for DP, 1 + dp[am - coin]
                    dp[am] = min(dp[am], 1 + dp[am - coin]) # recurrence relation

        # if dp[amount] is default value, return -1, could not compute amount
        return dp[amount] if dp[amount] != amount + 1 else -1

sol = Solution1()
coins = [1, 2, 5]
amount = 11
print(sol.coinChange(coins, amount)) # 3