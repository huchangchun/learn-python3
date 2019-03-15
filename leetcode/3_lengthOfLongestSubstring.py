class Solution:
    def lengthOfLongestSubstring(self, srcstr):
        """
        
        """
        
        s = [i for i in srcstr]
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
    