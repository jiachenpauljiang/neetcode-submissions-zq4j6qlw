class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) * len(matrix[0]) - 1

        while l <= r:
            mid = l + (r - l) // 2
            # 0, [0, 0]
            # 1, [0, 1] 
            # 2, [0, 2]
            # 3, [0, 3]
            # 4, [1, 0]
            # 5, [1, 1]
            # 6, [1, 2]
            # 7, [1, 3]
            # 8, [2, 0]
            # 10 [2, 2]
            curNum = matrix[mid // len(matrix[0])][mid % len(matrix[0])]
            if curNum < target:
                l  = mid + 1
            elif curNum > target:
                r = mid - 1
            else:
                return True
        return False