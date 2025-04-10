FROM rust:slim as builder

WORKDIR /usr/src/app

ENV RUSTFLAGS="-C target-cpu=native -C opt-level=3"

COPY Cargo.toml ./

RUN mkdir src && \
    echo "fn main() {println!(\"if you see this, the build broke\")}" > src/main.rs && \
    cargo build --release && \
    rm -rf src target/release/deps/rust_api*

COPY src ./src

RUN cargo build --release --locked

FROM debian:stable-slim

COPY --from=builder /usr/src/app/target/release/rust-api /usr/local/bin/rust-api

EXPOSE 8001

CMD ["/usr/local/bin/rust-api"]
