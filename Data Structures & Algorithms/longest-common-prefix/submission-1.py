class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m=len(strs[0])
        k=0
        for i in range(len(strs)):
            if len(strs[i])<m:
                k=i
                m=len(strs[i])
        test=False
        ch=strs[k]
        while not test:
            i=0
            while i<len(strs):
                if ch!=strs[i][:m]:
                    m=m-1
                    ch=ch[:len(ch)-1]
                i+=1
            if ch=="":
                return ch
            test=all(ch==strs[i][:m] for i in range(len(strs)))
        return ch


