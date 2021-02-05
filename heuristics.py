def manhattan(m, solved, size):
    res = 0
    for i in range (size * size):
        if m[i] != 0 and m[i] != solved[i]:
            dx = (i // size) - (solved.index(m[i]) // size)        
            dy = (i % size) - (solved.index(m[i]) % size)
            res += (abs(dx) + abs(dy))
    return (res)

def gaschnig(candidate, solved, size):
    res = 0
    candidate = list(candidate)
    solved = list(solved)
    while candidate != solved:
        zi = candidate.index(0)
        if solved[zi] != 0:
            sv = solved[zi]
            ci = candidate.index(sv)
            candidate[ci], candidate[zi] = candidate[zi], candidate[ci]
        else:
            for i in range(size * size):
                if solved[i] != candidate[i]:
                    candidate[i], candidate[zi] = candidate[zi], candidate[i]
                    break
        res += 1
    return res

def hamming(candidate, solved, size): #aka tiles out of place
    res = 0
    for i in range(size*size):
        if candidate[i] != 0 and candidate[i] != solved[i]:
            res += 1
    return res

H = {
        'hamming':      hamming,
        'gaschnig':     gaschnig,
        'manhattan':    manhattan,
        }