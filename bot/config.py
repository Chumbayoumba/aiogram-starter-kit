from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Bot configuration"""
    
    # Bot
    BOT_TOKEN: str
    ADMIN_IDS: list[int] = []
    
    # Database
    DATABASE_URL: str = "sqlite+aiosqlite:///bot.db"
    
    # Redis (optional)
    REDIS_URL: str | None = None
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
