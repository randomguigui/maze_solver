import random

class Maze:
    def __init__(self, maze: list):
        self.maze = maze
        self.height = len(self.maze)
        self.width = len(self.maze[0])

    def find_start(self):
        start = ()
        for n in range(len(self.maze)):
            for m in range(len(self.maze[n])):
                if self.maze[n][m] == 2:
                    start = (n, m)
                    return start

    def aside(self, x, y):
        aside = []

        if x != self.width - 1:
            if self.maze[y][x + 1] == 0 or self.maze[y][x + 1] == 3:
                aside.append((y, x + 1))
        if x != 0:
            if self.maze[y][x - 1] == 0 or self.maze[y][x - 1] == 3:
                aside.append((y, x - 1))
        if y != 0:
            if self.maze[y - 1][x] == 0 or self.maze[y - 1][x] == 3:
                aside.append((y - 1, x))
        if y != self.height - 1:
            if self.maze[y + 1][x] == 0 or self.maze[y + 1][x] == 3:
                aside.append((y + 1, x))

        return aside

    def solution(self):
        start = self.find_start()
        path = [start]
        forbidden = []

        while self.maze[path[-1][0]][path[-1][1]] != 3:
            aside = self.aside(path[-1][1], path[-1][0])
            len_aside = len(aside)
            for i in range(len_aside):
                if aside[len_aside - 1 - i] in forbidden or aside[len_aside - 1 - i] in path:
                    aside.pop(aside.index(aside[len_aside - 1 - i]))

            if not aside:
                case_pop = path.pop()
                forbidden.append(case_pop)
            else:
                chosen_case_aside = random.choice(aside)
                path.append(chosen_case_aside)
        return path


