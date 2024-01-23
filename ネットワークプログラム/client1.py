import socket, sys

ipaddr = '127.0.0.1'
port = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # サーバーを指定
    s.connect((ipaddr, port))
    # サーバーにメッセージを送る
    if len(sys.argv) != 1:
        s.send(str.encode(sys.argv[1]))
    else:
        s.send(b'hello')
    
    data = s.recv(1024)
    
    print(data)