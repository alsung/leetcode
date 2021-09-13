# Leetcode Question 36 [Medium]
# Valid Sudoku

"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be 
validated according to the following rules:
    1. Each row must contain digits 1-9 without repetition. 
    2. Each column must contain digits 1-9 without repetition. 
    3. Each of the nine 3 x 3 sub-boxes of grid must contain digits 1-9 without
       repetition. 

Note: 
    - A Sudoku board (partially filled) could be valid but is not necessarily 
    solvable. 
    - Only the filled cells need to be validated according to the rules. 

Example 1
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as example 1, except with the 5 in the top left corner being
modified to 8. Since there are two 8s in the top left 3 x 3 sub-box, its 
invalid

Constraints:
    board.length == 9
    board[i].length == 9
    board[i][j] is a digit 1-9 or '.'
"""

# Overview
"""
A valid sudoku board should satisfy three conditions: (1) each row, (2) each 
column, (3) each box has no duplicate numbers. 

For instance, in example 1, for board[2][1] = 9, need to check conditions: 
    1. Does 9 appear more than once in third row?
    2. Does 9 appear more than once in second column? 
    3. Does 9 appear more than once in first box?

In order to check 9 rows, 9 columns, and 9 boxes, we need to distinguish each 
of these entities. It is comparatively intuitive to check for duplicates in 
each row and column, given the row index r and column index c. 

We can create a hash set for each row. For board[r][c], we check if number
already exists in the hash set corresponding to r-th row. If yes, this row 
contains duplicate values, therefore not valid. Otherwise, we proceed to 
check the next position until we finish scanning the whole sudoku board. 
The same logic can be applied to each column. 

The tricky part is when we check the validity of each box. The question is, 
given row index r and column index c, how to assign position to one of the 9
boxes correctly? The first observation is that, in each column, rows 0, 1, and 
2 belong to the same box, as do rows 3, 4, and 5, and rows 6, 7, and 8. 

What do they have in common? Each group of three belonging to the same box has 
the same outcome when we perform integer division by 3. Therefore, we can use 
r/3 (/ signifies floor division) to ensure the rows are grouped as expected and
use c/3 to ensure that the columns are grouped correctly. Then, (r/3, c/3) can 
uniquely mark each box, and we can directly use the tuple as the hash key if we
wanted to create a hash set for each box. 

Alternatively, we can use the numbers 0 through 8 to represent these boxes, 
where (r/3) * 3 + (c/3) is used to calculate a number in the range from 0 to 8.
I.e. the square located at (r,c) belongs to the box (r/3) * 3 + (c/3). 

Notice that reading from left to right, the box indices are continuous from 0 
to 8, and will increase by column first. 

For each row, column, and box, there are several ways to storewhich numbers 
have already appeared so far. Here are three that we will use in this problem:
    1. Create a hash set for each row, column, and box (Approach 1)
    2. Create an array of length 9 with values 0 and 1 representing "not seen"
        and "previously seen" states, respectively (Approach 2)
    3. Use a binary number with a value 0 or 1 at each position representing
        the previous occurence of each number (Approach 3)
"""

# APPROACH 1: HASH SET # 
########################
"""
Intuition: 
In a valid sudoku puzzle, each row, column, and box contains digits 1-9 without
repetition. To check if the sudoku is valid, for each number, we must check if
that number is repeated anywhere in the same row, column, or box. However, it 
would be very inefficient to read entire row, column, and box every time we 
check if a number is duplicate. Instead, as we are iterating over the numbers, 
we can use hash sets to store the previously seen numbers in each row, column, 
and box. Via hash sets, we can determine if the current number already exists 
in the corresponding row, column, or box in constant time. 

Algorithm: 
1. Initialize a list containing 9 hash sets, where the hash set at index r will
    be used to store previously seen numbers in row r of sudoku. Likewise, 
    initialize lists of 9 hash sets to track the columns and boxes too. 
