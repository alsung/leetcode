# Leetcode Question 1143 [Medium]
# Longest Common Subsequence

"""
Given two strings text1 and text2, return the length of their longest common 
subsequence. If there is no common subsequence, return 0. 

A subsequence of a string is a new string generated from the original string 
with some characters (can be none) deleted without changing the relative order 
of the remaining characters. 
    - For example, "ace" is a subsequence of "abcde"

A common subsequence of two strings is a subsequence that is common to both 
strings. 

Example 1:
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3. 

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3. 

Example 3: 
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0. 

"""

# =============================================================================
# Approach 1: Memoization

"""
Intuition:
First step is to find a way to recursively break the original problem down into
subproblems. We want to find subproblems such that we can create an optimal 
solution from the results of those subproblems. 

Earlier, we were drawing lines between identical letters. 

Consider the greedy algorithm we tried earlier where we took the first possible
line. Instead of assuming that the line is part of the optimal solution, we 
could consider both cases: the line is part of the optimal solution or the 
line is not part of the optimal solution. 

If the line is part of the optimal solution, then we know that the rest of the 
lines must be in the substrings that follow the line. as such, we should find 
the solution for the substrings, and add 1 onto the result (for the new line) 
to get the optimal solution. 

However, if the line is not part of the optimal solution, then we know that the
letter in the first string is not included (as this would have been the best 
possible line for that letter). So instead, we remove the first letter of the 
first string and treat the remainder as the subproblem. Its solution will be 
the optimal solution. 

But remember, we don't know which of these two cases is true. As such, we need 
to compute the answer for both cases. The highest one will be the optimal 
solution and should be returned as the answer to the problem. 

Note that if either the first string or the second string is of length 0, we 
can just return 0. This acts as the base case for recursion. 

But how many total subproblems? Bc we always take a character off one, or both,
of the strings each time, there are M * N possible subproblems (where M is the
length of first string, and N the length of second string). Another way of 
seeing this is that subproblems are represented as suffixes of the original 
strings. A string of length K has K unique suffixes. Therefore, the first 
string has M suffixes and the second string has N suffixes. Therefore, M * N 
possible pairs of suffixes. 

Some subproblems may be visited multiple times, for example LCS("aac", "adf") 
has two subproblems LCS("ac", "df") and LCS("ac", "adf"). Both of these share 
a common subproblem of LCS("c", "df"). We should memoize the results of LCS 
calls so that the answers of previously computed subproblems can immediately 
be returned without recomputation. 

Algorithm:
Top-down recursive algo pseudocode:

define function LCS(text1, text2):
    # If either string is empty, there can be no common subsequence
    if length of text1 or text2 is 0:
        return 0
    
    letter1 = the first letter in text1
    firstOccurence = first position of letter1 in text2

    # the case where the line *is not* part of optimal solution
    case1 = LCS(text1.substring(1), text2)

    # the case where the line *is* part of optimal solution
    case2 = 1 + LCS(text1.substring(1), text2.substring(firstOccurence + 1))

    return maximum of case1 and case2

If letter1 is not part of text2, then we can't solve first subproblem. However,
in this case, we can simply ignore the first subproblem as the line doesn't 
exist: 

define function LCS(text1, text2):
    # If either string is empty there can be no common subsequence
    if length of text1 or text2 is 0:
        return 0

    letter1 = the first letter in text1

    # The case where the line *is not* part of optimal solution
    case1 = LCS(text1.substring(1), text2)

    case2 = 0
    if letter1 is in text2:
        firstOccurence = first position of letter1 in text2
        # the case where the line *is* part of optimal solution
        case2 = 1 + LCS(text1.substring(1), text2.substring(firstOccurence + 1))

    return maximum of case1 and case2
"""

from functools import lru_cache

class Solution:
    def longestCommonSubsequence(self, text1, text2):

        @lru_cache(maxsize=None)
        def memo_solve(p1, p2):

            # Base case: if either string is empty, we can't match up anymore
            # characters.
            if p1 == len(text1) or p2 == len(text2):
                return 0

            # Option 1: We don't include text1[p1] in solution
            option_1 = memo_solve(p1 + 1, p2)

            # Option 2: We include text1[p1] in solution, as long as a match
            # for it in text2 at or after p2 exists. 
            first_occurence = text2.find(text1[p1], p2)
            option_2 = 0
            if first_occurence != -1:
                option_2 = 1 + memo_solve(p1 + 1, first_occurence + 1)

            # Return the best option
            return max(option_1, option_2)

        return memo_solve(0, 0)

