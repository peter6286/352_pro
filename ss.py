import threading
import time
import random

import socket

try:
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[S]: Server socket created")
except socket.error as err:
    print('socket open error: {}\n'.format(err))
    exit()

server_binding = ('', 50007)
ss.bind(server_binding)
ss.listen(1)
host = socket.gethostname()
print("[S]: Server host name is {}".format(host))
localhost_ip = (socket.gethostbyname(host))
print("[S]: Server IP address is {}".format(localhost_ip))
csockid, addr = ss.accept()
print("[S]: Got a connection request from a client at {}".format(addr))

while True:     # 一个死循环，直到客户端发送‘exit’的信号，才关闭连接
    client_data = csockid.recv(1024).decode()      # 接收信息
    if client_data == "":       # 空格判断是否退出连接
        exit("通信结束")
    #print(client_data)
    str = client_data
    #print(type(str))
    #print(temp)
    temp=(str[::-1])
    result=temp+str
    #print(result)
    print("来自%s的客户端向你发来信息：%s" % (addr, client_data))
    print("最终结果：%s" % (result))
    #print("来自%s的客户端向你发来信息：%s" % (addr, client_data))
    csockid.send(result.encode())    # 回馈信息给客户端

# send a intro message to the client.
#msg = "Welcome to CS 352!"
#csockid.send(msg.encode('utf-8'))

# Close the server socket
conn.close()
ss.close()
exit()
