#encoding=utf-8
"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
"""
class Solution:
    #64 ms, faster than 64.97% of Python3
    def removeDuplicates(self, nums: [int]) -> int:
        step = end =  0
        j = len(nums)
        if len(nums) <=1:
            return len(nums)
        while step < j:
            if nums[step] != nums[end]:
                nums[end+1] = nums[step]
                end += 1
            step += 1
        print(nums[:end+1])
        return end + 1
        
if __name__=="__main__":
    l1 = [1,1,2]
    l2 = [0,0,1,1,1,2,2,3,3,4]
    Test = Solution()
    print(Test.removeDuplicates(l1))
    print(Test.removeDuplicates(l2))