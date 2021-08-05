# Leetcode Question 5 [Medium]

# Longest Palindrome Substring

# Given a string s, return the longest palindromic substring in s. 

# Example: 
# input: s = "babad"
# output: "bab"
# Note: "aba" is also valid answer. 

# input: s = "cbbd"
# output: "bb"

# input: s = "a"
# output: "a"

# input: s = "ac"
# output: "a"

# Constraints: 
#   - 1 <= s.length <= 1000
#   - s consist of only digits and English letters 

# Solution:

# Approach 1: Longest Common Substring
#   - Reverse S and become S'. Find the longest common substring between S
#     and S', which must also be the longest palindromic substring
#   - let S = "abacdfgdcaba", S' = "abacdgfcaba"
#   - longest common substring is "abacd", but is not a palindrome. 

# We can see that the longest common substring method fails when there exists 
# a reversed copy of a non-palindromic substring in some other part of S. To 
# rectify this, each time we find a longest common substring candidate, we 
# check if the substring's indices are the same as the reversed substring's 
# original indicies. If it is, then we attempt to update the longest 
# palindrome found so far; if not, we skip this and find next candidate. 

# Time: O(n^2)
# Space: O(n^2)

# =============================================================================

# Approach 2: Brute Force
# pick all possible starting and ending positions for a substring, and verify
# if it is a palindrome. 

# Time: O(n^3) - Assume that n is length of input string, there are total of 
#                n(n-1)/2 such substrings (excluding the trivial solution where
#                a character itself is a palindrome). Since verifying each 
#                substring takes O(n) time, the run time complexity is O(n^3)
# Space: O(1)

# =============================================================================

# Approach 3: Dynamic Programming
# to improve our brute force solution, we first observe how we can avoid 
# unnecessary re-computation while validating palindromes. Consider the case 
# "ababa". If we already knew that "bab" is a palindrome, it is obvous that 
# "ababa" must be a palindrome since the two left and right end letters are 
# the same. 

# We define P(i, j) as following: 
#   - P(i, j) = {true: if substring S_i...S_j is a palindrome
#                false: otherwise}
# therefore:
#   - P(i, j) = (P(i+1, j-1) and S_i == S_j)

# base cases:
#   - P(i,i) = true
#   - P(i, i+1) = (S_i == S_i+1)

# This yields a straight forward DP solution, which we first initialize the one
# and two letters palindromes, and work our way up finding all three letters 
# palindromes, and so on....

# Time: O(n^2)
# Space: O(n^2): O(n^2) space to store table. 

# =============================================================================

# Approach 4: Expand Around Center

# In fact, we could solve it in O(n^2) time using only constant space. 
# We observe that a palindrome mirrors around its center. Therefore, a 
# palindrome can be expanded from its center, and there are only 2n-1 centers. 

# Why are there 2n-1 but not n centers? The reason is because center of 
# palindrome can be two letters. Such palindromes have even number of letters 
# (such as "abba") and its center is between the two 'b's. 

class Solution(object):
    def longestPalindrome(self, s):
        res = ""
        res_len = 0

        for i in range(len(s)):
            # check odd length palindromes
            left, right = i, i
            # while palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > res_len:
                    res = s[left:right+1]
                    res_len = right - left + 1
                left -= 1
                right += 1

            # even length palindromes
            left, right = i, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > res_len:
                    res = s[left:right+1]
                    res_len = right - left + 1
                left -= 1
                right += 1

        return res

# Time: O(n^2)
# Space: O(1)

# =============================================================================

class Solution2(object):
    def longestPalindrome(self, s):
        if len(s) <= 1:
            return s
        start = end = 0
        length = len(s)
        for i in range(length):
            max_len_1 = self.get_max_len(s, i, i+1)
            max_len_2 = self.get_max_len(s, i, i)
            max_len = max(max_len_1, max_len_2)
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        return s[start:end+1]

    def get_max_len(self, s, left, right):
        length = len(s)
        i = 1
        max_len = 0
        while left >= 0 and right < length and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left + 1

