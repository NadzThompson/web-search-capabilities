import ipaddress
import socket
from urllib.parse import urlparse

class UnsafeURL(ValueError):
    pass

def validate_public_url(url: str) -> str:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        raise UnsafeURL("Only http/https are allowed")
    if not parsed.hostname:
        raise UnsafeURL("Missing hostname")
    host = parsed.hostname.lower()
    if host in {"localhost", "metadata.google.internal"} or host.endswith(".local"):
        raise UnsafeURL("Local or metadata endpoint blocked")
    try:
        addresses = {x[4][0] for x in socket.getaddrinfo(host, parsed.port or (443 if parsed.scheme == "https" else 80), type=socket.SOCK_STREAM)}
    except socket.gaierror as exc:
        raise UnsafeURL("DNS resolution failed") from exc
    for addr in addresses:
        ip = ipaddress.ip_address(addr)
        if not ip.is_global:
            raise UnsafeURL(f"Non-public address blocked: {ip}")
    return url
