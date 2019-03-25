#encoding=utf-8
"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""
class Solution:
   
   
    def longestPalindrome(self, s: str) -> str:
        """
        type s: str
        rtype : str 
        
        """
        maxlen = 0
        rstr = ''
        
        i = j = 0
        while i < len(s):
            if i == 0:
                rstr = s[i]
                tmplen = 1
            else:
                k = 1
                tmplen = 1
                tmpstr = s[i]
                while k <= i and i + k < len(s):
                    
                    if s[i] == s[i - k]:
                        tmplen += 1
                        tmpstr += tmpstr                        
                    if s[i] == s[i + k]:
                        tmplen += 1
                        tmpstr += tmpstr
                    elif s[i - k] == s[i + k]:
                        tmplen += 1
                        continue
                    else:
                        break 
                tmplen = 2 * k - 1           
                if tmplen > maxlen:
                    maxlen = tmplen
                    rstr = s[i + 1 - k:i + k] 
            i += 1
        return rstr
if __name__=="__main__":
    
    Test = Solution()
    s = "babad"
    s2 = "asdsaafdfndnfd"
    s3 = 'cbbd'
    print(Test.longestPalindrome(s))
    print(Test.longestPalindrome(s2))
    print(Test.longestPalindrome(s3))
  
