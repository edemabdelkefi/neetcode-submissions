class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        L=[]
        n=len(nums)
        for i in range(n):
            vus=set()
            for j in range(i+1,n):
                comp=-nums[i]-nums[j]
                if comp in vus:
                    triplet = sorted([nums[i], nums[j], comp])
                    if triplet not in L:
                        L.append(triplet)
                vus.add(nums[j])

        return L

