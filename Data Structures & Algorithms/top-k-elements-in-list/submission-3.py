class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dico={}
        for x in nums:
            dico[x]=dico.get(x,0)+1
        m=0
        L=[]
        cles = sorted(dico, key=dico.get)
        for i in range(len(cles)-k,len(cles)):
            L.append(cles[i])
        return L
