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