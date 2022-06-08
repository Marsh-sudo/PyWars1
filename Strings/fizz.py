class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ans = ""
        count = 0
        for i in s:
            if i not in ans:
                ans+=i
                
            else:
                ans = ans[ans.index(i) + 1:] +i
            count = max(count, len(ans))
            
        return count