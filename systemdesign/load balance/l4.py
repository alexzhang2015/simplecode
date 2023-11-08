import socket
import threading

# 后端服务器列表
backends = [('127.0.0.1', 8081), ('127.0.0.1', 8082)] 

# 当前后端服务器索引
backend_index = 0

def print_thread_id():
    print("Current thread ID is: ", threading.get_ident())

def handle_connection(client_socket, client_address):
    """Handle client connection"""
    global backend_index  # 使用全局变量
    
    # Simple round-robin policy to select backend server
    backend = backends[backend_index]
    backend_index = (backend_index + 1) % len(backends)  # 轮询选择后端服务器
    
    # Create socket connection to backend server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(backend)
    
    # Forward data between client and server
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            server_socket.sendall(data)
            data = server_socket.recv(1024)
            client_socket.sendall(data)
    finally:
        client_socket.close()
        server_socket.close()
        
def start_server(host, port):
    """启动负载均衡器"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5) # The argument 5 specifies the maximum number of queued connections.
    
    while True:
        client_sock, client_address = sock.accept()
        thread = threading.Thread(target=handle_connection, args=(client_sock,client_address))
        thread.start()

if __name__ == '__main__':
    # 启动负载均衡器,监听8080端口
    start_server('0.0.0.0', 8080)
