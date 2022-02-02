class Solution:
    # reverse chars[] in place
    # pre: s[h,e,l,l,o]
    # post: s[o,l,l,e,h]
    def reverseString(self, s):

        if len(s) == 1:
            return s

        front = 0
        end = len(s) - 1
        # testcase: "hello" front=0, end=4, tmp=h
        # testcase: "oellh" front=1, end=3, tmp=e
        # testcase: "olleh" front=2, end=2, tmp=l
        while front < end:
            tmp = s[front]
            s[front] = s[end]
            s[end] = tmp
            front += 1
            end -= 1

        return s
