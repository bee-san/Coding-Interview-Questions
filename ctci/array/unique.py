import unittest


def is_unique(text):

    # BitMap of chars
    char_set = [False for _ in range(128)]
    for char in text:
        val = ord(char)
        if char_set[val]:
            # Char already in string
            # so it's not unique
            return False
        char_set[val] = True

    return True


class Test(unittest.TestCase):
    test_true = [("abcde"), ("12345"), (""), ("1ab6")]
    test_false = [("aa"), (), ("  ")]

    def test_unique(self):
        for i in self.test_true:
            actual = is_unique(i)
            self.assertTrue(actual)

        for i in self.test_false:
            actual = is_unique(i)
            self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main()
