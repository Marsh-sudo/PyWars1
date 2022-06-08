from typing import Counter

class Solution(object):
    def findLonely(self, nums):
        dic = Counter(nums)
        lon = []
        
        for i in nums:
            if (dic[i] > 1 or i+1 in dic or i-1 in dic):
                pass
            else:
                lon.append(i)
                
        return lon