import unittest
from titanic.views.titanicview import TitanicView


class TitanicViewTest(unittest.TestCase):
    mock = TitanicView()

    def test_modeling(self):
      this = self.mock.modeling()

if __name__ == '__main__':
    unittest.main()