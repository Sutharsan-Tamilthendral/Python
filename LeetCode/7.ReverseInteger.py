# Leetcode accepted successfully

class Solution:
    def reverse(self, x: int) -> int:
        signed_min = -2 ** 31
        signed_max = 2 ** 31 - 1

        if x < 0:
            ans = "-"
            x *= -1
            while x > 0:
                rem = x%10
                x //= 10
                ans += str(rem)
        else:
            ans = ""
            while x > 0:
                rem = x % 10
                x //= 10
                ans += str(rem)

        if int(ans) < signed_min or int(ans) > signed_max:
            return 0
        else:
            return int(ans)


solution_obj = Solution()
x = int(input())
print(solution_obj.reverse(x))