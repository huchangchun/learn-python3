#encoding=utf-8
"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: 3
Output: "III"
Example 2:

Input: 4
Output: "IV"
Example 3:

Input: 9
Output: "IX"
Example 4:

Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 5:

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

class Solution:
    #Runtime: 136 ms
    def intToRoman(self, num: 'int') -> 'str':
        result = ""
        if num < 1 or num > 3999:
            return result
        while num >= 1000:
            result += "M"
            num -= 1000
        if num >= 900:
            result += "CM"
            num -= 900
        if num >= 500:
            result += "D"
            num -= 500
        if num >= 400:
            result += "CD"
            num -= 400
        while num >= 100:
            result += "C"
            num -= 100
        if num >= 90:
            result += "XC"
            num -= 90
        if num >= 50:
            result += "L"
            num -= 50
        if num >= 40:
            result += "XL"
            num -= 40
        while num >= 10:
            result += "X"
            num -= 10
        if num >= 9:
            result += "IX"
            num -= 9
        if num >= 5:
            result += "V"
            num -= 5
        if num >= 4:
            result += "IV"
            num -= 4
        while num >= 1:
            result += "I"
            num -= 1
        return result    
    #Runtime: 140 ms
    #Memory Usage: 13.2 MB    
    def intToRoman1(self, x: int) -> str:
        """
        :type x: int
        :rtype :str
        """
        stoi = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        rstr:str = ""
        xlst = []
        i = 0
        while x:
            xlst.append(x % 10 * 10**i) 
            x = x // 10
            i +=1
        xlst = xlst[::-1]  
        itos = {v:k for k, v in stoi.items()}
        for i , val in enumerate(xlst):
            if val >= stoi["M"]:# [1000,]
                rstr += "M" * (val // (stoi["M"]))
                continue
            elif stoi["D"] <= val < stoi["M"]: # [500,1000)
                if val == stoi["M"] - stoi["C"]:#900
                    rstr += "C" + "M"
                    continue
                #[500,800]
                else:
                    rstr += "D" + "C" * ((val - stoi["D"])//(stoi["C"]))
                    continue
            elif stoi["C"] <= val < stoi["D"]:#[100,500)
                if val == stoi["D"] - stoi["C"]: #400
                    rstr += "C" + "D"
                    continue
                else: #[100,400)
                    rstr += "C" * (val // (stoi["C"]))
                    continue
            elif  stoi["L"] <= val < stoi["C"]: #[50,100)
                if val == stoi["C"] - stoi["X"]:# 90
                    rstr += "X" + "C"
                    continue
                else:#[50,80]
                    rstr += "L" + "X" *((val -stoi["L"])//(stoi["X"]))
                    continue
            elif stoi["X"] <= val < stoi["L"]: #[10,50)
                if val == stoi["L"] - stoi["X"]:#(40)
                    rstr += "X" + "L"
                    continue
                else:#[10,30)
                    rstr += "X" * (val // (stoi["X"]))
                    continue
            elif stoi["V"] <= val < stoi["X"]:#[5,10) 
                if val == stoi["X"] - stoi["I"]: #9
                    rstr += "I" + "X"
                    continue
                else:#[5,8)
                    rstr += "V" + "I" * ((val - stoi["V"]) // (stoi["I"]))
                    continue
            elif stoi["I"] <= val < stoi["V"]:#[1,5)
                if val == stoi["V"] - stoi["I"]:#4
                    rstr += "I" + "V"
                    continue
                else:
                    rstr += "I" * (val // (stoi["I"]))
                    continue
                          
        return rstr
    #Runtime: 144 ms, faster than 28.82% 
    def intToRoman3(self, num: int) -> str:
        stoi = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
        strlst = ["M","D","C","L","X","V","I"]
        rstr = ""

        for idx in [0,2,4]:
            k = num // (stoi[strlst[idx]])
            re = (num % stoi[strlst[idx]]) // (stoi[strlst[idx + 2]])
            rstr += k * strlst[idx]
            if re >= 9:
                rstr += strlst[idx + 2] + strlst[idx]
            elif 5 <= re:
                rstr += strlst[idx + 1] + (re - 5) * strlst[idx + 2]
            elif re == 4:
                rstr += strlst[idx + 2] + strlst[idx + 1]
            else :
                rstr += re * strlst[idx + 2]
            num %= (stoi[strlst[idx + 2]])
        return rstr
if __name__=="__main__":
    import time
    Test=Solution()
    #rt = time.time()
    #print(Test.intToRoman(1994) == "MCMXCIV")
    #print(Test.intToRoman(58) == "LVIII")
    #print(Test.intToRoman(9) == "IX")
    #print(Test.intToRoman(4) == "IV")
    #print(Test.intToRoman(3) == "III")
    #print(time.time()-rt)
    #rt2 = time.time()
    #print(Test.intToRoman1(1994) == "MCMXCIV")
    #print(Test.intToRoman1(58) == "LVIII")
    #print(Test.intToRoman1(9) == "IX")
    #print(Test.intToRoman1(4) == "IV")
    #print(Test.intToRoman1(3) == "III")  
    #print(time.time()-rt2)
    rt2 = time.time()
    #print(Test.intToRoman3(1994) == "MCMXCIV")
    print(Test.intToRoman3(3) == "III") 
    print(time.time()-rt2) 
    print(Test.intToRoman3(58) == "LVIII")
    #print(Test.intToRoman3(9) == "IX")
    #print(Test.intToRoman3(4) == "IV")
    #print(Test.intToRoman3(3) == "III")  
 