#!/usr/bin/env python3

def main():
    python_hello_rps = [3330.83, 2851.11, 3235.88]
    python_hello_latency = [15.00, 17.53, 15.45]
    
    python_fib_rps = [2473.96, 2462.78, 2660.11]
    python_fib_latency = [20.21, 20.30, 18.79]
    
    rust_hello_rps = [36156.59, 36037.52, 35324.58]
    rust_hello_latency = [1.38, 1.38, 1.41]
    
    rust_fib_rps = [33808.83, 35896.07, 32856.46]
    rust_fib_latency = [1.48, 1.39, 1.52]
    
    avg_python_hello_rps = sum(python_hello_rps) / len(python_hello_rps)
    avg_python_hello_latency = sum(python_hello_latency) / len(python_hello_latency)
    
    avg_python_fib_rps = sum(python_fib_rps) / len(python_fib_rps)
    avg_python_fib_latency = sum(python_fib_latency) / len(python_fib_latency)
    
    avg_rust_hello_rps = sum(rust_hello_rps) / len(rust_hello_rps)
    avg_rust_hello_latency = sum(rust_hello_latency) / len(rust_hello_latency)
    
    avg_rust_fib_rps = sum(rust_fib_rps) / len(rust_fib_rps)
    avg_rust_fib_latency = sum(rust_fib_latency) / len(rust_fib_latency)
    
    hello_rps_diff = avg_rust_hello_rps / avg_python_hello_rps
    hello_latency_diff = avg_python_hello_latency / avg_rust_hello_latency
    
    fib_rps_diff = avg_rust_fib_rps / avg_python_fib_rps
    fib_latency_diff = avg_python_fib_latency / avg_rust_fib_latency
    
    print("## Performance Results\n")
    print("Below is a summary of the benchmark results (averaged across 3 runs):\n")
    print("| Metric | Python (FastAPI) | Rust (Actix Web) | Difference |")
    print("|--------|------------------|------------------|------------|")
    print(f"| `/hello` Requests/sec | {avg_python_hello_rps:.0f} | {avg_rust_hello_rps:.0f} | Rust is {hello_rps_diff:.1f}x faster |")
    print(f"| `/hello` Latency (ms) | {avg_python_hello_latency:.1f} | {avg_rust_hello_latency:.1f} | Rust is {hello_latency_diff:.1f}x faster |")
    print(f"| `/fib/35` Requests/sec | {avg_python_fib_rps:.0f} | {avg_rust_fib_rps:.0f} | Rust is {fib_rps_diff:.1f}x faster |")
    print(f"| `/fib/35` Latency (ms) | {avg_python_fib_latency:.1f} | {avg_rust_fib_latency:.1f} | Rust is {fib_latency_diff:.1f}x faster |")
    print()
if __name__ == "__main__":
    main() 