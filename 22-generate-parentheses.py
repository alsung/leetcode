# Leetcode Question 22 [Medium]
# Generate Parentheses

"""
Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses. 

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
    1 <= n <= 8
"""

# Approach 1: Brute Force
"""
Intuition: 
We can generate all 2^2n sequences of '(' and ')' characters. Then we check 
if each is valid. 

Algorithm:
To generate all sequences, we use recursion. All sequences of length n is just
'(' plus all sequences of length n-1, and then ')' plus all sequences of length
n-1.

To check whether a sequence is valid, we keep track of balance, the net number
of opening brackets minus closing brackets. If it falls below zero at any time,
or doesn't end in zero, sequence is invalid -- otherwise valid. 
"""

class Solution:
    def generateParentheses(self, n):
        def generate(A = []):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()
        
        def valid(A):
            bal = 0
            for c in A:
                if c == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate()
        return ans

# Time Complexity: O(2^2n * n). For each 2^2n sequences, need to create and 
# validate sequence, takes O(N) time each. 
# Space Complexity: O(2^2n * n). Naively creates every possible sequence. 

# Approach 2: Backtracking
"""
Intuition and Algorithm:
Instead of adding '(' or ')' every time like in Approach 1, let's only add them
 when we know it will remain a valid sequence. We can do this by keeping track 
 of the number of opening and closing brackets we have placed so far. 

We can start an opening bracket if we still have one (of n) left to place. And 
we can start a closing bracket if it would not exceed the number of opening 
brackets. 
"""

class Solution1:
    def generateParenthesis(self, n):
        ans = []

        def backtrack(S=[], left=0, right=0):
            if len(S) == 2*n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
    

        backtrack()
        return ans

"""
Complexity Analysis:
Time Complexity: O( 4*n / sqrt(n)). Each valid sequence has at most n steps 
during backtracking procedure. 
Space Complexity: O( 4*n / sqrt(n)), as described above, and using O(n) space 
to store sequence. 
"""