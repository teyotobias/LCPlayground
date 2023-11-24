
def rotate(matrix):
    left, right = 0, len(matrix) - 1
    
    while left < right:
        for i in range(right-left):
            top,bottom = left, right
            topLeft = matrix[top][left+ i]

            matrix[top][left+i] = matrix[bottom-i][left]
            
            matrix[bottom-i][left] = matrix[bottom][right-i]

            matrix[bottom][right-i] = matrix[top+i][right]
            
            matrix[top+i][right] = topLeft
        right -= 1
        left += 1

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print("Original Matrix: " + str(matrix))
rotate(matrix)
print("Rotated Matrix: " + str(matrix))

