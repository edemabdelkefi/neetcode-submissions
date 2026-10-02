class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L=[]
        p=1
        k=1
        s=0
        for j in range(len(nums)):
            p=p*nums[j]
            if nums[j]!=0:
                k=k*nums[j]
                s=s+1
        if len(nums)-s>1:
            return [0]*len(nums)
        for i in range(len(nums)):
            if nums[i]!=0:
                L.append(int(p/nums[i]))
            else:
                L.append(k)
        return L
        