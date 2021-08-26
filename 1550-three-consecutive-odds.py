# Leetcode Question 1550 [Easy]
# Three Consecutive Odds

"""
Given an integer array arr, return true if there are three consecutive odd 
numbers in the array. Otherwise, return false. 

Example 1: 
Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds. 

Example 2: 
Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds. 

Constraints: 
    1 <= arr.length <= 1000
    1 <= arr[i] <= 1000
"""

class Solution(object):
    def threeConsecutiveOdds(self, arr):
        if len(arr) <= 2:
            return False
        
        for i in range(len(arr) - 2):
            first, second, third = arr[i], arr[i+1], arr[i+2]
            if first % 2 == 0 and second % 2 == 0 and third % 2 == 0:
                return True
        return False

# Time: O(n), where n = len(arr)
# Space: O(1)
