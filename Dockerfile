FROM python:3.12-slim

#install uv
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh
ENV PATH="/root/.local/bin/:$PATH"
# install requirements
COPY pyproject.toml uv.lock ./

COPY app/ app/
WORKDIR /app
RUN chmod +x /app/app_run.sh

EXPOSE 8000
ENTRYPOINT [ "bash", "-c", "/app/app_run.sh" ]
