import os, sys, subprocess, re, time
from moduels.component.NormalValue import 常量


def wirelessAdb():
    重试次数 = 4
    adb端口 = 5555

    print('先断开所有 adb 连接')
    print(subprocess.run('adb disconnect', startupinfo=常量.subprocessStartUpInfo, capture_output=True, encoding='utf-8').stdout)

    Shell查找手机IP命令 = r'adb shell "ip address | grep inet | grep wlan | grep -v inet6 | grep -v 127\.0\.0\.1"'
    for 尝试序号 in range(重试次数):
        shell查找ip = subprocess.run(Shell查找手机IP命令, capture_output=True, encoding='utf-8', startupinfo=常量.subprocessStartUpInfo).stdout
        if not shell查找ip:
            print('无法找到手机在局域网中的 ip')
            if 尝试序号 < 1:
                subprocess.run('adb shell svc wifi enable', startupinfo=常量.subprocessStartUpInfo)
                print('已尝试使用 adb 命令打开 wifi，等待 3 秒')
                for i in range(3, 0, -1):
                    print(i)
                    time.sleep(1)
                continue
            if 尝试序号 < 重试次数 - 1:
                print(f'第 {尝试序号 + 1} 次尝试未找到手机在局域网中的 ip，等待 3 秒（最多再尝试 {重试次数 - 尝试序号 - 1} 次）')
            else:
                print(f'第 {尝试序号 + 1} 次尝试未找到手机在局域网中的 ip，不再尝试')
                return False
            for i in range(3, 0, -1):
                print(i)
                time.sleep(1)
            continue
        break
    手机在Wifi下的IP = re.search(r'\d+\.\d+\.\d+\.\d+', shell查找ip).group(0)
    print(f'得到手机的wifi下的ip为：{手机在Wifi下的IP}')
    subprocess.run(f'adb tcpip {adb端口}', capture_output=True, startupinfo=常量.subprocessStartUpInfo) # 打开端口
    adb连接返回 = subprocess.run(f'adb connect {手机在Wifi下的IP}:{adb端口}', capture_output=True, encoding='utf-8', startupinfo=常量.subprocessStartUpInfo) # 连接
    if re.match('^connected', adb连接返回.stdout):
        print(f'连接成功：{adb连接返回.stdout}')
        return True
    else:
        print(f'连接失败：{adb连接返回.stdout}')
        return False