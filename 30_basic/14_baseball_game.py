class Solution:
    def calPoints(self, ops) -> int:
        score = []
        for i in range(len(ops)):
            if ops[i] == "+":
                score.append(int(score[-2]) + int(score[-1]))
            elif ops[i] == "C":
                score.pop()
            elif ops[i] == "D":
                score.append(int(score[-1]) * 2)
            else:
                score.append(int(ops[i]))
        return sum(score)


ops = ["5", "2", "C", "D", "+"]

x = Solution().calPoints(ops)
print(x)
