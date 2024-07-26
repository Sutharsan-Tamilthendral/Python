class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        sep = [x for x in s]
        count = 0
        for i in range(len(sep)):
            if letter == sep[i]:
                count += 1

        return int((count/len(sep))*100)

obj = Solution()
s = input("Enter the word: ").lower()
letter = input("Enter the letter to find percentage: ").lower()
result = obj.percentageLetter(s, letter)
print(result)