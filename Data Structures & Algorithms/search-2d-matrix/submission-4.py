class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix[0])
        n = len(matrix)
        lower = 0 
        upper = m * n - 1
        prevMid = 0
        mid = -1
        while lower <= upper:
            prevMid = mid
            mid = (lower + upper) // 2
            y = mid // m
            x = mid % m 
            print(mid, y, x)
            if (target == matrix[y][x]):
                return True
            elif (target > matrix[y][x]):
                lower = mid + 1
            else:
                upper = mid
            
            if (prevMid == mid):
                break

            print(lower, upper)
    
        return False
