import unittest
from code import domain


class DefaultWidgetSizeTestCase(unittest.TestCase):
    def test_pay_cash(self):
        price = 2

        hs = domain.Homescreen(["Black"])
        tcc = domain.Coffeescreen(hs, domain.Coffee("Black", price))
        tcc.pay_cash(2)

        self.assertEqual(tcc.get_price_paid(), price)

    def test_make_coffee_True(self):
        price = 2

        hs = domain.Homescreen(["Black"])
        tcc = domain.Coffeescreen(hs, domain.Coffee("Black", price))
        tcc.pay_cash(2)

        self.assertTrue(tcc.make_coffee())

    def test_make_coffee_False(self):
        price = 2

        hs = domain.Homescreen(["Black"])
        tcc = domain.Coffeescreen(hs, domain.Coffee("Black", price))
        tcc.pay_cash(1)

        self.assertFalse(tcc.make_coffee())
