from puzzle import Puzzle


class MNPuzzle(Puzzle):
    """
    An nxm puzzle, like the 15-puzzle, which may be solved, unsolved,
    or even unsolvable.
    """

    def __init__(self, from_grid, to_grid):
        """
        MNPuzzle in state from_grid, working towards
        state to_grid

        @param MNPuzzle self: this MNPuzzle
        @param tuple[tuple[str]] from_grid: current configuration
        @param tuple[tuple[str]] to_grid: solution configuration
        @rtype: None
        """
        # represent grid symbols with letters or numerals
        # represent the empty space with a "*"
        assert len(from_grid) > 0
        assert all([len(r) == len(from_grid[0]) for r in from_grid])
        assert all([len(r) == len(to_grid[0]) for r in to_grid])
        self.n, self.m = len(from_grid), len(from_grid[0])
        self.from_grid, self.to_grid = from_grid, to_grid

    # TODO
    # implement __eq__ and __str__
    # __repr__ is up to you
    def __repr__(self):
        result = ''
        for row in self.from_grid:
            for number in row:
                result += number
            result += '\n'
        return result.strip()

    def is_solved(self):
        #  TODO
        return self.from_grid == self.to_grid

    def extensions(self):
        # TODO
        # override extensions
        # legal extensions are configurations that can be reached by swapping one
        # symbol to the left, right, above, or below "*" with "*"
        open_position = [-1,-1]
        y = 0
        #  Change the grid to a list because tuples are immutable
        grid_list = []
        for row in self.from_grid:
            grid_list.append(list(row))

        while open_position[0] == -1:
            x = 0
            while open_position[1] == -1 and x < len(self.from_grid[y]):
                if self.from_grid[y][x] == '*':
                    open_position = [y, x]
                x += 1
            y += 1
        possible_moves = []

        def list_to_tuple(grid):
            result = []
            for rows in grid:
                result.append(tuple(rows))
            return tuple(result)

        def move_left(grid,open_position):
            left = [a[:] for a in grid]
            y = open_position[0]
            x = open_position[1]
            left[y][x] = left[y][x + 1]
            left[y][x + 1] = "*"
            return list_to_tuple(left)

        def move_right(grid,open_position):
            right = [a[:] for a in grid]
            y = open_position[0]
            x = open_position[1]
            right[y][x] = right[y][x - 1]
            right[y][x - 1] = "*"
            return list_to_tuple(right)

        def move_up(grid,open_position):
            up = [a[:] for a in grid]
            y = open_position[0]
            x = open_position[1]
            up[y][x] = up[y + 1][x]
            up[y + 1][x] = "*"
            return list_to_tuple(up)

        def move_down(grid,open_position):
            down = [a[:] for a in grid]
            y = open_position[0]
            x = open_position[1]
            down[y][x] = down[y - 1][x]
            down[y - 1][x] = "*"
            return list_to_tuple(down)

        if open_position[0] != 0:
            possible_moves.append(MNPuzzle(move_down(grid_list,open_position),self.to_grid))
        if open_position[0] != len(self.from_grid) - 1:
            possible_moves.append(MNPuzzle(move_up(grid_list,open_position),self.to_grid))
        if open_position[1] != 0:
            possible_moves.append(MNPuzzle(move_right(grid_list,open_position),self.to_grid))
        if open_position[1] != len(self.from_grid[0]) - 1:
            possible_moves.append(MNPuzzle(move_left(grid_list,open_position),self.to_grid))
        return possible_moves
    # TODO
    # override is_solved
    # a configuration is solved when from_grid is the same as to_grid


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    target_grid = (("1", "2", "3"), ("4", "5", "*"))
    start_grid = (("*", "2", "3"), ("1", "4", "5"))
    from puzzle_tools import breadth_first_solve, depth_first_solve
    from time import time
    start = time()
    solution = breadth_first_solve(MNPuzzle(start_grid, target_grid))
    end = time()
    print("BFS solved: \n\n{} \n\nin {} seconds".format(
        solution, end - start))
    start = time()
    solution = depth_first_solve((MNPuzzle(start_grid, target_grid)))
    end = time()
    print("DFS solved: \n\n{} \n\nin {} seconds".format(
        solution, end - start))
