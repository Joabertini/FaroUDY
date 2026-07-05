from dataclasses import dataclass, field
from typing import List

@dataclass
class Resource:
    url: str
    kind: str

@dataclass
class DiscoveryReport:
    root_url: str
    robots: bool=False
    sitemap: bool=False
    resources: List[Resource]=field(default_factory=list)
