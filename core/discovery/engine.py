from .models import DiscoveryReport

class DiscoveryEngine:
    def discover(self, root_url:str)->DiscoveryReport:
        report=DiscoveryReport(root_url=root_url)
        # TODO: invoke robots, sitemap, cms, api detectors
        return report
