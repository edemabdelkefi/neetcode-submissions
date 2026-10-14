class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dico={}
        for c in nums:
            dico[c]=dico.get(c,0)+1
        for j in dico:
            if dico[j]>len(nums)//2:
                return j
                