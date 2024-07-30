
def optimizing_workspaces(size_zone):

    zero_matrix = [[0] * size_zone for i in range(size_zone)]
    
    for i in range(size_zone):
        for j in range(i + 1, size_zone - 1 - i):
            zero_matrix[i][j] = 1
            zero_matrix[j][i] = 2
            zero_matrix[size_zone - 1 - i][j] = 3
            zero_matrix[j][size_zone - 1 - i] = 4
    
    for i in range(size_zone):
        for j in range(size_zone):
            zero_matrix[i][-i - 1] = 5
        zero_matrix[i][i] = 0

    
    for row in zero_matrix:
        print(' '.join([str(elem) for elem in row]))
    

optimizing_workspaces(5)    
