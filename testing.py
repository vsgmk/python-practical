import unittest
def add(a,b):
    return a+b

class TestAddFunction(unittest.TestCase):
    def sum_add(self):
        self.assertEqual(add(1,2),3)
    def test_sum(self):
        self.assertEqual(add(2,3),5)

if _name=='main_':
    unittest.main()
   
