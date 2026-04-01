import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k

        self.nums = nums[:k]
        heapq.heapify(self.nums)

        for num in nums[k:]:
            heapq.heappushpop(self.nums, num)

        

    def add(self, val: int) -> int:
        if len(self.nums) == self.k:
            heapq.heappushpop(self.nums, val)
        else:
            heapq.heappush(self.nums, val)
        return self.nums[0]
        
