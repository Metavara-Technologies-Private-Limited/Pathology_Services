# ---------- Base Image ----------
FROM python:3.12-slim

# ---------- Environment ----------
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ---------- Working Directory ----------
WORKDIR /app

# ---------- System Dependencies ----------
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    postgresql-client \
    curl \
    graphviz \
    && rm -rf /var/lib/apt/lists/*

# ---------- Copy Requirements ----------
COPY requirements.txt .

# ---------- Install Python Dependencies ----------
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# ---------- Copy Project ----------
COPY . .

# ---------- Collect Static ----------
RUN python manage.py collectstatic --noinput || true

# ---------- Create Media & Logs ----------
RUN mkdir -p /app/media \
    && mkdir -p /app/logs

# ---------- Expose ----------
EXPOSE 8000

# ---------- Start Gunicorn ----------
CMD ["gunicorn", "pathology_lab.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--timeout", "120"]
