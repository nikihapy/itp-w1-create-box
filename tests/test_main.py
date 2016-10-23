import unittest
from create_box import create_box

first_box_expected = """
****
****
****
""".lstrip()

second_box_expected = """
@
""".lstrip()

third_box_expected = """
$$$
$$$
$$$
$$$
$$$
$$$
""".lstrip()


class TestCreateBox(unittest.TestCase):
    def test_box(self):
        self.assertEqual(create_box(3, 4, '*'), first_box_expected)

    def test_small_box(self):
        self.assertEqual(create_box(1, 1, '@'), second_box_expected)
        
    def test_new_box(self):
        self.assertEqual(create_box(6, 3, '$'), third_box_expected)

    # Add your own test using third_box_expected
