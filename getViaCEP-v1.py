import socket

HOST = 'viacep.com.br'
PORT = 80
CEP = "59064250"

sockTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockTCP.connect((HOST,PORT))

sockTCP.send(("GET /ws/"+CEP+"/json/ HTTP/1.1\r\n"+"HOST:"+HOST+"\r\n"+"\r\n").encode("utf-8"))
data = sockTCP.recv(4096)

print(data.decode("utf-8"))

sockTCP.close()