import socket
import json

HOST = '127.0.0.1'
PORT = 65432

sensor_id = input("Digite o ID do sensor para consultar: ")

mensagem = {
    "type": "query",
    "sensor_id": sensor_id
}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(json.dumps(mensagem).encode())
    data = s.recv(1024)
    resposta = json.loads(data.decode())
    print(f"Média do {sensor_id}: {resposta['average_temperature']}°C com {resposta['data_points']} registros.")