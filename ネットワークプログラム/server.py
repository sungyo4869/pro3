import socket

ipaddr = '127.0.0.1'
port = 50007

# ソケットを作成
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # IPアドレスとポートを指定
    s.bind((ipaddr, port))
    
    # 接続待ち
    s.listen()
    
    while True :
        # 誰かがアクセスしてきたら、コネクションとアドレスを入れる
        conn, addr = s.accept()
        with conn:
            while True:
                # データを受け取る
                data = conn.recv(1024)
                if not data:
                    print("データないよ")
                    break
                print('data : {}, addr: {}' .format(data, addr))
                # クライアントにデータを返す
                # (b -> byte でないといけない)
                break
                
            conn.send(b'Received: ' + data)