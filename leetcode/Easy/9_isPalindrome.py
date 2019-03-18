#encoding=utf-8
"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        :type x: int
        :rtype :bool
        """
        if x < 0:
            return False
        rev = 0
        origin = x
        while x:
            rev = rev * 10 + x % 10
            x //=10
        return True if rev==origin else False
if __name__=="__main__":
    Test = Solution()
    print(Test.isPalindrome(12321))
    print(Test.isPalindrome(-12321))
    print(Test.isPalindrome(123))
    