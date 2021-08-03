import paramiko
import os
import subprocess


host_ip = '192.168.1.175'
host_name = 'root'
passwd = '820@zongmutech'


def ssh_connect():
    if os.system('ping -c 1 -W 1 {}'.format(host_ip)):
        print("current ssh connect is faild")
        return
    print("current ssh connect is succeeded")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host_ip, port=22, username=host_name, password=passwd)
    stdin, stdout, stderr = ssh.exec_command('mount -o rw,remount /')
    check_dir(ssh)


def check_dir(ssh):
    # 判断/data/zros/是否为空
    stdin, stdout, stderr = ssh.exec_command("timeout 3 rmdir /data/zros/")
    if stdout:
        # 假设为空，创建/data/zros/文件夹后直接推送文件,default.xml和defaultDevice文件不存在
        print("/data/zros/ is existence")
        stdin, stdout, stderr = ssh.exec_command("mkdir /data/zros/")
        if stdout:
            # 假设创建成功
            print("/data/zros/ is create successfully")
            push_tar(ssh)
        else:
            # 假设创建失败
            print("/data/zros/ is create failed")
    else:
        # 假设不为空，备份文件后删除文件，再进行推送，default.xml和defaultDevice文件存在
        print("/data/zros/ is not existence")
        res = subprocess.call(
            'adb pull -p /data/zros/res/car_instance/default.xml {}'.format(defaultxml), shell=True)
        res = subprocess.call(
            'adb pull -p /data/zros/res/car_instance/defaultDevice {}'.format(defaultDevice), shell=True)


def push_tar(ssh):
    res = subprocess.call(
        'adb push -p {} /data/zros/'.format(TARFILE_PATH), shell=True)
    if not res:
        # 推送成功,进行解压
        print("{} push success".format(TARFILE_PATH))
        stdin, stdout, stderr = ssh.exec_command(
            "cd /data/zros/ \n tar -zxvf {}".format(TARFILE_PATH))
        if stdout:
            # 假设解压成功
            print("{} unzip success".format(TARFILE_PATH))
            push_default(ssh)
        else:
            # 假设解压失败
            print("{} unzip failed".format(TARFILE_PATH))
    else:
        # 推送失败
        print("{} push failed".format(TARFILE_PATH))


def push_default(ssh):
    if default_existent:
        # default.xml和defaultDevice文件存在
        print("default.xml and defaultDevice has old version")
        res = subprocess.call(
            'adb push -p {} /data/zros/res/car_instance/'.format(defaultxml), shell=True)
        res = subprocess.call(
            'adb push -p {} /data/zros/res/car_instance/'.format(defaultDevice), shell=True)
    else:
        # default.xml和defaultDevice文件不存在
        print("default.xml and defaultDevice not has old version")


def main():
    ssh_connect()


if __name__ == '__main__':
    main()
