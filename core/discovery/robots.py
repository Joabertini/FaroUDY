from urllib.parse import urljoin
import httpx


def detect(root_url:str)->bool:
    try:
        r=httpx.get(urljoin(root_url,'/robots.txt'),timeout=10)
        return r.status_code==200
    except Exception:
        return False