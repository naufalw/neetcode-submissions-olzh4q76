class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        idx = {}
        for i in range(len(nums)):
            curr = nums[i]
            reminder = target - curr
            if idx.get(reminder, None) is not None:
                return [idx[reminder], i]       
            idx[curr] = i
        
        return []