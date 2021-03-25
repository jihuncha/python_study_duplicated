from typing import List

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# Input: nums = []
# Output: []

# Input: nums = [0]
# Output: []

# nums = [-1,0,1,2,-1,-4]

nums = [0,0,0]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result_list = list(set(nums))
        # print(result_list)

        temp_list = []

        for i in range(len(result_list)):
            for j in range(i+1, len(result_list)):
                for k in range(i+2, len(result_list)):
                    if result_list[i] + result_list[j] + result_list[k] == 0:
                        result = [result_list[i],result_list[j],result_list[k]]
                        result.sort()
                        print(result)
                        if result not in temp_list:
                            temp_list.append(result)

        # print(temp_list)
        # for a in range(len(nums)):
        #     for b in range(len(nums)):
        #         for c in range(len(nums)):
        #             if nums[a] + nums[b] + nums[c] == 0:
        #
        #
        # if len(result_list) != 0:
        #     return result_list
        # else:
        #     return list()


print(Solution().threeSum(nums))