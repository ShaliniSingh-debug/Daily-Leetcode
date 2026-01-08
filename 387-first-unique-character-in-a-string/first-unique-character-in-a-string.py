class Solution:
    def firstUniqChar(self, s: str) -> int:
        # freq={}
        # for ch in s:
        #     if ch in freq:
        #         freq[ch] +=1
        #     else:
        #         freq[ch] =1
        
        # for i in range(len(s)):
        #     if freq[s[i]]==1:
        #         return i
        # return -1

        # another method  ---> create counter and check lookup

        freq = Counter(s)
        for i, num in enumerate(s):
            if freq[num] ==1:
                return i
        return -1

        # tc --> O(n)  , SC ---> O(1) ->constant space since 26 letters
        
      
        

        