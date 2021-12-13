# There are n rings and each ring is either red, green, or blue. The rings are distributed across ten rods labeled from 0 to 9. 

# You are given a string rings of length 2n that describes the n rings that re placed onto the rods. Every two characters in rings forms a color-position pair that is used to describe each ring where:
    # - the first character of the ith pair denotes the ith rings color ('R', 'G', 'B')
    # - the second character of the ith pair denotes the rod that the ith ring is placed on ('0' to '9')

# For example, "R3G2B1" describes n == 3 rings: a red ring placed onto the rob labeled 3, a green ring placed onto the rod labeled 2, and a blue ring placed onto the rod labeled 1

# Return the number of rods that have all three colors of rings on them

"""
Example 1
Input: rings = "B0B6G0R6R0R6G9"
Output: 1
Explanation: 
    - rod labeled 0 holds 3 rings with all colors: red, green and blue
    - rod labeled 6 holds 3 rings but only colors red and blue
    - rod 9 holds only a green ring
"""

"""
Constraints:
 - rings.length == 2*n
 - 1 <= n <= 100
 - rings[i] where i is even is either 'R', 'G', or 'B' (0-indexed)
 - rings[i] where i is odd is a digit from '0' to '9' (0-indexed)
"""

class Solution:
    def countPoints(self, rings):
        # list for every new rod
        # append color ring to corresponding rod

        colors = ['R', 'G', 'B']
        rings_dict = {}
        count = 0

        for char in rings:
            if char in colors:
                color = char
            else:
                if char not in rings_dict:
                    rings_dict[char] = [color]
                else: 
                    rings_dict[char].append(color)
            
        # check what rings have all 3 colors
        for rod in rings_dict:
            if 'R' in rings_dict[rod] and 'G' in rings_dict[rod] and 'B' in rings_dict[rod]:
                count += 1

        return count


test = Solution()
pass_list = test.countPoints("B0R0G0R9R0B0G0G9B9")
print(pass_list)