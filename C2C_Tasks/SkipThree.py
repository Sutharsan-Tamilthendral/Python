n = int(input("Enter range: "))
ans = 0

for i in range(1, n+1, 4):
    ans += i

print(ans)