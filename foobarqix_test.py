import unittest
from foobarqix import foobarqix

class FooBarQixTestCase(unittest.TestCase):
    def test_return_Foo_when_number_is_divisible_by_3(self):
        self.assertEqual(foobarqix(3), "Foo")
        self.assertEqual(foobarqix(6), "Foo")
        self.assertEqual(foobarqix(9), "Foo")

    def test_return_Bar_when_number_is_divisible_by_5(self):
        self.assertEqual(foobarqix(5), "Bar")

    def test_return_Qix_when_number_is_divisible_by_7(self):
        self.assertEqual(foobarqix(7), "Qix")

    def test_return_FooBar_when_number_is_divisible_by_15(self):
        self.assertEqual(foobarqix(15), "FooBar")

    def test_return_nomber_as_a_string_otherwise(self):
        self.assertEqual(foobarqix(1), "1")
        self.assertEqual(foobarqix(2), "2")


unittest.main()
