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
        """This is not being used"""
        if self.current == 25:
            self.current = 0
        else:
            self.current += 1
        return self

    def get_current(self, count, slot):
        self.current = count % ((len(self.letters) ** (slot)) // (len(self.letters)** (self.slot-1)))
        return self

    def push_char(self, char):
        new_char = self.letters[self.current]
        return new_char

    def set_rotor(self, slot, setting):
        #TODO: this needs to reset Enigma.count
        self.current = setting
        self.slot = slot
        return self


class Enigma(object):

    def __init__(self, rotors=[]):
        """Testing with single rotor and single slot"""
        self.rotors = rotors
        self.count = 0

    def set_rotor_slots():
        #TODO: poor encapsulation
        for r in rotors:
            r.slot(rotors.index(r)+1)
        return self

    def set_count(self):
        """Call only when re-setting rotors"""
        self.count = 0
        rotor_count = len(self.rotors)
        for r in self.rotors:
            self.count += r.current * len(r.letters) ** self.rotors.index(r)
        return self

    def spin_rotors(self):
        for r in self.rotors:
            # is count divisible by 26 ^ rotor slot?
            if not self.count % (len(r.letters) ** self.rotors.index(r)):
                r.rotate()
        # TODO: this is only counting to 25 before rotating
        self.count += 1
        return self

    def encode(self, char):
        # pass message through rotors.
        # rotate first rotor. If first rotor resets to 0, rotate second rotor.
        # if second rotor resets to 0, rotate third rotor
        # etc.
        for r in self.rotors:
            #r.get_current(count, (rotors.index(r) + 1))
            r.current = self.count % ((len(r.letters) ** (r.slot)) // (len(r.letters)** (r.slot-1)))
            char = r.push_char(char)
        self.count += 1
        #self.spin_rotors()
        return char


def main():
    rotors = [Rotor(1).set_rotor(1, 20), Rotor(2).set_rotor(2, 15),
              Rotor(3).set_rotor(3, 10)]
    enigma = Enigma(rotors)
    user_input = None
    while user_input != "end":
        user_input = input("Type next letter or type \"end\"\n> ")
        print(enigma.encode(user_input))
    sys.exit(0)


if __name__ == '__main__':
    main()
