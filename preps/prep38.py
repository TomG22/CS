def get_highest_sum(grid):
    max_num = 0
    for row in grid:
        i = 0
        for num in row:
            if i != len(row) - 1:
                if num + row[i + 1] > max_num:   
                    max_num = num + row[i + 1]
            i += 1
    return max_num
