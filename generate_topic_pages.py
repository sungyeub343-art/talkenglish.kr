import json
from html import escape
from pathlib import Path


ROOT = Path(__file__).parent
TOPICS = [
    {
        "slug": "beginner-adult-english-conversation",
        "title": "왕초보 성인 영어회화",
        "meta_title": "왕초보 성인 영어회화 | 기초 영어 말하기 시작법",
        "description": "영어를 오래 쉬었거나 처음 다시 시작하는 성인을 위한 왕초보 영어회화 안내. 기초 문장, 발음, 일상 표현부터 부담 없이 시작하세요.",
        "eyebrow": "Beginner English",
        "lead": "영어를 오래 쉬었어도 괜찮습니다. 단어만 외우기보다 짧은 문장을 직접 말하고 반복하면서 일상 대화의 기초를 만드는 방법을 안내합니다.",
        "stamp": "왕초보<br>기초부터<br>차근차근",
        "section_title": "영어가 막막할 때는<br>말할 수 있는 한 문장부터",
        "section_intro": "왕초보에게 필요한 것은 어려운 문법 진도가 아니라 자주 쓰는 문장을 이해하고 소리 내어 말하는 경험입니다.",
        "features": [
            ("01 · FOUNDATION", "기초 문장 만들기", "주어와 동사로 시작하는 짧은 문장부터 익혀 내 이야기를 직접 말합니다."),
            ("02 · PRONUNCIATION", "듣고 따라 말하기", "소리와 리듬을 듣고 반복해 영어 발음에 대한 부담을 줄입니다."),
            ("03 · DAILY", "생활 표현 익히기", "인사, 자기소개, 쇼핑, 식당처럼 자주 만나는 상황부터 연습합니다."),
        ],
        "note_title": "이런 분에게 맞습니다",
        "note": "알파벳과 기초 단어는 알지만 문장이 바로 나오지 않는 분, 오랫동안 영어를 쉬어 다시 시작하고 싶은 분, 문법 공부보다 실제 말하기 자신감을 먼저 키우고 싶은 분에게 적합합니다.",
        "faqs": [
            ("영어를 거의 못해도 시작할 수 있나요?", "네. 현재 알고 있는 단어와 짧은 표현을 확인한 뒤 말할 수 있는 기초 문장부터 단계적으로 시작합니다."),
            ("문법을 먼저 공부해야 하나요?", "말하기에 필요한 기본 문장 구조는 함께 익히되, 문법만 따로 외우기보다 실제 대화 문장 안에서 반복합니다."),
        ],
    },
    {
        "slug": "office-worker-english-conversation",
        "title": "직장인 영어회화",
        "meta_title": "직장인 영어회화 | 퇴근 후 실무 영어 말하기",
        "description": "바쁜 직장인을 위한 영어회화 안내. 퇴근 후 꾸준히 이어가는 학습 루틴과 회의, 전화, 이메일 등 실무 영어 말하기를 확인하세요.",
        "eyebrow": "English For Professionals",
        "lead": "업무에서 갑자기 영어가 필요할 때를 대비해 짧고 꾸준한 말하기 루틴을 만드세요. 자기소개부터 전화, 회의, 해외 동료와의 스몰토크까지 실제 장면을 중심으로 안내합니다.",
        "stamp": "직장인<br>퇴근 후<br>영어 루틴",
        "section_title": "바쁜 일정 속에서도<br>업무에 쓰이는 영어",
        "section_intro": "직장인 영어는 많이 아는 것보다 필요한 순간에 정확하고 자연스럽게 꺼내 말하는 연습이 중요합니다.",
        "features": [
            ("01 · SMALL TALK", "업무 관계 시작하기", "인사, 소개, 일정과 근황처럼 동료와 자연스럽게 대화를 여는 표현을 연습합니다."),
            ("02 · WORKPLACE", "실무 상황 말하기", "전화 응대, 요청, 일정 조율, 진행 상황 공유 등 반복되는 업무 장면을 익힙니다."),
            ("03 · ROUTINE", "지속 가능한 학습", "출퇴근과 퇴근 후 시간을 활용해 복습과 말하기를 꾸준히 이어갑니다."),
        ],
        "note_title": "직장인 영어회화의 핵심",
        "note": "직무와 회사 환경에 따라 자주 사용하는 표현이 다릅니다. 현재 필요한 회의, 전화, 프레젠테이션, 해외 고객 응대 장면을 우선 정하고 반복 가능한 학습 루틴을 만드는 것이 효율적입니다.",
        "faqs": [
            ("퇴근 후 짧게 공부해도 효과가 있나요?", "긴 수업 한 번보다 짧더라도 자주 듣고 말하는 편이 표현을 실제 업무에서 꺼내 쓰는 데 도움이 됩니다."),
            ("일상 영어와 비즈니스 영어 중 무엇부터 해야 하나요?", "기초가 부족하다면 일상 대화로 문장 구성력을 먼저 만들고, 필요한 업무 장면의 표현을 함께 확장하는 방식이 좋습니다."),
        ],
    },
    {
        "slug": "travel-english-conversation",
        "title": "여행 영어회화",
        "meta_title": "여행 영어회화 | 해외여행 상황별 필수 영어",
        "description": "공항, 호텔, 식당, 쇼핑과 교통 이용에 필요한 여행 영어회화 안내. 해외여행에서 바로 말할 수 있는 상황별 필수 표현을 익혀보세요.",
        "eyebrow": "English For Travel",
        "lead": "해외여행에서는 완벽한 문장보다 상황에 맞는 한마디를 바로 꺼내는 힘이 중요합니다. 출국부터 귀국까지 자주 만나는 장면을 순서대로 연습하세요.",
        "stamp": "공항부터<br>여행지까지<br>상황별 회화",
        "section_title": "낯선 여행지에서도<br>먼저 말할 수 있도록",
        "section_intro": "여행 동선을 따라 듣고 답할 표현을 함께 익히면 예상하지 못한 상황에서도 더 침착하게 소통할 수 있습니다.",
        "features": [
            ("01 · AIRPORT", "공항과 교통", "체크인, 입국 심사, 길 찾기, 택시와 대중교통 이용 표현을 익힙니다."),
            ("02 · STAY", "호텔과 식당", "예약 확인, 요청과 문제 해결, 주문과 계산에 필요한 문장을 연습합니다."),
            ("03 · EXPERIENCE", "쇼핑과 현지 대화", "가격과 사이즈를 묻고 추천을 요청하며 간단한 스몰토크를 이어갑니다."),
        ],
        "note_title": "여행 전에 이렇게 준비하세요",
        "note": "여행 일정에 포함된 공항, 숙소, 식당, 교통 상황을 먼저 정리하고 질문과 대답을 한 세트로 소리 내어 연습하세요. 표현을 통째로 익히면 현장에서 더 빠르게 반응할 수 있습니다.",
        "faqs": [
            ("여행 영어는 얼마나 미리 준비해야 하나요?", "출발 전 짧은 기간이라도 매일 상황별 핵심 문장을 듣고 말하면 도움이 됩니다. 실제 일정에 필요한 장면부터 우선하세요."),
            ("문장을 잊어버리면 어떻게 하나요?", "핵심 단어와 Could you, I'd like 같은 기본 문장 틀을 익히면 단어를 바꿔 여러 상황에 활용할 수 있습니다."),
        ],
    },
    {
        "slug": "business-english-conversation",
        "title": "비즈니스 영어회화",
        "meta_title": "비즈니스 영어회화 | 회의·전화·프레젠테이션 영어",
        "description": "회의, 전화, 이메일, 협상과 프레젠테이션에 필요한 비즈니스 영어회화 안내. 직무와 실무 상황에 맞는 영어 표현을 연습하세요.",
        "eyebrow": "Business Communication",
        "lead": "비즈니스 영어는 어려운 단어보다 목적을 분명하고 정중하게 전달하는 능력이 중요합니다. 실제 직무에서 반복되는 상황을 중심으로 소통의 정확도를 높이세요.",
        "stamp": "회의<br>프레젠테이션<br>실무 영어",
        "section_title": "업무의 목적을<br>분명하게 전달하는 영어",
        "section_intro": "회의 참여, 의견 제시, 일정 조율과 발표 등 실제 업무 흐름에 맞춰 표현을 익히고 돌발 질문에도 대응하는 연습이 필요합니다.",
        "features": [
            ("01 · MEETING", "회의와 의견 제시", "동의와 반대, 확인 질문, 진행 상황 공유를 명확하고 정중하게 표현합니다."),
            ("02 · PRESENTATION", "발표와 질의응답", "핵심 메시지를 구조화하고 자료 설명과 예상 질문에 답하는 연습을 합니다."),
            ("03 · GLOBAL WORK", "해외 업무 소통", "전화, 온라인 미팅, 협상과 후속 커뮤니케이션에 필요한 표현을 익힙니다."),
        ],
        "note_title": "직무에 맞춘 실전 연습",
        "note": "영업, 개발, 연구, 고객 응대 등 직무마다 필요한 어휘와 대화 흐름이 다릅니다. 자주 참여하는 회의와 발표 자료를 기준으로 우선순위를 정하면 학습 내용을 업무에 빠르게 연결할 수 있습니다.",
        "faqs": [
            ("비즈니스 영어는 어느 정도 기초가 필요하나요?", "기초 문장 구성력이 있으면 수월하지만, 현재 업무에 꼭 필요한 정형 표현부터 익히며 기초 회화를 함께 보완할 수도 있습니다."),
            ("이메일 영어도 함께 도움이 되나요?", "회의와 전화에서 쓰는 정중한 요청, 확인, 일정 조율 표현은 이메일에도 공통으로 활용할 수 있습니다."),
        ],
    },
]


