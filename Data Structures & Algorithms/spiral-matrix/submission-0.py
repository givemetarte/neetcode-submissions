class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n_rows, n_cols = len(matrix), len(matrix[0])
        row, col = 0, -1
        direction = 1 
        output = []

        while n_rows > 0 and n_cols > 0: 
            for _ in range(n_cols): 
                col += direction 
                output.append(matrix[row][col])
            n_rows -= 1 

            for _ in range(n_rows):
                row += direction
                output.append(matrix[row][col])
            n_cols -= 1

            direction *= -1

        return output


"""
- 위쪽 행을 순회하는 경우 컬럼 +1 증가  
- 오른쪽 컬럼을 순회하는 경우 행 +1 증가
- 아래쪽 행을 순회하는 경우 컬럼 -1 감소 
- 왼쪽 컬럼을 순회하는 경우 행 -1 감소 

n_rows = 3 > 2 > 1 > 0
n_cols = 3 > 2 > 1
row, col = (1,1)

>>>
↑>↓
<<↓

output:[1,2,3,6,9,8,7,4,]
"""