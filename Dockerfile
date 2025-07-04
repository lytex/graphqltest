FROM python:3.12-slim-bookworm
# Install uv binary:
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
# Use "uv" instead of "python -m venv":
RUN uv venv /opt/venv
# Make sure we use the virtualenv:
ENV UV_PROJECT_ENVIRONMENT=/opt/venv
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY uv.lock .
COPY pyproject.toml .
ENV UV_COMPILE_BYTECODE=1
RUN --mount=type=cache,target=/root/.cache/uv uv sync

COPY project /project

WORKDIR /project
ENTRYPOINT [ "sh", "entrypoint.sh" ]
