import math


class Solution:
    # return majority element(appearing ceil(n/2) times) in array
    # pre: nums=[3,2,3]
    # post:3
    def majorityElement(self, nums):
        map = {}
        majority_element = math.ceil(len(nums) / 2)

        # corner case
        if len(nums) == 1:
            return nums[0]

        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1

        for key, val in map.items():
            if val >= majority_element:
                return key


solution = Solution()
print(solution.majorityElement([6, 5, 5]))
