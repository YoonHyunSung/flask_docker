import unittest

from basic.one_to_ten_sum import one_to_ten_sum


class one_to_ten_sum_test(unittest.TestCase):
    mock = one_to_ten_sum()
    def test(self):
        self.mock.one_to_ten_sum1()
        self.mock.one_to_ten_sum2()
if __name__ == '__main__':
    unittest.main