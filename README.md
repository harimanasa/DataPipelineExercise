# Software Observability Pipeline (Simulated)

This project simulates a real-time software observability pipeline to monitor microservice performance. It demonstrates how platform engineering or SRE teams can track service health using metrics like latency and error rates.

## Features
- Simulates real-time logs from microservices
- Calculates per-service metrics:
  - Average latency
  - Error rate (% of failed requests)
  - Request count
- Provides both CLI and dashboard-based views (Streamlit)

## Technologies Used
- Python
- pandas
- Streamlit (for dashboard)

## Installation
```bash
pip install pandas streamlit

## How to Run

### 1. CLI Mode (Print metrics in terminal)
```bash
python iot_pipeline_simulation.py

### 2. Dashboard Mode (Streamlit UI)
streamlit run iot_pipeline_simulation.py dashboard

### 3. Sample Log Format
{
  "service": "auth-service",
  "timestamp": "2025-04-30T10:01:00Z",
  "status_code": 200,
  "latency_ms": 350,
  "error": false
}

### 4. Stretch Goals

- Add SLO alerting (e.g., if error rate > 2%)
- Simulate load spikes and autoscaling
- Add log persistence using SQLite or S3
- Deploy dashboard to Streamlit Cloud
