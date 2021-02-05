def make_solvable(size):
    lst = [[0 for x in range(size)] for y in range(size)]
    pos = 0
    i = 0
    j = 0
    square = size
    rem = 0
    while pos < size * size:
        while j < square:
            if lst[i][j] == 0:
                pos += 1
                if pos == size * size:
                        return(lst)
                lst[i][j] = pos
                j += 1
        if j == square:
                j -= 1
                i += 1
        while i < square:
            if lst[i][j] == 0:
                pos += 1
                if pos == size * size:
                        return(lst)
                lst[i][j] = pos
                i += 1
        if i == square:
                i -= 1
                j -= 1
        while j + 1 > rem:
            if lst[i][j] == 0:
                pos += 1
                if pos == size * size:
                        return(lst)
                lst[i][j] = pos
                j -= 1
        if j < rem:
                j += 1
                i -= 1
        while i > rem:
            if lst[i][j] == 0:
                pos += 1
                if pos == size * size:
                        return(lst)
                lst[i][j] = pos
                i -= 1
        if i <= rem:
                i += 1
                j += 1
                square -= 1
                rem += 1

def fill_solvable(size):
    lst = make_solvable(size)
    solvable = []
    for x in range(size):
        for y in range(size):
            solvable.append(lst[x][y])
    return(tuple(solvable))