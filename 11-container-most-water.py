# Leetcode Question 11

# Given n non-negative intergers a1, a2, ..., an, where each represents
# a point at coordinate (i, ai). n vertical lines are drawn such that 
# the two endpoints of a line i is at (i, ai) and (i, 0). Find two lines,
# which, together with the x-axis forms a container, such that the 
# container contains the most water. 

# Notice, you may not slant the container

# Example:
# input: height = [1,8,6,2,5,4,8,3,7]
# output: 49

# input: height = [4,3,2,1,4]
# output: 16

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        front_ptr = 0
        back_ptr = len(height) - 1
        max_area = 0
        while front_ptr < back_ptr:
            curr_area = min(height[front_ptr], height[back_ptr]) * (back_ptr - front_ptr)
            if curr_area > max_area:
                max_area = curr_area
            if height[front_ptr] < height[back_ptr]:
                front_ptr += 1
            else:
                back_ptr -= 1
        
        return max_area

# Time Complexity: O(N)
# Space Complexity: O(1)

###############################################################################
# Neetcode Approach: https://www.youtube.com/watch?v=UuiTKBwPgAo&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=10

"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at
coordinate (i, a[i]). n vertical lines are drawn such that the two endpoints 
of the line i is at (i, a[i]) and (i, 0). Find two lines, which, together with
the x-axis forms a container, such that the container contains the most water. 

Notice that you may not slant the container. 

Example 1: 
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array 
[1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the 
container can contain is 49. 
"""

class Solution1:
    def maxArea(self, height):
        # BRUTE FORCE
        res = 0

        for l in range(len(height)):
            for r in range(l+1, len(height)):
                area = (r - l) * min(height[l], height[r])
                res = max(res, area)

        return res

# Time: O(N^2)

# Exceeds Time Limit

"""
Try two pointer technique
- place left pointer at first element
- place right pointer at last element to maximize area
"""

class Solution2: 
    def maxArea(self, height):
        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

            if height[l] < height[r]: # left height shorter than right 
                # shift left pointer to right, search for larger height
                l += 1
            else:
                l += 1

        return res

# Time: O(N)
# Space: O(1)