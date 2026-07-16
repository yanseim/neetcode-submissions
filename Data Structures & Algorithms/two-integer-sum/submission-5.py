class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # A, B = dict(), dict()
        # for i,v in enumerate(nums):
        #     A[i]=v
        #     B[target-v]=i
        # for i in range(len(nums)):
        #     if B[target-A[i]]:
        #         return [min(i,B[target-A[i]]),max(i,B[target-A[i]])]
        
        indices = {}  # val -> index

        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        return []