# -------- Stage 1: Build Environment --------
FROM python:3.13-slim AS builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . .


RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# -------- Stage 2: Minimal Runtime Image --------
FROM python:3.13-slim AS runtime


WORKDIR /app


COPY --from=builder /usr/local /usr/local
COPY --from=builder /etc /etc


COPY app.py .
COPY .project-root/ .project-root/
COPY src/entity/config_entity.py src/entity/config_entity.py
COPY requirement_folder/ requirement_folder/
COPY src/app/ src/app/
COPY src/azure/ src/azure/
COPY src/components/recommendation_engine.py src/components/recommendation_engine.py
COPY src/constants/ src/constants/
COPY src/utils/ src/utils/
COPY src/logging src/logging
COPY src/exception src/exception 

EXPOSE 5000


CMD ["sh", "-c", "waitress-serve --listen=0.0.0.0:${PORT:-5000} app:app"]
    