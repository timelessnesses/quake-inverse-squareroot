import unittest
import sys

try:
    
    if '--include_this_directory' in sys.argv:
        raise Exception('Avoiding removing current directory from sys.path')
    if '.' in sys.path:
        sys.path.remove('.')
    if '' in sys.path:
        sys.path.remove('')
except:
    pass

import quake_inverse_sq


class TestCase(unittest.TestCase):
    def test_coarse_invert_squareroot(self) -> None:
        EXPECT = 0.49915357479239103
        INPUT = 4
        self.assertAlmostEqual(quake_inverse_sq.coarse_inv_sqrt(INPUT), EXPECT)
        
    def test_fined_invert_squareroot(self) -> None:
        EXPECT = 0.5
        INPUT = 4
        self.assertAlmostEqual(quake_inverse_sq.fined_inv_sqrt(INPUT), EXPECT)


if __name__ == '__main__':
    unittest.main()
