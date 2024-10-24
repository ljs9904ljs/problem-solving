from itertools import permutations

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        result = 0
        for i in range(1, len(tiles) + 1):
            # r - permutations of multisets 를 너무 무식한 방법으로 구하는 것 같다... 이게 최선일까?
            result += len(set(permutations(tiles, i)))
        
        return result
    
    
"""



You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

 

Example 1:

Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

Example 2:

Input: tiles = "AAABBC"
Output: 188

Example 3:

Input: tiles = "V"
Output: 1

 

Constraints:

    1 <= tiles.length <= 7
    tiles consists of uppercase English letters.



"""