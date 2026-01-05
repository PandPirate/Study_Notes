# usb网卡
```
1. 查看usb网卡信息
lsusb
Bus 001 Device 005: ID 0bda:1a2b Realtek Semiconductor Corp. RTL8188GU 802.11n WLAN Adapter (Driver CDROM Mode)

虽然识别出来USB设备了，但只是作为一个存储设备。根本没有任何网卡功能。
必须先把无线网卡的工作模式从存储切换到网卡才行

2. 安装USB设备切换模式软件
sudo pacman -S usb_modeswitch

3. 查看设备详细信息
sudo usb_modeswitch -v 0bda -p 1a2b -W

4. 切换无线网卡工作模式
sudo usb_modeswitch -KW -v 0bda -p 1a2b

5. 查看USB设备信息
lsusb -tv
Bus 001 Device 007: ID 0bda:c811 Realtek Semiconductor Corp. 802.11ac NIC

无线网卡使用的是rtw_8821cu驱动，并非USB光驱模式的8188GU，这点需要注意。至此已经切换为无线网卡模式。

```
# rtw_8821cu驱动
https://github.com/brektrou/rtl8821CU

## 手动安装
## 使用社区打包好的AUR版本
```
paru rtl8821cu-dkms-git
https://github.com/morrownr/8821cu-20210916
```

# DKMS
DKMS（Dynamic Kernel Module Support） 是一个 自动为内核编译和安装驱动模块 的系统。
简单说，它让第三方驱动（比如显卡驱动、VirtualBox、VMware、ZFS、WiFi 模块等）
在你更新内核后还能自动重新编译、自动可用

```
假设你安装了一个第三方驱动，比如：
    - NVIDIA 显卡驱动
    - VirtualBox 内核模块
    - Realtek WiFi 驱动
这些驱动不是 Linux 内核自带的，而是额外安装的。
每次你更新内核（例如从 6.16.7 升级到 6.16.8）时，旧模块就会失效。
如果有了 DKMS：
系统检测到内核更新时，
会自动调用 dkms build 和 dkms install，
为新内核编译并安装对应版本的模块。
所以内核更新后，你的驱动仍然能用。
```

| 命令                  | 功能说明              |
| ------------------- | ----------------- |
| `dkms status`       | 查看已注册的 DKMS 模块及状态 |
| `dkms add <模块>`     | 注册一个新模块           |
| `dkms build <模块>`   | 编译模块              |
| `dkms install <模块>` | 安装模块              |
| `dkms remove <模块>`  | 移除模块              |
| `dkms autoinstall`  | 为当前内核自动构建所有模块     |

### 安装路径
DKMS 模块一般位于：/usr/src/<模块名>-<版本号>/
构建出的模块会被安装到：/lib/modules/<内核版本>/extra/
# iw
iw 是一个命令行工具，用来 管理和配置无线网卡（Wi-Fi），功能比老旧的 iwconfig 更强大。
它直接与内核的 cfg80211/mac80211 驱动交互。

## 常用命令
```
1. 查找无线接口
iw dev
phy#0
    Interface wlan0
        ifindex 3
        wdev 0x1
        addr 12:34:56:78:9a:bc
        type managed
        txpower 20.00 dBm
-------------------------------------------
2. 扫描可用 Wi-Fi
sudo iw dev wlan0 scan | less
-------------------------------------------
3. 切换模式（管理/监控）
sudo ip link set wlan0 down
sudo iw dev wlan0 set type monitor
sudo ip link set wlan0 up
-------------------------------------------
4. 设置传输功率
sudo iw dev wlan0 set txpower fixed 2000  # 单位 mBm（2 dBm）

```
## 设置ap模式
1. 无线网卡驱动必须支持 AP/Hostap 模式
2. 内核必须启用 mac80211 和 cfg80211 支持
```
1. 检查 AP 支持
iw list | grep -A 10 "Supported interface modes"
如果输出没有 AP，说明你当前驱动不支持热点模式，需要换成支持 AP 的 RTL8821CU 驱动，例如 AUR 上 rtl8821cu-dkms-git 的版本。
2. 安装 hostapd
sudo pacman -S hostapd
3. 配置hostapd /etc/hostapd/hostapd.conf
interface=wlan0
driver=nl80211
ssid=MyHotspot
hw_mode=g
channel=6
auth_algs=1
wpa=2
wpa_passphrase=12345678
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP CCMP
rsn_pairwise=CCMP

4. 启动 hostapd
sudo ip link set wlan0 up
sudo hostapd /etc/hostapd/hostapd.conf

5. 给 AP 分配 IP

6. 修改防火墙配置

```
## iw list
iw list 是一个非常有用的命令，用于查看无线网卡（Wi-Fi 接口）的硬件能力与驱动支持的模式。
```
部分输出
Supported interface modes:
                 * IBSS
                 * managed
                 * AP
                 * AP/VLAN
                 * monitor
```
| 字段                      | 说明                     |
| ----------------------- | ---------------------- |
| **managed**             | STA（客户端）模式，用于连接路由器     |
| **AP**                  | Access Point 模式（热点模式）|
| **AP/VLAN**             | 多 SSID 支持（部分驱动）        |
| **monitor**             | 监听模式（抓包用）              |
| **P2P-client / P2P-GO** | Wi-Fi Direct 支持        |
| **IBSS**                | Ad-hoc 自组网模式           |


# ip
ip 是 Linux 下最常用的网络命令之一，
用来查看、配置、修改网络接口、路由、IP 地址等
## 常用命令
```
1. 查看所有网卡与 IP 地址
ip addr show 或简写 ip a
2. 查看路由表
ip route show 或简写 ip r
3. 查看链路状态（UP / DOWN）
ip link show
ip link show wlp0s20u2
4. 设置静态 IP
sudo ip addr add 192.168.50.1/24 dev wlp0s20u2
5. 删除 IP
sudo ip addr del 192.168.50.1/24 dev wlp0s20u2
6. 启用 / 禁用接口
sudo ip link set wlp0s20u2 up/down
7. 查看某接口的状态详细信息
ip -s link show wlp0s20u2



```
# bridge
所有 slave 接口都 down → bridge 也会 down
```
1. ip link
2. ip link set ethusb0 up
3. sudo ip link set ethusb0 master br0 把接口重新加入bridge
4. ip link set br0 up
5. 如果br0IP丢了 重新设置ip
sudo ip addr add 192.168.1.1/24 dev br0
