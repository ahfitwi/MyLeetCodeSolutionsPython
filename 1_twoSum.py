#---------------------------------------------------------------------------
"""1. **Two Sum**: Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.You may 
assume that each input would have exactly one solution, and you may not 
use the same element twice. You can return the answer in any order."""
#---------------------------------------------------------------------------
class Solution:    
    def twoSum(self, nums, target):       
        paired = dict(((v, i) for i, v in enumerate(nums)))
        return next(( (i, paired.get(target-v)) 
            for i, v in enumerate(nums) 
                if paired.get(target-v, i) != i), None)

#---------------------------------------------------------------------------
if __name__ == '__main__':
    inst1 = Solution()
    nums, target = (6, 7, 11, 15, 3, 6, 5, 3), 6
    print(inst1.twoSum(nums, target))
#---------------------------------------------------------------------------
# Location: cd /home/alem/0_Alem/alemprojects/FinalNotes/4_Algorithms/LeetCode/