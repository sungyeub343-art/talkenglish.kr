from html import escape
from pathlib import Path


ROOT = Path(__file__).parent
LAST_MODIFIED = "2026-10-07"
REGIONS = [
    ("서울", "seoul", "직장과 일상이 빠르게 이어지는 수도권 생활", [
        ("종로구", "jongno-gu"), ("중구", "jung-gu"), ("용산구", "yongsan-gu"),
        ("성동구", "seongdong-gu"), ("광진구", "gwangjin-gu"), ("동대문구", "dongdaemun-gu"),
        ("중랑구", "jungnang-gu"), ("성북구", "seongbuk-gu"), ("강북구", "gangbuk-gu"),
        ("도봉구", "dobong-gu"), ("노원구", "nowon-gu"), ("은평구", "eunpyeong-gu"),
        ("서대문구", "seodaemun-gu"), ("마포구", "mapo-gu"), ("양천구", "yangcheon-gu"),
        ("강서구", "gangseo-gu"), ("구로구", "guro-gu"), ("금천구", "geumcheon-gu"),
        ("영등포구", "yeongdeungpo-gu"), ("동작구", "dongjak-gu"), ("관악구", "gwanak-gu"),
        ("서초구", "seocho-gu"), ("강남구", "gangnam-gu"), ("송파구", "songpa-gu"),
        ("강동구", "gangdong-gu"),
    ]),
    ("부산", "busan", "관광과 비즈니스가 함께 활발한 해양도시 생활", [
        ("중구", "jung-gu"), ("서구", "seo-gu"), ("동구", "dong-gu"), ("영도구", "yeongdo-gu"),
        ("부산진구", "busanjin-gu"), ("동래구", "dongnae-gu"), ("남구", "nam-gu"),
        ("북구", "buk-gu"), ("해운대구", "haeundae-gu"), ("사하구", "saha-gu"),
        ("금정구", "geumjeong-gu"), ("강서구", "gangseo-gu"), ("연제구", "yeonje-gu"),
        ("수영구", "suyeong-gu"), ("사상구", "sasang-gu"), ("기장군", "gijang-gun"),
    ]),
    ("대구", "daegu", "교육과 산업, 생활권이 고르게 발달한 도시 생활", [
        ("중구", "jung-gu"), ("동구", "dong-gu"), ("서구", "seo-gu"), ("남구", "nam-gu"),
        ("북구", "buk-gu"), ("수성구", "suseong-gu"), ("달서구", "dalseo-gu"),
        ("달성군", "dalseong-gun"), ("군위군", "gunwi-gun"),
    ]),
    ("인천", "incheon", "공항과 국제업무 수요가 가까운 수도권 생활", [
        ("중구", "jung-gu"), ("동구", "dong-gu"), ("미추홀구", "michuhol-gu"),
        ("연수구", "yeonsu-gu"), ("남동구", "namdong-gu"), ("부평구", "bupyeong-gu"),
        ("계양구", "gyeyang-gu"), ("서구", "seo-gu"), ("강화군", "ganghwa-gun"),
        ("옹진군", "ongjin-gun"),
    ]),
    ("광주", "gwangju", "교육과 문화 활동이 활발한 호남권 도시 생활", [
        ("동구", "dong-gu"), ("서구", "seo-gu"), ("남구", "nam-gu"),
        ("북구", "buk-gu"), ("광산구", "gwangsan-gu"),
    ]),
    ("울산", "ulsan", "산업 현장과 국제업무가 밀접한 도시 생활", [
        ("중구", "jung-gu"), ("남구", "nam-gu"), ("동구", "dong-gu"),
        ("북구", "buk-gu"), ("울주군", "ulju-gun"),
    ]),
    ("세종", "sejong", "행정과 연구기관 종사자가 많은 계획도시 생활", [
        ("세종시", "sejong-si"),
    ]),
    ("경기", "gyeonggi", "통근과 업무, 가족 생활이 함께 이어지는 수도권 생활", [
        ("수원시", "suwon-si"), ("용인시", "yongin-si"), ("고양시", "goyang-si"),
        ("화성시", "hwaseong-si"), ("성남시", "seongnam-si"), ("부천시", "bucheon-si"),
        ("남양주시", "namyangju-si"), ("안산시", "ansan-si"), ("평택시", "pyeongtaek-si"),
        ("안양시", "anyang-si"), ("시흥시", "siheung-si"), ("파주시", "paju-si"),
        ("김포시", "gimpo-si"), ("의정부시", "uijeongbu-si"), ("광주시", "gwangju-si"),
        ("하남시", "hanam-si"), ("광명시", "gwangmyeong-si"), ("군포시", "gunpo-si"),
        ("양주시", "yangju-si"), ("오산시", "osan-si"), ("이천시", "icheon-si"),
        ("안성시", "anseong-si"), ("구리시", "guri-si"), ("의왕시", "uiwang-si"),
        ("포천시", "pocheon-si"), ("양평군", "yangpyeong-gun"), ("여주시", "yeoju-si"),
        ("동두천시", "dongducheon-si"), ("과천시", "gwacheon-si"), ("가평군", "gapyeong-gun"),
        ("연천군", "yeoncheon-gun"),
    ]),
    ("강원", "gangwon", "관광과 지역 산업에 필요한 소통이 많은 생활권", [
        ("춘천시", "chuncheon-si"), ("원주시", "wonju-si"), ("강릉시", "gangneung-si"),
        ("동해시", "donghae-si"), ("태백시", "taebaek-si"), ("속초시", "sokcho-si"),
        ("삼척시", "samcheok-si"), ("홍천군", "hongcheon-gun"), ("횡성군", "hoengseong-gun"),
        ("영월군", "yeongwol-gun"), ("평창군", "pyeongchang-gun"), ("정선군", "jeongseon-gun"),
        ("철원군", "cheorwon-gun"), ("화천군", "hwacheon-gun"), ("양구군", "yanggu-gun"),
        ("인제군", "inje-gun"), ("고성군", "goseong-gun"), ("양양군", "yangyang-gun"),
    ]),
    ("충북", "chungbuk", "산업단지와 도심, 지역 생활권이 연결된 일상", [
        ("청주시", "cheongju-si"), ("충주시", "chungju-si"), ("제천시", "jecheon-si"),
        ("보은군", "boeun-gun"), ("옥천군", "okcheon-gun"), ("영동군", "yeongdong-gun"),
        ("증평군", "jeungpyeong-gun"), ("진천군", "jincheon-gun"), ("괴산군", "goesan-gun"),
        ("음성군", "eumseong-gun"), ("단양군", "danyang-gun"),
    ]),
    ("충남", "chungnam", "산업과 행정, 지역 생활이 폭넓게 이어지는 일상", [
        ("천안시", "cheonan-si"), ("공주시", "gongju-si"), ("보령시", "boryeong-si"),
        ("아산시", "asan-si"), ("서산시", "seosan-si"), ("논산시", "nonsan-si"),
        ("계룡시", "gyeryong-si"), ("당진시", "dangjin-si"), ("금산군", "geumsan-gun"),
        ("부여군", "buyeo-gun"), ("서천군", "seocheon-gun"), ("청양군", "cheongyang-gun"),
        ("홍성군", "hongseong-gun"), ("예산군", "yesan-gun"), ("태안군", "taean-gun"),
    ]),
    ("전북", "jeonbuk", "교육과 관광, 지역 산업이 조화를 이루는 생활권", [
        ("전주시", "jeonju-si"), ("군산시", "gunsan-si"), ("익산시", "iksan-si"),
        ("정읍시", "jeongeup-si"), ("남원시", "namwon-si"), ("김제시", "gimje-si"),
        ("완주군", "wanju-gun"), ("진안군", "jinan-gun"), ("무주군", "muju-gun"),
        ("장수군", "jangsu-gun"), ("임실군", "imsil-gun"), ("순창군", "sunchang-gun"),
        ("고창군", "gochang-gun"), ("부안군", "buan-gun"),
    ]),
    ("전남", "jeonnam", "관광과 농수산업, 생활 서비스가 어우러진 지역", [
        ("목포시", "mokpo-si"), ("여수시", "yeosu-si"), ("순천시", "suncheon-si"),
        ("나주시", "naju-si"), ("광양시", "gwangyang-si"), ("담양군", "damyang-gun"),
        ("곡성군", "gokseong-gun"), ("구례군", "gurye-gun"), ("고흥군", "goheung-gun"),
        ("보성군", "boseong-gun"), ("화순군", "hwasun-gun"), ("장흥군", "jangheung-gun"),
        ("강진군", "gangjin-gun"), ("해남군", "haenam-gun"), ("영암군", "yeongam-gun"),
        ("무안군", "muan-gun"), ("함평군", "hampyeong-gun"), ("영광군", "yeonggwang-gun"),
        ("장성군", "jangseong-gun"), ("완도군", "wando-gun"), ("진도군", "jindo-gun"),
        ("신안군", "sinan-gun"),
    ]),
    ("경북", "gyeongbuk", "제조업과 관광, 지역 생활이 폭넓게 연결된 일상", [
        ("포항시", "pohang-si"), ("경주시", "gyeongju-si"), ("김천시", "gimcheon-si"),
        ("안동시", "andong-si"), ("구미시", "gumi-si"), ("영주시", "yeongju-si"),
        ("영천시", "yeongcheon-si"), ("상주시", "sangju-si"), ("문경시", "mungyeong-si"),
        ("경산시", "gyeongsan-si"), ("의성군", "uiseong-gun"), ("청송군", "cheongsong-gun"),
        ("영양군", "yeongyang-gun"), ("영덕군", "yeongdeok-gun"), ("청도군", "cheongdo-gun"),
        ("고령군", "goryeong-gun"), ("성주군", "seongju-gun"), ("칠곡군", "chilgok-gun"),
        ("예천군", "yecheon-gun"), ("봉화군", "bonghwa-gun"), ("울진군", "uljin-gun"),
        ("울릉군", "ulleung-gun"),
    ]),
    ("경남", "gyeongnam", "산업도시와 해안 관광권이 함께 이어지는 생활", [
        ("창원시", "changwon-si"), ("진주시", "jinju-si"), ("통영시", "tongyeong-si"),
        ("사천시", "sacheon-si"), ("김해시", "gimhae-si"), ("밀양시", "miryang-si"),
        ("거제시", "geoje-si"), ("양산시", "yangsan-si"), ("의령군", "uiryeong-gun"),
        ("함안군", "haman-gun"), ("창녕군", "changnyeong-gun"), ("고성군", "goseong-gun"),
        ("남해군", "namhae-gun"), ("하동군", "hadong-gun"), ("산청군", "sancheong-gun"),
        ("함양군", "hamyang-gun"), ("거창군", "geochang-gun"), ("합천군", "hapcheon-gun"),
    ]),
    ("제주", "jeju", "관광과 국제 교류가 일상 가까이 있는 섬 생활", [
        ("제주시", "jeju-si"), ("서귀포시", "seogwipo-si"),
    ]),
]


