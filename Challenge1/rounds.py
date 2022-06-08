
from typing import Counter

class Solution(object):
    def minimumRounds(self, tasks):
        rounds = dict(Counter(tasks))
        result = 0
        for key, val in rounds.items():
            if val == 1:
                return -1
            result += (val // 3)
            rem = val % 3 
            if(rem != 0):
                result += 1
        
        return result