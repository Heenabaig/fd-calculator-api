# FD Calculator API

[![CI](https://github.com/Heenabaig/fd-calculator-api/actions/workflows/ci.yml/badge.svg)](https://github.com/Heenabaig/fd-calculator-api/actions/workflows/ci.yml)

A small REST API that calculates the maturity amount of a fixed deposit (FD). I built it as a hands-on DevOps project: the app is tested automatically, packaged in Docker, and checked by a GitHub Actions pipeline on every change.

## What it does

- `GET /health` returns `{"status": "ok"}`. Use it for health checks.
- `POST /calculate` takes a principal, an annual interest rate and a tenure, and returns the maturity amount.

Interest is compounded **quarterly**:

```
maturity = principal * (1 + rate / (100 * 4)) ^ (4 * years)
```

Example request:

```json
{ "principal": 100000, "rate": 7, "years": 1 }
```

Example response:

```json
{ "maturity_amount": 107185.9 }
```

Interactive API docs are available at `/docs` while the app is running.

## Tech stack

- Python 3.12 and FastAPI
- pytest for tests
- Docker for packaging
- GitHub Actions for CI

## Run locally

```bash
git clone https://github.com/Heenabaig/fd-calculator-api.git
cd fd-calculator-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open http://127.0.0.1:8000/docs.

## Run with Docker

```bash
docker build -t fd-api .
docker run -d -p 8000:8000 --name fd fd-api
```

Then open http://localhost:8000/docs. Stop and remove the container with:

```bash
docker rm -f fd
```

## Run the tests

```bash
pytest
```

## CI pipeline

The workflow in `.github/workflows/ci.yml` runs on every push and pull request. It:

1. Checks out the code
2. Sets up Python 3.12
3. Installs dependencies
4. Runs the pytest suite
5. Builds the Docker image

If a test fails, the pipeline turns red and the problem is caught before the change is merged.

## Project structure

```
.
├── main.py              # FastAPI application
├── test_main.py         # Unit tests
├── requirements.txt     # Python dependencies
├── Dockerfile           # Container image definition
└── .github/workflows/
    └── ci.yml           # CI pipeline
```

## What I learned

- Writing a Dockerfile and why a successful build does not prove the app works
- Setting up a CI pipeline and reading a failed run
- Working with branches and pull requests
- Troubleshooting Docker and WSL 2 on Windows

## Next steps

- Provision cloud infrastructure with Terraform
- Deploy the container to Kubernetes
- Add monitoring with Prometheus and Grafana
