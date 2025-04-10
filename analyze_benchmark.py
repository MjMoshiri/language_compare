#!/usr/bin/env python3

def main():
    # 50 concurrent connections results
    python_hello_rps_50 = [3330.83, 2851.11, 3235.88]
    python_hello_latency_50 = [15.00, 17.53, 15.45]
    
    python_fib_rps_50 = [2473.96, 2462.78, 2660.11]
    python_fib_latency_50 = [20.21, 20.30, 18.79]
    
    rust_hello_rps_50 = [36156.59, 36037.52, 35324.58]
    rust_hello_latency_50 = [1.38, 1.38, 1.41]
    
    rust_fib_rps_50 = [33808.83, 35896.07, 32856.46]
    rust_fib_latency_50 = [1.48, 1.39, 1.52]
    
    # 200 concurrent connections results
    python_hello_rps_200 = [13515.69, 13870.32, 14666.90]
    python_hello_latency_200 = [14.79, 14.42, 13.63]
    
    python_fib_rps_200 = [11490.77, 11426.01, 11344.81]
    python_fib_latency_200 = [17.40, 17.50, 17.62]
    
    rust_hello_rps_200 = [69749.36, 72061.39, 71861.92]
    rust_hello_latency_200 = [2.86, 2.77, 2.78]
    
    rust_fib_rps_200 = [66202.39, 67462.36, 67405.98]
    rust_fib_latency_200 = [3.02, 2.96, 2.96]
    
    # Calculate averages for 50 concurrent connections
    avg_python_hello_rps_50 = sum(python_hello_rps_50) / len(python_hello_rps_50)
    avg_python_hello_latency_50 = sum(python_hello_latency_50) / len(python_hello_latency_50)
    
    avg_python_fib_rps_50 = sum(python_fib_rps_50) / len(python_fib_rps_50)
    avg_python_fib_latency_50 = sum(python_fib_latency_50) / len(python_fib_latency_50)
    
    avg_rust_hello_rps_50 = sum(rust_hello_rps_50) / len(rust_hello_rps_50)
    avg_rust_hello_latency_50 = sum(rust_hello_latency_50) / len(rust_hello_latency_50)
    
    avg_rust_fib_rps_50 = sum(rust_fib_rps_50) / len(rust_fib_rps_50)
    avg_rust_fib_latency_50 = sum(rust_fib_latency_50) / len(rust_fib_latency_50)
    
    hello_rps_diff_50 = avg_rust_hello_rps_50 / avg_python_hello_rps_50
    hello_latency_diff_50 = avg_python_hello_latency_50 / avg_rust_hello_latency_50
    
    fib_rps_diff_50 = avg_rust_fib_rps_50 / avg_python_fib_rps_50
    fib_latency_diff_50 = avg_python_fib_latency_50 / avg_rust_fib_latency_50
    
    # Calculate averages for 200 concurrent connections
    avg_python_hello_rps_200 = sum(python_hello_rps_200) / len(python_hello_rps_200)
    avg_python_hello_latency_200 = sum(python_hello_latency_200) / len(python_hello_latency_200)
    
    avg_python_fib_rps_200 = sum(python_fib_rps_200) / len(python_fib_rps_200)
    avg_python_fib_latency_200 = sum(python_fib_latency_200) / len(python_fib_latency_200)
    
    avg_rust_hello_rps_200 = sum(rust_hello_rps_200) / len(rust_hello_rps_200)
    avg_rust_hello_latency_200 = sum(rust_hello_latency_200) / len(rust_hello_latency_200)
    
    avg_rust_fib_rps_200 = sum(rust_fib_rps_200) / len(rust_fib_rps_200)
    avg_rust_fib_latency_200 = sum(rust_fib_latency_200) / len(rust_fib_latency_200)
    
    hello_rps_diff_200 = avg_rust_hello_rps_200 / avg_python_hello_rps_200
    hello_latency_diff_200 = avg_python_hello_latency_200 / avg_rust_hello_latency_200
    
    fib_rps_diff_200 = avg_rust_fib_rps_200 / avg_python_fib_rps_200
    fib_latency_diff_200 = avg_python_fib_latency_200 / avg_rust_fib_latency_200
    
    print("## Performance Results\n")
    print("Below is a summary of the benchmark results (averaged across 3 runs):\n")
    
    print("### Single Core - 50 Concurrent Connections\n")
    print("| Metric | Python (FastAPI) | Rust (Actix Web) | Difference |")
    print("|--------|------------------|------------------|------------|")
    print(f"| `/hello` Requests/sec | {avg_python_hello_rps_50:.0f} | {avg_rust_hello_rps_50:.0f} | Rust is {hello_rps_diff_50:.1f}x faster |")
    print(f"| `/hello` Latency (ms) | {avg_python_hello_latency_50:.1f} | {avg_rust_hello_latency_50:.1f} | Rust is {hello_latency_diff_50:.1f}x faster |")
    print(f"| `/fib/35` Requests/sec | {avg_python_fib_rps_50:.0f} | {avg_rust_fib_rps_50:.0f} | Rust is {fib_rps_diff_50:.1f}x faster |")
    print(f"| `/fib/35` Latency (ms) | {avg_python_fib_latency_50:.1f} | {avg_rust_fib_latency_50:.1f} | Rust is {fib_latency_diff_50:.1f}x faster |")
    print()
    
    print("### Dual Core - 200 Concurrent Connections\n")
    print("| Metric | Python (FastAPI) | Rust (Actix Web) | Difference |")
    print("|--------|------------------|------------------|------------|")
    print(f"| `/hello` Requests/sec | {avg_python_hello_rps_200:.0f} | {avg_rust_hello_rps_200:.0f} | Rust is {hello_rps_diff_200:.1f}x faster |")
    print(f"| `/hello` Latency (ms) | {avg_python_hello_latency_200:.1f} | {avg_rust_hello_latency_200:.1f} | Rust is {hello_latency_diff_200:.1f}x faster |")
    print(f"| `/fib/35` Requests/sec | {avg_python_fib_rps_200:.0f} | {avg_rust_fib_rps_200:.0f} | Rust is {fib_rps_diff_200:.1f}x faster |")
    print(f"| `/fib/35` Latency (ms) | {avg_python_fib_latency_200:.1f} | {avg_rust_fib_latency_200:.1f} | Rust is {fib_latency_diff_200:.1f}x faster |")
    print("*Note: Both tests used full CPU capacity. For Rust in the dual-core test, there might have been a network bottleneck affecting the results.")
    print()

if __name__ == "__main__":
    main() 