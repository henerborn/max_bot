from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # - Bot
    BOT_TOKEN: str
    DEBUG: bool
    DB_URL: str

    # - paths to attachment files
    # -- main page
    TITLE_IMG: str
    # -- admission page
    GUIDE_IMG: str
    # -- meeting page
    MEETING_SCHEDULE_IMG: str

    # - Workers
    PARSE_TIME: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


settings = Settings()