def page_filename(region_slug, area_slug):
    return f"{region_slug}-{area_slug}-adult-english-conversation.html"


def render_page(region_name, region_slug, context, area_name, area_slug, areas):
    filename = page_filename(region_slug, area_slug)
    nearby_links = "".join(
        f'<a href="{page_filename(region_slug, sibling_slug)}"'
        f'{" aria-current=\"page\"" if sibling_slug == area_slug else ""}>'
        f'{escape(sibling_name)}</a>'
        for sibling_name, sibling_slug in areas
    )
    return f'''<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{region_name} {area_name} 성인 영어 스피킹 안내. 일상, 여행, 업무에 필요한 실용 영어회화 학습 방향과 상담 정보를 확인하세요.">
  <title>{region_name} {area_name} 성인 영어 스피킹·영어회화 안내 | 파워잉글리쉬</title>
  <link rel="canonical" href="https://talkenglish.kr/{filename}">
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
    <nav class="breadcrumb" aria-label="현재 위치"><a href="index.html">홈</a><span>›</span><a href="conversation-guide.html">회화 안내</a><span>›</span><a href="regional-conversation-guide.html">전국 지역</a><span>›</span>{region_name} {area_name}</nav>
    <section class="guide-hero">
      <div class="guide-hero-copy"><p class="eyebrow">{area_slug.replace('-', ' ')} · {region_slug}</p><h1>{region_name} {area_name}<br>성인 영어 스피킹 안내</h1><p>{context}에 맞춰 영어 말하기를 시작해 보세요. 현재 수준과 목표를 확인하고 일상, 여행, 업무에서 실제로 사용할 표현을 중심으로 학습 방향을 안내합니다.</p></div>
      <div class="guide-hero-media"><img src="https://images.unsplash.com/photo-1529156069898-49953e39b3ac?auto=format&fit=crop&w=1400&q=88" alt="함께 영어 대화를 연습하는 성인 학습자들"><span class="location-stamp">{region_name}<br>{area_name}<br>스피킹 안내</span></div>
    </section>
    <section class="details">
      <p class="eyebrow">English For Real Life</p><h2>{area_name} 생활에 맞춘<br>실용 영어 스피킹</h2>
      <div class="feature-grid">
        <article class="feature"><b>01 · DAILY</b><h3>일상에서 바로 말하기</h3><p>자기소개와 스몰토크부터 전화, 쇼핑, 식당 등 자주 만나는 상황을 자연스럽게 연습합니다.</p></article>
        <article class="feature"><b>02 · PURPOSE</b><h3>목적에 맞춰 배우기</h3><p>여행, 업무, 취업 등 영어가 필요한 장면을 중심으로 꼭 필요한 표현부터 익힙니다.</p></article>
        <article class="feature"><b>03 · ROUTINE</b><h3>꾸준한 말하기 루틴</h3><p>현재 수준에 맞는 학습량과 반복 연습으로 영어가 입에 붙는 습관을 만듭니다.</p></article>
      </div>
      <div class="area-note"><strong>{region_name} {area_name} 영어회화 안내</strong>{area_name} 거주자와 직장인 등 지역 생활권의 성인 학습자를 위한 안내입니다. 상담을 통해 현재 영어 수준과 목표에 맞는 학습 방향을 확인할 수 있습니다.</div>
    </section>
    <section class="subareas"><div class="subareas-inner"><p class="eyebrow">Nearby Areas</p><h2>{region_name} 다른 시·군·구 안내</h2><p>{region_name}의 다른 지역 영어 스피킹 안내도 함께 확인하세요.</p><div class="subarea-grid">{nearby_links}</div></div></section>
    <section class="other-areas"><div class="other-areas-inner"><h2>전국 지역별 회화 안내</h2><div class="area-links"><a href="regional-conversation-guide.html">전국 시·군·구 보기</a><a href="conversation-guide.html">대전 지역 보기</a></div></div></section>
    <section class="contact"><div><p class="eyebrow">Start Here</p><h2>영어로 말하는 습관,<br>지금 시작하세요</h2><p>현재 수준과 학습 목적을 알려주시면 알맞은 회화 학습 방향을 안내해 드립니다.</p></div><a class="phone-button" href="tel:01029283614">전화 상담<br>010-2928-3614</a></section>
  </main>
  <footer class="site-footer"><div><a class="footer-brand" href="index.html">파워잉글리쉬</a><p class="footer-meta">교육문의 010-2928-3614<br>© 2026 파워잉글리쉬. All rights reserved.</p></div><div class="footer-links"><a href="index.html">홈</a><a href="conversation-guide.html">회화 안내</a></div></footer>
  <script src="guide.js"></script>
</body>
</html>
'''


