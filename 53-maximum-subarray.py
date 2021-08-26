# Leetcode Question 53 [Easy]
# Maximum Subarray

"""
Given an integer array nums, find the contiguous subarray (containing at least 
one number) which has the largest sum and return its sum. 

A subarray is a contiguous part of an array. 

Example 1: 
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6

Example 2: 
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23

Constraints:
    1 <= nums.length <= 3 * 10^4
    -10^5 <= nums[i] <= 10^5

Companies: LinkedIn, Amazon, Microsoft, Apple, Google, Adobe, Bloomberg, 
Facebook, eBay, Splunk, Uber, Yahoo, Walmart Labs
"""

"""
Brute Force Approach - Optimized

Calculate the sum of all subarrays and keep track of the best one. To actually
generate all subarrays would take O(N^3) time, but with a little optimization, 
we can achieve brute force in O(N^2) time. 

The trick is to recognize that all of the subarrays starting at a particular 
value will share a common prefix. 

Algo:
    1. Init a variable maxSubarray = -infinity to keep track of the best 
        subarray. We need to use negative infinity, not 0, because it is 
        possible that there are only negative numbers in the array. 
    2. Use for loop that considers each index of the array as a starting point.
    3. For each starting point, create a variable currSubarray = 0. Then, loop
        through the array from the starting index, adding each element to 
        currSubarray. Every time we add an element it represents a possible 
        subarray - so continuously update maxSubarray to contain the maximum 
        out of the currSubarray and itself. 
    4. Return maxSubarray
"""

import math

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_subarray = -math.inf
        for i in range(len(nums)):
            curr_subarray = 0
            for j in range(i, len(nums)):
                curr_subarray += nums[j]
                max_subarray = max(max_subarray, curr_subarray)
        
        return max_subarray

# Time: O(N^2), where N is len(nums), using 2 nested for loops
# Space: O(1)

"""
Approach 2: DP, Kadane's Algorithm

Intuition: 
Whenever you see a question that asks for the maximum or minimum of something, 
consider DP as a possibility. The difficult part of this problem is figuring 
out when a negative number is "worth" keeping in the subarray. This question in
particular is a popular problem that can be solved using an algorithm called 
Kadane's Algo. This algo also has a very greedy-like intuition behind it. 

Let's focus on one important part: where the optimal subarray begins. We'll use
the following example. 

nums = [-2,1,-3,4,-1,2,1,-5,4]

We can see that the optimal subarray couldn't possibly involve the first 3 
values - the overall sum of those numbers would always subtract from the total.
Therefore, the subarray either starts at the first 4, or somewhere further to 
the right. 

What if we had this example? 
nums = [-2, 10000000000, -3, 4, -1, 2, 1, -5, 4]

We need a general way to figure out when a part of the array is worth keeping.

As expected, any subarray whose sum is positive is worth keeping. Let's start 
with an empty array, and iterate through the input, adding numbers to our 
array as we go along. Whenever the sum of the array is negative, we know the 
entire array is not worth keeping, so we'll reset it back to an empty array. 

However, we don't actually need to build the subarray, we can just keep the 
integer variable curr_subarray and add the values of each element there. When 
it becomes negative, we reset it to 0 (an empty array). 

Algo: 
    1. Init 2 integer variables. Set both of them equal to the first value in 
        array
        - currSubarray: will keep running count of current subarray
        - maxSubarray: will be our final return value. Continuously update it 
            whenever we find a bigger subarray. 
    2. Iterate through array, starting with the 2nd element (as we used the 
        first element to init our variables). For each number, add it to the 
        currSubarray we are building. If currSubarray becomes negative, we know
        its not worth keeping, so throw it away. Remember to update maxSubarray
        every time we find a new maximum. 
    3. Return maxSubarray

Implementation: 
A clever way to update currSubarray is using 
currSubarray = max(num, currSubarray + num). If currSubarray is negative, then 
num > currSubarray + num. 
"""

