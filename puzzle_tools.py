"""
Some functions for working with puzzles
"""
from puzzle import Puzzle
from collections import deque
# set higher recursion limit
# which is needed in PuzzleNode.__str__
# you may uncomment the next lines on a unix system such as CDF
# import resource
# resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
import sys
sys.setrecursionlimit(10**6)


# TODO
# implement depth_first_solve
# do NOT change the type contract
# you are welcome to create any helper functions
# you like
def depth_first_solve(puzzle):
    """
    Return a path from PuzzleNode(puzzle) to a PuzzleNode containing
    a solution, with each child containing an extension of the puzzle
    in its parent.  Return None if this is not possible.

    @type puzzle: Puzzle
    @rtype: PuzzleNode
    """
    tree = PuzzleNode()
    tree.puzzle = puzzle
    searched = set()

    def find(node,searched):
        """

        @type node: PuzzleNode
        @type searched: Set
        @return:
        """

        found = None
        extensions = node.puzzle.extensions()
        temp_child = PuzzleNode()
        children = []

        if node.puzzle.is_solved():
            return node

        #  Check if the current puzzle is solved

        if node == None or node.puzzle.__repr__() in searched:
            return None
        searched.add(node.puzzle.__repr__())
        #  Trap for configurations that have already been searched.

        if node.puzzle.fail_fast():
            return None
        #  Trap for known incorrect configurations

        for extension in extensions:
            if extension.__repr__().strip() not in searched:
                #temp_child.puzzle = extension
                #temp_child.parent = node
                node.children.append(PuzzleNode(extension,None,node))
        x = 0
        while found == None and x < len(node.children):
            found = find(node.children[x],searched)
            x += 1

        #  check extensions for solutions one by one

        #if found != None:
        #    pass
            #  used for debugging purposes

        if found == None:
            node.children = None
            return None
        node.children = [found]
        return node

    return find(tree,searched)
# TODO
# implement breadth_first_solve
# do NOT change the type contract
# you are welcome to create any helper functions
# you like
# Hint: you may find a queue useful, that's why
# we imported deque
def breadth_first_solve(puzzle):
    """
    Return a path from PuzzleNode(puzzle) to a PuzzleNode containing
    a solution, with each child PuzzleNode containing an extension
    of the puzzle in its parent.  Return None if this is not possible.

    @type puzzle: Puzzle
    @rtype: PuzzleNode
    """
    tree = PuzzleNode()
    tree.puzzle = puzzle
    searched = set()
    queue = deque()

    if tree.puzzle.is_solved():
        return tree

    def find(node,searched,queue):
        """

        @type node: PuzzleNode
        @type searched: Set
        @return:
        """

        found = None
        extensions = node.puzzle.extensions()
        children = []

        if node.puzzle.fail_fast():
            return None
        #  Trap for known incorrect configurations

        if extensions == []:
            return None
            #  Return None for nodes with no children

        for extension in extensions:
            if extension.__repr__().strip() not in searched:
                if extension.is_solved():
                    return PuzzleNode(extension,None,node)

                #  Check the children for a solution, add to a queue if there isn't
                node.children.append(PuzzleNode(extension,None,node))
                queue.appendleft(PuzzleNode(extension,None,node))


        if list(queue) != []:
            return find(queue.pop(),searched,queue)
        #  check extensions for solutions one by one


        if found != None:
            pass
            #  used for debugging purposes

        return node
    solution = find(tree,searched,queue)
    while solution.parent != None:
        solution.parent.children = [solution]
        solution = solution.parent
    #  Format the node such that each parent has only one child.
    return solution
# Class PuzzleNode helps build trees of PuzzleNodes that have
# an arbitrary number of children, and a parent.
class PuzzleNode:
    """
    A Puzzle configuration that refers to other configurations that it
    can be extended to.
    """

    def __init__(self, puzzle=None, children=None, parent=None):
        """
        Create a new puzzle node self with configuration puzzle.

        @type self: PuzzleNode
        @type puzzle: Puzzle | None
        @type children: list[PuzzleNode]
        @type parent: PuzzleNode | None
        @rtype: None
        """
        self.puzzle, self.parent = puzzle, parent
        if children is None:
            self.children = []
        else:
            self.children = children[:]

    def __eq__(self, other):
        """
        Return whether Puzzle self is equivalent to other

        @type self: PuzzleNode
        @type other: PuzzleNode | Any
        @rtype: bool

        >>> from word_ladder_puzzle import WordLadderPuzzle
        >>> pn1 = PuzzleNode(WordLadderPuzzle("on", "no", {"on", "no", "oo"}))
        >>> pn2 = PuzzleNode(WordLadderPuzzle("on", "no", {"on", "oo", "no"}))
        >>> pn3 = PuzzleNode(WordLadderPuzzle("no", "on", {"on", "no", "oo"}))
        >>> pn1.__eq__(pn2)
        True
        >>> pn1.__eq__(pn3)
        False
        """
        return (type(self) == type(other) and
                self.puzzle == other.puzzle and
                all([x in self.children for x in other.children]) and
                all([x in other.children for x in self.children]))

    def __str__(self):
        """
        Return a human-readable string representing PuzzleNode self.

        # doctest not feasible.
        """
        return "{}\n\n{}".format(self.puzzle,
                                 "\n".join([str(x) for x in self.children]))
