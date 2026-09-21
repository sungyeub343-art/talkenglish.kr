from html import escape
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).parent
DISTRICTS = [
    ("동구", "dong-gu"),
    ("중구", "jung-gu"),
    ("서구", "seo-gu"),
    ("유성구", "yuseong-gu"),
    ("대덕구", "daedeok-gu"),
]


class SubareaLinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_grid = False
        self.current_href = None
        self.current_text = []
        self.links = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "div" and "subarea-grid" in attributes.get("class", "").split():
            self.in_grid = True
        elif self.in_grid and tag == "a":
            self.current_href = attributes.get("href")
            self.current_text = []

    def handle_data(self, data):
        if self.current_href:
            self.current_text.append(data)

    def handle_endtag(self, tag):
        if self.in_grid and tag == "a" and self.current_href:
            self.links.append(("".join(self.current_text).strip(), self.current_href))
            self.current_href = None
        elif self.in_grid and tag == "div":
            self.in_grid = False


def read_subareas(district_slug):
    parser = SubareaLinkParser()
    source = ROOT / f"daejeon-{district_slug}-adult-english-conversation.html"
    parser.feed(source.read_text(encoding="utf-8"))
    return parser.links


def render_page(district_name, district_slug, area_name, page_file, siblings):
    area_slug = page_file.removeprefix(f"daejeon-{district_slug}-").removesuffix(
        "-adult-english-conversation.html"
    )
    sibling_links = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if href == page_file else ""}>{escape(name)}</a>'
        for name, href in siblings
    )
    district_links = "".join(
        f'<a href="daejeon-{slug}-adult-english-conversation.html">{name}</a>'
        for name, slug in DISTRICTS
        if slug != district_slug
    )
    return f'''<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="대전 {district_name} {area_name} 성인영어회화 안내. 일상, 여행, 업무에 필요한 실용 영어회화 학습 방향과 상담 정보를 확인하세요.">
  <title>대전 {district_name} {area_name} 성인영어회화 안내 | 파워잉글리쉬</title>
  <link rel="canonical" href="https://talkenglish.kr/{page_file}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@500;600;700&family=Gowun+Batang:wght@700&family=Noto+Sans+KR:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="guide.css">
</head>
<body>
  <a class="skip-link" href="#main">본문 바로가기</a>
  <header class="site-header">
    <a class="brand" href="index.html" aria-label="파워잉글리쉬 홈"><span class="brand-mark" aria-hidden="true"><i></i><i></i><i></i><i></i></span>파워잉글리쉬</a>
    <nav class="nav-links" id="site-menu" aria-label="주요 메뉴"><a href="index.html#about">교육 철학</a><a href="index.html#program">프로그램</a><a href="conversation-guide.html" aria-current="page">회화 안내</a><a class="nav-cta" href="tel:01029283614">상담 신청</a></nav>
    <button class="menu-button" type="button" aria-label="메뉴 열기" aria-expanded="false" aria-controls="site-menu"><span></span></button>
  </header>
  <main id="main">
    <nav class="breadcrumb" aria-label="현재 위치"><a href="index.html">홈</a><span>›</span><a href="conversation-guide.html">회화 안내</a><span>›</span><a href="daejeon-{district_slug}-adult-english-conversation.html">대전 {district_name}</a><span>›</span>{area_name}</nav>
    <section class="guide-hero">
      <div class="guide-hero-copy"><p class="eyebrow">{area_slug.replace('-', ' ')} · Daejeon</p><h1>대전 {district_name}<br>{area_name} 성인영어회화 안내</h1><p>{area_name}에서 생활하는 성인 학습자가 영어를 부담 없이 시작하고 꾸준히 이어갈 수 있도록 수준과 목적에 맞는 회화 학습 방향을 안내합니다.</p></div>
      <div class="guide-hero-media"><img src="https://images.unsplash.com/photo-1529156069898-49953e39b3ac?auto=format&fit=crop&w=1400&q=88" alt="함께 영어 대화를 연습하는 성인 학습자들"><span class="location-stamp">{district_name}<br>{area_name}<br>회화 안내</span></div>
    </section>
    <section class="details">
      <p class="eyebrow">English For Real Life</p><h2>{area_name} 생활에 맞춘<br>실용 영어회화</h2>
      <div class="feature-grid">
        <article class="feature"><b>01 · DAILY</b><h3>일상에서 바로 쓰기</h3><p>자기소개와 스몰토크부터 전화, 쇼핑, 식당 등 자주 만나는 상황을 자연스럽게 말합니다.</p></article>
        <article class="feature"><b>02 · PURPOSE</b><h3>목적에 맞춰 배우기</h3><p>여행, 업무, 취업 등 영어가 필요한 장면을 중심으로 꼭 필요한 표현부터 익힙니다.</p></article>
        <article class="feature"><b>03 · ROUTINE</b><h3>꾸준한 말하기 루틴</h3><p>현재 수준에 맞는 학습량과 반복 연습으로 영어가 입에 붙는 습관을 만듭니다.</p></article>
      </div>
      <div class="area-note"><strong>대전 {district_name} {area_name} 회화 안내</strong>{area_name} 거주자와 직장인 등 지역 생활권의 성인 학습자를 위한 안내입니다. 상담을 통해 현재 영어 수준과 목표에 맞는 학습 방향을 확인할 수 있습니다.</div>
    </section>
    <section class="subareas"><div class="subareas-inner"><p class="eyebrow">Nearby Areas</p><h2>{district_name} 다른 동 안내</h2><p>{district_name}의 다른 행정동 회화 안내도 함께 확인하세요.</p><div class="subarea-grid">{sibling_links}</div></div></section>
    <section class="other-areas"><div class="other-areas-inner"><h2>대전 지역별 회화 안내</h2><div class="area-links"><a href="daejeon-{district_slug}-adult-english-conversation.html" aria-current="page">{district_name} 전체</a>{district_links}</div></div></section>
    <section class="contact"><div><p class="eyebrow">Start Here</p><h2>영어로 말하는 습관,<br>지금 시작하세요</h2><p>현재 수준과 학습 목적을 알려주시면 알맞은 회화 학습 방향을 안내해 드립니다.</p></div><a class="phone-button" href="tel:01029283614">전화 상담<br>010-2928-3614</a></section>
  </main>
  <footer class="site-footer"><div><a class="footer-brand" href="index.html">파워잉글리쉬</a><p class="footer-meta">교육문의 010-2928-3614<br>© 2026 파워잉글리쉬. All rights reserved.</p></div><div class="footer-links"><a href="index.html">홈</a><a href="conversation-guide.html">회화 안내</a></div></footer>
  <script src="guide.js"></script>
</body>
</html>
'''


pages = []
for district_name, district_slug in DISTRICTS:
    subareas = read_subareas(district_slug)
    for area_name, page_file in subareas:
        pages.append(page_file)
        (ROOT / page_file).write_text(
            render_page(district_name, district_slug, area_name, page_file, subareas),
            encoding="utf-8",
        )

if len(pages) != 82 or len(set(pages)) != len(pages):
    raise RuntimeError("Expected 82 unique neighborhood pages.")

sitemap_urls = "\n".join(
    f"""  <url>
    <loc>https://talkenglish.kr/{page}</loc>
    <lastmod>2026-09-21</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>"""
    for page in pages
)
(ROOT / "sitemap-neighborhoods.xml").write_text(
    f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{sitemap_urls}
</urlset>
''',
    encoding="utf-8",
)

print(f"Generated {len(pages)} neighborhood pages and sitemap-neighborhoods.xml")