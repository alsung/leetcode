# Leetcode Question 167
# Two Sum II - Input array is sorted

# Given an array of integers numbers that is already sorted in non-decreasing order, find two 
# numbers such that they add up to a specific target number. 
# Return the indices of the two numbers (1-indexed) as an integer array answer of size 2,
# where 1 <= answer[0] < answer[1] <= numbers.length.
# The tests are generated such that there is exactly one solution. You may not use the same element 
# twice. 

# input: numbers = [2,7,11,15], target = 9
# output: [1,2]

# input: numbers = [2,3,4], target = 6
# output: [1,3]

# input: numbers = [-1,0], target = -1
# output: [1,2]

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        low = 0
        high = len(numbers) - 1

        while low < high: # check pointers dont overlap
            sum = numbers[low] + numbers[high] # cur sum
            if sum == target: 
                return [low+1, high+1] # indices + 1
            elif sum < target: # sum too low, increase low
                low += 1
            else: # sum too high, decrease high
                high -= 1

