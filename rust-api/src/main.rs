use actix_web::{get, web, App, HttpServer, Responder, HttpResponse, ResponseError};
use serde::Serialize;
use std::fmt;

// --- Error Handling ---
#[derive(Debug)]
enum AppError {
    BadRequest(String),
    CalculationError(String),
}

impl fmt::Display for AppError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            AppError::BadRequest(msg) => write!(f, "Bad Request: {}", msg),
            AppError::CalculationError(msg) => write!(f, "Calculation Error: {}", msg),
        }
    }
}

impl ResponseError for AppError {
    fn error_response(&self) -> HttpResponse {
        match self {
            AppError::BadRequest(msg) => HttpResponse::BadRequest().json(ErrorMessage { error: msg.clone() }),
            AppError::CalculationError(msg) => HttpResponse::InternalServerError().json(ErrorMessage { error: msg.clone() }),
        }
    }
}

#[derive(Serialize)]
struct ErrorMessage {
    error: String,
}

// --- Response Structure ---
#[derive(Serialize)]
struct FibResponse {
    n: u64,
    result: u64,
}

// --- Fibonacci Logic ---
// Iterative Fibonacci function using u64. Returns Result to handle potential overflow,
// though unlikely with the input limit.
fn calculate_fibonacci(n: u64) -> Result<u64, AppError> {
    if n == 0 {
        return Ok(0);
    } else if n == 1 {
        return Ok(1);
    }

    let mut a: u64 = 0;
    let mut b: u64 = 1;

    for _ in 2..=n {
        // Check for potential overflow before adding
        // checked_add returns None if overflow occurs
        match a.checked_add(b) {
            Some(next_b) => {
                a = b;
                b = next_b;
            }
            None => {
                // This shouldn't happen with n <= 40 and u64, but good practice
                return Err(AppError::CalculationError(format!("Fibonacci sequence overflowed u64 at n={}", n)));
            }
        }
    }
    Ok(b)
}

// --- Route Handler ---
#[get("/fib/{n}")]
async fn get_fibonacci(path: web::Path<u64>) -> Result<impl Responder, AppError> {
    let n = path.into_inner();

    // Input validation (similar limit to Python)
    const MAX_N: u64 = 40;
    if n > MAX_N {
        return Err(AppError::BadRequest(format!(
            "Input 'n' must be less than or equal to {}.", MAX_N
        )));
    }

    // Optional: Simulate async work if needed
    // tokio::time::sleep(std::time::Duration::from_millis(10)).await;

    let result = calculate_fibonacci(n)?; // Propagate error if calculation fails

    Ok(HttpResponse::Ok().json(FibResponse { n, result }))
}

#[get("/hello")]
async fn hello() -> impl Responder {
    HttpResponse::Ok().body("Hello from Rust Actix-Web")
}


// --- Server Setup ---
#[actix_web::main]
async fn main() -> std::io::Result<()> {
    println!("🚀 Server starting on port 8001...");

    HttpServer::new(|| {
        App::new()
            .service(get_fibonacci)
            .service(hello)
    })
    .bind(("0.0.0.0", 8001))?
    .workers(1) // Explicitly set to 1 worker thread for fair comparison initially
    .run()
    .await
}