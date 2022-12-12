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
