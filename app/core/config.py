from dotenv import load_dotenv
from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str

    def __init__(self) -> None:
        # load env
        load_dotenv()
        super().__init__()

    class Config:
        case_sensitive = True
        env_file = '.env'

    DB_URL: str


SystemConfig = Settings()
