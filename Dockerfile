# syntax=docker/dockerfile:1.4
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Set workdir
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies using uv
RUN uv sync

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Command to run the application
CMD ["dg", "dev"]