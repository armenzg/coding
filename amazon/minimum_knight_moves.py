'''Minimum Knight Moves
In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

Return the minimum number of steps needed to move the knight to the square [x, y].  It is guaranteed the answer exists.

Example 1:

Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]

Example 2:

Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]

Constraints:

    |x| + |y| <= 300
'''
def _move_x_first(pos, x, y):
    # Current position is less than target; increment
    if pos[0] + 2 <= x:
        pos[0] += 2
        if pos[1] <= y:
            pos[1] += 1
        else:
            pos[1] -= 1
        
    return pos

def _move_y_first(pos, x, y):
    return pos

def movePiece(pos: (int, int), x: int, y: int) -> (int, int):
    new_pos = None
    if abs(x) >= abs(y):
        # x=2 && (y<=2)
        new_pos = _move_x_first(pos, x, y)
    else:
        new_pos = _move_y_first(pos, x, y)
    return new_pos

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # x =  2, y =  1
        # x = -2, y =  1
        # x = -2, y = -1
        # x =  2, y = -1
        count = 0
        position = [0, 0]
        while position != [x, y]:
            position = movePiece(position, x, y)
            print(position)
            
        return count

sol = Solution()
assert sol.minKnightMoves(-2, -2) == 1
assert sol.minKnightMoves(-1, -2) == 1
assert sol.minKnightMoves( 0, -2) == 1
assert sol.minKnightMoves( 1, -2) == 1
assert sol.minKnightMoves( 2, -2) == 1
assert sol.minKnightMoves(-2, -1) == 1
assert sol.minKnightMoves(-1, -1) == 1
assert sol.minKnightMoves( 0, -1) == 1
assert sol.minKnightMoves( 1, -1) == 1
assert sol.minKnightMoves( 2, -1) == 1
assert sol.minKnightMoves(-2,  0) == 1
assert sol.minKnightMoves(-1,  0) == 1
assert sol.minKnightMoves( 0,  0) == 1
assert sol.minKnightMoves( 1,  0) == 1
assert sol.minKnightMoves( 2,  0) == 1
assert sol.minKnightMoves(-2,  1) == 1
assert sol.minKnightMoves(-1,  1) == 1
assert sol.minKnightMoves( 0,  1) == 1
assert sol.minKnightMoves( 1,  1) == 1
assert sol.minKnightMoves( 2,  1) == 1
assert sol.minKnightMoves(-2,  2) == 1
assert sol.minKnightMoves(-1,  2) == 1
assert sol.minKnightMoves( 0,  2) == 1
assert sol.minKnightMoves( 1,  2) == 1
assert sol.minKnightMoves( 2,  2) == 1