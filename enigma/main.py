import sys
import random
import string

# Enigma: the big picture:
# Input a character. Out comes a different character
# Do this by:
# 1) Making input uppercase
# 2) Run input through plugboard
# 3) Run input through series of rotors
# 4) Run input through rotors in reverse order
# 5) Run input through plugboard once more
# 6) Display final character

class Rotor(object):

    def __init__(self, rotor_id="default"):
        self.id = rotor_id
        self.letters = random.sample(string.ascii_uppercase,
                                     k=len(string.ascii_uppercase))
        self.current = 1
        # used to determine how often rotor rotates
        self.slot = 1
        self.setting = 1

    def rotate(self):
        self.current += 1
        return self

    def push_char(self, c):
        #TODO: abstract this for all rotor slots
        if self.slot == 1:
            self.rotate()
        # This inc's out of index for slots beyond 1.
        new_char = self.letters[self.current-1]
        return new_char

    def set_rotor(self, slot, setting):
        self.current = setting - 1
        self.slot = slot
        return self


class Slot(object):
    """moving logic for spinning the rotor reader here. Facilitates making
    rotors that rotate at different rates to one another.
    """

    def __init__(self, position=1):
        """Only what's important."""
        self.position = position

    def spin(self):
        pass


class Enigma(object):

    def __init__(self):
        """Testing with single rotor and single slot"""
        self.rotors = [Rotor()]
        self.slots = [Slot(1)]

    def encode(self, char):
        # pass message through rotors.
        # rotate first rotor. If first rotor resets to 0, rotate second rotor.
        # if second rotor resets to 0, rotate third rotor
        # etc.
        for r in self.rotors:
            char = r.push_char(char)
        return char


def main():
    enigma = Enigma()
    user_input = None
    while user_input != "end":
        user_input = input("Type next letter or type \"end\"\n> ")
        print(enigma.encode(user_input))
    sys.exit(0)


if __name__ == '__main__':
    main()
