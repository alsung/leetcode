# Leetcode Question 1911 [Medium]
# Maximum Alternating Subsequence Sum

# The alternating sum of a 0-indexed array is defined as the sum of the 
# elements at even indices minus the sum of the elements of odd indices. 

# For example, the alternating sum of [4,2,5,3] is (4 + 5) - (2 + 3) = 4

# Given an array nums, return the maximum alternating sum of any subsequence 
# of nums (after reindexing the elements of the subsequence). 

# A subsequence of an array is a new array generated from the original array 
# by deleting some elements (possibly none) without changing the remaining 
# elements' relative order. For example, [2,7,4] is a subsequence of 
# [4,2,3,7,2,1,4], while [2,4,2] is not. 

# Example:
# input: nums = [4,2,5,3]
# output: 7
# optimal choice is sequence [4,2,5] with alternating sum (4 + 5) - 2 = 7

# input: nums = [5,6,7,8]
# output: 8
# it is optimal to choose the subsequence [8] with alternating sum 8

# input: nums = [6,2,1,2,4,5]
# output: 10
# it is optimal to choose the subsequence [6,1,5] with alternating sum 
# (6 + 5) - 1 = 10

