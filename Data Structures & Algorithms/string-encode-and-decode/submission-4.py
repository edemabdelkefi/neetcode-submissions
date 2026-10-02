class Solution:

    def encode(self, strs: List[str]) -> str:
        ch=""
        for i in range(len(strs)):
            ch=ch+str(len(strs[i]))+"#"+strs[i]
        return ch

    def decode(self, s: str) -> List[str]:
        i=0
        n=len(s)
        L=[]
        while i<n:
            j = s.find("#", i)
            a = int(s[i:j])
            L.append(s[j+1:j+1+a])
            i = j+1+a
        return L