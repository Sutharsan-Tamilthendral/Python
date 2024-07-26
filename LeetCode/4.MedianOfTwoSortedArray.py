# Leetcode accepted successfully

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        res_arr = nums1 + nums2
        sort_res_arr = sorted(res_arr)

        if len(sort_res_arr) == 0:
            return None
        elif len(sort_res_arr) % 2 != 0:
            t_res = len(sort_res_arr) // 2
            tot_res = sort_res_arr[t_res]
            return float(tot_res)
        elif len(sort_res_arr) == 2:
            tot_res = sum(sort_res_arr) / len(sort_res_arr)
            return tot_res
        else:
            tet = len(sort_res_arr) // 2
            start = tet - 1
            last = start * -1
            res = sort_res_arr[start:last]
            tot_res = sum(res) / len(res)
            return tot_res


solution_obj = Solution()
print(solution_obj.findMedianSortedArrays([3], [-2, -1]))
