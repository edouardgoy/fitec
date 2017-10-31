import unittest


def foobarqix(number):
    return  "Foo"


class FooBarQixTestCase(unittest.TestCase):
    def test_return_Foo_when_number_is_divisible_by_3(self):
        self.assertEqual(foobarqix(3), "Foo")


unittest.main()
