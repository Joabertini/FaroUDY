from urllib.parse import urljoin
import httpx


def detect(root_url:str)->bool:
    paths=['/sitemap.xml','/sitemap_index.xml']
    for path in paths:
        try:
            r=httpx.get(urljoin(root_url,path),timeout=10)
            if r.status_code==200:
                return True
        except Exception:
            pass
    return False