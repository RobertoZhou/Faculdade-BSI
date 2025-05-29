import socket
import threading
import json
from data_storage import store_data, get_average

HOST = '127.0.0.1'
PORT = 65432

def handle_client(conn, addr):
    print(f"[NOVA CONEXAO] {addr} conectado.")
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
                    store_data(message["sensor_id"], message["temperature"])
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