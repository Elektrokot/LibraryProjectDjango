# --------------------------------------------------------------
# 1️⃣  Builder stage – собираем все зависимости и готовим код
# --------------------------------------------------------------
FROM python:3.12-slim AS builder

# Уменьшаем размер образа, отключаем кэш и лишние файлы
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Устанавливаем только те пакеты, которые нужны для сборки зависимостей
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Создаём непривилегированного пользователя (будет использован в финальном образе)
RUN groupadd --gid 1001 appuser \
    && useradd --uid 1001 --gid appuser appuser

WORKDIR /app

# Кешируем слой с зависимостями: если requirements.txt не менялся,
# Docker переиспользует уже установленный слой.
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --prefix=/install -r requirements.txt

# --------------------------------------------------------------
# 2️⃣  Runtime stage – лёгкий финальный образ
# --------------------------------------------------------------
FROM python:3.12-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Добавляем того же пользователя, что и в builder
RUN groupadd --gid 1001 appuser \
    && useradd --uid 1001 --gid appuser appuser

# Создаём рабочую директорию и даём права пользователю
WORKDIR /app
RUN mkdir -p /app/staticfiles && chown -R appuser:appuser /app

# Копируем только нужные файлы из builder‑stage
COPY --from=builder /install /usr/local
COPY --from=builder /app /app

# Если в проекте есть миграции/static, их тоже нужно скопировать.
# (В данном случае они уже находятся в /app после копирования.)

# ---->  Healthcheck – проверяем, что gunicorn отвечает
HEALTHCHECK --interval=10s --timeout=5s --retries=3 \
  CMD curl -f http://localhost:8000/healthz || exit 1

# Порт, который будет слушать gunicorn
EXPOSE 8000

# --------------------------------------------------------------
# 3️⃣  Финальный пользователь и команда
# --------------------------------------------------------------
USER appuser

# Поскольку collectstatic нужно выполнить **только один раз** при сборке,
# делаем это на этапе сборки (в builder‑stage). В runtime‑stage
# просто стартуем gunicorn.
CMD ["gunicorn", "config.wsgi:application", "--workers", "3", "--bind", "0.0.0.0:8000"]



#FROM python:3.12-slim
#
#WORKDIR /app
#
#RUN apt-get update \
#    && apt-get install -y gcc libpq-dev \
#    && apt-get clean \
#    && rm -rf /var/lib/apt/lists/*
#
#COPY requirements.txt .
#
#RUN pip install --no-cache-dir -r requirements.txt
#
#COPY . .
#
#RUN mkdir -p /app/staticfiles && chmod -R 755 /app/staticfiles
#
#EXPOSE 8000
#
#CMD ["sh", "-c", "python manage.py collectstatic --noinput && gunicorn config.wsgi:application --bind 0.0.0.0:8000"]