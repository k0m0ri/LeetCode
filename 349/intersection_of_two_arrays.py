class Solution:
    # return array of items which appear in both num1 and num2
    # pre: num1=[1,2,2,1], num2=[2,2]
    # post: result=[2]
    def intersection(self, nums1, nums2):

        map = {}
        # testcase: num1=[1,2,2,1], num2=[2,2], map={(1,1), (2,1)}
        for num in nums1:
            if not num in map:
                map[num] = 1

        # testcase: num2=[2,2], map={(1,1), (2,0)}
        for num in nums2:
            if num in map:
                map[num] = 0

        result = []
        # testcase: map={(1,1), (2,0)}, result=[]
        for key, val in map.items():
            if val == 0:
                # testcase: map={(1,1), (2,0)}, result=[2]
                result.append(key)

        return result
