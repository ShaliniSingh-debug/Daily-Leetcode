class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

       # first we will find which word has the smallest length because prefix wont be working on the list which is not matching in length 
        # sortest = min(strs , key= len)

        # for i in range(len(sortest)):

        #     for s in strs:
        #         if s[i] != sortest[i]:
        #             return sortest[:i]
        # return sortest
        if not strs:
            return ""
        
        min_strs = min(strs)
        max_strs= max(strs)
        i=0
        while i<len(min_strs) and i<len(max_strs) and min_strs[i] == max_strs[i]:
            
            i +=1
        return min_strs[:i]

        