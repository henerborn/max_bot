from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    BOT_TOKEN: str
    DEBUG: bool

    # - paths to attachment files
    # -- main page
    TITLE_IMG: str
    VUC_PRESENTATION_PDF: str
    SELECTION_REGULATIONS_PDF: str
    VUC_REGULATION_PDF: str
    # -- admission page
    REMINDER_IMG: str
    # -- meeting page
    MEETING_SCHEDULE_IMG: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


settings = Settings()