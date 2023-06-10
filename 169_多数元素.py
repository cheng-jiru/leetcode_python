# Author:chengjiru
# 2023年06月09日19时27分12秒
# Connect:jiru_cheng@163.com

class Solution:
    def majorityElement(self, nums) -> int:
        leader = 0
        count = 0
        for i in nums:
            if count == 0:
                leader = i
            if leader == i:
                count += 1
            else:
                count -= 1
        return leader

if __name__ =="__main__":
    list_1=[1,2,3,1,1,1,1]
    a=Solution()
    print(a.majorityElement(list_1))
