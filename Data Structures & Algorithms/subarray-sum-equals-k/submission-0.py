class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dico={0:1}
        s=0
        count=0
        for x in nums:
            s+=x
            count+=dico.get(s-k,0)
            dico[s]=dico.get(s,0)+1
        return count