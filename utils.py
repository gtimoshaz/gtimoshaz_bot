import requests
from lxml import etree

def get_bruh_html() -> str:
    r = requests.get("https://bruhanova.ru/")
    return r.text

def get_signs_count(html: str) -> int:
    htmlparser = etree.HTMLParser()
    tree = etree.fromstring(html, htmlparser)
    xpath = "/html/body/main/section[3]/div/div/div[1]/div[2]/p[1]/span"
    el = tree.xpath(xpath)
    return int(el[0].text)

