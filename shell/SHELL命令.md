# SHELL命令

###  timeout   **指定运行的命令最大运行时长，时间到则终止该命令**

```shell
# 5分钟之后终止ping操作
timeout 5 ping www.baidu.com   
# 1天之后终止ping操作
timeout 1d ping www.baidu.com
# 2.5秒之后终止ping操作
```
- 当达到时间限制时，timeout将SIGTERM信号发送到受管命令。可以使用-s（-signal）选项指定要发送的信号
 ```shell
# 5秒钟后timeout 发送SIGKILL信号给ping命令
sudo timeout -s SIGKILL 5s ping www.baidu.com
# 5秒钟后timeout 发送9号信号（即SIGKILL）给ping命令
sudo timeout -s 9 5s ping www.baidu.com
 ```
- 运行在前台

    ```shell
    # timeout在后台运行托管命令。如果要在前台运行该命令，请使用--foreground选项
    timeout --foreground 5m ./script.sh
    ```

参考: https://blog.csdn.net/bandaoyu/article/details/116450256

### shell后台运行

- 使用ctrl+z把当前正在运行的进程切换到后台并暂停,使用bg number让其在后台运行,number是通过jobs查询得到

    ```bash
    ~/test $ ls
    chibifu  log  ooo.sh  test  test.c
    ~/test $ cat test.c
    void main(void)
    {
            while(1) sleep(1);
    }
    ~/test $ ./test
    ^Z
    [1]+  Stopped                 ./test
    ~/test $ jobs
    [1]+  Stopped                 ./test
    ~/test $ bg 1
    [1]+ ./test &
    ~/test $ jobs
    [1]+  Running                 ./test &
    ~/test $
    ```

- 直接在命令后添加&使其在后台运行

    ```bash
    ~/test $ ./test &
    [1] 31350
    ~/test $ jobs
    [1]+  Running                 ./test &
    ~/test $ ps -elf | grep test
    0 S u0_a132  31350 23317  0  70 -10 -  2305 hrtime  1970 pts/2    00:00:00 ./test
    0 S u0_a132  31354 23317  1  70 -10 -  2480 pipe_w  1970 pts/2    00:00:00 grep test
    ```

- 不中断后台运行脚本 nohup

        ```bash
        ~/test $ nohup ./test &
        [1] 31376
        ~/test $ nohup: ignoring input and appending output to 'nohup.out'
        ls
        chibifu  log  nohup.out  ooo.sh  test  test.c
        ~/test $ jobs
        [1]+  Running                 nohup ./test &
        ```
    
        ####  不中断的在后台运行test.sh：nohup ./test.sh &（test.sh的打印信息会输出到当前目录下的nohup.out中）退出当前shell终端，再重新打开，使用jobs看不到正在运行的test.sh，但使用ps -ef可以看到

- 使用setsid将其父进程改为init进程（进程号为1）
  
        ```bash
        ~/test $ setsid ./test &
        [1] 31507
        ~/test $ ps -ef | grep test
        u0_a132  31508     1  0  1970 ?        00:00:00 ./test
        u0_a132  31511 23317  2  1970 pts/2    00:00:00 grep test
        [1]+  Done                    setsid ./test
        ```
        
        #### 不中断的在后台运行test.sh另一个命令：setsid ./test.sh &
        
        #### 使用ps -ef |grep test.sh可看到test.sh进程的父进程id为1
    

参考: https://blog.csdn.net/londa/article/details/115698093

### wc   **统计行数、单词数、字节数/字符数**

- 语法：`wc [选项]... [文件]...`，无文件时从标准输入读入；多文件时逐个统计并输出total总计行

```shell
# 无参数时输出三列：行数  单词数  字节数  文件名
wc test.txt
# 5  23  190  test.txt
# 从管道读入时不显示文件名
echo "hello world" | wc
#       1       2      12
```

- 常用选项
    - `-l` 行数（实际统计换行符个数）
    - `-w` 单词数（按空格/Tab/换行等空白字符切分）
    - `-c` 字节数
    - `-m` 字符数（按locale编码，UTF-8下1个汉字=1字符、3字节）
    - `-L` 最长一行的长度

```shell
# 统计行数
wc -l *.py
# 递归统计所有.py文件行数（多文件末尾会输出total总计）
find . -name '*.py' | xargs wc -l
# 统计当前进程数
ps aux | wc -l
# 检查是否有超过80列的行
wc -L *.py
```

- 易错点

    ```shell
    # 1. wc -l 数的是换行符\n：最后一行没有结尾换行符就不计数
    printf 'a'   | wc -l   # 0
    printf 'a\n' | wc -l   # 1
    # 2. 字节 vs 字符：UTF-8下汉字占3字节
    echo "中文" | wc -c   # 7  （6字节 + 换行）
    echo "中文" | wc -m   # 3  （2汉字 + 换行）
    # 3. 中文无空格时按一个"词"计算
    echo "你好世界" | wc -w   # 1
    # 4. locale不支持多字节时（如LC_ALL=C），-m等价于-c
    LC_ALL=C wc -c test.txt
    ```

参考: https://www.gnu.org/software/coreutils/manual/html_node/wc-invocation.html
