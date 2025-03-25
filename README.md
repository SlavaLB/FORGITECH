# Tron Wallet API

API для работы с кошельками TRON

## 🚀 Быстрый старт

```bash
docker-compose --project-name tron_db up -d

alembic upgrade head

python -m venv venv

source venv/bin/activate  # Linux/Mac

venv\Scripts\activate  # Windows

pip install -r requirements.txt

uvicorn backend.main:app --reload

pytest

```
📚 Документация API
После запуска сервера доступны:

Документация Swagger: http://localhost:8000/docs

Альтернативная документация: http://localhost:8000/redoc

⚙️ Конфигурация
Создайте файл .env в корне проекта: