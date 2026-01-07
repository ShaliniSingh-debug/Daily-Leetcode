class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

       # first we will find which word has the smallest length because prefix wont be working on the list which is not matching in length 
        sortest = min(strs , key= len)

        for i in range(len(sortest)):

            for s in strs:
                if s[i] != sortest[i]:
                    return sortest[:i]
        return sortest
        