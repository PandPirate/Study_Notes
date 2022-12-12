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

