import unittest
import files.first_def as fd

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(fd.add(1,2), 3)  # add assertion here

    def test_something_2(self):
        self.assertEqual(fd.add(1,3), 4)

if __name__ == '__main__':
    unittest.main()
