from urllib.parse import urlparse
from app.models.enums import SourceTier
from app.skills.types import SkillResult

PRIMARY_HINTS = ('gov','gc.ca','bis.org','imf.org','worldbank.org','ecb.europa.eu','bankofengland.co.uk','federalreserve.gov')
ESTABLISHED_HINTS = ('reuters.com','ft.com','bloomberg.com')

def run(url: str, registry: dict[str, dict] | None = None) -> SkillResult:
    domain = (urlparse(url).hostname or '').lower()
    if registry and domain in registry:
        item = registry[domain]
        return SkillResult(True, {'domain': domain, 'tier': item.get('tier','t6_unverified'), 'primary_source': bool(item.get('primary_source'))})
    if any(domain.endswith(x) for x in PRIMARY_HINTS):
        return SkillResult(True, {'domain': domain, 'tier': SourceTier.T1_PRIMARY.value, 'primary_source': True})
    if any(domain.endswith(x) for x in ESTABLISHED_HINTS):
        return SkillResult(True, {'domain': domain, 'tier': SourceTier.T3_ESTABLISHED.value, 'primary_source': False})
    return SkillResult(True, {'domain': domain, 'tier': SourceTier.T6_UNVERIFIED.value, 'primary_source': False}, warnings=['unverified_source'])
