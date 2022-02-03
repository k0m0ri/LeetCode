import math


class Solution:
    # return majority element(appearing ceil(n/2) times) in array
    # pre: nums=[3,2,3]
    # post:3
    def majorityElement(self, nums):
        map = {}
        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1

        majority_element = nums[0]
        for key, val in map.items():
            if val >= math.ceil(len(nums) / 2):
                majority_element = key

        return majority_element


solution = Solution()
print(solution.majorityElement([6, 5, 5]))
