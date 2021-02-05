import parse
import pathfinding
import heuristics
import resource
from pathfinding import a_star_search
from solvable_state import fill_solvable
from solvable import solvable
import sys

if __name__ == '__main__':
    data = parse.get_input()
    puzzle, size, args = data
    HEURISTIC = heuristics.H[args.f]
    y = puzzle.index(0)
    solved = fill_solvable(size)
    if solvable(puzzle, size, solved) != 'solvable':
        print('this puzzle is unsolvable')
        sys.exit(0)
    res = a_star_search(puzzle, solved, size, HEURISTIC)