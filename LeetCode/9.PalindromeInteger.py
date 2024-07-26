# Accepted in Leetcode

class Solution:
    def isPalindrome(self, x: int) -> bool:
        dup_x = str(x)
        ans = ""
        if x < 0:
            x *= -1
            while x > 0:
                rem = x%10
                x //= 10
                ans += str(rem)
            ans += "-"
        elif x > 0:
            while x > 0:
                rem = x%10
                x //= 10
                ans += str(rem)
        else:
            str(x)

        if dup_x == "0":
            return True
        elif dup_x == ans:
            return True
        else:
            return False

solution_obj = Solution()

x = int(input("Enter integer: "))

print(solution_obj.isPalindrome(x))
