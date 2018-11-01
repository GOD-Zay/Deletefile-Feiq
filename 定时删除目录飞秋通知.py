import os
import shutil
import time
import socket

"""
    删除目录函数 Delete
    发送飞秋通知函数 Feiq
    主函数 main
        检测是否有生成当天的目录文件
            无当天目录则执行Feiq函数
            有当天目录则执行Delete函数
        定时每天执行一次，一个月检测一次脚本是否正常并执行Feiq函数
"""

#删除目录函数 Delete
def Delete(path):
    ds = os.listdir(path)
    for d in ds:
        tmp = os.path.join(path, d)
        if os.path.isfile(tmp):
            print ('file:%s'%tmp)
        else:
            print ('dir:%s'%tmp)
    print (path + '/' + ds[0] + '------正在删除------')
    shutile.rmtree(path + '/' + ds[0])
    print ('------删除完成------')

#发送飞秋通知信息函数 Feiq
def Feiq(ip, message):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#    a = "1:525:name:localhost:32:%s"%message
    s.sendto(a.encode("gbk"),ip)
    s.close()

#主函数 main
def main():
#    path =
#    ip =
#    error =
#    over =
    for i in range(30):
        lf = os.listdir(path)
        t = time.strftime('%Y%m%d', time.localtime())
        if lf[-1] == t:
            print ('------目录正常，正在执行删除操作------')
            Delete(path)
        else:
            return Feiq(ip, error)
            break
        p = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        print ('------定时任务执行完成 ' + p + ' ------')
        print ('------------------------等待下一次执行------------------------')
        time.sleep(86400)
    print ('------每月脚本执行完成------')
    Feiq(ip, over)

if __name__ == '__main__':
    main()
