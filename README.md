# N-Puzzle solver

N-Puzzle solver is an implementation of 15 puzzle game with an algorithmic solver and complexity analysis.<br/>

![Alt text](https://github.com/igorgarbuz/cdn/blob/main/n-puzzle/n-puzzle-demo.gif)

## Description of used algorithms:

| Algorithm  | Cost_function | Description|
| ------------- | ------------- |-----------------|
| A* (A-star)  | g(x) + h(x)  | A* is a popular algorithm for finding the shortest path in a graph. A* is an informed version of Dijkstra's algorithm as it uses an additional heuristic. At each step it takes the best shortest path based on the cost function `f(x) = g(x) + h(x)` , where x is the graph distance metric, g(x) is the exact traveled distance and h(x) is the remaining distance estimated by the heuristic function. A* guarantees the shortest path if an admissible heuristic is used.|
|Best-1st|h(x)|Best-1st is the greedy version of A*: it selects the next node to explore based exclusively on the heuristic's estimation of remaining path. Unlike A*, Best-1st doesn't guarantee the shortest path, but it converges much faster.|

## Description of used heuristics:

| Heuristic  | Admissibility | Description|
| ------------- | ------------- |-----------------|
|Hamming|Yes|Simple heuristic that represents the number of misplaced tiles.|
|Euclidean	|Yes|Estimates distances between current and solved board states if tiles were moved in straight lines.|
|Manhattan|Yes|Estimates distances between current and solved board states according to taxicab geometry (a.k.a L1 norm).|
|Linear conflict|No|Based on manhattan distance, with an additional amendment on tiles that are in the same line or column and must be moved behind each other.|
|Permutation number|No|Primitive heuristic computes the number of tiles out of increasing order. It skips tiles that are both ordered and misplaced.|

## Usage

```
usage: solver.py [-h] [-c] [-ida] [-g] [-u]
                 [-f {hamming,gaschnig,manhattan,conflicts}]
                 [-s {zero_first,zero_last,snail}] [-p] [-v]
                 file

n-puzzle @ 42 fremont

positional arguments:
  file                  input file

optional arguments:
  -h, --help            show this help message and exit
  -c                    colors
  -ida                  ida* search
  -g                    greedy search
  -u                    uniform-cost search
  -f {hamming,gaschnig,manhattan,conflicts}
                        heuristic function
  -s {zero_first,zero_last,snail}
                        solved state
  -p                    pretty print solution steps
  -v                    gui visualizer
  ```
