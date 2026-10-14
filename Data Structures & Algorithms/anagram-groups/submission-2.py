class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dico={}
        for mot in strs:
            compte=[0]*26
            for c in mot:
                compte[ord(c)-97]+=1
            compte=tuple(compte)
            if compte not in dico:
                dico[compte]=[]
            dico[compte].append(mot)
        return list(dico.values())