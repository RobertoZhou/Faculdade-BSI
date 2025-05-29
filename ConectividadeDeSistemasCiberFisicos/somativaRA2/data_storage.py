from collections import defaultdict

sensor_data = defaultdict(list)

def store_data(sensor_id, temperature):
    sensor_data[sensor_id].append(temperature)

def get_average(sensor_id):
    dados = sensor_data.get(sensor_id, [])
    if dados:
        media = sum(dados) / len(dados)
        return {
            "sensor_id": sensor_id,
            "average_temperature": round(media, 2),
            "data_points": len(dados)
        }
    return {
        "sensor_id": sensor_id,
        "average_temperature": None,
        "data_points": 0
    }