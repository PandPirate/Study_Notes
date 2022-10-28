- git status 不显示中文显示八进制数字

  ![img](C:\Users\pp\Documents\GitHub\Study_Notes\3f6f41a20f3da19933ec07a71951c12f.png)

**解决办法** 

将git 配置文件 `core.quotepath`项设置为false。
quotepath表示引用路径
加上`--global`表示全局配置

``` git
git config --global core.quotepath false
```

引用 https://blog.csdn.net/u012145252/article/details/81775362