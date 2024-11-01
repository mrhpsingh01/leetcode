class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        initial = [0, 0]
        dirString = ["U", "L", "D", "R"]
        dir = "U"
        cycle = 0
        i = 0
        while cycle >= 0:
            if i == len(instructions):
                if initial == [0, 0]:
                    return True
                cycle += 1
                i = 0
            if instructions[i] == "L":
                index = 0 if dirString.index(dir) == 3 else dirString.index(dir) + 1
                dir = dirString[index]
                i += 1
            elif instructions[i] == "R":
                index = 0 if dirString.index(dir) == 0 else dirString.index(dir) - 1
                dir = dirString[index]
                i += 1
            else:
                if dir == "U":
                    initial[1] = initial[1] + 1
                elif dir == "D":
                    initial[1] = initial[1] - 1
                elif dir == "L":
                    initial[0] = initial[0] - 1
                elif dir == "R":
                    initial[0] = initial[0] + 1
                i += 1

            if cycle == 4:
                return False


moves = "GLRLGLLGLGRGLGL"


x = Solution().isRobotBounded(moves)
print(x)
