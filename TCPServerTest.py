import socket
import threading 


bind_ip = "127.0.0.1"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)

print ("[*] Listening on ",bind_ip,":",bind_port)
def handle_client(client_socket):

    #reads a 1024 bit packet
    request = client_socket.recv(1024).decode()

    print ("Action report: ", request)

    #send back a packet
    client_socket.send("ROG!".encode())

    client_socket.close()

while True:

    client,addr = server.accept()   

    print ("[!] Message from the front ", addr[0], ":",addr[1])

    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()