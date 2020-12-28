import unittest
import SARPGaS.experiences as exp


class MyTestCase(unittest.TestCase):
    # y = 2x^2 + 3x + y
    def test_xp_conversion(self):
        xp = exp.Exp()
        self.assertEqual(xp.level_to_exp(0), 0)
        self.assertEqual(xp.level_to_exp(1), 5)
        self.assertEqual(xp.level_to_exp(2), 19)
        self.assertEqual(xp.level_to_exp(3), 46)
        self.assertEqual(xp.level_to_exp(4), 90)


if __name__ == '__main__':
    unittest.main()
