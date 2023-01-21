import unittest

# aaa model : Arrange, Act, Assert]

def sum(a, b):
    return a + b

# class LearnTest(unittest.TestCase):
    
#     def test_func_1(self):
#         pass
    
# class AnotherTest(unittest.TestCase):
    
#     def test_func_2(self):
#         pass

class SumTest(unittest.TestCase):
    
    # To avoid writing arrange part again and again we can use setUp()
    def setUp(self):
        self.a = 10
        self.b = 20
        
    
    
    def test_sum(self):
        #Arrange
        a = 20
        b = 15
        #Act
        result = sum(a, b)
        #Assert
        self.assertEqual(result, a + b)
        
    def test_sum2(self):
        #Arrange
        a = 20
        b = 15
        #Act
        result = sum(b, a)
        #Assert
        self.assertEqual(result, a + b)
    
if __name__ == "__main__":
    unittest.main()