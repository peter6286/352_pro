#! /usr/bin/python
import threading
import time
import random
import socket

try:
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[C]: Client socket created")
except socket.error as err:
    print('socket open error: {} \n'.format(err))
    exit()

# Define the port on which you want to connect to the server
port = 50007
localhost_addr = socket.gethostbyname(socket.gethostname())

# connect to the server on local machine
server_binding = (localhost_addr, port)
cs.connect(server_binding)

result=[]
i=0
for line in open("in-proj0.txt"):
    result.append(line.strip('\n')) #将空行去掉
#print(result)
#while True:     # 通过一个死循环不断接收用户输入，并发送给服务器
for ll in result:
    print("[%d],%s" % (i,ll))
    inp = ll
    if not inp:     # 防止输入空信息，导致异常退出
        continue
    cs.send(inp.encode())

    #if inp == "exit":   # 如果输入的是‘exit’，表示断开连接
    #    print("结束通信！")
    #    break

    server_reply = cs.recv(1024).decode()
    print("来自server向你发来信息：[%d]clea%s" % (i,server_reply ))
    f = open("out-proj0.txt",'a') #读取label.txt文件，没有则创建，‘a’表示再次写入时不覆盖之前的内容
    f .write(server_reply)
    f.write('\n')
    i=i+1
    # Receive data from the server
    #data_from_server = cs.recv(100)
    #print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))

# close the client socket
cs.close()
exit()