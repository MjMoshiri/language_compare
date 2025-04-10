#!/bin/bash

CONCURRENCY=50
DURATION="30s"
FIB_N=35
RUNS=3
PYTHON_URL="http://localhost:8000"
RUST_URL="http://localhost:8001"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
OUTPUT_FILE="benchmark_results_${TIMESTAMP}.txt"
SLEEP_BETWEEN_TESTS=5
SLEEP_BETWEEN_RUNS=10

export PATH="$HOME/go/bin:$PATH"

if ! command -v bombardier &> /dev/null
then
    echo "ERROR: bombardier command could not be found."
    echo "Please install it (e.g., 'go install github.com/codesenberg/bombardier@latest', brew install bombardier) and ensure it's in your PATH."
    exit 1
fi

echo "Starting Benchmark..."
echo "Parameters:"
echo "  Concurrency: $CONCURRENCY"
echo "  Duration:    $DURATION"
echo "  Fibonacci N: $FIB_N"
echo "  Runs:        $RUNS"
echo "Saving results to: $OUTPUT_FILE"
echo ""
echo "NOTE: This script focuses on bombardier results (RPS, Latency) saved to the file."
echo "      Bombardier progress bars will show ONLY in this terminal during execution."
echo "      Please monitor CPU/Memory/IO manually using the command below in a separate terminal:"
echo "      docker stats --format \"table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.NetIO}}\t{{.BlockIO}}\" python_api_service rust_api_service"
echo ""

echo "Benchmark Run: ${TIMESTAMP}" > "$OUTPUT_FILE"
echo "Parameters:" >> "$OUTPUT_FILE"
echo "  Concurrency: $CONCURRENCY" >> "$OUTPUT_FILE"
echo "  Duration:    $DURATION" >> "$OUTPUT_FILE"
echo "  Fibonacci N: $FIB_N" >> "$OUTPUT_FILE"
echo "  Runs:        $RUNS" >> "$OUTPUT_FILE"
echo "==================================================" >> "$OUTPUT_FILE"

for (( run=1; run<=RUNS; run++ ))
do
    echo "" | tee -a "$OUTPUT_FILE"
    echo "--- Starting Run $run of $RUNS ---" | tee -a "$OUTPUT_FILE"
    echo "Timestamp: $(date)" >> "$OUTPUT_FILE"
    echo "--------------------------------------------------" >> "$OUTPUT_FILE"

    echo "[$run/$RUNS] Testing Python /hello..."
    echo -e "\n--- Python /hello (Run $run) ---" >> "$OUTPUT_FILE"
    bombardier -c $CONCURRENCY -d $DURATION "${PYTHON_URL}/hello" 1>> "$OUTPUT_FILE"
    echo "--------------------------------------------------" >> "$OUTPUT_FILE"
    sleep $SLEEP_BETWEEN_TESTS

    echo "[$run/$RUNS] Testing Python /fib/${FIB_N}..."
    echo -e "\n--- Python /fib/${FIB_N} (Run $run) ---" >> "$OUTPUT_FILE"
    bombardier -c $CONCURRENCY -d $DURATION "${PYTHON_URL}/fib/${FIB_N}" 1>> "$OUTPUT_FILE"
    echo "--------------------------------------------------" >> "$OUTPUT_FILE"
    sleep $SLEEP_BETWEEN_TESTS

    echo "[$run/$RUNS] Testing Rust /hello..."
    echo -e "\n--- Rust /hello (Run $run) ---" >> "$OUTPUT_FILE"
    bombardier -c $CONCURRENCY -d $DURATION "${RUST_URL}/hello" 1>> "$OUTPUT_FILE"
    echo "--------------------------------------------------" >> "$OUTPUT_FILE"
    sleep $SLEEP_BETWEEN_TESTS

    echo "[$run/$RUNS] Testing Rust /fib/${FIB_N}..."
    echo -e "\n--- Rust /fib/${FIB_N} (Run $run) ---" >> "$OUTPUT_FILE"
    bombardier -c $CONCURRENCY -d $DURATION "${RUST_URL}/fib/${FIB_N}" 1>> "$OUTPUT_FILE"
    echo "--------------------------------------------------" >> "$OUTPUT_FILE"

    if [ $run -lt $RUNS ]; then
        echo ""
        echo "--- Run $run finished, sleeping for $SLEEP_BETWEEN_RUNS seconds before next run ---"
        sleep $SLEEP_BETWEEN_RUNS
    fi
done

echo "" | tee -a "$OUTPUT_FILE"
echo "==================================================" >> "$OUTPUT_FILE"
echo "Benchmark Completed: $(date)" >> "$OUTPUT_FILE"
echo "==================================================" >> "$OUTPUT_FILE"
echo ""
echo "Benchmark Finished!"
echo "Results saved to: $OUTPUT_FILE"
