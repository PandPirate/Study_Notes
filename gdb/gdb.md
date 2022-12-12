# GDB调试

**在gdb中,按run或c使程序执行时,按ctrl+c使程序停止**

```gdb
(gdb) c
Continuing.
^C
Program received signal SIGINT, Interrupt.
0x00000076ef7a02bc in timesub () from /system/lib64/libc.so
```



- where 当前运行 到哪一行

```gdb
(gdb) where
#0  0x00000077c029f31c in __kernel_gettimeofday ()
#1  0x00000077bff7e5b8 in time () from /system/lib64/libc.so
#2  0x0000005aea0e9980 in main () at tell_time.c:36
```

### 断点

- break  普通断点

- watch 观察断点 设置的变量发生改变程序会暂停

    ```gdb
    (gdb) watch info->tm_min
    Hardware watchpoint 1: info->tm_min
    (gdb) c
    Continuing.
    
    Hardware watchpoint 1: info->tm_min
    
    Old value = 35
    New value = 36
    0x00000076ef7a02c0 in timesub () from /system/lib64/libc.so
    ```

- catch  捕捉断点 

### 查看和取消断点

- info 查看所有断点,包括普通断点,观察断点, 捕捉断点

    ```gdb
    (gdb) info breakpoint [n]
    (gdb) info break [n]
    
    参数 n 作为可选参数，为某个断点的编号，表示查看指定断点而非全部断点
    ```

- clear 删除指定位置处的所有断点

        ```gdb
        (gdb) clear location
        
        参数 location 通常为某一行代码的行号或者某个具体的函数名。当 location 参数为某个函数的函数名时，表示删除位于该函数入口处的所有断点。
        ```
    
- delete 可以缩写为 d ）通常用来删除所有断点，也可以删除指定编号的各类型断点

    ```gdb
    delete [breakpoints] [num]
    breakpoints 参数可有可无，num 参数为指定断点的编号，其可以是 delete 删除某一个断点，而非全部。
    
    eg:
    (gdb) info watch
    Num     Type           Disp Enb Address            What
    1       hw watchpoint  keep y                      info->tm_min
            breakpoint already hit 6 times
    (gdb) d 1
    (gdb) info watch
    No watchpoints.
    ```

    #### **无论是普通断点、观察断点还是捕捉断点，都可以使用 clear 或者 delete 命令进行删除。**

- disable 禁用断点

    ```gdb
    disable [breakpoints] [num...]
    
    breakpoints 参数可有可无；num... 表示可以有多个参数，每个参数都为要禁用断点的编号。如果指定 num...，disable 命令会禁用指定编号的断点；反之若不设定 num...，则 disable 会禁用当前程序中所有的断点。
    
    eg:
    (gdb) info break
    Num     Type                   Disp Enb    Address                                     What
    1           breakpoint         keep y        0x0000555555555189 in main  at main.c:2 breakpoint already hit 1 time
    2           hw watchpoint   keep y                                                          num
    3           catchpoint          keep y        exception throw                       matching: int
    (gdb) disable 1 2
    (gdb) info break
    Num     Type                  Disp Enb    Address                                      What
    1           breakpoint        keep n       0x0000555555555189 in main    at main.c:2 breakpoint already hit 1 time
    2           hw watchpoint  keep n                                                           num
    3           catchpoint         keep y       exception throw                          matching: int
    (gdb)
    ```

- enable 激活被禁用的断点

    ```gdb
    enable [breakpoints] [num...]                
    激活用 num... 参数指定的多个断点，如果不设定 num...，表示激活所有禁用的断点
    
    enable [breakpoints] once num…                 
    临时激活以 num... 为编号的多个断点，但断点只能使用 1次，之后会自动回到禁用状态
    
    enable [breakpoints] count num...              
    临时激活以 num... 为编号的多个断点，断点可以使用 count次，之后进入禁用状态
    
    enable [breakpoints] delete num…              
    激活 num.. 为编号的多个断点，但断点只能使用 1 次，之后会被永久删除。
    
    其中，breakpoints 参数可有可无；num... 表示可以提供多个断点的编号，enable 命令可以同时激活多个断点。
    ```







参考:

https://blog.csdn.net/weixin_39630880/article/details/110659763

http://c.biancheng.net/view/8219.html