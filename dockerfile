FROM python:3.10-slim AS build

RUN apt-get update
RUN apt-get install -y 

WORKDIR /uptime

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY REQUIREMENTS.txt .
RUN pip install --upgrade pip
RUN pip install -r REQUIREMENTS.txt

COPY config.py .
COPY api_v1.0.py .
COPY prometheus.yml .

FROM python:3.10-slim AS run

RUN set -eux; \
    apt-get update; \
    DEBIAN_FRONTEND=noninteractive apt-get upgrade -y; \
    rm -rf /var/lib/apt/lists/*; \
    apt-get clean

WORKDIR /uptime

COPY --from=build /opt/venv /opt/venv
COPY --from=build /uptime .

EXPOSE 9400

ENV TZ="Europe/Paris"
ENV PATH="/opt/venv/bin:$PATH"

CMD [ "api.py" ]
ENTRYPOINT [ "python" ]
