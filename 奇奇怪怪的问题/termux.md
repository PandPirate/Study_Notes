# 安装archlinux

1. apt update
2. 安装proot
3. 下载安装脚本wget https://gitee.com/brx86/brx86/raw/web/arch.sh
4. bash arch.sh
5. ./startarch.sh

## 修改时区

1. 使用timedatectl status  检查当前时区

2.  timedatectl list-timezones  显示可用时区

3. timedatectl set-timezone <Zone>/<SubZone>  修改时区

    eg: timedatectl set-timezone Asia/Shanghai

    此命令会创建一个`/etc/localtime`软链接，指向`/usr/share/zoneinfo/`中的时区文件，如果手动创建此链接请确保是相对链接而不是绝对链接

    ###  或者直接生成一个软连接   ln -sf /usr/share/zoneinfo/Region（地区名）/City（城市名） /etc/localtime