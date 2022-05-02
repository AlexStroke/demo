import pydantic


class Settings(pydantic.BaseSettings):
    browser: str = 'chrome'
    timeout: float = 4.0

settings = Settings(_env_file='config.env')