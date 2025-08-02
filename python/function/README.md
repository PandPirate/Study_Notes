# 高阶函数
### map
map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
```python
>>> def f(x):
...     return x * x
...
>>> r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> list(r)
[1, 4, 9, 16, 25, 36, 49, 64, 81]

# 一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, # 4, 5, 6, 7, 8, 9]上
```
### reduce
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数</br>
reduce把结果继续和序列的下一个元素做累积计算，其效果就是：</br>
`reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)`

```python
>>> from functools import reduce
>>> def add(x, y):
...     return x + y
...
>>> reduce(add, [1, 3, 5, 7, 9])
25

# 个序列求和
```
### filter
Python内建的filter()函数用于过滤序列。</br>
filter()也接收一个函数和一个序列 </br>
filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。</br>
```python
def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
# 结果: [1, 5, 9, 15]
# 在一个list中，删掉偶数，只保留奇数
```
### sorted
Python内置的sorted()函数就可以对list进行排序</br>
sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序</br>
key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。然后sorted()函数按照keys进行排序，并按照对应关系返回list相应的元素</br>
默认情况下，对字符串排序，是按照ASCII的大小比较的
```python
>>> sorted([36, 5, -12, 9, -21], key=abs)
[5, 9, -12, -21, 36]

# 按绝对值排序
```

# 返回函数
高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回 </br>
**返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。**
```python
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

>>> f = lazy_sum(1, 3, 5, 7, 9)
>>> f
<function lazy_sum.<locals>.sum at 0x101c6ed90>
>>> f()
25

# 请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
>>> f1 = lazy_sum(1, 3, 5, 7, 9)
>>> f2 = lazy_sum(1, 3, 5, 7, 9)
>>> f1==f2
False

```
# 闭包
闭包就是能够读取外部函数内的变量的函数</br>
闭包作用
1. 闭包是将外层函数内的局部变量和外层函数的外部连接起来的一座桥梁
2. 将外层函数的变量持久地保存在内存中
```python
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
```
在上面的例子中，每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了。
</br>
你可能认为调用f1()，f2()和f3()结果应该是1，4，9，但实际结果是：
```python
>>> f1()
9
>>> f2()
9
>>> f3()
9
```

__**返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量**__

```python
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

>>> f1, f2, f3 = count()
>>> f1()
1
>>> f2()
4
>>> f3()
9

```
### nonlocal
**使用闭包时，对外层变量赋值前，需要先使用nonlocal声明该变量不是当前函数的局部变量。**
```python
# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    def counter():
        return 1
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

```
# 匿名函数
当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。</br>

在Python中，对匿名函数提供了有限支持。还是以map()函数为例，计算f(x)=x2时，除了定义一个f(x)的函数外，还可以直接传入匿名函数：</br>
```python
>>> list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
[1, 4, 9, 16, 25, 36, 49, 64, 81]
```
**关键字lambda表示匿名函数，冒号前面的x表示函数参数。**</br>
**匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。**
# 装饰器 decorator
```python
# 不带参数的装饰器
import functools

def log(func):
    @functools.wraps(func) # wrapper.__name__ = func.__name__
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
```

```python
# 带参数的装饰器
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

```
# 偏函数 functools.partial
```python
max2 = functools.partial(max, 10)
# 实际上会把10作为*args的一部分自动加到左边，也就是：
max2(5, 6, 7)  
# 相当于 
args = (10, 5, 6, 7)
max(*args)

```
把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
