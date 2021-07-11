#---------------------------------------------------------------------------
"""3. Longest Substring Without Repeating Characters: Given a string s, 
find the length of the longest substring without repeating characters.
."""
#---------------------------------------------------------------------------
class Solution:
    def lengthOfLongestSubstring(self, str1):
        self.str1 = str1  
        if str1 == 0:
            return 0
        i, j, slen = 0, 0, 0
        unique_elements = set()
        while j < len(str1):
            if str1[j] not in unique_elements:
                unique_elements.add(str1[j])
                j += 1
                slen = max(slen, len(unique_elements))
            else:
                unique_elements.remove(str1[i])
                i += 1
        return slen
#---------------------------------------------------------------------------
if __name__ == '__main__':
    inst3 = Solution()
    str1 = "abcabcbb"  
    print(inst3.lengthOfLongestSubstring(str1))
#---------------------------------------------------------------------------
# Location: cd /home/alem/0_Alem/alemprojects/FinalNotes/4_Algorithms/LeetCode/
#---------------------------------------------------------------------------