class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        L=[[]]
        dico={}
        for mot in strs:
            compte=[0]*26
            for lettre in mot:
                i=ord(lettre)-ord('a')
                compte[i]+=1
            cle=tuple(compte)
            if cle not in dico:
                dico[cle]=[]
            dico[cle].append(mot)
        return list(dico.values())