#encoding=utf-8
"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
"""
P_MAX = 2 ** 31 -1
N_MAX = -2 ** 31 
class Solution:
    # 52 ms, faster than 83.97%
    def reverse(self, x:int) -> int:
        """
        :type x:int
        :rtype :int
        """
        rev = 0
        sign = False
        if x < 0:
            sign = True
            x = -1 * x  
        while x:
            rev = rev * 10 + x % 10 
            x = x // 10
            if sign:
                if -1 * rev < N_MAX:
                    return 0
            else:
                if rev > P_MAX:
                    return 0
        if sign:
            rev *= -1
        return rev
    #56 ms, faster than 62.99%
    def reverse(self, x:int) -> int:
        """
        :type x:int
        :rtype :int
        """
        rev = 0
        sign = x < 0 and -1 or 1
        x = abs(x)
        while x:
            rev = rev * 10 + x % 10 
            x //= 10

        return sign * rev if rev <= P_MAX else 0 
    #shoter code version : 64 ms, faster than 30.87% 
    def reverse1(self, x: int) -> int:
        """
        :type x:int
        :rtype :int
        """
        sign = x < 0 and -1 or 1
        x = abs(x)
        rev = 0
        while x:
            rev = rev*10 + x % 10
            x  //= 10
        return sign * rev if rev <= 0x7fffffff else 0
            
if __name__ == "__main__":
    Test = Solution()
    print(Test.reverse1(123))
    print(Test.reverse(2147483649))
    print(Test.reverse(-1234))
    