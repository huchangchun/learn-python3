#encoding=utf-8
"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.
从1开始报数，1个1：11
第二个人总结第1个人的报数一共2个1：21
第三个人总结第二个人的报数，1个2，一个1：1211
第四个人总结第三个人报数，1个1，1个2,两个1：111221
...到第n个
两层循环:
第一层循环从1开始报数到第n个人
  第二层循环：
     总结上一个人的数
  总结第二层循环中最后一个数的个数加到总数中  
"""
class Solution:
    
    def countAndSay(self, n):
        
        rstr = '1'
        for i in range(n - 1):
            res=''
            pre = rstr[0]
            count = 0
            for j in range(len(rstr)):
                if pre == rstr[j]:
                    count += 1
                else:
                    res += str(count) + pre
                    count = 1
                    pre = rstr[j]
            rstr = res + str(count) + pre
            
        return rstr
    
       
   
if __name__=="__main__":
    Test = Solution()
    print(Test.countAndSay(1))
    print(Test.countAndSay(2))
    print(Test.countAndSay(3))
    print(Test.countAndSay(4))
    print(Test.countAndSay(5))
    print(Test.countAndSay(6))
    print(Test.countAndSay(7))
    
