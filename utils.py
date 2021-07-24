import httpx
from lxml import etree

async def get_bruh_html() -> str:
    async with httpx.AsyncClient() as client:
        r = await client.get("https://bruhanova.ru/")
        return r.text

def get_signs_count(html: str) -> int:
    htmlparser = etree.HTMLParser()
    tree = etree.fromstring(html, htmlparser)
    xpath = "/html/body/main/section[3]/div/div/div[1]/div[2]/p[1]/span"

    el = tree.xpath(xpath)
    return int(el[0].text)

async def download_signs_count() -> int:
    s = await get_bruh_html()
    return get_signs_count(s)
