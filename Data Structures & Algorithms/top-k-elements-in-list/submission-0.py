class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dico={}
        L=[]
        for i in range(len(nums)):
            if nums[i] not in dico:
                dico[nums[i]]=0
            dico[nums[i]]+=1
        for j in range(k):
            m=max(dico.values())
            s=0
            for cle in dico:
                if dico[cle]==m:
                    s=cle
            L.append(s)
            dico.pop(s)
        return L