2. Iterate over each position (r, c) in sudoku. At each iteration, if there is 
    a number at current position: 
        - Check if the number exists in the hash set for the current row, 
            column or box. If it does, return false, because this is the second
            occurence of the number in the current row, column, or box. 
        - Otherwise, update the set responsible for tracking previoiusly seen 
            numbers in the current row, column, and box. The index of the 
            current box is (r / 3) * 3 + (c / 3) where / represents floor 
            division. 
3. If no duplicates were found after every position on the sudoku board has
    been visited, then sudoku is valid, return true. 
"""

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        N = 9

        # Use hash set to record the status
        rows = [set() for i in range(N)]
        cols = [set() for i in range(N)]
        boxes = [set() for i in range(N)]

        for r in range(N):
            for c in range(N):
                val = board[r][c]
                # Check if position is filled with number
                if val == ".":
                    continue

                # Check the row
                if val in rows[r]:
                    return False
                rows[r].add(val)

                # Check the column
                if val in cols[c]:
                    return False
                cols[c].add(val)

                # Check the box
                idx = (r // 3) * 3 + c // 3
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)

        return True

"""
Let N be the board length, which is 9. Note that since value of N is fixed, 
the time and space of this algo can be interpreted as O(1). However, to better 
compare each of the presented approaches, we will treat N as an arbitrary 
value in the complexity analysis below. 

Time: O(N^2) because we traverse every position on the board. each of the four 
    check steps are O(1) operations. 
Space: O(N^2) because in worst case, if board is full, we need hash set with 
    size N to store all seen numbers for each of the N rows, N columns, and N 
    boxes, respectively. 
"""

#==============================================================================
# APPROACH 2: ARRAY OF FIXED LENGTH #
#####################################
"""
Intuition: 
Apart from using a hash set, we can also use an array of fixed length to check 
for duplicates. Each position (pos) in the array represents the status of the 
number pos + 1. Therefore, we can determine if we have already seen some 
number in constant time. We need an array for each row, column, and box. This 
approach is a mental stepping stone for Approach 3 where bitmasking is used. 

Algorithm: 
1. Initialize an array of size N filled with zeros for each row, column, and 
    box, where N is the sudoku board length, which in this case is 9. 
2. Iterate over each position (r, c) in sudoku. At each iteration, if there is 
    a number at the current position: 
    - Check if the number n has been previously seen by checking the n - 1 
        index in the array. If the value at this index equals 1, it means we 
        have already seen this number, so sudoku is not valid. Return false. 
    - Otherwise, if the value at this position equals 0, then it is the first 
        time encountering the number, so update the value at this position to 
        1 to mark that we have seen this number. 
3. Once every position on the sudoku board is check, with no duplicates found,
    we return true. 
"""

class Solution1: 
    def isValidSudoku(self, board):
        N = 9

        # Use an array to record the status
        rows = [[0] * N for i in range(N)]
        cols = [[0] * N for i in range(N)]
        boxes = [[0] * N for i in range(N)]

        for r in range(N):
            for c in range(N):
                # Check if the position is filled with number
                if board[r][c] == ".":
                    continue

                pos = int(board[r][c]) - 1

                # Check the row
                if rows[r][pos] == 1:
                    return False
                rows[r][pos] = 1

                # Check the column
                if cols[c][pos] == 1:
                    return False
                cols[c][pos] = 1

                # Check the box
                idx = (r // 3) * 3 + c // 3
                if boxes[idx][pos] == 1:
                    return False
                boxes[idx][pos] = 1

            return True

"""
Time: O(N^2) bc we need to traverse every position on the board, each check is 
    O(1) operation. 
Space: O(N^2) because we need to create 3N arrays each with size N to store all
    previously seen numbers for all rows, cols, and boxes. 
"""

#==============================================================================
# APPROACH 3: BITMASKING #
##########################
"""
Intuition:
In Approach 2 we showed how we can use values at different positions of an 
array to mark whether the number corresponding to each position has been seen 
or not. Each position in the array can take a value of 0 or 1, which can be 
represented by a single bit. Therefore, we can improve space complexity by 
bitmasking. 

