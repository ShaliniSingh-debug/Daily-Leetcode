1class Solution:
2    def searchInsert(self, nums: List[int], target: int) -> int:
3         left =0
4         right = len(nums)-1
5
6         while left <= right:
7            mid = (left+right)//2
8
9            if nums[mid]==mid:
10                return mid
11            elif nums[mid]<target:
12                left = mid+1
13            else:
14                right = mid-1
15         return left
16
17      
18        
19
20        
21        