class Solution1(object):
    def maxSubArray(self, nums):
        # Initialize our variables using first element
        curr_subarray, max_subarray = nums[0], nums[0]

        # Start with the 2nd element since we already used first one. 
        for num in nums[1:]:
            # If curr_subarray is negative, throw it away. OW, keeping adding to it
            curr_subarray = max(num, curr_subarray + num)
            max_subarray = max(max_subarray, curr_subarray)

        return max_subarray

# Time: O(N), where len(nums) = N
# Space: O(1)

"""
Approach 3: Divide and Conquer (advanced)

Intuition:
This approach is slower than the second approach and uses more space, but it's 
still a nice and different way to approach the problem. In an interview, 
sometimes you may be asked for alternative ways to solve a problem - and divide
and conqueer is an extremely common type of algorithm. This solution will make 
use of recursion. 

Divide and conquer algos involve splitting up the input into smaller chunks 
until they're small enough to be easily solved, and then combining the 
solutions to get the final overall solution. 

If we were to split our input in half, then logically the optimal subarray either:
    - uses elements only from the left side
    - uses elements only from the right side
    - uses a combination of elements from both left and right side

Thus, the answer is simply the largest of:
    - the maximum subarray contained only in the left side
    - the maximum subarray contained only in the right side
    - the maximum subarray that can use elements from both sides. 

Finding the maximum subarray from the left and right half is straightforward - 
just recurse the respective half of the array. So, the hard part is figuring 
out how to find the best subarray that uses elements froom both sides. Lets 
use a smaller example, nums = [5, -2, 1, -3, 4, -2, 1]. Since we want to use 
elements from both sides, we also must use the middle element, -3. Now, we can 
take from the left and right side, but every element must be connected to the 
middle (since we're forming a subarray). 

The fact that every element must be connected to the middle actually makes our 
lives a lot easier - every subarray we consider must contain the element 
immediately beside the center, which means there are only as many subarrays as 
there are elements. In our example, the right side is [4, -2, 1]. There are 
only 3 subarrays to consider - [4], [4, -2], [4, -2, 1]. To find the best 
chain of elements we can take from a half, iterate from the middle to the end 
(start of the array for the left half) and continuously update some counter 
curr.

Algo: 
Now that we know how to find the best subarray containing elements from both 
sides of any given array, as follows:
    1. Define a helper function that we will use for recursion:
        - this function will take input left and right, which defines the 
            bounds of the array. The return value of this function will be the 
            best possible subarray for the array that fits between left and right. 
        - if left > right, we have an empty array. Return negative infinity
        - Find the midpoint of array. This is (left + right) / 2, rounded down. 
            Using this midpoint, find the best possible subarray that uses elements 
            from both sides of the array. 
        - the best subarray using elements from both sides is only 1 of 3 
            possibilities. We still need to find the best subarray using only 
            the left or right halves. So, call this function again, once with 
            the left half, and once with the right half. 
        - return the largest of the 3 values - the best left half sum, best 
            right half sum, best combined sum. 
    2. Call our helper function with entire input array 
        (left = 0, right = length - 1). Return final answer. 
"""

class Solution2(object):
    def maxSubArray(self, nums):
        def findBestSubArray(nums, left, right):
            # base case - empty array
            if left > right:
                return -math.inf
            
            mid = (left + right) // 2
            curr = best_left_sum = best_right_sum = 0

            # Iterate from middle to beginning
            for i in range(mid - 1, left - 1, -1):
                curr += nums[i]
                best_left_sum = max(best_left_sum, curr)

            # reset curr and iterate from middle to end
            curr = 0
            for i in range(mid + 1, right + 1):
                curr += nums[i]
                best_right_sum = max(best_right_sum, curr)

            # the best_combined_sum uses the middle element and the best 
            # possible sum from each half. 
            best_combined_sum = nums[mid] + best_right_sum + best_left_sum

            # find the best subarray possible from both halves
            left_half = findBestSubArray(nums, left, mid-1)
            right_half = findBestSubArray(nums, mid+1, right)

            # the largest of the 3 is answer
            return max(best_combined_sum, left_half, right_half)

        # our helper function is designed to solve this problem for any 
        # array - so just call it using the entire input! 
        return findBestSubArray(nums, 0, len(nums)-1)
