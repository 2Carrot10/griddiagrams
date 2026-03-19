import unittest
from core import Dir, stabilize, print_vertlist, destab, print_clean, x_nw

class LearningCase(unittest.TestCase):
    def test_starting_out(self):
        knot = [(0,1), (1,0)]

        for dir in Dir:
            for index in [0, 1]:
                print(f"stab({knot}, (0,1), {dir}, {index})")
                b = stabilize([(0,1), (1,0)], (0,1), dir, index)
                print_vertlist(b)
                print_clean(b)
                a = destab(b, 1, dir, index)
                self.assertEqual(a, knot) # I⁻¹ (I knot) = knot

        location = (0,1)
        self.assertEqual(x_nw(knot, location), stabilize(knot, location, Dir.NW, 0), knot)
        location = (1,0)
        self.assertEqual(x_nw(knot, location), stabilize(knot, location, Dir.NW, 0), knot)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
