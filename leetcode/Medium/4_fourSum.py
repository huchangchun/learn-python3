#encoding=utf-8
"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
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
 
    #1172 ms, faster than 21.72% of Python3
    @SolutionTiming.timeit(level=1, prefix="[API] ")
    def fourSum1(self, nums: [int], target:int) -> [[int]]:
        lst = []
        nums = sorted(nums)
        print(nums)
        for i in range(len(nums)):
            if i>0  and nums[i]==nums[i-1]:#表示i和上一次的相同则要跳过
                continue    
            j = i + 1
            for j in range(i+1, len(nums)):   
                if j > i + 1 and nums[j] == nums[j-1]:#表示j和上一次的相同，则要跳过
                    continue
                left = j + 1
                right = len(nums)-1
                while left < right:
                    curSum = nums[left] +  nums[right] + nums[j]
                    curTarget = target - nums[i]
                    if curSum == curTarget:
                        print("i=:%d,j=:%d->"%(i,j),end="")
                        print([nums[i],nums[j],nums[left],nums[right]])
                        lst.append([nums[i],nums[j],nums[left],nums[right]])
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
                j += 1
        return lst 
     #136 ms, faster than 76.61%
    @SolutionTiming.timeit(level=1, prefix="[API] ")
    def fourSum(self, nums, target):
        res = []
        nums.sort()
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            if nums[i] + nums[-1] + nums[-2] + nums[-3] < target:
                continue
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[-1] + nums[-2] < target:
                    continue
                l = j+1
                r = len(nums)-1
                while l < r:
                    addition = nums[i] + nums[j] + nums[l] + nums[r]
                    numsL = [nums[i], nums[j], nums[l], nums[r]]
                    if addition == target:
                        res.append(numsL)
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                    elif addition > target:
                        r -= 1
                    else:
                        l += 1
        return res
    
if __name__=="__main__":
    nums = [1, 0, -1, 0, -2, 2]
    nums2 = [1,0,0,0,0,-1,-2,2]
    Test = Solution()
    print(Test.fourSum1(nums2,0))
    print(Test.fourSum(nums2,0))
    Test.SolutionTiming.show_timing_log()
    
  
