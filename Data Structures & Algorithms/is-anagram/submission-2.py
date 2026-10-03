class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dico={}
        if len(s)!=len(t):
            return False
        for i in range (len(s)):
            dico[s[i]]=dico.get(s[i],0)+1
            if t[i] in s:
                dico[t[i]]=dico.get(t[i],0)-1
        return all(dico[c]==0 for c in dico)