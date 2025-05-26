FROM python:3.12-slim-bookworm

RUN useradd -m -U dagster

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV DAGSTER_HOME=/opt/dagster/dagster_home/
RUN mkdir -p $DAGSTER_HOME && \
    chown -R dagster:dagster $DAGSTER_HOME

# Copy Dependecy Files
COPY pyproject.toml uv.lock $DAGSTER_HOME/

WORKDIR $DAGSTER_HOME

# Install Dependencies
RUN uv sync --frozen --no-cache

# Copy Application Code
# COPY dagster.yaml $DAGSTER_HOME
COPY projects/ $DAGSTER_HOME/src/

USER dagster

EXPOSE 4000

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD dagster api grpc-health-check

CMD ["uv", "run", "dagster", "api", "grpc", "--host", "0.0.0.0", "--port", "4000"]
