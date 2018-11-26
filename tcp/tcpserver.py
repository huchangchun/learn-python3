#encoding=utf8
import socket
import threading
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1',9999))
s.listen(5) #5表示设置最大连接数
print("Waiting for connection.........")
#每个连接都必须创建新线程或进程来处理，否则，单线程在处理连接的过程中，无法接受其他客户端的连接
def tcplink(sock, addr):
    print("Accept new connection from %s:%s..." %addr)
    sock.send(b'Welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(("hello, %s!" %data.decode("utf-8")).encode("utf-8"))
    sock.close()
    print('Connection from %s :%s colosed' %addr) 
while True:
    #接受一个新连接
    sock,addr=s.accept()
    #创建新线程来处理TCP连接：
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

