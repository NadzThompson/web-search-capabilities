import hashlib
import json
import logging
import uuid
from datetime import datetime, timezone
log = logging.getLogger("nova.audit")

def query_hash(query: str) -> str:
    return hashlib.sha256(query.encode()).hexdigest()

def record(event_type: str, **fields):
    safe = {"event_id": str(uuid.uuid4()), "event_type": event_type, "timestamp": datetime.now(timezone.utc).isoformat(), **fields}
    log.info(json.dumps(safe, sort_keys=True, default=str))
