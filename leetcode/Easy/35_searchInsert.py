#encoding=utf-8
"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0's indexOf().
"""
class Solution:
    
    def searchInsert(self, nums: [int], target: int) -> int:
        if len(nums) == 0:
            return -1
        i = 0
        while i < len(nums):
            if  target <= nums[i]:
                return i
            i += 1
        return i
    
    #this version time Limit Exceeded
    def searchInsert1(self, nums: [int], target: int) -> int:
    
        low = 0
        high = len(nums)
        while low < high:
            mid = int(low + (high - low)/2)
            if target < nums[mid]:
                high = mid
            elif target > nums[mid]:
                low = mid
            else:
                return mid
           
        return low
       
   
if __name__=="__main__":
    Test = Solution()
    lst = [1,3,5,6,8]
    print(Test.searchInsert(lst, 5) == 2)
    print(Test.searchInsert(lst, 2) == 1)
    print(Test.searchInsert(lst, 7) == 4)
    print(Test.searchInsert(lst, 0) == 0)
