class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            diff = target - nums[i]
            if (diff in nums)and nums.index(diff) != i:
                ans = [i, nums.index(diff)]
        return ans