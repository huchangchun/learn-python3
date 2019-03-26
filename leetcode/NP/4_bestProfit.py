#encoding=utf-8
"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
注意你不能在买入股票前卖出股票。
示例 1：

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。 
"""
class Solution:
    def bestProfit_recurve(self, prices: [int]) -> int:
        if len(prices) < 2:
            return 0
        return max(prices[-1] - min(prices[:-1]),self.bestProfit_recurve(prices[:-1]))
    def bestProfit_np(self, prices: [int]) -> int:
        if len(prices) < 2:
            return 0
        result = [0]
        minPrice = prices[0] #初始化一个最小值
        for i in range(1, len(prices)):
            minPrice = min(minPrice,prices[i - 1]) #从0开始记录和第i-1个比较后的最小值，然后第i个值减去最小值得到一个当前的最大值，和数组中的比较得到最大值
            result.append(max(prices[i] - minPrice,result[i - 1]))
        return result[-1]
if __name__ =="__main__":
    Test = Solution()
    lst = [7,1,5,3,6,4]
    print(Test.bestProfit_recurve(lst))
    print(Test.bestProfit_np(lst))