# Debugger
## pdb
``` bash
$ python -m pdb xxx.py
> /Users/michael/Github/learn-python3/samples/debug/xxx.py(2)<module>()
-> s = '0'
```
pdb的命令和gdb相仿

### pdb.set_trace()
```python
# xxx.py
import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停 进入pdb调试环境
print(10 / n)

```