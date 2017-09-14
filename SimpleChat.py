import socket 

target_host = "127.0.0.1"
target_port = 9999

target_host = input("Enter IP: ")

try:
    
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    client.connect((target_host,target_port))

    client.send("test".encode())

    response = client.recv(4096)
    
    print(response.decode())
except:
    print ("Connecting failed")




