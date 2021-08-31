# Leetcode Question 17 [Medium]
# Letter Combinations on a Phone Number 

"""
Given a string containing digits from 2-9 inclusive, return all possible 
letter combinations that the number could represent. Return the answer in 
any order. 

A mapping of digit to letters (just like on the telephone buttons) is given 
below. Note that 1 does not map to any letters. 

Example 1:
Input: digits = "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

Example 2: 
Input: digits = ""
Output: []

Example 3: 
Input: digits = "2"
Output: ["a", "b", "c"]

Constraints:
    0 <= digits.length <= 4
    digits[i] is a digit in the range ['2', '9']
"""

# Whenever you have a problem where you need to generate all combinations/
# permutations of some group of letters/numbers, first think BACKTRACKING. 
# Backtracking algos can often keep space complexity linear with input size.

# Approach 1: Backtracking
# Intuition
"""
Starting with an input that is only 1-digit long, for example, digits "2", 
just generate all letters that correspond with digit = "2", which is 
["a", "b", "c"]. 

What if we have 2-digit long input, digits = "23". Take each letter of 
digit = "2" as a starting point. Lock the first letter in, and solve all 
possible combinations that start with that letter. If our first letter will 
always be "a", then the problem is trivial again - it's 1-digit case again, 
all we have to do is generate all letters corresponding with digit = "3", 
and add that to "a", to get ["ad", "ae", "af"]. This was easy bc we ignored 
the first letter and set it will always be "a". But we know how to generate 
all the first letters too - 1-digit case which we already solved to be 
["a", "b", "c"]. 

As you can see, solving the 1-digit case is trivial, and solving the 2-digit 
case is just solving the 1-digit case twice. Then the same reasoning can be 
extended to n digits. For 3-digit case, solve 2-digit case to generate all 
combinations of the first 2 letters, and then solve 1-digit case for final 
digit. Now we know how to solve 3-digit, to solve 4-digit, solve the 3-digit 
case for all combos for first 3 letters, and then solve 1-digit case for the 
final digit. Ends at 4. 

Algo:
As mentioned previously, we need to lock-in letters when we generate new 
letters. The easiest way to save state like this is use recursion.
1.  If the input is empty, return an empty array
2.  Initialize a data structure (e.g. hash map) that maps digit to their 
    letters, for example, mapping "6" to "m", "n", and "o". 
3.  Use a backtracking function to generate all possible combinations. 
    - The function should take 2 primary inputs: the current combination 
        of letters we have, path, and the index we are currently checking. 
    - As a base case, if our current combo of letters is the same length as 
        the input digits, that means we have a complete combo. Therefore, 
        add it to our answer, and backtrack. 
    - Otherwise, get all the letters that correspond with current digit we 
        are looking at, digits[index]. 
    - Loop through these letters. For each letter, add the letter to our 
        current path, and call backtrack again, but move on to the next digit 
        by incrementing index by 1. 
    - Make sure to remove the letter from path once finished with it. 
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # If input is empty, return empty answer array
        if len(digits) == 0:
            return []

        # Map all digits to corresponding letters
        letters = {
            "2": "abc", 
            "3": "def", 
            "4": "ghi",
            "5": "jkl", 
            "6": "mno", 
            "7": "pqrs", 
            "8": "tuv", 
            "9": "wxyz"
        }

        def backtrack(index, path):
            # If path is same length as digits, we have complete combination
            if len(path) == len(digits):
                combinations.append("".join(path))
                return # Backtrack
            
            # Get the letters that the current digit maps to, and loop through
            possible_letters = letters[digits[index]]
            for letter in possible_letters:
                # Add letter to our current path
                path.append(letter)
                # Move on to the next digit
                backtrack(index + 1, path)
                # Backtrack by removing the letter before moving onto next
                path.pop()

        # Init backtracking with empty path and starting index of 0
        combinations = []
        backtrack(0, [])
        return combinations

# Time: O(N * 4^N). upto to 4 possible letters per digit for N digits
# Space: O(N), N is length of digits for hash map

"""
Neetcode simpler version
"""

class Solution1(object):
    def letterCombinations(self, digits):
        res = []
        letters = {
            "2": "abc", 
            "3": "def", 
            "4": "ghi",
            "5": "jkl", 
            "6": "mno", 
            "7": "pqrs", 
            "8": "tuv", 
            "9": "wxyz"
        }

        def backtrack(i, curr_str):
            if len(curr_str) == len(digits):
                res.append(curr_str)
                return
            for char in letters[digits[i]]:
                backtrack(i + 1, curr_str + char)

        if digits:
            backtrack(0, "")

        return res