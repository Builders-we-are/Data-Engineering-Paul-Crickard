# Data-Engineering-Paul-Crickard

 # Data Engineering with Python – Companion Repository

A hands‑on project repo that follows Data Engineering with Python by Paul Crickard (2nd ed.).  Each chapter is translated into reproducible code, datasets, and unit‑tested pipelines so you can learn by doing and build a portfolio piece at the same time.

---

 What You’ll Find Here

| Folder              | Chapter | Theme                       | Deliverable                                  |
| ------------------- | ------- | --------------------------- | -------------------------------------------- |
| `01_extract/`       | 1‑2     | Extract, APIs, Web Scraping | Python scripts + RAW data snapshots          |
| `02_transform/`     | 3‑5     | Cleaning, Pandas, PySpark   | Jupyter notebooks + pytest‑backed transforms |
| `03_load/`          | 6       | Loading to Postgres, S3     | SQL DDL + bulk‑loader helpers                |
| `04_orchestration/` | 7‑8     | Airflow DAGs, Scheduling    | Docker‑Compose Airflow stack, unit DAG tests |
| `05_streaming/`     | 9       | Kafka, Real‑time ETL        | Dockerized Kafka connect + Stream demo       |
| `06_visualization/` | 10      | Dashboards                  | Superset charts + Grafana panels             |
| `infra/`            | —       | Terraform IaC               | Local‑stack + AWS option                     |
| `tests/`            | —       | Pytest test‑suite           | 90%+ coverage target                         |

Each folder is self‑contained—open the README inside a sub‑folder to dive into just that piece.



---

## 🛠  Quick‑Start (Local Docker Compose)

1. Clone & bootstrap

   ```bash
   git clone https://github.com/your‑handle/data‑eng‑with‑python.git
   cd data‑eng‑with‑python
   make init          # sets up .env & pre‑commit hooks
   make compose‑up    # spins Postgres, Kafka, Airflow, Superset
   ```
2. **Run pipelines**

   ```bash
   make run‑extract   # scrapes + drops raw JSON in /data/raw
   make run‑airflow   # triggers DAGs to transform & load
   ```
3. Explore

   * Airflow UI 
   * Superset 
   * pgAdmin



---

## ☁️  Deploying to AWS (Optional)

```bash
cd infra/aws
terraform init && terraform apply
```

Creates:

* VPC with Public–Private subnets
* RDS Postgres, MSK‑Kafka, MWAA‑Airflow
* S3 bucket for raw & processed layers
  
#TODO by Ade
See `infra/README.md` for teardown & cost‑saving tips.

---

## 🧪 Testing & Quality

* Linters – `ruff`, `black`, `mypy`
* Tests – `pytest` + coverage report (`make test`)
* CI – GitHub Actions workflow (`.github/workflows/ci.yml`)

---

Contributing

Spotted a bug or have an idea? Open an **issue** or submit a **PR**. Please follow the conventional commit style and ensure `make test` passes.

---

📄 License

Apache‑2.0.  Feel free to fork and adapt for your own learning!

---
 🔗 References

* Paul Crickard – *Data Engineering with Python*, O’Reilly, 2nd ed., 2023.
* Official repo: [https://github.com/PacktPublishing/Data‑Engineering‑With‑Python‑Second‑Edition](https://github.com/PacktPublishing/Data‑Engineering‑With‑Python‑Second‑Edition)
