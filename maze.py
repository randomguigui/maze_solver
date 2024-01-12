import random

class Maze:
    def __init__(self, maze: list):
        self.maze = maze

    def find_start(self):
        start = ()
        for n in range(len(self.maze)):
            for m in range(len(self.maze[n])):
                if self.maze[n][m] == 2:
                    start = (n, m)
                    return start

    def aside(self, x, y):
        aside = []
        try:
            if self.maze[y][x + 1] == 0 or self.maze[y][x + 1] == 3:
                aside.append((y, x + 1))
            if self.maze[y][x - 1] == 0 or self.maze[y][x - 1] == 3:
                if x - 1 != -1:
                    aside.append((y, x - 1))
            if self.maze[y - 1][x] == 0 or self.maze[y - 1][x] == 3:
                if y - 1 != -1:
                    aside.append((y - 1, x))
            if self.maze[y + 1][x] == 0 or self.maze[y + 1][x] == 3:
                aside.append((y + 1, x))
        except IndexError:
            pass

        return aside

    def solution(self):
        start = self.find_start()
        road = [start]
        forbidden = []

        while self.maze[road[-1][0]][road[-1][1]] != 3:
            aside = self.aside(road[-1][1], road[-1][0])
            len_aside = len(aside)
            for i in range(len_aside):
                if aside[len_aside - 1 - i] in forbidden or aside[len_aside - 1 - i] in road:
                    aside.pop(aside.index(aside[len_aside - 1 - i]))

            if not aside:
                case_pop = road.pop()
                forbidden.append(case_pop)
            else:
                chosen_case_aside = random.choice(aside)
                road.append(chosen_case_aside)
        return road

lab = [[1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [2, 0, 1, 0, 0, 0, 1, 0, 1, 0, 3],
        [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1]]
#lab[1][0] = 2
#lab[8][3] = 3

maze = Maze(lab)

s = maze.solution()
print(s)
print(len(s))