# API Performance Comparison: Python (FastAPI) vs Rust (Actix Web)

This project compares the performance of two simple web APIs implementing the same functionality, one using Python with FastAPI and the other using Rust with Actix Web. Both APIs run in Docker containers with defined resource limits (CPU, Memory) for a fair comparison.

## Endpoints

Both APIs expose the following endpoints:

*   `GET /hello`: Returns a simple JSON `{"message": "Hello from ..."}`. Useful for measuring baseline framework overhead.
*   `GET /fib/{n}`: Calculates the nth Fibonacci number (0-indexed) using an iterative algorithm. Takes an integer `n` (0 <= n <= 40) as a path parameter. Returns JSON `{"n": N, "result": R}`. Tests framework handling, path parameter parsing, integer computation, and JSON serialization under load.

## Setup and Running

1.  **Prerequisites:**
    *   Docker & Docker Compose installed.
    *   A load testing tool installed (e.g., `bombardier`). Install `bombardier`: Check its GitHub releases or use a package manager (`brew install bombardier`, `go install github.com/codesenberg/bombardier@latest`).

2.  **Build Docker Images:**
    ```bash
    docker compose build
    ```

3.  **Run Services:**
    ```bash
    docker compose up -d
    ```
    This starts both API containers in the background with CPU/Memory limits applied.

4.  **Verify Services:**
    *   Python: `curl http://localhost:8000/hello` and `curl http://localhost:8000/fib/10`
    *   Rust: `curl http://localhost:8001/hello` and `curl http://localhost:8001/fib/10`

## Load Testing

```bash
chmod +x ./bombardier.sh
./run_benchmark.sh
```

## Performance Results

Below is a summary of the benchmark results (averaged across 3 runs):

| Metric | Python (FastAPI) | Rust (Actix Web) | Difference |
|--------|------------------|------------------|------------|
| `/hello` Requests/sec | 3139 | 35840 | Rust is 11.4x faster |
| `/hello` Latency (ms) | 16.0 | 1.4 | Rust is 11.5x faster |
| `/fib/35` Requests/sec | 2532 | 34187 | Rust is 13.5x faster |
| `/fib/35` Latency (ms) | 19.8 | 1.5 | Rust is 13.5x faster |


