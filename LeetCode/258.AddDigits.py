class Solution:
    def addDigits(num) -> int:
        ans = 0
        if num == 0 or num <= 9:
            return num
        else:
            while num >= 10:
                ans = 0
                while num > 0:
                    ans += num % 10
                    num //= 10
                num = ans
        return ans

S_obj = Solution
print(S_obj.addDigits(38))