# Time Complexity: O(M * N^2). The input parameters to the recusive function 
# are a pair of integers; representing a position in each string. There are 
# M possible positions for the first string, and N for the second string. 
# Therefore, this gives us M * N possible pairs of integers, and is the 
# number of problems to be solved. 
# Solving each subproblem requires, in the worst case, an O(N) operation; 
# searching for a character in a string of length N. This gives total (M * N^2)

# Space Complexity: O(M * N). We need to store the answer for each of the M * N
# subproblems. Each subproblem takes O(1) space to store. Total O(M * N). 

# =============================================================================
# Approach 2: Improved Memoization

from functools import lru_cache

class Solution2:
    def longestCommonSubsequence(self, text1, text2):

        @lru_cache(maxsize=None)
        def memo_solve(p1, p2):

            # Base case: If either string is empty, can't match any more chars
            if p1 == len(text1) or p2 == len(text2):
                return 0

            # Recursive case 1
            if text1[p1] == text2[p2]:
                return 1 + memo_solve(p1 + 1, p2 + 1)

            # Recursive case 2
            else:
                return max(memo_solve(p1 + 1, p2), memo_solve(p1, p2 + 1))

        return memo_solve(0, 0)

# Time Complexity: O(M * N). Solving each subproblem has a cost of O(1). Again,
# there are M * N subproblems, and so total O(M * N). 

# Space Complexity: O(M * N). We need to store answer for each M * N subproblem

# =============================================================================
# Approach 3: Dynamic Programming

"""
Intuition:
Iteration is faster than recursion in most programming languages. Therefore, we
often want to convert a top-down memoization approach into a bottom-up dynamic 
programming one (some people go directly to bottom-up, but most people find it 
easier to come up with a recursive top-down approach then convert it). 

Observe that the subproblems have a natural "size" ordering; the largest 
subproblem is the one we start with, and the smallest subproblems are the ones 
with just one letter left in each word. The answer for each subproblem depends 
on the answers to some of the smaller subproblems. 

Remembering too that each subproblem is represented as a pair of indexes, and 
that there are text1.length() * text2.length() such possible subproblems, we 
can iterate through the subproblems, starting with the smallest ones, and 
storing the answer for each. When we get to the largest subproblems, the 
smaller ones that they depend on will already have been solved. the best way 
to do this is to use a 2D array. 

Each cell represents one subproblem. cell (g, a) represents subproblem 
lcs("attag", "gtgatcg"). 

Remember, there are two cases:
1. The first letter of each string is the same. 
2. The first letter of each string is different.

For the first case, we solve the subproblem that removes the first letter from 
each, and add 1. In the grid, this subproblem is always the diagonal 
immediately down and right. 

For the second case, we consider the subprob that removes the first letter of 
the first word, and then the subprob that removes the first letter off the 
second word. In the grid, these are subproblems immediately right and below. 

Putting this all together, we iterate over each column in reverse, starting 
from the last column (we could also do rows, the final result will be the 
same). For a cell (row, col), we look at whether or not 
text1.charAt(row) == text2.charAt(col) is true. If it is, then set 
grid[row][col] = 1 + grid[row+1][col+1]. Otherwise, we set 
grid[row][col] = max(grid[row + 1][col], grid[row][col + 1]).

For easy implementation, we add an extra row of zeroes at the bottom and to the
right. 
"""

class Solution2:
    def longestCommonSubsequence(self, text1, text2):

        # Make a grid of 0's with len(text2)+1 columns and len(text1)+1 rows.
        dp_grid = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        # Iterate up each column, starting from the last one. 
        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                # If the corresponding characters for this cell are the same...
                if text2[col] == text1[row]:
                    dp_grid[row][col] = 1 + dp_grid[row + 1][col + 1]
                # Otherwise they must be different...
                else:
                    dp_grid[row][col] = max(dp_grid[row + 1][col], dp_grid[row][col + 1])

        # original problems answer is in dp_grid[0][0]. Return it. 
        return dp_grid[0][0]

# Time Complexity: O(M * N). Solve M * N subproblems at O(1) operation

# Space Complexity: O(M * N). Allocate 2D array size M * N to store all subprob
# answers