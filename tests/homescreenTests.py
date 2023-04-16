import unittest
from code import domain


class DefaultWidgetSizeTestCase(unittest.TestCase):
    def test_pay_cash(self):
        hs = domain.Homescreen(["Black"])
        hs.pay_cash(2)
        hs.pay_cash(4)

        self.assertEqual(hs.price_paid, 6)
        