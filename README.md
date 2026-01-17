<div align="center">

# 🤖 Aiogram Starter Kit

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Aiogram](https://img.shields.io/badge/Aiogram-3.x-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://aiogram.dev)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

**Production-ready шаблон Telegram бота на Aiogram 3.x**

[🇷🇺 Русский](#) | [🇬🇧 English](#english)

</div>

---

## ⚡ Быстрый старт

```bash
# Клонируйте репозиторий
git clone https://github.com/Chumbayoumba/aiogram-starter-kit.git
cd aiogram-starter-kit

# Скопируйте .env файл
cp .env.example .env

# Запустите через Docker
docker-compose up -d
```

---

## ✨ Особенности

- 🚀 **Aiogram 3.x** — современный async фреймворк
- 🐘 **PostgreSQL** — надёжная база данных
- 🔄 **Redis** — кэширование и FSM
- 🐳 **Docker** — одной командой в продакшен
- 📊 **Alembic** — миграции базы данных
- ⚙️ **Pydantic Settings** — типизированная конфигурация
- 🎨 **Структура проекта** — готова к масштабированию
- 🔐 **Middleware** — throttling, logging, auth

---

## 📁 Структура проекта

```
aiogram-starter-kit/
├── bot/
│   ├── __init__.py
│   ├── __main__.py          # Точка входа
│   ├── config.py             # Конфигурация
│   ├── handlers/
│   │   ├── __init__.py
│   │   ├── start.py          # /start команда
│   │   ├── help.py           # /help команда
│   │   └── admin.py          # Админ-команды
│   ├── keyboards/
│   │   ├── __init__.py
│   │   ├── inline.py         # Inline клавиатуры
│   │   └── reply.py          # Reply клавиатуры
│   ├── middlewares/
│   │   ├── __init__.py
│   │   ├── throttling.py     # Антиспам
│   │   └── database.py       # DB сессии
│   ├── database/
│   │   ├── __init__.py
│   │   ├── models.py         # SQLAlchemy модели
│   │   └── queries.py        # Запросы к БД
│   ├── services/
│   │   └── __init__.py
│   └── utils/
│       └── __init__.py
├── docker-compose.yml
├── Dockerfile
├── .env.example
├── requirements.txt
└── README.md
```

---

## ⚙️ Конфигурация

Создайте файл `.env` на основе `.env.example`:

```env
# Bot
BOT_TOKEN=your_bot_token_here
ADMIN_IDS=123456789,987654321

# Database
POSTGRES_USER=bot
POSTGRES_PASSWORD=password
POSTGRES_DB=telegram_bot
DATABASE_URL=postgresql+asyncpg://bot:password@db:5432/telegram_bot

# Redis
REDIS_URL=redis://redis:6379/0
```

---

## 🐳 Docker

### Запуск в продакшене

```bash
docker-compose up -d --build
```

### Просмотр логов

```bash
docker-compose logs -f bot
```

### Остановка

```bash
docker-compose down
```

---

## 🔧 Команды бота

| Команда | Описание |
|---------|----------|
| `/start` | Начало работы с ботом |
| `/help` | Список команд |
| `/stats` | Статистика (только админ) |
| `/broadcast` | Рассылка (только админ) |

---

## 📊 База данных

### Модели

```python
from sqlalchemy import Column, Integer, BigInteger, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger, unique=True, index=True)
    username = Column(String(32), nullable=True)
    first_name = Column(String(64))
    created_at = Column(DateTime, server_default="now()")
```

### Миграции

```bash
# Создать миграцию
alembic revision --autogenerate -m "Add users table"

# Применить миграции
alembic upgrade head
```

---

## 🛡️ Middleware

### Throttling (антиспам)

```python
from aiogram import BaseMiddleware
from aiogram.types import Message

class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, rate_limit: float = 0.5):
        self.rate_limit = rate_limit
        
    async def __call__(self, handler, event: Message, data: dict):
        # Проверка лимита...
        return await handler(event, data)
```

---

## 🚀 Деплой

### Рекомендуемые сервисы

| Сервис | Описание | Оплата из РФ |
|--------|----------|--------------|
| [Amvera](https://amvera.ru/) | Российский PaaS | ✅ |
| [Selectel](https://selectel.ru/) | Облачный VPS | ✅ |
| [TimeWeb](https://timeweb.cloud/) | VPS от ₽150/мес | ✅ |

### Webhook vs Polling

По умолчанию используется **polling**. Для webhook:

```python
# В config.py
WEBHOOK_URL = "https://your-domain.com/webhook"
WEBHOOK_SECRET = "your-secret"
```

---

## 🤝 Contributing

1. Fork репозитория
2. Создайте ветку: `git checkout -b feature/amazing-feature`
3. Commit изменений: `git commit -m 'Add amazing feature'`
4. Push: `git push origin feature/amazing-feature`
5. Откройте Pull Request

---

## 📄 License

MIT License — используйте свободно!

---

<div align="center">

**Сделано с ❤️ [Egor Terskii](https://github.com/Chumbayoumba)**

[![Telegram](https://img.shields.io/badge/Вопросы-@longfest-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/longfest)

⭐ **Если шаблон полезен — поставьте звезду!**

</div>

---

<a name="english"></a>
## 🇬🇧 English

Production-ready Telegram bot template with Aiogram 3.x, PostgreSQL, Redis, and Docker.

See the Russian documentation above — the code is self-explanatory!