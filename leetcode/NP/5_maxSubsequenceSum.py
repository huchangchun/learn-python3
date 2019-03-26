#encoding=utf-8
"""
 
"""
class Solution:
    def maxSubsequenceSum1(self, nums: [int]) -> int:
        maxSum = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                thisSum = 0
                for k in range(i,j+1):
                    thisSum += nums[k]
                if thisSum > maxSum:
                    maxSum = thisSum
        return maxSum
    
    def maxSubsequenceSum2(self, nums: [int]) -> int:
        maxSum = 0
        for i in range(len(nums)):
            thisSum = 0
            for j in range(i, len(nums)):
                thisSum += nums[j]
            if thisSum > maxSum:
                maxSum = thisSum
        return maxSum
    
    def maxSubsequenceSum(self, nums: [int]) -> int:
        maxSum = thisSum = 0
        for i in range(len(nums)):
            thisSum += nums[i]
            if thisSum > maxSum:
                maxSum = thisSum
            elif thisSum < 0:
                thisSum = 0
        return maxSum
    def maxSubsequenceSum_np(self, nums: [int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i] + nums[i - 1], nums[i])
        print(nums)
        return max(nums)
if __name__ =="__main__":
    Test = Solution()
    lst = [-2, 11, 8, -4, -1, 16, 5, 0]
    print(Test.maxSubsequenceSum(lst))
    #print(Test.maxSubsequenceSum2(lst))
    #print(Test.maxSubsequenceSum1(lst))
    print(Test.maxSubsequenceSum_np(lst))
    