import unittest
import random
import string
from enigma import main

class TestMain(unittest.TestCase):


    def test_Rotor(self):
        r = main.Rotor(1)
        count = 0
        char = (random.choice(string.ascii_uppercase), True)
        results = []
        # run through all possible combinations
        for n in range(25):
            r.set_current(count)
            new_char = r.push_char(char)
            results.append(new_char)
            count += 1
        self.assertEqual(len(set(results)), len(results))

    def test_push_char(self):
        r = main.Rotor()
        r.set_rotor(1, 25)
        count = r.current ** r.slot
        char = random.choice(string.ascii_uppercase)
        r.push_char(char)
        count += 1
        r.set_current(count)
        self.assertEqual(r.current, 0)

    def test_rotate_math(self):
        """I need a calculation to make the rotor turns for this work properly"""
        r1 = main.Rotor(1).set_rotor(1, 2)
        r2 = main.Rotor(2).set_rotor(2, 2)
        r3 = main.Rotor(3).set_rotor(3, 2)
        slots = [r1, r2, r3]
        e = main.Enigma(slots).set_count()
        """In short, rotor 1 should complete a rotation every 26th time
        Rotor 2 every 26 * 26 th time
        Rotor 3 every 26 * 26 * 26th time
        """
        count = 2 + (26*2) + (2*26**2)
        self.assertEqual(count, e.count)

    def test_my_math(self):
        """I should be able to use an incrementing variable and floor division
        to determine each rotor's position.
        """
        r1 = main.Rotor(1).set_rotor(1, 25)
        r2 = main.Rotor(2).set_rotor(2, 23)
        r3 = main.Rotor(3).set_rotor(3, 18)
        slots = [r1, r2, r3]
        e = main.Enigma(slots).set_count()
        print("Current e.count = " + str(e.count))
        # e.count = 17,575
        print("r1 current setting = " + str(r1.current))
        # 25, or e.count % (26 ** 1)
        self.assertEqual(r1.current, e.count % (len(r1.letters) ** (e.rotors.index(r1)+1))
        // (len(r1.letters)** e.rotors.index(r1)))
        print("r2 current setting = " + str(r2.current))
        # 25, or
        self.assertEqual(r2.current, e.count % (len(r2.letters) ** (e.rotors.index(r2)+1))
        // (len(r2.letters)** e.rotors.index(r2)))
        print("r3 current setting = " + str(r3.current))
        # 25 or e.count % 26
        self.assertEqual(r3.current, e.count % (len(r3.letters) ** (e.rotors.index(r3)+1))
        // (len(r3.letters)** e.rotors.index(r3)))

    def test_Enigma(self):
        r1 = main.Rotor(1).set_rotor(1, 25)
        r2 = main.Rotor(2).set_rotor(2, 23)
        r3 = main.Rotor(3).set_rotor(3, 18)
        slots = [r1, r2, r3]
        e = main.Enigma(slots).set_count()

        for n in range(400):
            char = random.choice(string.ascii_uppercase)
            e.encode(char)
            for r in e.rotors:
                print("Rotor %d setting: %d" % (r.slot, r.current))
            print("\n\n")





if __name__ == '__main__':
    unittest.main()
