"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
 
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0 
        d = {}
        start = 0
        for i in range(len(s)):
            if s[i] in d and d[s[i]] >= start:
                #start 移动
                start = d[s[i]] + 1
            #start移动了要加回来
            tmplen = i + 1 - start
            if tmplen > maxlen:
                maxlen = tmplen
            d[s[i]] = i
            
        return maxlen


if __name__== "__main__":
    strlst1 = "aa"
    strlst2 = "pwwkew"
    strlst3 = "abcabcbb"
    Test = Solution()
    
    print(Test.lengthOfLongestSubstring(strlst1))
    print(Test.lengthOfLongestSubstring(strlst2))
    print(Test.lengthOfLongestSubstring(strlst3))
    