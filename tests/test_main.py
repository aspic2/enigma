import unittest
import random
import string
from enigma import main

class TestMain(unittest.TestCase):
    

    def test_Rotor(self):
        r = main.Rotor(1)
        char = random.choice(string.ascii_uppercase)
        results = []
        # run through all possible combinations
        for n in range(25):
            new_char = r.push_char(char)
            results.append(new_char)
        self.assertEqual(len(set(results)), len(results))





if __name__ == '__main__':
    unittest.main()
