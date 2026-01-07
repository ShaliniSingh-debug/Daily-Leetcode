class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) ==1 and len(word2)==1:
            return word1+word2
        leftpart = 0
        rightpart=0
        output=""
        while leftpart<len(word1) or rightpart<len(word2):
            if leftpart<len(word1):
                output +=word1[leftpart]
                leftpart +=1
            if rightpart <len(word2):
                output += word2[rightpart]
                rightpart+=1
        return output

    
