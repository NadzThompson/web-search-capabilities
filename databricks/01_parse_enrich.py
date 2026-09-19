# Databricks job skeleton: raw ADLS evidence -> cleaned/enriched Delta tables.
# Replace paths/catalog/schema with NOVA-approved Unity Catalog objects.
from pyspark.sql import functions as F

RAW_PATH = "abfss://web-evidence@<account>.dfs.core.windows.net/raw/"
TARGET_TABLE = "nova_web.web_evidence_documents"

df = (spark.read.format("binaryFile").option("recursiveFileLookup", "true").load(RAW_PATH)
      .withColumn("content_hash", F.sha2(F.col("content"), 256))
      .withColumn("ingested_at", F.current_timestamp()))

(df.select("path","length","modificationTime","content_hash","ingested_at")
   .write.mode("append").format("delta").saveAsTable(TARGET_TABLE))
