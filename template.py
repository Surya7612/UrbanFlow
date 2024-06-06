import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "urbanflow"

list_of_files = [
    f"{project_name}/docker-compose.yml",
    f"{project_name}/kafka_producer/gps_producer.py",
    f"{project_name}/kafka_producer/weather_producer.py",
    f"{project_name}/kafka_producer/emergency_producer.py",
    f"{project_name}/kafka_producer/traffic_producer.py",
    f"{project_name}/spark_consumer/consumer.py",
    f"{project_name}/spark_consumer/validation.py",
    f"{project_name}/api/app.py",
    f"{project_name}/api/models.py",
    f"{project_name}/api/routes.py",
    f"{project_name}/data/vehicle_data.csv",
    f"{project_name}/vehicle_info/vehicle_info_generator.py",
    f"{project_name}/requirements.txt"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory {filedir} for the file {filename}")

    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"File {filepath} already exists")
