from puzzle import Puzzle


class GridPegSolitairePuzzle(Puzzle):
    """
    Snapshot of peg solitaire on a rectangular grid. May be solved,
    unsolved, or even unsolvable.
    """

    def __init__(self, marker, marker_set):
        """
        Create a new GridPegSolitairePuzzle self with
        marker indicating pegs, spaces, and unused
        and marker_set indicating allowed markers.

        @type marker: list[list[str]]
        @type marker_set: set[str]
                          "#" for unused, "*" for peg, "." for empty
        """
        assert isinstance(marker, list)
        assert len(marker) > 0
        assert all([len(x) == len(marker[0]) for x in marker[1:]])
        assert all([all(x in marker_set for x in row) for row in marker])
        assert all([x == "*" or x == "." or x == "#" for x in marker_set])
        self._marker, self._marker_set = marker, marker_set

    # TODO
    # implement __eq__, __str__ methods
    def __eq__(self, other):
        """

        @param other: None, GridPegSolitarePuzzle
        @rtype: bool
        >>> test = GridPegSolitairePuzzle([["*","*","."]], {"*", ".", "#"})
        >>> copy = GridPegSolitairePuzzle([["*","*","."]], {"*", ".", "#"})
        >>> test == copy
        True
        >>> copy._marker = [[]]
        >>> test == copy
        False
        """
        if other == None:
            return False
        return self._marker == other._marker

    def __str__(self):
        result = ''
        for row in self._marker:
            for column in row:
                if row == '#':
                    result += ' '
                else:
                    result += column
            result += '\n'
        return result

    # __repr__ is up to you
    def __repr__(self):
        """Returns an unambiguious string representation of the puzzle
        @rtype: str
        >>> test = GridPegSolitairePuzzle([["*","*","."]], {"*", ".", "#"})
        >>> test.__repr__()
        '**.'
        """
        result = ''
        for row in self._marker:
            for column in row:
                result += column
        return result

    def extensions(self):
        """Returns a list of extensions from the current configuration.

        @rtype: list[GridPegSolitarePuzzle]
        >>> test = GridPegSolitairePuzzle([["*",".","."]], {"*", ".", "#"})
        >>> test.extensions()
        []
        """

        extension_list = []

        def check_up(position):
            if position[0] > 1:
                #  Ensure resulting peg is on the board.
                up = [a[:] for a in self._marker]
                #  Copy the puzzle grid
                if up[position[0] - 1][position[1]] == '*' and up[position[0] - 2][position[1]] == '.':
                    up[position[0] - 2][position[1]] = '*'
                    up[position[0] - 1][position[1]] = '.'
                    up[position[0]][position[1]] = '.'
                    #  Make the move on the resulting grid
                    return GridPegSolitairePuzzle(up,self._marker_set)

        def check_down(position):
            if position[0] < len(self._marker) - 2:
                #  Ensure resulting peg is on the board.
                down = [a[:] for a in self._marker]
                #  Copy the puzzle grid
                if down[position[0] + 1][position[1]] == '*' and down[position[0] + 2][position[1]] == '.':
                    down[position[0] + 2][position[1]] = '*'
                    down[position[0] + 1][position[1]] = '.'
                    down[position[0]][position[1]] = '.'
                    #  Make the move on the resulting grid
                    return GridPegSolitairePuzzle(down, self._marker_set)

        def check_left(position):
            if position[1] > 1:
                #  Ensure resulting peg is on the board.
                left = [a[:] for a in self._marker]
                #  Copy the puzzle grid
                if left[position[0]][position[1] - 1] == '*' and left[position[0]][position[1] - 2] == '.':
                    left[position[0]][position[1] - 2] = '*'
                    left[position[0]][position[1] - 1] = '.'
                    left[position[0]][position[1]] = '.'
                    #  Make the move on the resulting grid
                    return GridPegSolitairePuzzle(left, self._marker_set)

        def check_right(position):
            if position[1] < len(self._marker) - 2:
                #  Ensure resulting peg is on the board.
                right = [a[:] for a in self._marker]
                #  Copy the puzzle grid
                if right[position[0]][position[1] + 1] == '*' and right[position[0]][position[1] + 2] == '.':
                    right[position[0]][position[1] + 2] = '*'
                    right[position[0]][position[1] + 1] = '.'
                    right[position[0]][position[1]] = '.'
                    #  Make the move on the resulting grid
                    return GridPegSolitairePuzzle(right, self._marker_set)

        for y in range(len(self._marker)):
            for x in range(len(self._marker[0])):
                check = [y,x]
                #  iterate through all the pieces on the board and check each peg.
                if self._marker[y][x] == '*':
                    extension_list.append(check_up(check))
                    extension_list.append(check_down(check))
                    extension_list.append(check_left(check))
                    extension_list.append(check_right(check))
        while None in extension_list:
            extension_list.remove(None)
        return list(extension_list)

    # TODO
    # override is_solved
    def is_solved(self):
        """Returns true if the current puzzle is solved and false otherwise

        @rtype: bool
        >>> test = GridPegSolitairePuzzle([['*','*','.']], {"*", ".", "#"})
        >>> test.is_solved()
        False
        >>> test._marker = [['.','.','*']]
        >>> test.is_solved()
        True
        """
        count = 0
        #  Iterate through each piece in the board and count the amount of pegs.
        for row in self._marker:
            for column in row:
                if column == '*':
                    count += 1
                    if count > 1:
                        #  Return False iff the board has more than 1 piece.
                        return False
        if count == 1:
            return True
            #  A configuration is solved when there is exactly one "*" left
        #  Return None otherwise.
if __name__ == "__main__":
    import doctest

    doctest.testmod()
    from puzzle_tools import depth_first_solve

    grid = [["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", ".", "*", "*"],
            ["*", "*", "*", "*", "*"]]
    gpsp = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
    print(gpsp)
    import time

    start = time.time()
    solution = depth_first_solve(gpsp)
    end = time.time()
    print("Solved 5x5 peg solitaire in {} seconds.".format(end - start))
    print("Using depth-first: \n{}".format(solution))
