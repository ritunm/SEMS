# SEMS - Smart Energy Management System

[![CI/CD](https://github.com/ritunm/SEMS/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/ritunm/SEMS/actions)

Smart Energy Management System (SEMS) intelligently balances load across energy zones, optimizes energy distribution, and monitors system performance using advanced profiling, testing, and visualization techniques.

---

## Features

-  **Load Balancing** with overload detection and redistribution
-  **Unit & Integration Testing** with `pytest`
-  **Performance Profiling** using `cProfile` + `snakeviz`
-  **Code Quality** via `flake8`, `radon`, `coverage`
-  **Security Analysis** with `Bandit` and `OWASP ZAP`
-  **Containerized** with Docker & Docker Compose
-  **CI/CD Pipeline** using GitHub Actions
-  **Monitoring** using Prometheus + Grafana
-  **Load Testing** with JMeter

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/ritunm/SEMS.git
cd SEMS
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Tests and Metrics

### Unit Tests & Coverage

```bash
pytest
coverage run -m pytest
coverage report -m
```

### Cyclomatic Complexity

```bash
radon cc load_balancer_sems.py -a
```

---

## Run with Docker

### Build & Run the Application

```bash
docker-compose up --build
```

---

## Security Analysis

### Static Scan (Bandit)

```bash
bandit -r .
```

### Dynamic Scan (ZAP Docker)

```bash
docker run -t owasp/zap2docker-stable zap-baseline.py -t http://localhost:8000
```

---

## Monitoring

### Prometheus + Grafana

Start with:

```bash
docker-compose up
```

Access dashboards:
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000

---

## Load Testing

### Apache JMeter

```bash
jmeter -n -t sems_load_test.jmx -l results.jtl
```

---


## Contributing

This project is part of CS352 Software Engineering Lab at NIT Meghalaya. Contributions, suggestions, and issue reports are welcome.

