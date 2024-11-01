class Solution:
    def checkStraightLine(self, coordinates) -> bool:
        diff = [
            abs(coordinates[1][1] - coordinates[0][1]),
            abs(coordinates[1][0] - coordinates[0][0]),
        ]
        print(diff)
        for i in range(len(coordinates) - 1):
            if (
                abs(coordinates[i][i - 1] - coordinates[i - 1][i - 1]) != diff[1]
                and abs(coordinates[i][i] - coordinates[i - 1][i]) != diff[0]
            ):
                print(
                    i,
                    abs(coordinates[i][i - 1] - coordinates[i - 1][i - 1]),
                    abs(coordinates[i][i] - coordinates[i - 1][i]),
                )
                return False
        return True


coordinates = [[0, 0], [0, 1], [0, -1]]


x = Solution().checkStraightLine(coordinates)
print(x)
