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

    def push_char(self, char):
        new_char = self.letters[self.current]
        return new_char

    def set_current(self, count):
        #TODO: BIG ERROR: ROTORS ARE MOVING IN LOCKSTEP
        self.current = (count % ((len(self.letters) ** (self.slot))) //
                                  (len(self.letters)** (self.slot-1)))

    def set_rotor(self, slot, setting):
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

    def encode(self, char):
        for r in self.rotors:
            r.set_current(self.count)
            char = r.push_char(char)
        self.count += 1
        return char


def main():
    rotors = [Rotor(1).set_rotor(1, 20), Rotor(2).set_rotor(2, 15),
              Rotor(3).set_rotor(3, 10)]
    enigma = Enigma(rotors).set_count()
    user_input = None
    while user_input != "end":
        user_input = input("Type next letter or type \"end\"\n> ")
        print(enigma.encode(user_input))
    sys.exit(0)


if __name__ == '__main__':
    main()
