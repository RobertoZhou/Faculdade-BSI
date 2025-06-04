import socket
import threading
import json
from data_storage import store_data, get_average

HOST = '127.0.0.1'
PORT = 65432

# Dicionário para contar quantas temperaturas foram recebidas por sensor
contador_temperaturas = {}

def handle_client(conn, addr):
    print(f"[NOVA CONEXÃO] {addr} conectado.")
    with conn:
        while True:
            try:
                data = conn.recv(1024)
                if not data:
                    break
                message = json.loads(data.decode())

                if message.get("type") == "query":
                    sensor_id = message.get("sensor_id")
                    avg_data = get_average(sensor_id)
                    conn.sendall(json.dumps(avg_data).encode())
                else:
                    sensor_id = message["sensor_id"]
                    temperatura = message["temperature"]
                    
                    # Armazena a temperatura
                    store_data(sensor_id, temperatura)

                    # Atualiza contador
                    contador_temperaturas[sensor_id] = contador_temperaturas.get(sensor_id, 0) + 1
                    
                    # A cada 5 temperaturas, imprime a média
                    if contador_temperaturas[sensor_id] % 5 == 0:
                        media_info = get_average(sensor_id)
                        print(f"[{sensor_id}] Média de {media_info['data_points']} registros: {media_info['average_temperature']}°C")

            except Exception as e:
                print(f"Erro: {e}")
                break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"[SERVIDOR] Escutando em {HOST}:{PORT}")
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
