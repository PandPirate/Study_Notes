Windows 11 SSH Server 配置指南
🎯 目标
Windows 11 作为 SSH Server
Linux（如 Arch）通过 SSH 免密登录
---
**管理员打开powershell**
---
一、安装 OpenSSH Server
1. 检查是否已安装
```powershell
Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH.Server*'
```
---
2. 安装（如果未安装）
```powershell
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
```
---
3. 启动服务
```powershell
Start-Service sshd
Set-Service -Name sshd -StartupType Automatic
```
---
4. 开放防火墙
```powershell
New-NetFirewallRule -Name sshd -DisplayName "OpenSSH Server" -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22
```
---
二、SSH 登录说明
用户名示例：
```bash
ssh 12724@192.168.1.22
```
确认用户名：
```
whoami
```
输出类似：theblackpearl\12724， 用户名即12724
---
三、免密登录配置（重点）
管理员用户路径
```
C:\ProgramData\ssh\administrators_authorized_keys
```
---
添加公钥
```powershell
notepad C:\ProgramData\ssh\administrators_authorized_keys
```
---
设置权限
```powershell
icacls C:\ProgramData\ssh\administrators_authorized_keys /inheritance:r
icacls C:\ProgramData\ssh\administrators_authorized_keys /grant Administrators:F
```
---
重启服务
```powershell
Restart-Service sshd
```
---
四、测试登录
```bash
ssh -i ~/.ssh/id_rsa 12724@192.168.1.22
```
---

---
六、总结
管理员用户必须使用：
```
C:\ProgramData\ssh\administrators_authorized_keys
```
管理员确认
```
whoami /groups
```
如果包含**BUILTIN\Administrators**， 即是管理员