class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        temp = []
        for i in range(n):
            if nums[i] not in temp:
                temp.append(nums[i])
            else:
                return True
        return False