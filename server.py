import socket

host_ip='localhost'
host_socket=5000
full_addr='http://'+host_ip+':'+str(host_socket)
print('open and connect to',full_addr)

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock_listen=(host_ip,host_socket)

sock.bind(sock_listen)

sock.listen()

connection,address=sock.accept()
print('got the conenction from',address)