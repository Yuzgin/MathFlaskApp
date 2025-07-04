FROM python:3.11-slim

WORKDIR /app

# 1) Install OS libs needed by Matplotlib
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      libpng-dev \
      libfreetype6-dev \
      pkg-config \
 && rm -rf /var/lib/apt/lists/*

# 2) Copy & install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3) Copy in your Flask-Math code
COPY . .
RUN chmod +x run_tests.sh

ENV FLASK_APP=app.py \
    FLASK_ENV=production

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]


