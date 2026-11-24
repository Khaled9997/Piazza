"""Application settings read from environment variables.

Only placeholders belong in the repository. Real values are supplied at
runtime (shell environment, Docker -e/--env-file, Kubernetes Secret).
"""
import os
from dataclasses import dataclass

MIN_SECRET_LENGTH = 32


class ConfigError(RuntimeError):
    """Raised when required configuration is missing or unsafe."""


@dataclass(frozen=True)
class Settings:
    database_path: str
    jwt_secret: str
    jwt_algorithm: str = "HS256"
    jwt_expire_minutes: int = 30
    bcrypt_rounds: int = 12

    def validate(self) -> "Settings":
        if not self.jwt_secret or len(self.jwt_secret) < MIN_SECRET_LENGTH:
            raise ConfigError(
                f"PIAZZA_JWT_SECRET must be set to at least {MIN_SECRET_LENGTH} characters"
            )
        if not 4 <= self.bcrypt_rounds <= 31:
            raise ConfigError("bcrypt_rounds must be between 4 and 31")
        if self.jwt_expire_minutes <= 0:
            raise ConfigError("PIAZZA_JWT_EXPIRE_MINUTES must be positive")
        return self


def load_settings() -> Settings:
    """Build settings from the process environment."""
    return Settings(
        database_path=os.getenv("PIAZZA_DATABASE_PATH", "./data/piazza.db"),
        jwt_secret=os.getenv("PIAZZA_JWT_SECRET", ""),
        jwt_expire_minutes=int(os.getenv("PIAZZA_JWT_EXPIRE_MINUTES", "30")),
    ).validate()
