# April Shen

import fileinput

class BraidGame:

    def __init__(self):
        # This string gives the order in which we define actions, from
        # left to right.  E.g., 'e' corresponds to swapping the
        # leftmost two letters, etc.
        self.dictionary = 'etaoinshrdlucmfwypvbgkjqxz'
        # This gives the initial and target strings for each level.
        self.all_levels = [ (['t', 'a'], ['a', 't']) ]
        self.level = 0
        self.reset()

    def reset(self):
        # Resets current and target to the strings in levels.
        self.current = self.all_levels[self.level][0]
        self.target = self.all_levels[self.level][1]

    def advance(self):
        # Advances one level.
        self.level += 1
        if self.level >= len(self.all_levels):
            print 'you win it all! :)'
        else:
            self.reset()
        
    def swap(self, i, j):
        # Swaps current[i] with current[j].
        temp = self.current[i]
        self.current[i] = self.current[j]
        self.current[j] = temp

    def unscramble(self, word):
        # Unscrambles current using the actions defined by word.
        # Returns true if current == target.
        for char in word:
            i = self.dictionary.index(char)
            if i > -1 and i < len(self.current)-1:
                self.swap(i, i+1)
        return self.current == self.target


if __name__ == '__main__':
    #args = sys.argv

    game = BraidGame()
    while True:
        line = raw_input(''.join(game.current) + '?: ')
        if game.unscramble(line):
            print 'you win!'
            break
        else:
            print 'try again!'
