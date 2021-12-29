# ArchLinux Clash 安装

##  1 下载安装clash
+ 方法一    paru clash
+ 方法二  https://github.com/Dreamacro/clash 选择合适版本下载
	运行clash  在 ~/.config 会生成clash目录 包含cache.db config.yaml Country.mmdb

##  2 配置clash
从代理商拿到config.yam 文件把内容复制过来
	如果只有连接的话 在浏览器l中输入连接 下载文件
	==修改外部控制设置（external-controller）地址为：0.0.0.0:9990，==
##  3 设置clash 为开机自启
+  在 /usr/lib/systemd/user 目录中 创建clash.service 

```
[Unit]
Description=A rule based proxy in Go
After=network.target

[Service]
Type=exec 
Restart=on-abort
ExecStart=/usr/bin/clash

[Install]
WantedBy=default.target
```
+ 把clash二进制文件移到/usr/bin/clash目录下
+ 把clash配置文件（cache.db config.yaml Country.mmdb） 移入 /etc/clash
+ 'sudo systemctl daemon-reload 重新加载 systenctl'  
+ 管理clash.service命令
 'sudo systemctl enable clash.service   设置开机自启'
 'sudo systemctl disable clash.service   关闭开机自启'
 'sudo systemctl start clash.service  启动'
 'sudo systemctl stop clash.service 关闭'

参考 https://wiki.archlinux.org/title/Systemd_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)/User_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)#%E5%B7%A5%E4%BD%9C%E5%8E%9F%E7%90%86

##  4 为git chrome 设置代理

方法一 ： 使用proxyman-git 
	'paru proxyman-git'
	==把~/.local/bin 加入环境变量 如果没有此目录创建并把proxyman复制过去==
方法二： 在.bashrc中添加如下
	'''
	# 端口号 7890 需要和  config.yaml 中的保持一致 默认为7890
	 export http_proxy="http://127.0.0.1:7890/"
	  export https_proxy="http://127.0.0.1:7890/" 
	  export HTTP_PROXY="http://127.0.0.1:7890/"
	  export HTTPS_PROXY="http://127.0.0.1:7890/"
	 export rsync_proxy="rsync://127.0.0.1:7890/"
	 export RSYNC_PROXY="rsync://127.0.0.1:7890/"
	 export no_proxy="localhost,127.0.0.1,192.168.1.1,::1,*.local"
	 
	 #proxy-on 使用代理   
	  function proxy-on(){
	   	gsettings set org.gnome.system.proxy mode "manual"
	  }
	  # proxy-off 关闭代理
	  function proxy-off(){ 
	    gsettings set org.gnome.system.proxy mode none
	   }
	   
	   #clash-on 打开clash并且打开代理
	   alias clash-on='sudo systemctl start clash.service && gsettings set org.gnome.system.proxy mode "manual" ' 
	   #clash-off 关闭clash并且关闭代理
	    alias clash-off='sudo systemctl stop clash.service && gsettings set org.gnome.system.proxy mode none ' 
	   #clash-status 查看clash服务的状态
	    alias clash-status='sudo systemctl status clash.service'  
	'''
参考https://wiki.archlinux.org/title/Proxy_server_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)
## 5 查看代理是否正常工作
'curl www.google.com'

参考：https://zhuanlan.zhihu.com/p/396272999
