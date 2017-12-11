import sys
import random
import string

# Enigma: the big picture:
# Input a character. Out comes a different character
# Do this by:
# 1) Making input uppercase
# 2) Run input through series of rotors, which change the letter
# 3) Run changed input through plugboard
# 4) Run input through rotors in reverse order
# 5) Display final character

class Rotor(object):

    def __init__(self, rotor_id):
        self.id = rotor_id
        self.letters = random.sample(string.ascii_uppercase,
                                     k=len(string.ascii_uppercase))
        self.current = 0

    def push_char(self, c):
        new_char = self.letters[self.current]
        if self.current == 25:
            self.current = 0
        else:
            self.current += 1
        if new_char == c:
            new_char = self.push_char(c)
        return new_char

    def set_rotor(self, setting):
        self.current = setting - 1


class Enigma(object):

    def __init__(self):
        self.rotors = []

    def encode(self, char):
        # pass message through rotors.
        # rotate first rotor. If first rotor resets to 0, rotate second rotor.
        # if second rotor resets to 0, rotate third rotor
        # etc.




def rotor(c):
    character_set = random.sample(string.ascii_uppercase, k=len(string.ascii_uppercase))
    new = character_set.pop(0)
    # keep full list so cycle can start over
    character_set.append(new)
    # letter cannot become itself
    if new == c:
        new = character_set.pop(0)
        character_set.append(new)
    return new

def process_char(i):
    i = i.upper()
    i = rotor(i)
    return i

def main():
    user_input = None
    while user_input != "end":
        user_input = input("Type next letter or type \"end\"\n> ")
        print(process_char(user_input))
    sys.exit(0)


if __name__ == '__main__':
    main()
