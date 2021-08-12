# Leetcode Question 70 [Easy]
# Climbing Stairs

# You are climbing a staircase. It takes n steps to reach the top. 
# Each time you can either climb 1 or 2 steps. In how many distinct ways can 
# you climb to the top? 

# Example: 
# input: n = 2
# output: 2
# explanation: there are two ways to climb to the top. 
#   1. 1 step + 1 step
#   2. 2 steps

# input: n = 3
# output: 3
# explanation: there are three ways to climb to the top. 
#   1. 1 step + 1 step + 1 step
#   2. 1 step + 2 steps
#   3. 2 steps + 1 step

class Solution(object):
    def climbStairs(self, n):
        one_step, two_step = 1, 1

        for i in range(n-1):
            temp = one_step
            one_step = one_step + two_step
            two_step = temp

        return one_step

# Time: O(n)
# Space: O(1) because we use the two variables to compute values, no extra
#   space needed. 