To recap, for a binary number, each bit can take a value of 0 or 1. We can use 
a binary number with 9 digits to represent whether numbers 1-9 have been 
visited or not. Now, "how do we set a bit to 1 when a number is seen and how 
do we check if a bit is already set to 1?" Let's first review the two most 
commonly used operations for get and set in bitmasking. Such operations on 
bits are commonly referred to as bitwise operations. 
1. Check if the ith bit of a binary number is set to 1: x & (1 << i). If this 
    expression evaluates to 0, the bit is not set.
    - 1 << i means the number 1 is bit shifted to the left i times. For 
        example, 1 << 2 changes the number 1 ('001') to the number 4 ('0100'). 
        Notice that in binary representation, the 1 is shifted two places to 
        the left. 
    - Bitwise AND (&) returns only the bits that are set in both the left AND
        right operand. For example, 5 & 4 = '0101' & '0100' = '0100' = 4. 
        Notice that in binary representation, the only remaining set bit is the
        bit that was set in both numbers. One more example for clarity: 
        10 & 4 = '1010' & '0100' = '0000' = 0. When two numbers do not share 
        any bits, bitwise AND returns 0, otherwise, it will return a nonzero 
        value. This is why we can use bitwise AND to check if ith bit from the 
        right has been set. 
2. Set the ith bit of a binary number x to 1: x = x | (1 << i)
    - Bitwise OR (|) returns the bits that are set in the left OR right 
        operand. For example, 10 | 4 = '1010' | '0100' = '1110' = 14. Notice 
        that the third bit from the right has been set (changed from 0 to 1). 
        This is why we can use x = x | (1 << i) to set the ith bit from the 
        right in the integer x. 

Here we use 9 bits to represent numbers 1-9. You might wonder, if these numbers
are not continuous, can we still use bitmasking to represent the presence or 
absence of each number? Yes. For instance, if we know upfront that the possible
discrete values are [1,9,10,100] (any small set of possible values), we can use
a hashmap {1:0, 9:1, 10:2, 100:3} to track the correspondence between possible 
values and positions in binary number. So, we can use a 4-digit binary number 
to represent the status of each number in [1,9,10,100], even though these 
numbers are not continuous. 

Algo: 
1. Use an integer for each row, column, and box to track whcih numbers have 
    been previously seen. The i-th bit from the right marks the previous 
    occurrence of the number i. For example, '000001010' signifies the numbers
    2 and 4 have been previously seen. 
2. Iterate over each position (r, c) in the sudoku board. At each iteration, if
    there is a number at the current position:
    - use x & (1 << i) to check if we have seen the number i + 1 previously. If
        x & (1 << i) is nonzero, the number i + 1 is duplicate and the sudoku 
        is not valid. 
    - otherwise, we havent seen this number before, and we will use 
        x | (1 << i) to set the i-th bit from the right to signify the number 
        i + 1 has been seen. 
3. Once every position on the sudoku board has been checked, if no duplicates 
    were found, we return true. 
"""

class Solution2: 
    def isValidSudoku(self, board):
        N = 9
        # Use binary number to check previous occurrence
        rows = [0] * N
        cols = [0] * N
        boxes = [0] * N

        for r in range(N):
            for c in range(N):
                # check if the position is filled with number
                if board[r][c] == ".":
                    continue

                pos = int(board[r][c]) - 1

                # Check row
                if rows[r] & (1 << pos):
                    return False
                rows[r] |= (1 << pos)

                # Check column
                if cols[c] & (1 << pos):
                    return False 
                cols[c] |= (1 << pos)

                # Check box
                idx = (r // 3) * 3 + c // 3
                if boxes[idx] & (1 << pos):
                    return False
                boxes[idx] |= (1 << pos)

        return True

# Time: O(N^2), traverse every position on board
# Space: O(N), in worst scenario, if board is full, we need 3N binary numbers
# to store all seen numbers in all rows, columns, and boxes. Using a binary 
# number to record the occurrence of numbers is probably the most 
# space-efficient method. 