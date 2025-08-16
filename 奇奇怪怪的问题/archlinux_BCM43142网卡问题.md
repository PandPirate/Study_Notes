# BCM43142
BCM43142 是一块无线网卡

Linux 内核自带的 b43 / brcmsmac / brcmfmac 都不支持 BCM43142。

唯一能驱动它的就是 闭源的 broadcom-wl (wl) 驱动.
wl 驱动闭源、不维护，和新内核的安全补丁、调度器兼容性差，所以内核日志会出现：

```
wl: module license 'MIXED/Proprietary' taints kernel.
You are using the broadcom-wl driver, which is not maintained...
```

## 可选方案
### 1. 继续用broadcom-wl
```bash
# Arch Linux
sudo pacman -S broadcom-wl-dkms
```
### 2. 禁用BCM43142
```bash
# 永久禁用 开机不加载

# 1. 创建黑名单文件
sudo tee /etc/modprobe.d/blacklist-wl.conf <<EOF
blacklist wl
blacklist bcma
blacklist brcmsmac
blacklist b43
EOF

# 2. 更新 initramfs（Arch Linux）
sudo mkinitcpio -P
```
### 3. 更换无线网卡
更换无线网卡
BCM43142 用的是 Mini PCIe 或 M.2 接口，可以直接换掉。

推荐 Intel AX200 / AX210 / AX211，开源驱动 iwlwifi，Linux 内核原生支持，性能好且非常稳定。