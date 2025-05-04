# Simulated Software Engineering Observability Pipeline (Ready-to-Run Demo)
# Requires: pandas, streamlit (for optional dashboard)

import random
import time
import json
from datetime import datetime
import pandas as pd
import streamlit as st

# Simulate microservice log generation
def generate_log():
    services = ["auth-service", "payment-service", "catalog-service", "user-service"]
    status_codes = [200, 200, 200, 200, 500, 502, 503, 404]
    log = {
        "service": random.choice(services),
        "timestamp": datetime.utcnow().isoformat(),
        "status_code": random.choice(status_codes),
        "latency_ms": random.randint(50, 1000),
        "error": False
    }
    log["error"] = log["status_code"] >= 500
    return log

# Simulate a stream of logs
def simulate_logs(n=100):
    logs = []
    for _ in range(n):
        logs.append(generate_log())
        time.sleep(0.01)  # simulate streaming delay
    return logs

# Aggregation logic
def aggregate_logs(logs):
    df = pd.DataFrame(logs)
    grouped = df.groupby("service").agg(
        total_requests=("service", "count"),
        avg_latency=("latency_ms", "mean"),
        error_rate=("error", "mean")
    ).reset_index()
    grouped["error_rate"] = grouped["error_rate"] * 100
    return grouped

# Main logic for notebook or CLI
def run_pipeline():
    print("Generating sample logs...")
    logs = simulate_logs(200)
    df = pd.DataFrame(logs)
    summary = aggregate_logs(logs)
    print("--- Full Logs ---")
    print(df.head())
    print("--- Aggregated Metrics ---")
    print(summary)

# Optional Streamlit dashboard
def run_dashboard():
    st.title("Microservice Observability Dashboard")
    logs = simulate_logs(200)
    df = pd.DataFrame(logs)
    agg = aggregate_logs(logs)

    st.subheader("Raw Logs")
    st.dataframe(df)

    st.subheader("Aggregated Metrics")
    st.dataframe(agg)

    st.bar_chart(agg.set_index("service")["avg_latency"])
    st.bar_chart(agg.set_index("service")["error_rate"])

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "dashboard":
        run_dashboard()
    else:
        run_pipeline()
