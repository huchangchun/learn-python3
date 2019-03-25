#encoding=utf-8
"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""
class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        isOdd  = False
        if (len(nums1) +  len(nums2)) % 2 == 1:
            isOdd = True
        mid = int ((len(nums1) +  len(nums2)) / 2)   

        mergelst = []
        i = j = idx = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                mergelst.append(nums1[i])
                i += 1
            else:
                mergelst.append(nums2[j])
                j += 1

            if idx  >= mid:
                if isOdd:
                    return mergelst[idx]
                else:
                    return (mergelst[idx - 1] + mergelst[idx])/2
            idx += 1  
        if i < len(nums1):
            for k in range(i,len(nums1)):
                mergelst.append(nums1[k])
                if idx  >= mid:
                    if isOdd:
                        return mergelst[idx]
                    else:
                        return (mergelst[idx - 1] + mergelst[idx])/2                
                idx += 1
        if j < len(nums2):
            for k in range(j,len(nums2)):
                mergelst.append(nums2[k])
                if idx  >= mid:
                    if isOdd:
                        return mergelst[idx]
                    else:
                        return (mergelst[idx - 1] + mergelst[idx])/2                
                idx += 1 
if __name__=="__main__":
    nums1 = [1,2]
    nums2 = [3,4]
    Test = Solution()
    print(Test.findMedianSortedArrays(nums1, nums2))
    nums1 = [1,3,5,7]
    nums2 = [2,4,6,8]    
    print(Test.findMedianSortedArrays(nums1, nums2))
    