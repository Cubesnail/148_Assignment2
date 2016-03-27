from puzzle import Puzzle


class WordLadderPuzzle(Puzzle):
    """
    A word-ladder puzzle that may be solved, unsolved, or even unsolvable.
    """

    def __init__(self, from_word, to_word, ws):
        """
        Create a new word-ladder puzzle with the aim of stepping
        from from_word to to_word using words in ws, changing one
        character at each step.

        @type from_word: str
        @type to_word: str
        @type ws: set[str]
        @rtype: None
        """
        (self._from_word, self._to_word, self._word_set) = (from_word,
                                                            to_word, ws)
        # set of characters to use for 1-character changes
        self._chars = "abcdefghijklmnopqrstuvwxyz"

    def __eq__(self, other):
        """Returns true if this puzzle is equal to the other puzzle and false otherwise.

        @type other: WordLadderPuzzle
        @rtype: bool
        >>> test = WordLadderPuzzle('test','case',['test','case'])
        >>> copy = WordLadderPuzzle('test','case',['test','case'])
        >>> test == copy
        True
        >>> copy._to_word = 'test'
        >>> test = copy
        False
        """
        return self._from_word == other._from_word and self._to_word == other._to_word
        # implement __eq__ and __str__

    def __str__(self):
        """Returns a human readable string representation of the string.

        @rtype: string
        >>> test = WordLadderPuzzle('test','case',['test','case'])
        >>> print(test)
        From word: test
        To word: case
        """
        return 'From word: {} \nTo word: {}'.format(self._from_word,self._to_word)

    def __repr__(self):
        """Returns an unambiguous string representation of the puzzle

        @return:
        >>> test = WordLadderPuzzle('case', 'test',['case','test'])
        >>> test.__repr__()
        'case'
        """
        return self._from_word

    def fail_fast(self):
        """

        @return:
        >>> test_word = 'dome'
        >>> to_word = 'bong'
        >>> ws = ['come','dome','bong']
        >>> w = WordLadderPuzzle(test_word,to_word,ws)
        >>> w.fail_fast()
        False
        >>> w._from_word = w._to_word
        >>> w.fail_fast()
        True
        """
        return self.extensions() == []

    def extensions(self):
        """

        @return:
        >>> test_word = 'dome'
        >>> to_word = 'bong'
        >>> ws = ['come','dome','bong']
        >>> w = WordLadderPuzzle(test_word,to_word,ws)
        >>> L1 = w.extensions()
        >>> result = 'come'
        >>> check = WordLadderPuzzle(result, to_word, ws)
        >>> check in L1
        True
        >>> check._from_word = check._to_word
        >>> check in L1
        False
        >>> w in L1
        False
        """

        extension = []

        for x in range(len(self._from_word)):
            word_list = list(self._from_word)
            #  Parse the word into a list of characters.
            del word_list[x]
            #  Delete a character from the word
            for temp_word in self._word_set:
                if len(temp_word) == len(self._from_word) and temp_word != self._from_word:
                    #  Trap for words that are not the same length
                    temp_list = list(temp_word)

                    del temp_list[x]
                    if temp_list == word_list:
                        extension.append(WordLadderPuzzle(temp_word, self._to_word, self._word_set))

                        #  Compare dictionary with word

        return extension

        # length of the word * word set comparisons.

    def is_solved(self):
        """Returns true if the current word ladder is solved and false otherwise.

        @rtype: bool
        >>> test = WordLadderPuzzle('test','case',['test','case'])
        >>> test.is_solved()
        False
        >>> test._from_word = 'case'
        >>> test.is_solved()
        True
        """
        # override is_solved
        # this WordLadderPuzzle is solved when _from_word is the same as
        # _to_word
        return self._from_word == self._to_word


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    from puzzle_tools import breadth_first_solve, depth_first_solve
    from time import time
    with open("words", "r") as words:
        word_set = set(words.read().split())
    w = WordLadderPuzzle("same", "cost", word_set)
    start = time()
    sol = breadth_first_solve(w)
    end = time()
    print("Solving word ladder from same->cost")
    print("...using breadth-first-search")
    print("Solutions: {} took {} seconds.".format(sol, end - start))
    start = time()
    sol = depth_first_solve(w)
    end = time()
    print("Solving word ladder from same->cost")
    print("...using depth-first-search")
    print("Solutions: {} took {} seconds.".format(sol, end - start))
