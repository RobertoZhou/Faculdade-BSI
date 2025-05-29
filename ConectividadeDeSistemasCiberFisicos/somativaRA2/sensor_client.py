import socket
import json
import time
import random
from datetime import datetime

HOST = '127.0.0.1'
PORT = 65432

sensor_id = input("Digite o ID do sensor: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        temperatura = round(random.uniform(20.0, 30.0), 2)
        mensagem = {
            "sensor_id": sensor_id,
            "temperature": temperatura,
            "timestamp": datetime.now().isoformat()
        }
        s.sendall(json.dumps(mensagem).encode())
        print(f"Enviado: {mensagem}")
        time.sleep(5)
