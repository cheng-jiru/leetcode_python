# Author:chengjiru
# 2023年06月06日15时48分58秒
# Connect:jiru_cheng@163.com

class Solution:
    def removeDuplicates(self, nums):
        slow, fast = 0, 1
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1



