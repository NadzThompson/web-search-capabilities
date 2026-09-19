# Databricks job skeleton: approved cleaned chunks -> embedding publication queue.
# The actual embedding model endpoint must be bank-approved.
from pyspark.sql import functions as F

SOURCE_TABLE = "nova_web.web_evidence_chunks"
PUBLISH_TABLE = "nova_web.embedding_publish_queue"

chunks = spark.table(SOURCE_TABLE).filter("quarantined = false")
(chunks.select("chunk_id","text","content_hash","source_url","source_tier")
       .withColumn("queued_at", F.current_timestamp())
       .write.mode("append").format("delta").saveAsTable(PUBLISH_TABLE))
