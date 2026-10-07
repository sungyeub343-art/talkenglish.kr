from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import xml.etree.ElementTree as ET


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.titles = []
        self.canonicals = []
        self.in_title = False

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        self.links.extend(attributes[key] for key in ("href", "src") if key in attributes)
        if tag == "link" and attributes.get("rel") == "canonical":
            self.canonicals.append(attributes.get("href"))
        self.in_title = tag == "title"

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title and data.strip():
            self.titles.append(data.strip())


root = Path(__file__).parent
html_files = list(root.glob("*.html"))
neighborhood_files = list(root.glob("daejeon-*-dong-adult-english-conversation.html"))
regional_files = [
    path
    for path in root.glob("*-adult-english-conversation.html")
    if not path.name.startswith("daejeon-")
]
missing_links = []
titles = []
canonicals = []

for html_file in html_files:
    parser = PageParser()
    parser.feed(html_file.read_text(encoding="utf-8"))
    titles.extend(parser.titles)
    canonicals.extend(parser.canonicals)
    for link in parser.links:
        parsed = urlparse(link)
        if parsed.scheme or link.startswith(("#", "tel:", "mailto:", "//")):
            continue
        if parsed.path and not (root / parsed.path).exists():
            missing_links.append((html_file.name, link))

namespace = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
sitemap = ET.parse(root / "sitemap-neighborhoods.xml")
sitemap_count = len(sitemap.findall("s:url", namespace))
region_sitemap = ET.parse(root / "sitemap-regions.xml")
region_sitemap_count = len(region_sitemap.findall("s:url", namespace))

checks = {
    "neighborhood_pages": len(neighborhood_files) == 82,
    "regional_pages": len(regional_files) == 224,
    "missing_local_links": not missing_links,
    "unique_titles": len(titles) == len(set(titles)),
    "unique_canonicals": len(canonicals) == len(set(canonicals)),
    "neighborhood_sitemap_urls": sitemap_count == 82,
    "regional_sitemap_urls": region_sitemap_count == 225,
}

for name, passed in checks.items():
    print(f"{name}: {'PASS' if passed else 'FAIL'}")
if missing_links:
    print(missing_links[:10])
if not all(checks.values()):
    raise SystemExit(1)