# Leetcode Question 189 [Medium]
# Rotate Array

"""
Given an array, rotate the array to the right by k steps, where k is non-negative. 

Example 1: 
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation: 
rotate 1 steps to right: [7,1,2,3,4,5,6]
rotate 2 steps to right: [6,7,1,2,3,4,5]
rotate 3 steps to right: [5,6,7,1,2,3,4]

Example 2: 
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Constraints:
1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
"""

# Brute Force Approach
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # if k == len(nums), we dont have to do anything so k == 0
        k %= len(nums)

        for i in range(k):
            prev = nums[-1]
            for j in range(len(nums)):
                # print('before', nums[j], prev)
                nums[j], prev = prev, nums[j]
                # print('after', nums[j], prev)

# Time: O(n * k), numbers shifted by one step (O(n)) k times
# Space: O(1)

test = Solution()
arr = [1,2,3,4,5,6,7]
k = 3
test.rotate(arr, k)
print(arr)

# Extra Array Approach
"""
Use an extra array in which we place every element of the array at its correct 
position i.e. the number at index i in the original array is placed at the 
index (i + k) % length of array. then we copy the new array to the original 
one. 
"""
class Solution1(object):
    def rotate(self, nums, k):
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[(i + k) % n] = nums[i]
        
        nums[:] = a

# Time: O(n)
# Space: O(n)