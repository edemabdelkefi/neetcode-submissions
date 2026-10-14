class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        L=[]
        dico={}
        for x in nums:
            dico[x]=dico.get(x,0)+1
        for c in dico:
            if dico[c]>len(nums)//3:
                L.append(c)
        return L
