def operation_table(operation, num_columns=6, num_rows=6):
    table = [[operation(i, j) for i in range(1, num_columns + 1)] for j in range(1, num_rows + 1)]
    for i in table:
        print(*i)
operation_table(lambda x, y: x * y)