def render_guide():
    region_sections = "\n".join(
        f'''      <section class="subareas"><div class="subareas-inner"><p class="eyebrow">{region_slug.upper()}</p><h2>{region_name} 영어 스피킹 안내</h2><p>{context}에 맞는 지역별 안내를 확인하세요.</p><div class="subarea-grid">{''.join(f'<a href="{page_filename(region_slug, area_slug)}">{escape(area_name)}</a>' for area_name, area_slug in areas)}</div></div></section>'''
        for region_name, region_slug, context, areas in REGIONS
    )
    total = sum(len(areas) for _, _, _, areas in REGIONS)
    return f'''<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="서울, 경기, 부산, 인천 등 전국 {total}개 시·군·구 성인 영어 스피킹 및 영어회화 학습 안내를 확인하세요.">
  <title>전국 시·군·구 성인 영어 스피킹 안내 | 파워잉글리쉬</title>
  <link rel="canonical" href="https://talkenglish.kr/regional-conversation-guide.html">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@500;600;700&family=Gowun+Batang:wght@700&family=Noto+Sans+KR:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="guide.css">
</head>
<body>
  <a class="skip-link" href="#main">본문 바로가기</a>
  <header class="site-header"><a class="brand" href="index.html" aria-label="파워잉글리쉬 홈"><span class="brand-mark" aria-hidden="true"><i></i><i></i><i></i><i></i></span>파워잉글리쉬</a><nav class="nav-links" id="site-menu" aria-label="주요 메뉴"><a href="index.html#about">교육 철학</a><a href="index.html#program">프로그램</a><a href="conversation-guide.html" aria-current="page">회화 안내</a><a class="nav-cta" href="tel:01029283614">상담 신청</a></nav><button class="menu-button" type="button" aria-label="메뉴 열기" aria-expanded="false" aria-controls="site-menu"><span></span></button></header>
  <main id="main">
    <nav class="breadcrumb" aria-label="현재 위치"><a href="index.html">홈</a><span>›</span><a href="conversation-guide.html">회화 안내</a><span>›</span>전국 지역</nav>
    <section class="guide-hero"><div class="guide-hero-copy"><p class="eyebrow">Korea Conversation Guide</p><h1>전국 시·군·구<br>성인 영어 스피킹 안내</h1><p>사는 곳과 생활 패턴에 맞는 영어 말하기 학습 정보를 찾아보세요. 대전을 제외한 전국 {total}개 시·군·구별 학습 방향을 안내합니다.</p></div><div class="guide-hero-media"><img src="https://images.unsplash.com/photo-1529156069898-49953e39b3ac?auto=format&fit=crop&w=1400&q=88" alt="편안하게 영어 대화를 나누는 성인 학습자들"><span class="location-stamp">전국<br>{total}개 지역<br>스피킹 안내</span></div></section>
{region_sections}
    <section class="contact"><div><p class="eyebrow">Start Here</p><h2>나에게 맞는 회화 과정,<br>상담부터 시작하세요</h2><p>현재 영어 수준과 배우는 목적을 알려주시면 알맞은 학습 방향을 안내해 드립니다.</p></div><a class="phone-button" href="tel:01029283614">전화 상담<br>010-2928-3614</a></section>
  </main>
  <footer class="site-footer"><div><a class="footer-brand" href="index.html">파워잉글리쉬</a><p class="footer-meta">교육문의 010-2928-3614<br>© 2026 파워잉글리쉬. All rights reserved.</p></div><div class="footer-links"><a href="index.html">홈</a><a href="conversation-guide.html">회화 안내</a></div></footer>
  <script src="guide.js"></script>
</body>
</html>
'''


pages = []
for region_name, region_slug, context, areas in REGIONS:
    for area_name, area_slug in areas:
        filename = page_filename(region_slug, area_slug)
        pages.append(filename)
        (ROOT / filename).write_text(
            render_page(region_name, region_slug, context, area_name, area_slug, areas),
            encoding="utf-8",
        )

if len(pages) != 224 or len(set(pages)) != len(pages):
    raise RuntimeError(f"Expected 224 unique regional pages, found {len(set(pages))}.")

(ROOT / "regional-conversation-guide.html").write_text(render_guide(), encoding="utf-8")
sitemap_urls = "\n".join(
    f"  <url>\n    <loc>https://talkenglish.kr/{page}</loc>\n    <lastmod>{LAST_MODIFIED}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.7</priority>\n  </url>"
    for page in ["regional-conversation-guide.html", *pages]
)
(ROOT / "sitemap-regions.xml").write_text(
    f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{sitemap_urls}
</urlset>
''',
    encoding="utf-8",
)

print(f"Generated {len(pages)} regional pages, regional guide, and sitemap-regions.xml")