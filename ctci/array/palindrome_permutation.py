from collections import Counter

def palindrome_permutation(text):

    # Firstly, the same letter cannot appear 3 times in a row
    # The string must be longer than 1, because it cant be a permtuation
    """
    What if I used a 2 pointer approach?
    The letter at the start has to match the letter at the end
    To do this, the input text has to contain 2 letters which are the same
    So the string cannot be entirely unique.

    If we pute letters into a hashtable, we can work out letters which are 2 chars
    to put them on the ends
    We can then build permutations of these 2 letters
    If we have 1 singular letter, it has to be in the middle
    or else it cant be a palindrome.

    that means that if we have 1 single letter and the string is not
    an odd length, we cannot do it.
    """
    len_text = len(text)

    if len_text == 0:
        return False

    chars = Counter()

    for i in text:
        chars[i] += 1
    
    # If a char is not even, but the list is text is even length
    # We cannot build a palindrome
    if any([x % 2 != 0 for x in chars.values()])  && len_text % 2 == 0:
        return False
    
    pointer1 = 0
    pointer2 = len_text


    result_string = []

    while not chars.isEmpty():
        for i in chars.keys():
            if chars[i] == 1:
                continue
            else if chars[i] == 1 and len(chars) == 1:
                # We're in the middle of the array
                result_string[len_text / 2] = i
            # places 2 chars on either side, and removes them
            result_string[pointer1] = i
            chars[i] = chars[i] - 1
            result_string[pointer2] = i
            chars[i] = chars[i] - 1
    return True


class Test(unittest.TestCase):
    dataT = (
        "Tact Coa",
    )
    dataF = (
        "acb",
    )

    def test_cp(self):
        # true check
        for test_strings in self.dataT:
            result = check_permutation(*test_strings)
            self.assertTrue(result)
        # false check
        for test_strings in self.dataF:
            result = check_permutation(*test_strings)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()