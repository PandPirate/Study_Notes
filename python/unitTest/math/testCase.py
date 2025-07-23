import unittest
from myMath import myMath

# 创建测试用例类
class MyMathTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Setting up the test class...")

    def setUp(self):
        print("Setting up for a test...")

    def test_add(self):
        """Test the add method."""
        math_instance = myMath(10, 5)
        self.assertEqual(math_instance.add(), 15)
    
    def test_sub(self):
        """Test the sub method."""
        math_instance = myMath(10, 5)
        self.assertEqual(math_instance.sub(), 5)

    def test_multiply(self):
        """Test the multiply method."""
        math_instance = myMath(10, 5)
        self.assertEqual(math_instance.multiply(), 50)

    def test_divide(self):
        """Test the divide method."""
        math_instance = myMath(10, 5)
        self.assertEqual(math_instance.divide(), 2.0)

    def test_divide(self):
        """Test the divide method."""
        math_instance = myMath(10, 0)
        self.assertEqual(math_instance.divide(), None)

    def test_divide2(self):
        """Test the divide2 method."""
        math_instance = myMath(10, 0)
        with self.assertRaises(ValueError):
            math_instance.divide2()

    def tearDown(self):
        print("Tearing down after a test...")

    @classmethod
    def tearDownClass(cls):
        print("Tearing down the test class...")        

if __name__ == '__main__':
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(MyMathTest('test_add'))
    suite.addTest(MyMathTest('test_sub'))
    suite.addTest(MyMathTest('test_multiply'))
    suite.addTest(MyMathTest('test_divide'))
    suite.addTest(MyMathTest('test_divide2'))
    # 运行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)


    # 直接运行所有测试
    # unittest.main()