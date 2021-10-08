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
            char_set[ord(char_r)] += 1 # +1 count for char seen, returns an integer representing Unicode character
            
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

# Brute Force Approach
"""
Intuition:
Check all substrings one by one to see if it has no duplicate character.

Algorithm:
Suppose we have a function boolean allUnique(String substring) which will 
return true if the characters in the substring are all unique, otherwise false.
We can iterate through all the possible substrings of a given string s and 
call the function allUnique. If it turns out to be true, then we update our 
answer of the maximum length of substring without duplicate characters. 

1. To enumerate all substrings of a given string, we enumerate the start and 
    end indices of them. Suppose the start and end indices are i and j, 
    respectively. Then we have 0 <= i < j <= n (here end index j is exclusive 
    by convention). Thus, using two nested loops with i from 0 to n-1 and j 
    from i+1 to n, we can enumerate all the substring of s. 
2. To check if one string has duplicate characters, we can use a set. We 
    iterate through all the characters in the string and put them into the set 
    one by one. Before putting one character, we check if the set already 
    contains it. If so, we return false. After the loop, we return true. 
"""

class Solution1: 
    def lengthOfLongestSubstring(self, s):
        def check(start, end):
            chars = [0] * 128 # there are 128 Unicode characters
            for i in range(start, end+1):
                c = s[i]
                chars[ord(c)] += 1
                if chars[ord(c)] > 1:
                    return False
            return True
        
        n = len(s)
        res = 0
        for i in range(n):
            for j in range(i, n):
                if check(i, j):
                    res = max(res, j - i + 1)
        
        return res

# Time Complexity: O(N^3). 
# Space Complexity: O(min(n, m)). Size of set is size of string n and the size 
# of charset m.  


# Approach 3: Sliding Window Optimized
"""
Instead of using a set to tell if a character exists or not, we could define a 
mapping of the characters to its index. Then we can skip the characters 
immediately when we found a repeated character. 

The reason is if s[j] have a duplicate in the range [i, j) with index j', we 
don't need to increase i little by little. we can skip all the elements in 
range [i, j'] and let i be j' + 1 directly. 

Using Hashmap:
"""

class Solution2:
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)
            
            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans