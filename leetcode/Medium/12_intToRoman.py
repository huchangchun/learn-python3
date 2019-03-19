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
     
    def intToRoman(self, x: int) -> str:
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
    
if __name__=="__main__":
    Test=Solution()
    print(Test.intToRoman(1994) == "MCMXCIV")
    print(Test.intToRoman(58) == "LVIII")
    print(Test.intToRoman(9) == "IX")
    print(Test.intToRoman(4) == "IV")
    print(Test.intToRoman(3) == "III")