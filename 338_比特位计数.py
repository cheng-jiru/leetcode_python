# Author:chengjiru
# 2023年06月06日17时08分23秒
# Connect:jiru_cheng@163.com
class Solution:
    def countBits(self, n):
        list_1 = []
        for i in range(0, n + 1):
            num = bin(i).count("1")
            list_1.append(num)
        return list_1
