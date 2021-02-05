import heuristics
from itertools import count
from heapq import heappush, heappop
from collections import deque
from math import inf
import sys

def swap_moves(node, pos, new_pos):
    tmp = []
    tmp = node[pos]
    node[pos] = node[new_pos]
    node[new_pos] = tmp
    return tuple(node)


def get_moves(node, size):
    pos = node.index(0)
    moves = []
    if pos % size > 0:
        left = swap_moves(list(node), pos, pos - 1)
        moves.append(left)
    if (pos + 1) % size > 0:
        right = swap_moves(list(node), pos, pos + 1) 
        moves.append(right)
    if pos + size < size * size:
        down = swap_moves(list(node), pos, pos + size)
        moves.append(down)
    if pos - size >= 0:
        up = swap_moves(list(node), pos, pos - size)
        moves.append(up)
    return moves

def a_star_search(puzzle, solved, size, HEURISTIC):
    count = 0
    queue = [(0, puzzle, 0, None)]
    openlist = {}
    closelist = {}
    while queue:
        f, node, node_g, parent = heappop(queue)
        if node == solved:
            board = [node]
            while parent is not None:
                board.append(parent)
                parent = closelist[parent]
            board.reverse()
            print(len(openlist), len(closelist))
            return(True, board, len(openlist), len(closelist))
        if node in closelist:
            continue
        closelist[node] = parent
        deep_g = node_g + 1
        all_moves = get_moves(node, size)
        for moves in all_moves:
            if moves in closelist:
                continue
            if moves in openlist:
                move_g, heuristic = openlist[moves]
                if move_g <= deep_g:
                    continue
            else:
                heuristic = HEURISTIC(moves, solved, size)
            openlist[moves] = deep_g, heuristic
            heappush(queue, (heuristic + deep_g, moves, deep_g, node))
        count += 1
    return(False, [], len(openlist), len(closelist))
