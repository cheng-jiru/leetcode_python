# Author:chengjiru
# 2023年06月06日11时17分15秒
# Connect:jiru_cheng@163.com
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            sub = target - nums[i]
            if sub in nums[i + 1:]:
                return [i, nums[i + 1:].index(sub) + i + 1]