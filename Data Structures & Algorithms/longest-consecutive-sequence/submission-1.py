class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        L=set(nums)
        M=[]
        for x in L:
            s=0
            p=x
            if x-1 not in L:
                while p in L:
                    p+=1
                    s+=1
                M.append(s)
        return max(M)
