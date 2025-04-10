FROM rust:slim as builder

WORKDIR /usr/src/app

COPY Cargo.toml ./

RUN mkdir src && \
    echo "fn main() {println!(\"if you see this, the build broke\")}" > src/main.rs && \
    cargo build --release && \
    rm -rf src target/release/deps/rust_api*

COPY src ./src

RUN cargo build --release --locked

FROM debian:sid-slim

ARG APP_USER=appuser
ARG APP_GROUP=appgroup
ARG UID=1001
ARG GID=1001

RUN groupadd -g ${GID} ${APP_GROUP} && \
    useradd -u ${UID} -g ${APP_GROUP} --no-create-home -s /sbin/nologin ${APP_USER}

COPY --from=builder /usr/src/app/target/release/rust-api /usr/local/bin/rust-api

RUN chmod +x /usr/local/bin/rust-api

RUN chown ${APP_USER}:${APP_GROUP} /usr/local/bin/rust-api

USER ${APP_USER}

EXPOSE 8001

CMD ["/usr/local/bin/rust-api"]
