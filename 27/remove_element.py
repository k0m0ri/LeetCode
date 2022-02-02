from unittest import runner


class Solution:
    # return lengh of array section without val
    # pre: nums=[3,2,2,3], val=3
    # post: 2(nums=[2,2,3,3])
    def removeElement(self, nums, val):

        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            if nums[0] == val:
                return 0
            else:
                return 1

        non_val_last = 0
        runner = 0

        # testcase: nums=[3,2,2,3] non_val_last=0 runner=0
        # testcase: nums=[3,2,2,3] non_val_last=0 runner=1
        # testcase: nums=[2,3,2,3] non_val_last=1 runner=2
        # testcase: nums=[2,2,3,3] non_val_last=2 runner=3
        while runner < len(nums):
            # testcase: nums=[2,3,2,3] non_val_last=1 runner=2
            # testcase: nums=[2,2,3,3] non_val_last=2 runner=3
            if not nums[runner] == val:
                self.swap(nums, non_val_last, runner)
                non_val_last += 1
            # testcase: nums=[3,2,2,3] non_val_last=0 runner=1
            # testcase: nums=[2,3,2,3] non_val_last=1 runner=3
            runner += 1
        return non_val_last

    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
