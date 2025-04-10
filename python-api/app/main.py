from fastapi import FastAPI, Path, HTTPException
import time # Optional: to add a slight delay if needed for testing scaling

app = FastAPI()

# Iterative Fibonacci function (more efficient than recursive)
def calculate_fibonacci(n: int) -> int:
    if n < 0:
        # Should be caught by Path validation, but good practice
        raise ValueError("Input must be a non-negative integer.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        # Python integers handle arbitrary size, overflow isn't an issue here
        # for reasonable n
        return b

@app.get("/fib/{n}")
async def get_fibonacci(
    n: int = Path(..., title="The index 'n' for the Fibonacci sequence", ge=0, le=40)
    # ge=0: Must be greater than or equal to 0
    # le=40: Limit to prevent excessive calculation time/potential DoS. Adjust if needed.
    #        Fibonacci grows very fast. fib(40) is already > 100 million.
    #        Higher values might strain even Rust if not careful with types/limits.
):
    """
    Calculates the nth Fibonacci number (0-indexed).
    Example: /fib/10 returns {"n": 10, "result": 55}
    """
    try:
        # Optional: Add a small artificial delay if you want to simulate more I/O
        # await asyncio.sleep(0.01)

        result = calculate_fibonacci(n)
        return {"n": n, "result": result}
    except ValueError as e:
        # This is redundant because of Path validation, but shows manual handling
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        # Catch unexpected errors
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")

@app.get("/hello") # Keep the simple hello endpoint for basic overhead comparison
async def hello():
    return {"message": "Hello from Python FastAPI"}