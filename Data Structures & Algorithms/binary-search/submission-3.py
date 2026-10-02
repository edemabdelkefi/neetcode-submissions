class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1
        while i<=j:
            if target>nums[(i+j)//2]:
                i=(i+j)//2 +1
            elif target<nums[(i+j)//2]:
                j=(i+j)//2 -1
            else:
                return (i+j)//2
        return -1