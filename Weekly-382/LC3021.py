'''
3021. Alice and Bob Playing Flower Game 

Alice and Bob are playing a turn-based game on a circular field surrounded by flowers. The circle represents the field, and there are x flowers in the clockwise direction between Alice and Bob, and y flowers in the anti-clockwise direction between them.

The game proceeds as follows:

Alice takes the first turn.
In each turn, a player must choose either the clockwise or anti-clockwise direction and pick one flower from that side.
At the end of the turn, if there are no flowers left at all, the current player captures their opponent and wins the game.
Given two integers, n and m, the task is to compute the number of possible pairs (x, y) that satisfy the conditions:

Alice must win the game according to the described rules.
The number of flowers x in the clockwise direction must be in the range [1,n].
The number of flowers y in the anti-clockwise direction must be in the range [1,m].
Return the number of possible pairs (x, y) that satisfy the conditions mentioned in the statement.

 

Example 1:

Input: n = 3, m = 2
Output: 3
Explanation: The following pairs satisfy conditions described in the statement: (1,2), (3,2), (2,1).
Example 2:

Input: n = 1, m = 1
Output: 0
Explanation: No pairs satisfy the conditions described in the statement.
 

Constraints:

1 <= n, m <= 105
'''

class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        '''
        By understanding the problem better and trying out for different values of n and m, the sum of (x,y) must be odd.

        Brute Force solution:
        1. Iterate through n and m, check the parity of (i+j) if odd add to the ans. Finally return the ans
         cnt = 0
         for i in range(1, n+1):
             for j in range(1, m+1):
                 if (i + j)%2 == 1:
                     cnt += 1
         return cnt
        TC: O(N**2) SC: O(1)
        2. So we only need to get the odd sum values from [1...n] and [1..m]

        Sum of x, y is odd if
        x-even, y-odd --> x+y odd
        x-odd, y-even --> x+y odd
        x-odd, y-odd --> x+y odd

        Hence calculate the odd count and even count from n and m.

        So the final ans --> odd_count_n * even_count_m + even_count_n * odd_count_m
        '''
        odd_count_n = (n + 1) // 2
        even_count_n = n // 2

        # Calculate the count of odd and even numbers in the range [1, m]
        odd_count_m = (m + 1) // 2
        even_count_m = m // 2

        # Calculate the total count of pairs with odd sums using the formula
        total_odd_pairs = odd_count_n * even_count_m + even_count_n * odd_count_m

        return total_odd_pairs

