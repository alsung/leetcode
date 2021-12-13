"""
Alice and Bob want to water n plants in their garden. The plants are arranged in a row and are 
labeled from 0 to n - 1 from left to right where the ith plant is located at x = i. 

Each plant needs a specific amount of water. Alice and Bob have a watering can each, initially 
full. They water the plants in the following way:
    - Alice waters the plants in order from left to right, starting from the 0th plant. Bob 
        waters the plants in order from right to left, starting from the (n - 1)th plant. They 
        begin water the plants simultaneously
    - If one does not have enough water to completely water the current plant, he/she refills
        the water can instantaneously
    - It takes the same amount of time to water each plant regardless of how much water it needs
    - One cannot refill the watering can early
    - Each plant can be watered by either Alice or by Bob
    - In case both Alice and bob reach the same plant, the one with more water currently in 
        his/her watering can should water this plant. If they have the same amount of water, then 
        Alice should water this plant

Given a 0-indexed integer array plants of n integers, where plants[i] is the amount of water the 
ith plant needs, and two integers capacityA and capacityB representing the capacities of Alice's 
and Bob's watering cans respectively, return the number of times they have to refill to water all
the plants.
"""

"""
Example 1
Input: plants = [2,2,3,3], capacityA = 5, capacityB = 5
Output: 1
Explanation:
 - Initially, Alice and Bob have 5 units of water each in their water cans.
 - Alice waters plant 0, Bob waters plant 3
 - Alice and Bob now have 3 units and 2 units of water respectively
 - Alice has enough water for plant 1, so she waters it. Bob does not have enough water for plant 
    2, so he refills his can then waters it. So, the total number of times to refil os 0 + 0 + 1 + 0 = 1
"""

class Solution:
    def minimumRefill(self, plants, capacityA, capacityB):
        n = len(plants)
        plantA = 0
        plantB = n - 1
        amountA = capacityA
        amountB = capacityB
        num_refills = 0
        completed_plants = []

        while plantA <= plantB:
            if plantA == plantB and plantA not in completed_plants:
                print("here")
                if amountA >= amountB:
                    if amountA >= plants[plantA]:
                        amountA -= plants[plantA]
                    else:
                        num_refills += 1
                        amountA = capacityA
                        amountA -= plants[plantA]
                else:
                    if amountB >= plants[plantB]:
                        amountB -= plants[plantB]
                    else:
                        num_refills += 1
                        amountB = capacityB
                        amountB -= plants[plantB]
                break

            if amountA >= plants[plantA] and plantA not in completed_plants:
                amountA -= plants[plantA]
                completed_plants.append(plantA)
                plantA += 1
            else:
                amountA = capacityA
                num_refills += 1
                amountA -= plants[plantA]
                completed_plants.append(plantA)
                plantA += 1

            if amountB >= plants[plantB] and plantB not in completed_plants:
                amountB -= plants[plantB]
                completed_plants.append(plantB)
                plantB -= 1
            else:
                amountB = capacityB
                num_refills += 1
                amountB -= plants[plantB]
                completed_plants.append(plantB)
                plantB -= 1
            
        return num_refills


test = Solution()
plants = [2,1,1]
capacityA = 10
capacityB = 8
test.minimumRefill(plants, 2, 2)