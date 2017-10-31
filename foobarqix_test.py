import unittest


def foobarqix(number):
    if number % 3 == 0:
        return  "Foo"
    else:
        return "Bar"


class FooBarQixTestCase(unittest.TestCase):
    def test_return_Foo_when_number_is_divisible_by_3(self):
        self.assertEqual(foobarqix(3), "Foo")

    def test_return_Bar_when_number_is_divisible_by_5(self):
        self.assertEqual(foobarqix(5), "Bar")


unittest.main()
