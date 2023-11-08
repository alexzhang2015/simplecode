import socket
from threading import Thread
import datetime

class ClientThread(Thread):
    def __init__(self, conn, server_name):
        Thread.__init__(self)
        self.conn = conn
        self.server_name = server_name

    def run(self):
        try:
            while True:
                data = self.conn.recv(1024)
                if not data:
                    break
                print('Received:', data.decode())
                timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                response = 'Response from {} at time {} with thread ID {}'.format(
                    self.server_name, timestamp, self.ident)
                self.conn.send(response.encode())
        except Exception as e:
            print('Error:', e)
        finally:
            self.conn.close()

class BackendServer(Thread):
    def __init__(self, name, ip, port):
        Thread.__init__(self)
        self.name = name
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  
        self.sock.bind((self.ip, self.port))

    def run(self):
        self.sock.listen(5)
        while True:
            conn, addr = self.sock.accept()
            client_thread = ClientThread(conn, self.name)
            client_thread.start()

if __name__ == '__main__':
    # 生成两个后端服务器
    server1 = BackendServer('server1', '127.0.0.1', 8081)
    server2 = BackendServer('server2', '127.0.0.1', 8082)
    server1.start()
    server2.start()
