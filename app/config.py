from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="", extra="ignore")
    nova_env: str = "dev"
    nova_log_level: str = "INFO"
    nova_policy_file: Path = Path("config/policy.yaml")
    nova_source_registry: Path = Path("config/source_registry.yaml")
    nova_allow_live_fetch: bool = False
    nova_allow_external_provider_fallback: bool = False
    nova_max_fetch_bytes: int = 8_000_000
    nova_fetch_timeout_seconds: float = 10
    nova_search_top_k: int = 10
    nova_adls_account_url: str | None = None
    nova_adls_container: str = "web-evidence"
    nova_elastic_url: str | None = None
    nova_elastic_index: str = "nova-web-evidence"
    nova_pgvector_dsn: str | None = None
    nova_pgvector_table: str = "nova_web_chunks"

settings = Settings()
