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
        self.current = 0
        # used to determine how often rotor rotates
        self.slot = 1

    def rotate(self):
        if self.current == 25:
            self.current = 0
        else:
            self.current += 1
        return self

    def push_char(self, char):
        #TODO: should this come before or after new_char?
        # char[1] is a boolean
        # if char[1]:
        #     self.rotate()
        new_char = self.letters[self.current]
        return (new_char, self.current == 0)

    def set_rotor(self, slot, setting):
        self.current = setting
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

    def __init__(self, rotors=[]):
        """Testing with single rotor and single slot"""
        self.rotors = rotors
        self.slots = [Slot(1)]
        self.count = 0

    def set_count(self):
        """Call only when re-setting rotors"""
        self.count = 0
        rotor_count = len(self.rotors)
        for r in self.rotors:
            self.count += r.current * len(r.letters) ** self.rotors.index(r)
        return self

    def spin_rotors(self):
        # TODO: this is only counting to 25 before rotating
        self.count += 1
        for r in self.rotors:
            # is count divisible by 26 ^ rotor slot?
            if not self.count % (len(r.letters) ** self.rotors.index(r)):
                r.rotate()
        return self

    def encode(self, char):
        # pass message through rotors.
        # rotate first rotor. If first rotor resets to 0, rotate second rotor.
        # if second rotor resets to 0, rotate third rotor
        # etc.
        for r in self.rotors:
            char = r.push_char(char)
        self.spin_rotors()
        return char


def main():
    rotors = [Rotor(1).set_rotor(1, 20), Rotor(2).set_rotor(2, 15),
              Rotor(3).set_rotor(3, 10)]
    enigma = Enigma(rotors)
    user_input = None
    while user_input != "end":
        user_input = input("Type next letter or type \"end\"\n> ")
        print(enigma.encode((user_input, True)))
    sys.exit(0)


if __name__ == '__main__':
    main()
