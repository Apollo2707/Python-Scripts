import socket 

target_host= ''
target_port = 9999


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    
    
    
    client.connect((target_host,target_port))

    client.send("test".encode())

    response = client.recv(4096)
    
    print(response.decode())
except:
    print ("Connecting failed")


message = ''
while(message != 'q'):
    message = input()
    client.send(message.encode("utf-8"))

    response = client.recv(4096)

    print(response.decode("utf-8"))

