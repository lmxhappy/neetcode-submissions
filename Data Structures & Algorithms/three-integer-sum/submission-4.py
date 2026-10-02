class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        sorted_nums = sorted(nums)

        ret = []
        for j in range(1, len(sorted_nums) - 1):

            i = j - 1
            k = j + 1
            while i >= 0 and k < len(sorted_nums):

                if i < j - 1 and sorted_nums[i] == sorted_nums[i + 1]:
                    i -= 1
                    continue

                if k > j + 1 and sorted_nums[k] == sorted_nums[k - 1]:
                    k += 1
                    continue

                if sorted_nums[i] + sorted_nums[j] + sorted_nums[k] == 0:
                    ret.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                    i -=1
                    k +=1
                    
                elif sorted_nums[i] + sorted_nums[j] + sorted_nums[k] > 0:
                    i -= 1
                else:
                    k += 1

        ret = [list(x) for x in set(map(tuple, ret))]

        return ret