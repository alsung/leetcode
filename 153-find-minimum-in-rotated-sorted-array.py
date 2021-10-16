# Leetcode Question 153 [Medium]
# Find Minimum in Rotated Sorted Array

"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
    - [4,5,6,7,0,1,2] if it was rotated 4 times
    - [0,1,2,4,5,6,7] if it was rotated 7 times

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array. 

You must write an algorithm that runs in O(log N) time. 

Example:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times. 

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

Constraints:
n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique
nums is sorted and rotated between 1 and n times. 
"""

"""
Neetcode Approach: https://www.youtube.com/watch?v=nIVW4P8b1VA&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=6

We know the left group will always have larger values than the right group if 
the array is rotated. Rotating the array places the highest value (farthest 
right of sorted array) to the left of everything. 

[3,4,5,1,2]
 L   m   R

if nums[mid] >= nums[left]:
    search right
else:
    search left

in this case:
5 >= 3
nums[mid] part of left sorted portion, so we want to search right
if case is:
1 >= 3 == false
if 1 is middle, then we are in right sorted portion, so we want to search left 
for lower value because all values to right will be higher values. 

[3,4,5]
only works for rotated arrays. 
if array is already sorted (L < R), then we can check if L is less than our 
result. 

[3,4,5,1,2]  ==>  [3,4,5,1,2]
L    m   R             m L R
since value at L is < value at R, new array is sorted, so check if L <= res,
or m, if it is, then we can reassign res and return. 
"""

class Solution:
    def findMin(self, nums):
        res = nums[0] # some value in nums
        left, right = 0, len(nums) - 1 # left and right pointer

        while left <= right:
            if nums[left] < nums[right]: # check if array sorted
                res = min(res, nums[left])
                break
        
            mid = (left + right) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[left]: # mid part of left sorted portion
                # search right portion
                # update left pointer
                left = mid + 1
            else: # mid part of right sorted portion
                # search left portion
                # update right pointer
                right = mid - 1
        
        return res

# Time Complexity: O(log N)
# Space Complexity: O(1), use 2 pointers and mid pointer 