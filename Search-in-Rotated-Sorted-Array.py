1from typing import List
2
3class Solution:
4    def search(self, nums: List[int], target: int) -> int:
5        left, right = 0, len(nums) - 1
6        
7        while left <= right:  # must be <=
8            mid = (left + right) // 2
9            
10            if nums[mid] == target:
11                return mid
12            
13            if nums[left] <= nums[mid]:  # left half sorted
14                if nums[left] <= target < nums[mid]:
15                    right = mid - 1
16                else:
17                    left = mid + 1
18            else:  # right half sorted
19                if nums[mid] < target <= nums[right]:
20                    left = mid + 1
21                else:
22                    right = mid - 1
23        
24        return -1
25