from typing import List
from pprint import pprint


class RatMaze:
    def __init__(self, maze):
        self.maze = maze
        self.way_to_out = []

    def rat_maze_solution(self) -> List:

        for puzz in self.maze:
            print(puzz)

        return self.way_to_out


if __name__ == '__main__':
    maze_matrix = [
                    [1, 0, 0], 
                    [1, 1, 0], 
                    [1, 1, 1]
                ]
    rat_maze_puzzle = RatMaze(maze_matrix)
    rat_maze_puzzle.rat_maze_solution()
    