import argparse
import heuristics

def is_valid_input(data):
    size = data.pop(0)[0]
    if size <= 2:
        return ('Size of the puzzle too small')
    if len(data) != size:
        return ('Number of line doesnt match with puzzle size')
    if len(data[0]) != size:
        return ('Number of col doesnt match with puzzle size')
    return 'parsed'


def get_input():
    parser = argparse.ArgumentParser(description='n-puzzle @ 42 Paris')
    parser.add_argument('-ida', action='store_true', help='ida* search')
    parser.add_argument('-f', help='heuristic function', choices=list(heuristics.H.keys()), default='manhattan')
    parser.add_argument('file', help='input file', type=argparse.FileType('r'))
    args = parser.parse_args()
    data = args.file.read().splitlines()
    args.file.close()
    data = [line.split('#')[0] for line in data]
    data = [line for line in data if len(line) > 0]
    puzzle = []
    for line in data:
        row = []
        for x in line.split(' '):
            if len(x) > 0:
                if not x.isdigit:
                    print('Parser: invalid input, must be all numeric')
                    return None
                row.append(int(x))
        puzzle.append(row)
    size = puzzle[0][0]
    is_valid = is_valid_input(puzzle)
    if is_valid is not 'parsed':
        print('Parser: invalid input', is_valid)
        return None
    puzzle1d = []                   
    for row in puzzle:
        for item in row:
            puzzle1d.append(item)
    return (tuple(puzzle1d), size, args)

#get_input()    