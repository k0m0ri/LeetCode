from numpy import nonzero


class Solution:
    # move all zeros toward the end
    # pre: nums=[0,1,0,3,12]
    # post: nums=[1,3,12,0,0]
    def moveZeros(self, nums):

        if len(nums) == 1:
            return nums

        non_zeros_last = 0
        runner = 0

        # testcase: nums=[0,1,0,3,12], non_zeros_index=0, running_index=1
        # testcase: nums=[1,0,0,3,12], non_zeros_index=1, running_index=2
        # testcase: nums=[1,3,0,0,12], non_zeros_index=2, running_index=3
        # testcase: nums=[1,3,12,0,0], non_zeros_index=3, running_index=4
        while runner < len(nums):
            if not nums[runner] == 0:
                self.swap(nums, non_zeros_last, runner)
                non_zeros_last += 1
            runner += 1
        return nums

    def swap(self, nums, front, end):
        tmp = nums[front]
        nums[front] = nums[end]
        nums[end] = tmp
