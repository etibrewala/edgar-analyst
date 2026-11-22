from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    sec_user_agent: str
    anthropic_api_key: str = ""


settings = Settings()  # type: ignore[call-arg]
