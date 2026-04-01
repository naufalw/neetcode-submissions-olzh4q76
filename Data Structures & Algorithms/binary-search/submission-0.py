class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums) // 2 

        left = 0
        right = len(nums) - 1

        while left <= right:
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
            
            mid = (right + left) // 2

        return -1
