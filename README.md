# UrbanFlow: Real-time Smart City Data Streaming and Analysis

## Overview
UrbanFlow is a comprehensive data streaming pipeline designed to enhance smart city infrastructure. It ingests, processes, and analyzes real-time data from various sources such as IoT devices, weather APIs, and traffic APIs. The system provides insights for traffic management, public safety, and environmental monitoring, ensuring efficient and proactive urban management.

## Features
- **Real-time Data Ingestion**: Collects data from GPS, weather, traffic, and emergency sources.
- **Scalability**: Utilizes Apache Kafka and Spark for scalable data streaming and processing.
- **Data Integration**: Integrates multiple data sources for a comprehensive view of urban conditions.
- **Visualization**: Uses Power BI for real-time data visualization.
- **Security**: Implements data encryption and access control using AWS services.
- **API Integration**: Provides an API for external interaction and data retrieval.

## Technologies Used
- **Apache Kafka**: Data streaming platform.
- **Apache Spark**: Real-time data processing.
- **Docker**: Containerization.
- **Flask**: API development.
- **AWS Glue, Athena, Redshift**: Data cataloging, querying, and storage.
- **Power BI**: Data visualization.
- **Python**: Core programming language.
- **REST APIs**: Integration with external weather and traffic data sources.

## Project Structure
```bash
urbanflow/
├── docker-compose.yml
├── kafka_producer/
│   ├── gps_producer.py
│   ├── weather_producer.py
│   ├── emergency_producer.py
│   ├── traffic_producer.py
├── spark_consumer/
│   ├── consumer.py
│   ├── validation.py
├── api/
│   ├── app.py
│   ├── models.py
│   ├── routes.py
├── data/
│   └── vehicle_data.csv
├── vehicle_info/
│   ├── vehicle_info_generator.py
└── requirements.txt
```

## Getting Started

### Prerequisites
- Docker
- Python 3.6+
- AWS Account (for AWS services)

### Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Surya7612/UrbanFlow.git
   cd UrbanFlow
   cd urbanflow
   ```
2. **Generate Vehicle Data**
    ```bash
    python vehicle_info/vehicle_info_generator.py
    ```
3. **Start Docker Containers**
    ```bash
    docker-compose up -d
    ```
4. **Install Python Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
5. **Run Kafka Producers**
    ```bash
    python kafka_producer/gps_producer.py
    python kafka_producer/weather_producer.py
    python kafka_producer/traffic_producer.py
    python kafka_producer/emergency_producer.py
    ```
6. **Run Spark Consumer**
    ```bash
    python spark_consumer/consumer.py
    ```
7. **Run Flask API**
    ```bash
    python api/app.py
    ```

### API Endpoints

- **Add Vehicle Data**

    - URL: /vehicle
    - Method: POST
    - Payload:
    ```bash
    {
    "vehicle_id": "vehicle_1",
    "latitude": 40.7128,
    "longitude": -74.0060,
    "temperature": 22.5,
    "condition": "sunny",
    "traffic": "heavy",
    "emergency_type": "none",
    "severity": "low"
    }
    ```
### Future Enhancements
- **Predictive Analytics**: Implement machine learning models to predict traffic congestion, accident likelihood, and optimal routes.
- **Anomaly Detection**: Use ML models to detect anomalies in data, such as unusual traffic patterns or sudden weather changes.
- **User Notifications**: Add a notification system to alert users about traffic conditions, weather changes, or emergencies in real-time.

### Contributors
- Surya Nediyadeth

### License
- This project is licensed under the MIT license