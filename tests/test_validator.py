import unittest
from aadhaar_validator import validate_aadhaar


class TestAadhaarValidator(unittest.TestCase):

    def test_valid_number(self):
        self.assertTrue(validate_aadhaar("234567890123"))

    def test_short_number(self):
        self.assertFalse(validate_aadhaar("12345"))

    def test_letters_in_number(self):
        self.assertFalse(validate_aadhaar("23456A890123"))

    def test_zero_at_start(self):
        self.assertFalse(validate_aadhaar("012345678901"))


if __name__ == "__main__":
    unittest.main()
