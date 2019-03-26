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

manacher:
  时间要比np慢很多，自己开始做的时候没有加入“#”,在“cbbd"这种情况就有问题了，后面将原字符串加入#，隔开“cbbd"中的bb这种，
  使得所有的字符串都可以用中心扩散法来计算最大回文
NP:
  基本思路是对任意字符串，如果头和尾相同，那么它的最长回文子串一定是去头去尾之后的部分的最长回文子串加上头和尾
  如果头和尾不同，那么它的最长回文子串是去头的部分的最长回文子串和去尾的部分的最长回文子串的较长的那一个
   
"""
import os
import sys
root_path = os.path.abspath("../../")
if root_path not in sys.path:
    sys.path.append(root_path)
from timeopt.Timing import Timing
class Solution:
    SolutionTiming = Timing()
    #manacher
    @SolutionTiming.timeit(level=1, prefix="[API] ")
    def longestPalindrome_manacher(self, s: str) -> str:
        """
        type s: str
        rtype : str 
        
        """
        jen = 0
        rstr = ''
        s = '#' + '#'.join(s) + '#'
        i = j = 0
        tmplen = 0
        start = 0
        end = 0
        for i in range(len(s)):
            if i == 0:
                start = 0
                end = start + 1
                tmplen = 1
            else:
                k = 1 
                while k <= i and i + k < len(s) and s[i - k] == s[i + k]:
                    k += 1
                tmplen = 2 * k - 1           
                if tmplen > jen:
                    jen = tmplen
                    start = i + 1 - k
                    end =i + k 
        ret = ''
        while start < end:
            if s[start] != "#":
                ret += s[start]
            start += 1
        return ret
    @SolutionTiming.timeit(level=1, prefix="[API] ")
    #Faster Version: 68 ms, faster than 98.97%,
    def longestPalindrome_np(self, s: str) -> str:
        n = len(s)
        j = 0
        start = 0
        for i in range(n):
            if i-j >= 1 and s[i-j-1:i+1] == s[i-j-1:i+1][::-1]:
                start = i - j - 1
                j += 2
                continue
            if i - j >= 0 and s[i-j: i+1] == s[i-j:i+1][::-1]:
                start = i - j
                j += 1
        return s[start : start + j]
    @SolutionTiming.timeit(level=1, prefix="[API] ")
    #shorter Verison faster than 20.81% 
    def longestPalindrome_np2(self, s: str) -> str:
        """
        状态dp[j][i]表示索引j到索引i的子串是否是回文串：
        dp[j][i] = {true , j = i; #只有1个的情况
                    str[i] == str[j] ,i-j=1 #相邻的情况"bb"
                    str[i] == str[j], &&dp[j+1][i-1], i-j > 1 #头尾相同，且中间部分是回文的情况 i-j>1 
                    }
        """
        jen = 1
        start = 0
        end = 0
        k = len(s)
        dp = [[0 for i in range(k)] for i in range(k)]
        
        for i in range(k): #i表示回文子串的尾部索引
            for j in range(i+1):#j表示回文子串的头部索引
                if i - j <= 1: #相邻的情况
                    dp[j][i] = 1 if s[i]==s[j] else 0
                    
                else: #如果头尾间隔大于1且字符相同，且中间部分为回文，d[j][i]也为回文  
                    dp[j][i] = 1 if s[i]==s[j] and dp[j+1][i-1] else 0
                    
                #如果[j,i]为回文，回文长度为i - j + 1,start = j,end = i + 1，子串为s[start:end](切片为左开右闭区间)
                if dp[j][i] and jen <= i - j + 1:
                    jen = i - j + 1
                    start = j
                    end = i + 1
        print(dp)
        return s[start: end]       
        
                
                
if __name__=="__main__":
    
    Test = Solution()
    s = "ababasdfad"
    s2 = "asdsadfndnfd"
    s3 = 'dsfsdhadhfkdsdsfsdhadhdsfsdhadhfkddsfsdhadhfkdsahfksadhdsfsdhadhfkdsahfksadhfksddsfsdhadhfkdsahfksadhfksdhfusdihfksjadfhksadjkdsahfdsjkhfksdhffhiawoeuruihweiyrtiuoncsdbfzmbfkhfioaewncfhskdsfsdhadhfkdsahfksadhfksdhfusdihfksjadfhksadjkdsahfdsjkhfksdhffhiawoeuruihweiyrtiuoncsdbfzmbfkhfioaewncfhskhfusdihfksjadfhksadjkdsahfdsjkhfksdhffhiawoeuruihweiyrtiuoncsdbfzmbfkhfioaewncfhskdsfsdhadhfkdsahfksadhfksdhfusdihfksjadfhksadjkdsahfdsjkhfksdhffhiawoeuruihweiyrtiuoncsdbfzmbfkhfioaewncfhskdsfsdhadhfkdsahfksadhfksdhfusdihfksjadfhksadjkdsahfdsjkhfksdhffhiawoeuruihweiyrtiuoncsdbfzmbfkhfioaewncfhskdsfsdhadhfkdsahfksadhfksdhfusdihfksjadsfsdhadhfkdsahfksadhfksdhfusdihfksjadfhksadjkdsahfdsjkhfksdhffhiawoeuruihweiyrtiuoncsdbfzmbfkhfioaewncfhskdsfsdhadhfkdsahfksadhfksdhfusdihfksjadfhksadjkdsahfdsjkhfksdhffhiawoeuruihweiyrtiuoncsdbfzmbfkhfioaewncfhskdfhksadjkdsahfdsjkhfksdhffhiawoeuruihweiyrtiuoncsdbfzmbfkhfioaewncfhskfdsfsdhadhfkdsahfksadhfksdhfusdihfksjadfhksadjkdsahfdsjkhfksdhffhiawoeuruihweiyrtiuoncsdbfzmbfkhfioaewncfhskksdhfusdihfksjadfhksadjkdsahfdsjkhfksdhffhiawoeuruihweiyrtiuoncsdbfzmbfkhfioaewncfhsksahfksadhfksdhfusdihfksjadfhksadjkdsahfdsjkhfksdhffhiawoeuruihweiyrtiuoncsdbfzmbfkhfioaewncfhskfkdsahfksadhfksdhfusdihfksjadfhksadjkdsahfdsjkhfksdhffhiawoeuruihweiyrtiuodsfsdhadhfkdsdsfsdhadhdsfsdhadhfkddsfsdhadhfkdsahfksadhdsfsdhadhfkdsahfksadhfksddsfsdhadhfkdsahfksadhfksdhfusdihfksjadfhksadjkdsahfdsjkhfksdhffhiawoeuruihweiyrtiuoncsdbfzmbfkhfioaewncfhskdsfsdhadhfkdsahfksadhfksdhfusdihfksjadfhksadjkdsahfdsjkhfksdhffhiawoeuruihweiyrtiuoncsdbfzmbfkhfioaewncfhskhfusdihfksjadfhksadjkdsahfdsjkhfksdhffhiawoeuruihweiyrtiuoncsdbfzmbfkhfioaewncfhskdsfsdhadhfkdsahfksadhfksdhfusdihfksjadfhksadjkdsahfdsjkhfksdhffhiawoeuruihweiyrtiuoncsdbfzmbfkhfioaewncfhskdsfsdhadhfkdsahfksadhfksdhfusdihfksjadfhksadjkdsahfdsjkhfksdhffhiawoeuruihweiyrtiuoncsdbfzmbfkhfioaewncfhskdsfsdhadhfkdsahfksadhfksdhfusdihfksjadsfsdhadhfkdsahfksadhfksdhfusdihfksjadfhksadjkdsahfdsjkhfksdhffhiawoeuruihweiyrtiuoncsdbfzmbfkhfioaewncfhskdsfsdhadhfkdsahfksadhfksdhfusdihfksjadfhksadjkdsahfdsjkhfksdhffhiawoeuruihweiyrtiuoncsdbfzmbfkhfioaewncfhskdfhksadjkdsahfdsjkhfksdhffhiawoeuruihweiyrtiuoncsdbfzmbfkhfioaewncfhskfdsfsdhadhfkdsahfksadhfksdhfusdihfksjadfhksadjkdsahfdsjkhfksdhffhiawoeuruihweiyrtiuoncsdbfzmbfkhfioaewncfhskksdhfusdihfksjadfhksadjkdsahfdsjkhfksdhffhiawoeuruihweiyrtiuoncsdbfzmbfkhfioaewncfhsksahfksadhfksdhfusdihfksjadfhksadjkdsahfdsjkhfksdhffhiawoeuruihweiyrtiuoncsdbfzmbfkhfioaewncfhskfkdsahfksadhfksdhfusdihfksjadfhksadjkdsahfdsjkhfksdhffhiawoeuruihweiyrtiuoncsdbfzmbfkdsfsdhadhfkdsdsfsdhadhdsfsdhadhfkddsfsdhadhfkdsahfksadhdsfsdhadhfkdsahfksadhfksddsfsdhadhfkdsahfksadhfksdhfusdihfksjadfhksadjkdsahfdsjkhfksdhffhiawoeuruihweiyrtiuoncsdbfzmbfkhfioaewncfhskdsfsdhadhfkdsahfksadhfksdhfusdihfksjadfhksadjkdsahfdsjkhfksdhffhiawoeuruihweiyrtiuoncsdbfzmbfkhfioaewncfhskhfusdihfksjadfhksadjkdsahfdsjkhfksdhffhiawoeuruihweiyrtiuoncsdbfzmbfkhfioaewncfhskdsfsdhadhfkdsahfksadhfksdhfusdihfksjadfhksadjkdsahfdsjkhfksdhffhiawoeuruihweiyrtiuoncsdbfzmbfkhfioaewncfhskdsfsdhadhfkdsahfksadhfksdhfusdihfksjadfhksadjkdsahfdsjkhfksdhffhiawoeuruihweiyrtiuoncsdbfzmbfkhfioaewncfhskdsfsdhadhfkdsahfksadhfksdhfusdihfksjadsfsdhadhfkdsahfksadhfksdhfusdihfksjadfhksadjkdsahfdsjkhfksdhffhiawoeuruihweiyrtiuoncsdbfzmbfkhfioaewncfhskdsfsdhadhfkdsahfksadhfksdhfusdihfksjadfhksadjkdsahfdsjkhfksdhffhiawoeuruihweiyrtiuoncsdbfzmbfkhfioaewncfhskdfhksadjkdsahfdsjkhfksdhffhiawoeuruihweiyrtiuoncsdbfzmbfkhfioaewncfhskfdsfsdhadhfkdsahfksadhfksdhfusdihfksjadfhksadjkdsahfdsjkhfksdhffhiawoeuruihweiyrtiuoncsdbfzmbfkhfioaewncfhskksdhfusdihfksjadfhksadjkdsahfdsjkhfksdhffhiawoeuruihweiyrtiuoncsdbfzmbfkhfioaewncfhsksahfksadhfksdhfusdihfksjadfhksadjkdsahfdsjkhfksdhffhiawoeuruihweiyrtiuoncsdbfzmbfkhfioaewncfhskfkdsahfksadhfksdhfusdihfksjadfhksadjkdsahfdsjkhfksdhffhiawoeuruihweiyrtiuoncsdbfzmbfkhfioaewncfhskahfksadhfksdhfusdihfksjadfhksadjkdsahfdsjkhfksdhffhiawoeuruihweiyrtiuoncsdbfzmbfkhfioaewncfhskhfioaewncfhskahfksadhfksdhfusdihfksjadfhksadjkdsahfdsjkhfksdhffhiawoeuruihweiyrtiuoncsdbfzmbfkhfioaewncfhskncsdbfzmbfkhfioaewncfhskahfksadhfksdhfusdihfksjadfhksadjkdsahfdsjkhfksdhffhiawoeuruihweiyrtiuoncsdbfzmbfkhfioaewncfhsk'

 
    print(Test.longestPalindrome_manacher(s))
    print(Test.longestPalindrome_np(s))
    print(Test.longestPalindrome_np2(s))
    print(Test.longestPalindrome_manacher(s2))
    print(Test.longestPalindrome_np(s2))
    print(Test.longestPalindrome_np2(s2))
    print(Test.longestPalindrome_manacher(s3))    
    print(Test.longestPalindrome_np2(s3))
    Test.SolutionTiming.show_timing_log()
    """
    ==============================================================================================================
    Timing log
    --------------------------------------------------------------------------------------------------------------
              Solution                    [API]         longestPalindrome_np :           0.0 s (Call Time:      2)
              Solution                    [API]        longestPalindrome_np2 :      14.18881 s (Call Time:      3)
              Solution                    [API]   longestPalindrome_manacher :    0.02500153 s (Call Time:      3)
    --------------------------------------------------------------------------------------------------------------
    """
  
