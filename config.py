import pydantic


class Settings(pydantic.BaseSettings):
    browser: str = 'chrome'
    timeout: float = 9.0

settings = Settings(_env_file='config.env')