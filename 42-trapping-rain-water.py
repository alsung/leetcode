# Leetcode Question 42 [Hard]

# Trapping Rain Water

# Given n non-negative integers representing an elevation map where the 
# width of each bar is 1, compute how much water it can trap after raining. 

# Example: 
# input: height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# output: 6

# input: height = [4, 2, 0, 3, 2, 5]
# output: 9

# Constraints:
#   - n == height.length
#   - 0 <= n <= 2 * 10^4
#   - 0 <= height[i] <= 10^5

# Approach 1 Brute Force
# For each element in the array, we find the maximum level of water it can 
# trap after the rain, which is equal to the minimum of maximum height of 
# bars on both sides minus its own height. 
#   - initialize ans = 0
#   - iterate array from left to right:
#       - initialize left_max = 0 and right_max = 0
#       - iterate from current element to beginning of array updating:
#           - left_max = max(left_max, height[j])
#       - iterate from current element to end of array updating:
#           - right_max = max(right_max, height[j])
#       - add min(left_max, right_max) - height[i] to ans

# Time Complexity: O(n^2). For each element of array, we iterate both left
# and right parts. 
# Space Complexity: O(1)

# =============================================================================
# Approach 2: Dynamic Programming
#   - Find maximum height of bar from left end upto index i in  array left_max
#   - Find maximum height of bar from right end upto index i in array right_max
#   - Iterate over the height array and update ans:
#       - add min(left_max[i], right_max[i]) - height[i] to ans

# Time Complexity: O(n)
#   - store maximum heights upto a point using 2 iterations of O(n) each. 
#   - finally update ans using the stored values in O(n)
# Space Complexity: O(n)
#   - additional O(n) space for left_max and right_max arrays

# =============================================================================
# Approach 3: Using Stacks
# Instead of storing the largest bar upto an index as in Approach 2, we can use
# stack to keep track of the bars that are bounded by longer bars and hence, 
# may store water. Using the stack, we can do the calculations in only one 
# iteration. 

# We keep a stack and iterate over the array. We add the index of the bar to 
# the stack if bar is smaller than or equal to the bar at top of stack, which 
# means that the current bar is bounded by the previous bar in the stack. If 
# we found a bar longer than that at the top, we are sure that the bar at the
# top of stack is bounded by current bar and a previous bar in the stack, 
# hence, we can pop it and add resulting trapped water to ans. 

#   - use stack to store indices of the bars
#   - iterate the array:
#       - while stack is not empty and height[current] > height[st.top()]
#           - it means that the stack element can be popped. Pop top element 
#             as top
#           - find distance between current elem and elem at top of stack,
#             which is to be filled. distance = current - st.top() - 1
#           - find bounded height bounded_height = 
#             min(height[current], height[st.top()]) - height[top]
#           - add resulting trapped water to answer
#             ans += distance * bounded_height
#       - push current index to top of stack
#       - move current to next position

# =============================================================================
# Approach 4: Using 2 pointers
# As in Approach 2, instead of computing the left and right parts separately, 
# we may think of some way to do it in one iteration. From the figure in DP 
# approach, notice that as long as right_max[i] > left_max[i] (from element 0 
# to 6), the water trapped depends on the left_max, similar is the case when 
# left_max[i] > right_max[i] (for element 8 to 11). So we can say that if there 
# is a larger bar at one end (say right), we are assured that the water trapped 
# would be dependent on height of bar in current direction (left to right). As 
# soon as we find the bar at the other right (right) is smaller, we start 
# iterating in opposite direction (right to left). We must maintain left_max 
# and right_max during iteration, but now we can do it in one iteration using 
# 2 poiinters, switching between the two. 

#   - initialize left pointer to 0 and right pointer to size-1
#   - while left < right:
#       - if height[left] is smaller than height[right]:
#           - if height[left] >= left_max:
#               - update left_max
#           - else add left_max - height[left] to ans
#           - add 1 to left
#       - else
#           - if height[right] >= right_max:
#               - update right_max
#           - else add right_max - height[right] to ans
#           - subtract 1 from right
#   - return ans

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = 0
        right = len(height) - 1
        ans = 0

        left_max, right_max = 0, 0

        while (left < right):
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += (left_max - height[left])
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += (right_max - height[right])
                right -= 1
        
        return ans

# Time Complexity: O(n)
# Space Complexity: O(1)

