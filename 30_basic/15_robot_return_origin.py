class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # initial = [0, 0]
        # for move in moves:
        #     if move == "U":
        #         initial[1] = initial[1] + 1
        #     elif move == "D":
        #         initial[1] = initial[1] - 1
        #     elif move == "L":
        #         initial[0] = initial[0] - 1
        #     elif move == "R":
        #         initial[0] = initial[0] + 1

        # if initial == [0, 0]:
        #     return True
        # else:
        #     return False
        if moves.count("R") == moves.count("L") and moves.count("U") == moves.count(
            "D"
        ):
            return True
        else:
            return False


moves = "RDDDDDURD"


x = Solution().judgeCircle(moves)
print(x)
