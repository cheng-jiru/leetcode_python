# Author:chengjiru
# 2023年06月06日11时19分42秒
# Connect:jiru_cheng@163.com
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)[::-1] == str(x)