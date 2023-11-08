import socket
import time

def start_client(server_ip, server_port):
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        client_socket.connect((server_ip, server_port))
    except socket.error as e:
        print(f"Error connecting to server: {e}")
        return

    while True:
        try:
            client_socket.send('Hello from client'.encode())
            data = client_socket.recv(1024)
            print('Received from server:', data.decode())

            # 模拟客户端做一些工作
            time.sleep(5)
        except socket.error as e:
            print(f"Error sending/receiving data: {e}")
            break

    client_socket.close()

if __name__ == "__main__":
    start_client('127.0.0.1', 8080)
