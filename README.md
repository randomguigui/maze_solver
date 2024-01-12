<h1>This is a maze solver.</h1>

`Maze(maze)` to create a maze

The `maze` argument must be a list of list of same length each where 0 are empty spaces, 1 are walls, 2 is the start and 3 is the end.

The square on the top left corner is `(0, 0)` 

There is an example of how you can use it below.

```python
import maze

maze = maze.Maze([[1, 1, 1, 3],
                  [2, 0, 1, 0],
                  [1, 0, 1, 0],
                  [0, 0, 0, 0]])

print(maze.solution())
```

`Maze.solution()` returns a list of coordinates that represent the path where the first and the last are the start and the finish. The coordinates are represented as `(y, x)`.
