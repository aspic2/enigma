import unittest
import random
import string
from enigma import main

class TestMain(unittest.TestCase):


    def test_rotor(self):
        char = random.choice(string.ascii_uppercase)
        print(char)
        transformed_char = main.rotor(char)
        print(transformed_char)
        self.assertNotEqual(char, transformed_char)

    def test_Rotor(self):
        r = main.Rotor(1)
        char = random.choice(string.ascii_uppercase)
        self.assertNotEqual(char, r.push_char(char))
        results = []
        # run through all possible combinations
        for n in range(25):
            results.append(r.push_char(char))
        self.assertEqual(len(set(results)), len(results))



if __name__ == '__main__':
    unittest.main()
