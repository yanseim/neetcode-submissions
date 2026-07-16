import numpy as np

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tmp = np.sort(nums)
        if len(tmp)==1:
            return False
        for i in range(len(tmp)-1):
            if tmp[i]==tmp[i+1]:
                return True
        return False