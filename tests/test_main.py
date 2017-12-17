import unittest
import random
import string
from enigma import main

class TestMain(unittest.TestCase):


    def test_Rotor(self):
        r = main.Rotor(1)
        char = (random.choice(string.ascii_uppercase), True)
        results = []
        # run through all possible combinations
        for n in range(25):
            new_char = r.push_char(char)
            results.append(new_char)
            r.rotate()
        self.assertEqual(len(set(results)), len(results))

    def test_push_char(self):
        r = main.Rotor()
        r.set_rotor(1, 25)
        char = random.choice(string.ascii_uppercase)
        r.push_char((char, True))
        r.rotate()
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

    def test_rotations(self):
        r1 = main.Rotor(1).set_rotor(1, 25)
        r2 = main.Rotor(2).set_rotor(2, 25)
        r3 = main.Rotor(3).set_rotor(3, 25)
        slots = [r1, r2, r3]
        e = main.Enigma(slots).set_count()
        e.encode(("q", False))
        self.assertEqual(r1.current, 0)
        print("Count is " + str(e.count))
        print("r2 current is " + str(r2.current))
        self.assertEqual(r2.current, 0)
        self.assertEqual(r3.current, 0)
        start_count = e.count
        iters = 800
        for num in range(iters):
            e.encode((random.choice(string.ascii_uppercase), False))
            print( str(num) + " " + str(e.rotors[1].current))
        end_count = e.count
        self.assertTrue(end_count == start_count + iters)
        self.assertEqual(r1.current, iters % 26)
        self.assertEqual(r2.current, iters % (26**2))









if __name__ == '__main__':
    unittest.main()
