class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row = 0

        for i in range(len(matrix)):
            if matrix[i][0] <= target:
                row = i
            else:
                break
        
        left = 0
        right = len(matrix[row]) - 1
        mid = len(matrix[row]) // 2 
        while left <= right:
            if target < matrix[row][mid]:
                right = mid -1 
            elif target > matrix[row][mid]:
                left = mid + 1
            else:
                return True
            
            mid = (left + right) // 2
        
        return False