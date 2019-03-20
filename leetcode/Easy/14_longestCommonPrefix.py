#encoding=utf-8
"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""
"""
思路分析：
1.确定题目是相同的最长的前缀
2.遍历列表，取出第一个，然后和其他项匹配，如果下一个和前一个不相同，说明没有共同项直接break
3.循环一遍没有break，则要匹配下一个字符，step+1,重新从列表第一个开始匹配，停止位也加1
4.如果没有循环完一遍，则i+1
5.如果长短不一的情况下，需要限制step的长度，不会超过其中最短的一项
"""
class Solution:
   
    #Runtime: 44 ms, faster than 45.92% 
    def longestCommonPrefix(self, strs: [str]) -> str:
        end = step = i = 0
        char =''
        if len(strs) == 0:
            return ''
    
        while i < len(strs) and step < len(strs[i]):
            if i == 0:
                char = strs[i][step]
            else:
                if char != strs[i][step]:
                    break
            if i == len(strs) - 1:
                step += 1
                i = 0
                end += 1
            else:
                i += 1
        return strs[i][:end]
            
if __name__=="__main__":
    s = ["Soluationasd","Solutiona","SolutionahaMostBest"]
    s2 = ["asd","cdf","hjk"]
    s3 = ["dog","racecar","car"]
    s4 = ["aa","aa"]    
    Test = Solution()
    print(Test.longestCommonPrefix(s))
    print(Test.longestCommonPrefix(s2))
    srt3 = Test.longestCommonPrefix(s3)
    print(Test.longestCommonPrefix(s4)=="aa")
    