# unittest
unittest是Python自带的一个单元测试框架, 它可以做单元测试, 也能用于编写和运行重复的测试工作.
它给自动化测试用例开发和执行提供了丰富的断言方法, 判断测试用例是否通过, 并最终生成测试结果.
### TestCase编写
- TestCase指的就是测试用例
- 测试类必须继承unittest.TestCase
- 测试方法名称命名必须以test开头
- 测试方法的执行顺序有Case序号决定, 并非由代码顺序决定
### TestFixture
#### setUp和tearDown
##### setUp
主要是用来初始化测试环境, 它在每条测试用例执行前都会调用
##### tearDown
主要作用是测试用例执行完毕后恢复测试环境， 即使出现异常也会调用此方法，每条用例执行结束后都会运行
```python
import unittest

class MyTestCase(unittest.TestCase):
    def setUp(self):
        # 初始化测试环境
        self.data = [1, 2, 3, 4, 5]

    def tearDown(self):
        # 清理测试资源
        del self.data

    def test_addition(self):
        result = sum(self.data)
        self.assertEqual(result, 15)

    def test_empty_list(self):
        self.data = []
        result = sum(self.data)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
```
#### setUpClass和tearDownClass
##### setUpClass
初始化测试环境且只会执行一次。在类中需要加上@classmethod
##### tearDownClass
恢复测试环境且只会执行一次。在类中需要加上@classmethod
</br>
**setUpClass和tearDownClass执行一次是针对当前的测试类而言的，如果当前的py文件有多个测试类， 那么它每个测试类都会执行一次**

### 断言
| 方法                  | 检查             |
|-----------------------|------------------|
| `assertEqual(a, b)`   | `a == b`         |
| `assertNotEqual(a, b)`| `a != b`         |
| `assertTrue(x)`       | `x` 的布尔值为真 |
| `assertFalse(x)`      | `x` 的布尔值为假 |
| `assertIn(a, b)`      | `a in b`         |
| `assertNotIn(a, b)`   | `a not in b`     |

### skip跳过用例
在遇到不想执行的测试用例时，可以使用skip方法

- @unittest.skip(reason) ：无条件跳过用例, reason是说明原因
- @unittest.skipIf(condition, reason)：condition为true时跳过用例
- @ unittest.skipUnless(condition, reason)：condition为False的时候跳过
```python
import unittest

class MyTestCase(unittest.TestCase):
    @unittest.skip("跳过这个测试方法")
    def test_method1(self):
        self.assertTrue(False)

    @unittest.skipIf(1 > 0, "如果条件成立则跳过")
    def test_method2(self):
        self.assertTrue(True)

    @unittest.skipUnless(1 < 0, "除非条件成立则跳过")
    def test_method3(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
```
在上述示例中，test_method1使用了@unittest.skip()，因此它将被跳过，而test_method2和test_method3分别使用了@unittest.skipIf和@unittest.skipUnless，根据条件来决定是否跳过测试方法。
### 测试套件
```python
import unittest
from test_module1 import TestModule1
from test_module2 import TestModule2

# 创建一个TestLoader实例
test_loader = unittest.TestLoader()

# 使用TestLoader来加载测试用例
test_suite = test_loader.loadTestsFromTestCase(TestModule1)
test_suite.addTest(test_loader.loadTestsFromTestCase(TestModule2))

# 创建测试运行器，这里使用unittest.TextTestRunner来运行测试
test_runner = unittest.TextTestRunner()
result = test_runner.run(test_suite)
```

### 期望异常
有时，希望测试方法引发异常，可以通过@unittest.expectedFailure来标记。这在处理正在修复的问题时很有用，以确保问题确实被修复。
```python
import unittest

class MyTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_fail(self):
        self.assertTrue(False)

    @unittest.expectedFailure
    def test_success(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
```
在上述示例中，test_fail和test_success都使用了@unittest.expectedFailure，但分别引发了失败和成功的断言。测试方法标记为期望失败后，如果测试方法成功，将不会报告为失败，而是作为“已通过但是预期失败的”测试。

这些功能使得unittest模块更加灵活，能够适应不同的测试需求，同时提供更详细的测试结果和跳过测试的灵活性。
                            
