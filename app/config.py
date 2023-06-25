from pydantic import BaseSettings

class Settings(BaseSettings):
    database_username: str
    database_password: str
    database_host: str
    database_port: str
    database_name: str
    secret_key: str

    class Config:
        env_file = "app/.env"

settings = Settings.parse_obj({})
