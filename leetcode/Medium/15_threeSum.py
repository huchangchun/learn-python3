#encoding=utf-8
"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
import os
import sys
root_path = os.path.abspath("../../")
if root_path not in sys.path:
    sys.path.append(root_path)
from timeopt.Timing import Timing
class Solution:
    SolutionTiming = Timing()
 
    @SolutionTiming.timeit(level=1, prefix="[API] ")
    #time exceed
    def threeSum(self, nums: int) -> [[int]]:
        lst = []
        uniqueset= set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if k > j >i and nums[i]+nums[j]+nums[k] == 0:
                        tmplist = [nums[i],nums[j],nums[k]]
                        if frozenset(tmplist) not in uniqueset:
                            uniqueset.add(frozenset(tmplist))
                            lst.append(tmplist)
                       
        return lst
if __name__=="__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    Test = Solution()
    print(Test.threeSum(nums))
    Test.SolutionTiming.show_timing_log()
     
  
