import paramiko
import getpass
import pdb

def main():
    remote_host = "122.51.163.86"
    remote_port = "22"
    remote_user = "ubuntu"
    remote_passwd = getpass.getpass(
        f"please password for {remote_host}:{remote_user}\n")
    cmd = "ls -1"

    ssh = paramiko.SSHClient()
    # 允许连接不在know_hosts文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(
            hostname=remote_host,
            port = remote_port,
            username = remote_user,
            password = remote_passwd
        )
    except Exception as e:
        print(f"connect error: {e}")
    print("connect successful")
    _, output, _ = ssh.exec_command(cmd)
    pdb.set_trace()
    print(f"cmd output {output.read().decode()}")

    ssh.close()

main()