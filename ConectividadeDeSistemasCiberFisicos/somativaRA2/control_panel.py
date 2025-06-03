import socket
import json

# Solicita IP e porta do servidor
HOST = input("Digite o IP do servidor: ")
PORT = int(input("Digite a porta do servidor: "))
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

    if resposta["average_temperature"] is not None:
        print(f"Média do {sensor_id}: {resposta['average_temperature']}°C com {resposta['data_points']} registros.")
    else:
        print(f"Nenhum dado encontrado para o sensor '{sensor_id}'.")