def render_page(topic):
    features = "".join(
        f'<article class="feature"><b>{escape(number)}</b><h3>{escape(title)}</h3><p>{escape(body)}</p></article>'
        for number, title, body in topic["features"]
    )
    faq_items = "".join(
        f'<details><summary>{escape(question)}</summary><p>{escape(answer)}</p></details>'
        for question, answer in topic["faqs"]
    )
    schema = json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": question,
                    "acceptedAnswer": {"@type": "Answer", "text": answer},
                }
                for question, answer in topic["faqs"]
            ],
        },
        ensure_ascii=False,
    )
    return f'''<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{escape(topic["description"])}">
  <title>{escape(topic["meta_title"])} | 파워잉글리쉬</title>
  <link rel="canonical" href="https://talkenglish.kr/{topic["slug"]}.html">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@500;600;700&family=Gowun+Batang:wght@700&family=Noto+Sans+KR:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="guide.css">
  <script type="application/ld+json">{schema}</script>
</head>
<body>
  <a class="skip-link" href="#main">본문 바로가기</a>
  <header class="site-header">
    <a class="brand" href="index.html" aria-label="파워잉글리쉬 홈"><span class="brand-mark" aria-hidden="true"><i></i><i></i><i></i><i></i></span>파워잉글리쉬</a>
    <nav class="nav-links" id="site-menu" aria-label="주요 메뉴"><a href="index.html#about">교육 철학</a><a href="index.html#program">프로그램</a><a href="conversation-guide.html" aria-current="page">회화 안내</a><a class="nav-cta" href="tel:01029283614">상담 신청</a></nav>
    <button class="menu-button" type="button" aria-label="메뉴 열기" aria-expanded="false" aria-controls="site-menu"><span></span></button>
  </header>
  <main id="main">
    <nav class="breadcrumb" aria-label="현재 위치"><a href="index.html">홈</a><span>›</span><a href="conversation-guide.html">회화 안내</a><span>›</span>{escape(topic["title"])}</nav>
    <section class="guide-hero">
      <div class="guide-hero-copy"><p class="eyebrow">{escape(topic["eyebrow"])}</p><h1>{escape(topic["title"])}</h1><p>{escape(topic["lead"])}</p></div>
      <div class="guide-hero-media"><img src="https://images.unsplash.com/photo-1529156069898-49953e39b3ac?auto=format&fit=crop&w=1400&q=88" alt="{escape(topic["title"])}를 연습하는 성인 학습자들"><span class="location-stamp">{topic["stamp"]}</span></div>
    </section>
    <section class="details">
      <p class="eyebrow">Practical Speaking</p><h2>{topic["section_title"]}</h2>
      <p class="topic-intro">{escape(topic["section_intro"])}</p>
      <div class="feature-grid">{features}</div>
      <div class="area-note"><strong>{escape(topic["note_title"])}</strong>{escape(topic["note"])}</div>
    </section>
    <section class="faq"><div class="faq-inner"><p class="eyebrow">Frequently Asked Questions</p><h2>{escape(topic["title"])} FAQ</h2>{faq_items}</div></section>
    <section class="goal-links"><div class="goal-links-inner"><p class="eyebrow">More Learning Goals</p><h2>다른 목적의 영어회화도 살펴보세요</h2><div class="goal-link-grid"><a href="beginner-adult-english-conversation.html">왕초보 영어회화</a><a href="office-worker-english-conversation.html">직장인 영어회화</a><a href="travel-english-conversation.html">여행 영어회화</a><a href="business-english-conversation.html">비즈니스 영어</a></div></div></section>
    <section class="other-areas"><div class="other-areas-inner"><h2>지역별 성인 영어회화</h2><div class="area-links"><a href="conversation-guide.html">지역별 회화 안내</a><a href="regional-conversation-guide.html">전국 시·군·구 보기</a></div></div></section>
    <section class="contact"><div><p class="eyebrow">Start Here</p><h2>목표에 맞는 영어 말하기,<br>지금 시작하세요</h2><p>현재 수준과 영어가 필요한 상황을 알려주시면 알맞은 학습 방향을 안내해 드립니다.</p></div><a class="phone-button" href="tel:01029283614">전화 상담<br>010-2928-3614</a></section>
  </main>
  <footer class="site-footer"><div><a class="footer-brand" href="index.html">파워잉글리쉬</a><p class="footer-meta">교육문의 010-2928-3614<br>© 2026 파워잉글리쉬. All rights reserved.</p></div><div class="footer-links"><a href="index.html">홈</a><a href="conversation-guide.html">회화 안내</a></div></footer>
  <script src="guide.js"></script>
</body>
</html>
'''


for topic in TOPICS:
    (ROOT / f'{topic["slug"]}.html').write_text(render_page(topic), encoding="utf-8")

print(f"Generated {len(TOPICS)} topic pages")
