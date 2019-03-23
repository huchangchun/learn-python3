#encoding=utf-8
"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        
        i = 0
        j = 0
        step = 0
        lengthOfNeedle = len(needle)
        while i < len(haystack):
            if haystack[i] == needle[j]:    
                j += 1
            else:
                i = i - j
                j = 0
            if j == lengthOfNeedle:
                return i - j + 1
            i += 1
        return -1
if __name__=="__main__":
    Test = Solution()
    haystack='helillo'
    needle='ll'
    print(Test.strStr(haystack, needle)==4)
    haystack = 'aaaaa'
    needle = 'bba'
    print(Test.strStr(haystack, needle)==-1)    
    haystack = 'mississippi'
    needle = 'issip'
    needle2 = 'issi'
    print(Test.strStr(haystack, needle)==4)
    print(Test.strStr(haystack, needle2)==1)
    print("finish")
    