
import unittest
 
from gc_calc import gc

class GcTests(unittest.TestCase):
    def test_gc(self):
        self.assertEqual(gc('ACTG'), 0.5)

if __name__ == '__main__':
    unittest.main()

def test_long(self):
        self.assertAlmostEqual(gc('ACTGCAGATCTGAAATTCAGTAAGGG'), 0.4230769)

def test_empty(self):
    self.assertRaises(TypeError, gc, )

def test_lowercase(self):
    self.assertEqual(gc('AcTg'), 0.5)

def test_random(self):
    self.assertRaises(Exception, gc, 'This is just a random sentence, but we still get a gc content back.')

def test_empty_string(self):
    self.assertEqual(gc(''), 0)
