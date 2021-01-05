import unittest
import SARPGaS.Trash.experiences as exp


class MyTestCase(unittest.TestCase):
    # y = 2x^2 + 3x + y
    # def test_xp_conversion(self):
    #     xp = exp.Exp()
    #     self.assertEqual(xp.level_to_exp(0), 0)
    #     self.assertEqual(xp.level_to_exp(1), 5)
    #     self.assertEqual(xp.level_to_exp(2), 19)
    #     self.assertEqual(xp.level_to_exp(3), 46)
    #     self.assertEqual(xp.level_to_exp(4), 90)

    def test_level_to_level_1(self):  # Testing converting from level to xp then converting back to level
        xp = exp.Exp()
        amount = xp.convert_to_xp(1)
        self.assertEqual(amount, .75)
        value = xp.convert_to_level(amount)
        self.assertEqual(value, 1)

    def test_level_to_level_4(self):  # Testing converting from level to xp then converting back to level
        xp = exp.Exp()
        amount = xp.convert_to_xp(4)
        self.assertEqual(amount, 48)
        value = xp.convert_to_level(amount)
        self.assertEqual(value, 4)

    def test_xp_to_xp_1(self):  # Testing converting from xp to level then converting back to xp
        xp = exp.Exp()
        amount = xp.convert_to_level(.75)
        self.assertEqual(amount, 1)
        value = xp.convert_to_xp(amount)
        self.assertEqual(value, .75)

    def test_xp_to_xp_4(self):  # Testing converting from xp to level then converting back to xp
        xp = exp.Exp()
        amount = xp.convert_to_xp(48)
        self.assertEqual(amount, 4)
        value = xp.convert_to_level(amount)
        self.assertEqual(value, 48)


if __name__ == '__main__':
    unittest.main()
