# Author:chengjiru
# 2023年06月06日17时24分11秒
# Connect:jiru_cheng@163.com
class Solution:
    def addBinary(self, a, b) -> str:
        return "{0:b}".format(int(b,2)+int(a,2))
