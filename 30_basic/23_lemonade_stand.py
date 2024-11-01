class Solution:
    def lemonadeChange(self, bills) -> bool:
        print(bills)
        five = 0
        ten = 0
        twenty = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five >= 1:
                    five -= 1
                    ten += 1
                else:
                    return False
            else:
                if ten >= 1 and five >= 1:
                    twenty += 1
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                    twenty += 1
                else:
                    return False
        return True


bills = [20]

x = Solution().lemonadeChange(bills)
print(x)
