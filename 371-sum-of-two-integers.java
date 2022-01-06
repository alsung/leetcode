// Leetcode Question 371 [Medium]
// Sum of Two Integers

// Given two integers a and b, return the sum of the two integers without using the operators + and -.

// Example 1:
// Input: a = 1, b = 2
// Output: 3

// Example 2:
// input: a = 2, b = 3
// output: 5

// If we XOR the bits together, we add the bits of the number, then we will need to include a carry. 
// Carry only needed during instances of bits 1 + 1. 

// To get the carry value, we can use the operation: (a & b) << 1
// and add the value to the original a value to calculate the new sum of values. We continue 
// doing this until the carry value, b, equals 0. 

class Solution {
    public int getSum(int a, int b) {
        // b will be reused for the carry
        while (b != 0) {
            int tmp = (a & b) << 1;
            a = a ^ b; // use XOR to add mismatched bits together
            b = tmp; // store calculated and shifted carry in b 
        }
        return a; // final answer when b == 0 is stored in a
    }
}

// Time Complexity: O(1)
// Space Complexity: O(1)