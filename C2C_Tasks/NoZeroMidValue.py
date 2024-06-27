# Today's Technical Task
#
# 1. Write a program to print the mid elements of an array after the removal of '0' occurred elements from a given
# input array.
#
# Note: If the '0' removed array consists of an even number of elements, then print average of mid two elements of an
# array.
#
# Sample Testcase 1
# Input:
# 7
# 10 5 0 890 50 71 8
#
# Output:
# 71
#
# Sample Testcase 2
# Input:
# 5
# 10 5 390 24 123
#
# Output:
# 14
#
# Try this logic in the compiler and DM the output screenshot 👍

n = int(input())
n_ele = input().__str__().split()
nums = []
for i in n_ele:
    a = int(i)
    nums.append(a)

# for i in nums:
#     if nums[i] == 0:
#         del nums[i]
    # elif nums[i]%10 == 0:
    #     nums.pop(i)
    # elif nums[i] > 9:
    #     while nums[i] > 9:
    #         d = nums[i]%10
    #         if d == 0:
    #             nums.pop(i)
    #         else:
    #             nums[i] //= 10

print(nums)