class Solution:
    # return true if nums[] contains duplicate
    # pre: nums[1, 2, 3, 1]
    # post: true
    def containsDuplicate(self, nums):

        if len(nums) <= 1:
            return False

        map = {}
        for num in nums:
            if num in map:
                return True
            map[num] = True
        return False
