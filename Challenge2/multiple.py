class Solution(object):
    def intersection(self, nums):
        d={}
        for i in nums:
            for j in i:
                if j not in d:
                    d[j]=1
                else:
                    d[j]+=1
        
        l = []
        ln = len(nums)
        for key,value in d.items():
            if value == ln:
                l.append(key)
        l.sort()
        return l