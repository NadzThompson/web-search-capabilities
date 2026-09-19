CREATE EXTENSION IF NOT EXISTS vector;
CREATE TABLE IF NOT EXISTS nova_web_chunks (
  chunk_id text PRIMARY KEY,
  url text NOT NULL,
  domain text NOT NULL,
  title text,
  content_hash text NOT NULL,
  text_content text NOT NULL,
  embedding vector(1536),
  source_tier text,
  jurisdiction text,
  primary_source boolean DEFAULT false,
  published_at timestamptz,
  retrieved_at timestamptz NOT NULL,
  injection_risk double precision DEFAULT 0,
  metadata jsonb DEFAULT '{}'::jsonb
);
CREATE INDEX IF NOT EXISTS nova_web_chunks_embedding_idx ON nova_web_chunks USING hnsw (embedding vector_cosine_ops);
CREATE INDEX IF NOT EXISTS nova_web_chunks_domain_idx ON nova_web_chunks(domain);
CREATE INDEX IF NOT EXISTS nova_web_chunks_retrieved_idx ON nova_web_chunks(retrieved_at DESC);
