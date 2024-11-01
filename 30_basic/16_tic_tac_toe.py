class Solution:
    def tictactoe(self, moves: str) -> bool:
        if moves.count("R") == moves.count("L") and moves.count("U") == moves.count(
            "D"
        ):
            return True
        else:
            return False


moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]


x = Solution().tictactoe(moves)
print(x)
