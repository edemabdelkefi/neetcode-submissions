class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        j=0
        ch=""
        if len(word1)<=len(word2):
            for i in range(len(word1)):
                ch=ch+word1[i]+word2[i]
            ch=ch+word2[len(word1):]
        elif len(word2)<len(word1):
            for i in range(len(word2)):
                ch=ch+word1[i]+word2[i]
            ch=ch+word1[len(word2):]
        return ch
