import socket

HOST= "127.0.0.1"
PORT=5000

server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST , PORT))
server.listen()
print("server waiting on port" , PORT)

conn, addr = server.accept()
print("client connected from" , addr)
data= conn.recv(1024).decode()
print("client said: " , data)
conn.sendall(("Server got: " + data).encode())
conn.close()
server.close()