#---------------------------------------------------------------------------
"""4. Median of Two Sorted Arrays: Given two sorted arrays nums1 and nums2 
of size m and n respectively, return the median of the two sorted arrays. 
The overall run time complexity should be O(log (m+n)).
."""
#---------------------------------------------------------------------------
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        nums = nums1 + nums2
        nums.sort()
        if len(nums)%2 == 1:
            return nums[len(nums)//2]
        else:
            return (nums[len(nums)//2-1]+nums[len(nums)//2])/2
#---------------------------------------------------------------------------
if __name__ == '__main__':
    inst4 = Solution()
    nums1 = [1,3]
    nums2 = [2] 
    print(inst4.findMedianSortedArrays(nums1, nums2))
#---------------------------------------------------------------------------
# Location: cd /home/alem/0_Alem/alemprojects/FinalNotes/4_Algorithms/LeetCode/
#---------------------------------------------------------------------------