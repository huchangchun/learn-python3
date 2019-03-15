#encoding=utf-8
class Solution:
    def twoSum(self,nums,target):
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
 
                
if __name__=="__main__":
    num = [1,3,1,5,6,13,64]
    target = 19
    Test = Solution()
    i,j = Test.twoSum(num, target)
    print("i:%d,j:%d"%(i,j))