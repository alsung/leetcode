# Leetcode Question 3

# Given a string s, find the length of the longest substring 
# without repeating characters. 

# Example 1: 
# input: s = "abcabcbb"
# output: 3

# input: s = "bbbbb"
# output: 1

# input: s = "pwwkew"
# output: 3

# input: s = ""
# output: 0

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        char_set = [0] * 128
        
        left = 0
        right = 0
        
        res = 0
        while right < len(s):
            char_r = s[right] # pointer to right char
            char_set[ord(char_r)] += 1 # +1 count for char seen
            
            # if duplicate found, move left pointer to right pointer at second duplicate
            while char_set[ord(char_r)] > 1: # close window, duplicate found
                char_l = s[left]
                char_set[ord(char_l)] -= 1
                left += 1
            
            # update substring length
            res = max(res, right - left + 1)
            
            right += 1
        
        return res

# Sliding Window Approach
# Time Complexity: O(N). in the worst case, each character will be visited twice by i and j
# Space Complexity: O(min(m,n)). We need O(k) space for the sliding window, where k is the size 
# of the set. The size of set is upper bounded by size of string n and size of charset m
