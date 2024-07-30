def spiral_matrix(matrix_data):
    
    line_x, line_y = 0, 0
    dx, dy = 1, 0
    zero_matrix = [[0] * matrix_data for i in range(matrix_data)]
    
    for i in range(1, matrix_data ** 2 + 1):
        
        zero_matrix[line_x][line_y] = i
        nx, ny = line_x + dx, line_y + dy
        
        if 0 <= nx < matrix_data and 0 <= ny < matrix_data and not zero_matrix[nx][ny]:
            line_x, line_y = nx, ny
        else:
            dx, dy = -dy, dx
            line_x, line_y = line_x + dx, line_y + dy
    
    for x in list(zip(*zero_matrix)):
        print(*x)


spiral_matrix(5)
