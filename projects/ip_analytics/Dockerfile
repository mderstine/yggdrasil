FROM python:3.12-slim-bookworm

RUN useradd -m -U dagster

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV DAGSTER_HOME=/opt/dagster/dagster_home/
RUN mkdir -p $DAGSTER_HOME && \
    chown -R dagster:dagster $DAGSTER_HOME

WORKDIR /opt/dagster/app

COPY pyproject.toml .
COPY uv.lock .
COPY src/ ./src/

RUN uv sync --frozen --no-cache

USER dagster
# Expose Port for Dagster Code Server
EXPOSE 4000

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD dagster api grpc-health-check

# CMD allows this to be overridden from run launchers or executors
CMD ["dagster", "code-server", "start", "-h", "0.0.0.0", "-p", "4000", "-m", "ip_analytics"]
