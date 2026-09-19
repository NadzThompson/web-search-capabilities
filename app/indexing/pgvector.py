"""PGVector adapter placeholder for semantic retrieval.
Production deployments should use the organization's approved embedding service and connection management.
"""
from app.config import settings

class PGVectorIndex:
    def __init__(self):
        if not settings.nova_pgvector_dsn:
            raise RuntimeError("NOVA_PGVECTOR_DSN is required")
        self.dsn = settings.nova_pgvector_dsn
        self.table = settings.nova_pgvector_table
