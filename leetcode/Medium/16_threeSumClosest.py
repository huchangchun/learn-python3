#encoding=utf-8
"""
Given an array nums of n integers and an integer target, 
find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
import os
import sys
import math
root_path = os.path.abspath("../../")
if root_path not in sys.path:
    sys.path.append(root_path)
from timeopt.Timing import Timing
class Solution:
    SolutionTiming = Timing()
    @SolutionTiming.timeit(level=1, prefix="[API] ")
    def threeSum(self, nums: int) -> [[int]]:
        lst = []
        target = 0
        nums = sorted(nums)
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                curSum = nums[left] +  nums[right]
                curTarget = target - nums[i]
                if curSum == curTarget:
                    lst.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while left < len(nums)-1 and (nums[left] == nums[left-1]):
                        left +=1
                    while right > 0 and nums[right]==nums[right+1]:
                        right -=1
                elif curSum < curTarget:
                    left += 1
                else:
                    right -= 1
    
        return lst   
   
 
    @SolutionTiming.timeit(level=1)
    #Runtime: 88 ms, faster than 92.65% of Python3
    def threeSumClosest(self, nums: [int], target: int) -> int:

        nums = sorted(nums)
        import math
        minest = math.inf
        ret = 0
        for i  in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums) - 1
            while left < right:
                curSum = nums[left] + nums[right] + nums[i]
                margin = target-curSum
                if margin == 0:
                    return curSum
                if margin > 0:
                    left += 1
                else:
                    right -= 1
                if abs(margin)< minest:
                    minest = abs(margin)
                    ret = curSum

        return ret
    
if __name__=="__main__":
    nums = [-1, 2, 1, -4]
    Test = Solution()
    print(Test.threeSumClosest(nums,1)==2)
    print(Test.threeSumClosest([0,0,0],1)==0)
 
     
  
