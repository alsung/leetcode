# Leetcode Question 20 [Easy]

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid. 

# An input string is valid if:
#   1. open brackets must be closed by the same type of brackets
#   2. open brackets must be closed in the correct order

# Examples: 
# input: s = "()"
# output: true

# Constraints:
#   - 1 <= s.length <= 10^4
#   - s consists of parentheses only '()[]{}'

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket_map = {"(": ")", "[": "]", "{": "}"}
        open_par_set = set(["(", "[", "{"])
        stack = []

        for i in s:
            if i in open_par_set:
                stack.append(i)
            elif stack and i == bracket_map[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []