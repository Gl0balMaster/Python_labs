def matrix_transpose(matrix):
    row_size = len(matrix[0])
    transposed = list()
    for item in matrix:
        if row_size != len(item):
            print("неправильно задана матрица")
            return
    for i in range(0,row_size):
        temp = []
        for k in range(0,len(matrix)):
            temp.append(matrix[k][i])
        transposed.append(list())
        for item in temp:
            transposed[i].append(item)
        temp.clear()
    print(transposed)
    return transposed