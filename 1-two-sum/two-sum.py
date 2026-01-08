class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i, num in enumerate(nums):
            print(i,num)
            complement = target - num
            if complement in lookup:
                return [lookup[complement],i]
            lookup[num] = i
       