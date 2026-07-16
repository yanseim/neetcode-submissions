class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        S = []
        for index,num in enumerate(nums):# 注意enu语法！先index再内容！
            S.append([num,index])
        
        S.sort()

        i,j = 0,len(nums)-1
        # while i<j:
        #     if S[i][0]+S[j][0]<target:
        #         j=j-1
        #     elif S[i][0]+S[j][0]>target:
# 这部分我一直在想，如果j减下来减多了发现小于了怎么办？后来明白如果sorted就不可能会减多
        while i<j:
            cur = S[i][0]+S[j][0]
            # print(cur)
            if cur==target:
                return [min(S[i][1],S[j][1]),max(S[i][1],S[j][1])]
            elif cur<target:
                i = i+1
            else:
                j = j-1

        return []
