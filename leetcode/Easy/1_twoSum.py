#encoding=utf-8

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""
class Solution:
    #Accepted exactly one solution
    def twoSum(self, nums: [int], target: int) -> [int]:
        """       
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dic = {}
        for idx,num in enumerate(nums):
            if num in dic:
                return (dic[num],idx)
            else:
                dic[target - num] = idx
                
    def twoSum2(self, nums, target):
        for i in range(0,len(lst)):
            for j in range(i,len(lst)):
                if i != j:      
                    if target == lst[i] + lst[j]:
                        return i,j            
    
    def twoSum3(self, nums, target) -> [[int]]:
        nums = sorted(nums)
        left = 0
        right = len(nums)-1
        lst = []
        while left < right:
            if nums[left] + nums[right] == target:
                lst.append([nums[left],nums[right]])
                left += 1
                right -= 1
                
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
        return lst
                             
if __name__=="__main__":
    num = [1,3,2,1,4,5,6,8,13,64]
    target = 19
    Test = Solution()
    i,j = Test.twoSum(num, target)
    print("i:%d,j:%d"%(i,j))
    print(Test.twoSum3(num, 8))