def count_solvable(puzzle, size, solved):
    res = 0
    vi = 0
    vj = 0
    for i in range(size * size - 1):
        for j in range(i + 1, size * size):            
            vi = puzzle[i]
            vj = puzzle[j]
            if solved.index(vi) > solved.index(vj):
                res += 1
                
    return res

def solvable(puzzle, size, solved):
    inversions = count_solvable(puzzle, size, solved)
    puzzle_x = puzzle.index(0) // size
    puzzle_y = puzzle.index(0) % size
    solved_x = solved.index(0) // size
    solved_y = solved.index(0) % size
    dist = abs(puzzle_x - solved_x) + abs(puzzle_y - solved_y)
    if dist % 2 == 0 and inversions % 2 == 0:
        return('solvable')
    if dist % 2 == 1 and inversions % 2 == 1:
        return('solvable')
    return False 