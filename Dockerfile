# -------- Stage 1: Build Environment --------
FROM python:3.13-slim AS builder

# Set working directory
WORKDIR /app

# Disable Python writing .pyc files and enable stdout logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy everything (for training or full build context)
COPY . .

# Upgrade pip and install dependencies (cached if unchanged)
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# -------- Stage 2: Minimal Runtime Image --------
FROM python:3.13-slim AS runtime

# Set working directory
WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /usr/local /usr/local
COPY --from=builder /etc /etc

# Copy only necessary runtime files
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
# Expose Flask default port
EXPOSE 5000

# Run the app
CMD ["sh", "-c", "waitress-serve --listen=0.0.0.0:${PORT:-5000} app:app"]
    