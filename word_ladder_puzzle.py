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
        pass
        # TODO
        # implement __eq__ and __str__

    def __str__(self):
        pass
        # __repr__ is up to you

    def extensions_2(self):
        extension = set()
        word_list = self._from_word[:]
        for temp_word in self._word_set:
            for x in range(len(word_list)):
                x += 1
                pass
        # TODO
        # override extensions
        # legal extensions are WordPadderPuzzles that have a from_word that can
        # be reached from this one by changing a single letter to one of those
        # in self._chars

    def extensions(self):
        extension = set()
        for x in range(len(self._from_word)):
            word_list = list(self._from_word)
            del word_list[x]
            for temp_word in self._word_set:
                if len(temp_word) == len(self._from_word):
                    temp_list = list(temp_word)
                    del temp_list[x]
                    if temp_list == word_list:
                        extension.add(temp_word)
        return extension
        # length of the word * word set comparisons.

    def is_solved(self):
        """

        @return:
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
    #w = WordLadderPuzzle("same", "cost", word_set)
    #start = time()
    #sol = breadth_first_solve(w)
    #end = time()
    print("Solving word ladder from same->cost")
    print("...using breadth-first-search")
    #print("Solutions: {} took {} seconds.".format(sol, end - start))
    start = time()
    sol = depth_first_solve(w)
    end = time()
    print("Solving word ladder from same->cost")
    print("...using depth-first-search")
    print("Solutions: {} took {} seconds.".format(sol, end - start))
