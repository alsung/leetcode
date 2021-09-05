# Leetcode Question 41 [Hard]
# First Missing Positive

"""
Given an unsorted integer array nums, return the smallest missing positive 
integer.

You must implement an algorithm that runs in O(n) time and uses constant space.

Example 1
Input: nums = [1,2,0]
Output: 3

Example 2
Input: nums = [3,4,-1,1]
Output: 2

Example 3 
Input: nums = [7,8,9,11,12]
Output: 1

Constraints:
    1 <= nums.length <= 5 * 10^5
    -2^31 <= nums[i] <= 2^31 - 1
"""

"""
Approach: Index as a hash key.

Data Clean Up:
    First get rid of negative numbers or zeros. We can get rid of all 
    numbers > n as well since the first missing positive is for sure smaller 
    or equal to n + 1. The case when the first missing positive is equal to 
    n + 1 will be treated separately. 

    example: n = 8
        [1,2,3,4,5,6,7,8] --> 9
        [1,2,48,14,15,16,17,18] --> 3
        [1,2,3,4,5,6,7,18] --> 8

    max possible first missing number is n + 1 = 9

    replace negative numbers, zeros, and numbers > n by 1s

    [3,4,-1,-2,1,5,16,0,2,0] --> [3,4,1,1,1,5,1,1,2,1]

    to ensure first missing positive is not 1, we have to verify presence of 
    1 before proceeding. 

Solve in-Place:
    now we have an array of only positive numbers from 1 to n, the problem is 
    finding first missing positive in O(n) time and constant space. 
    
    this would be simple if we use a hash-map positive number -> its presence
    for the array. 

    O(n) space complexity solution with hash map: 
        [3,4,1,1,1,5,1,1,2,1] --> 
        {1: 6, 2: 1, 3: 1, 4: 1, 5: 1, 6: missing}

    sort of 'dirty workaround' solution would be allocating a string hash_str
    with n zeros, and use it as a sort of hash map by changing hash_str[i] to
    1 each time one meets number i in the array. 

    "O(1) space complexity" solution with string
        [3,4,1,1,1,5,1,1,2,1] -->
            number 6 is missing
                   | 
                   v
        "1 1 1 1 1 0 0 0 0 0"
                 ^
                 |
        number 5 is present
    
    let's not use this solution, but just take away an idea to use index as a 
    hash-key for a positive number. 

    the final idea is to use index in nums as a hash key and sign of the 
    element as a hash value which is presence indicator. 

        For example, negative sign of nums[2] means number 2 is present in 
        nums. Positive sign of nums[3] means that number 3 is not present 
        (missing) in nums. 

    To achieve, lets walk along array (after cleaning up only contains 
    positive numbers), check each elem value and change the sign of nums[elem]
    to negative to mark that number elem is present in nums. Be careful with 
    duplicates and ensure that the sign is changed only once. 

    O(1) space complexity solution
        [3,4,1,1,1,5,1,1,2,1] --> 
        [3,-4,-1,-1,-1,-5,1,1,2,1,1]
            number 6 is missing bc nums[6] > 0
            number 5 is present bc nums[5] < 0

Algorithm:
    - check if 1 is present in array. if not, you're done, return 1
    - replace negative nums, zeros, and nums larger than n by 1s
    - walk along array, change sign of a-th elem if you meet num a. Be careful
      with duplicates: do sign change only once. Use index 0 to save 
      information about present of number n since index n is not available. 
    - walk along array again. Return index of first positive element. 
    - if nums[0] > 0 return n
    - if on previous step no positive element found in nums, return n + 1
"""

class Solution: 
    def firstMissingPositive(self, nums):
        n = len(nums)

        # Base case
        if 1 not in nums:
            return 1

        # Replace negative numbers, zeros, and nums larger than n by 1s
        # After conversion, nums contains only positive numbers. 
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n: 
                nums[i] = 1

        # Use index as hash key and num sign as presence indicator. 
        # Ex: if nums[1] < 0, num '1' is present in array
        #     if nums[2] > 0, num '2' is missing. 
        for i in range(n):
            a = abs(nums[i])
            # If you meet num a in array, change sign of a-th element
            # only do this once
            if a == n:
                nums[0] = - abs(nums[0])
            else:
                nums[a] = - abs(nums[a])

        # Now index of first positive number == first missing positive
        for i in range(1, n):
            if nums[i] > 0:
                return i

        if nums[0] > 0:
            return n

        return n + 1        

# Time complexity: O(3n) = O(n)
# Space complexity: O(1), done in place
