class Solution:
    def isValid(self, s: str) -> bool:
        L=[]
        dico={")":"(","]":"[","}":"{"}
        for c in s:
            if c in "([{":
                L.append(c)
            else:
                if not L:
                    return False
                elif L[-1]!=dico[c]:
                    return False
                L.pop()
        return len(L)==0