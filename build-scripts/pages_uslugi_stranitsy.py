#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Развёрнутые страницы услуг (19.08.2026) — пилот на 2 из 7 услуг: «Резидентура» и
«Инвесторский путь». По запросу заказчика («нужно сделать развёрнутые страницы под все
услуги, на странице с услугами оставить анонсы») — карточки на «Услугах» (`pages_home_uslugi.py`,
USLUGI_PAGE) для этих двух услуг превращены в короткие анонсы со ссылкой «Подробнее →», а
полный текст переехал сюда. Остальные 5 услуг пока не тронуты (полный абзац на «Услугах»,
как раньше) — решение сделать пилот на 2 страницах, а не сразу все 7, см. design-документ
`design/plan-razvernutye-stranitsy-uslug.md`.

Старт RU-only, по образцу уже обкатанного паттерна хаба «Парагвай для переезда»: сначала один
язык, перевод на ES/EN/DE — отдельным шагом после того, как подход утверждён на пилоте. Слаги
на ES/EN/DE сознательно не заведены в build.py (см. комментарий там) — до перевода это были бы
битые ссылки, href_to()/header() уже умеют пропускать язык, если слага нет.

Факты — только уже опубликованные на сайте (карточки «Услуг», хаб «Парагвай для переезда»,
раздел «Документы»), никакого нового исследования фактуры не потребовалось — только более
подробное изложение и перелинковка того, что уже проверено и размещено. Единственный новый
элемент — график сравнения таймлайна «Стандартный путь vs Инвесторский путь» на странице
«Инвесторский путь»: оба диапазона (2–5 лет / 4–7 мес.) уже были текстом на «Услугах» и в хабе,
здесь просто визуализированы тем же bar_chart, что и слайдер «Парагвай в цифрах» — численные
значения используются только для пропорции столбцов, отображаемые подписи — честные диапазоны,
не выдуманная точная цифра (тот же приём, что у dashed_idx/приблизительных подписей в
chart_data.py)."""
from build import page, breadcrumbs, schema_breadcrumb, href_to, NAV_LABELS, ICONS
from chart_data import build_topics, render_topic
from charts import bar_chart


def L(lang):
    l = {pid: href_to(pid, lang) for pid in [
        "home", "uslugi", "protsess", "riski", "stoimost", "terminologiya", "kontakty", "keisy",
        "pochemu-paragvay", "dok-temporal", "dok-permanente", "dok-investor", "dok-grazhdanstvo",
        "usluga-residencia", "usluga-investor", "usluga-relocation", "usluga-medicina",
        "meditsina-v-paragvae", "mify-voprosy",
        "usluga-compliance", "usluga-citizenship", "usluga-realestate", "usluga-company", "usluga-business",
        "nalogi-inostrantsev",
    ]}
    # «Резидентура»/«Инвесторский путь» остаются RU-only (пилот развёрнутых страниц ещё не
    # переведён) — на ES/EN/DE-версии «Релокации организаций» (21.08.2026) ссылки на них ведут
    # не в никуда, а на карточку соответствующей услуги на уже переведённой странице «Услуги»,
    # тот же fallback-приём "usluga-x or uslugi+'#x'", что уже используется в pages_home_uslugi.py.
    if l["usluga-residencia"] is None:
        l["usluga-residencia"] = l["uslugi"] + "#residencia"
    if l["usluga-investor"] is None:
        l["usluga-investor"] = l["uslugi"] + "#investor"
    return l


USLUGA_LABEL = {
    "usluga-residencia": {"ru": "Резидентура (ВНЖ)"},
    "usluga-investor": {"ru": "Инвесторский путь"},
    "usluga-relocation": {"ru": "Релокация организаций", "es": "Relocalización de empresas",
                           "en": "Business Relocation", "de": "Unternehmensrelokation"},
    "usluga-medicina": {"ru": "Медицинское сопровождение", "es": "Asistencia médica",
                         "en": "Medical Support", "de": "Medizinische Begleitung"},
    "usluga-compliance": {"ru": "Сопровождение и комплаенс", "es": "Acompañamiento y cumplimiento",
                           "en": "Ongoing Compliance", "de": "Begleitung und Compliance"},
    "usluga-citizenship": {"ru": "Гражданство Парагвая", "es": "Ciudadanía paraguaya",
                            "en": "Paraguayan Citizenship", "de": "Paraguayische Staatsbürgerschaft"},
    "usluga-realestate": {"ru": "Проверка и покупка недвижимости", "es": "Verificación y compra de inmuebles",
                           "en": "Real Estate Verification & Purchase", "de": "Prüfung und Kauf von Immobilien"},
    "usluga-company": {"ru": "Открытие компании (EAS/SRL)", "es": "Apertura de empresa (EAS/SRL)",
                        "en": "Company Formation (EAS/SRL)", "de": "Unternehmensgründung (EAS/SRL)"},
    "usluga-business": {"ru": "Покупка и продажа бизнеса", "es": "Compra y venta de empresas",
                         "en": "Buying & Selling a Business", "de": "Kauf und Verkauf von Unternehmen"},
}


def crumbs(lang, page_id):
    """Хлебные крошки: Главная › Услуги › [текущая страница]."""
    l = L(lang)
    return breadcrumbs([
        (NAV_LABELS[lang]["home"], l["home"]),
        (NAV_LABELS[lang]["uslugi"], l["uslugi"]),
        (USLUGA_LABEL[page_id][lang], None),
    ])


def schema_crumbs(lang, page_id):
    l = L(lang)
    return schema_breadcrumb([
        (NAV_LABELS[lang]["home"], f"/{lang}/"),
        (NAV_LABELS[lang]["uslugi"], f"/{lang}/{l['uslugi']}"),
        (USLUGA_LABEL[page_id][lang], f"/{lang}/{l[page_id]}"),
    ])


def _dnm_chart():
    """Переиспользуем уже готовую тему 'dnm' слайдера «Парагвай в цифрах» — те же данные,
    без нового исследования (см. chart_data.py: DNM_VALS, источники в fakty-dlya-kontenta.md)."""
    topic = next(t for t in build_topics("ru") if t["key"] == "dnm")
    return render_topic(topic), topic["caption"]


def _investor_timeline_chart():
    """Новый график — единственный новый визуальный элемент этого пилота. Значения (месяцы)
    служат только для пропорции столбцов — медианы уже опубликованных диапазонов (2–5 лет
    стандартный путь; 5 раб. дней на CIE + 3–6 мес. на саму Permanente — итого «около 4–7
    мес.» для инвесторского). Названия маршрутов — подписи над столбцами (не подписи категорий
    снизу): у столбцов разная высота, поэтому подписи расходятся по вертикали и не накладываются
    друг на друга, в отличие от подписи категорий, которая всегда идёт на одной строке снизу и
    для двух длинных названий подряд не помещается."""
    cats = ["2–5 лет", "4–7 мес."]
    values = [42, 5.5]
    disps = ["Стандартный путь", "Инвесторский путь"]
    svg = bar_chart(cats, values, disps, y_fmt=lambda v: f'{v:.0f} мес.')
    summary = ("Столбчатая диаграмма сравнения времени до постоянной резиденции: "
               "стандартный путь — 2–5 лет, инвесторский путь (SUACE) — около 4–7 месяцев.")
    return svg.replace('aria-label=""', f'aria-label="{summary}"', 1)


def _compliance_cycle_svg(lang):
    """Условная схема цикла (НЕ график с данными — см. design/plan-razvernutye-stranitsy-uslug.md,
    идея для услуги №3): RUC → ежемесячная отчётность → контроль статуса дела. Три подписанных
    блока и стрелки между ними; цикличность объясняется подписью под схемой, а не отдельной
    стрелкой возврата — так рисунок остаётся простым и однозначно читаемым."""
    LABELS = {
        "ru": ["RUC", "Ежемесячная отчётность", "Контроль статуса дела"],
        "es": ["RUC", "Declaraciones mensuales", "Seguimiento del trámite"],
        "en": ["RUC", "Monthly filings", "Case status tracking"],
        "de": ["RUC", "Monatliche Meldungen", "Statuskontrolle"],
    }
    ARIA = {
        "ru": "Условная схема из трёх шагов: регистрация RUC, затем ежемесячная отчётность, затем контроль статуса дела.",
        "es": "Esquema ilustrativo de tres pasos: inscripción del RUC, luego declaraciones mensuales, luego seguimiento del estado del trámite.",
        "en": "Illustrative three-step diagram: RUC registration, then monthly filings, then case status tracking.",
        "de": "Schematische Darstellung in drei Schritten: RUC-Registrierung, dann monatliche Meldungen, dann Statuskontrolle des Verfahrens.",
    }
    labels = LABELS[lang]
    W, H = 620, 150
    box_w, box_h = 168, 60
    gap = 30
    total = box_w * 3 + gap * 2
    x0 = (W - total) / 2
    y = 30
    svg = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{ARIA[lang]}">',
           '<defs><marker id="cc-arrow" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">'
           '<path d="M0,0 L8,4 L0,8 z" fill="var(--ink-dim-on-dark)"/></marker></defs>']
    for i, label in enumerate(labels):
        bx = x0 + i * (box_w + gap)
        svg.append(f'<rect x="{bx:.1f}" y="{y:.1f}" width="{box_w}" height="{box_h}" rx="10" '
                   f'fill="none" stroke="var(--red-on-dark)" stroke-width="2"/>')
        svg.append(f'<text x="{bx+box_w/2:.1f}" y="{y+box_h/2+5:.1f}" text-anchor="middle" '
                   f'font-size="13" font-weight="600">{label}</text>')
        if i < 2:
            ax1, ax2 = bx + box_w + 4, bx + box_w + gap - 6
            ay = y + box_h / 2
            svg.append(f'<line x1="{ax1:.1f}" y1="{ay:.1f}" x2="{ax2:.1f}" y2="{ay:.1f}" '
                       f'stroke="var(--ink-dim-on-dark)" stroke-width="2" marker-end="url(#cc-arrow)"/>')
    svg.append('</svg>')
    return "".join(svg)


def _citizenship_timeline_svg(lang):
    """Таймлайн-полоса (design/plan-razvernutye-stranitsy-uslug.md, идея для услуги №4): три
    сегмента разной ширины. Ширины сегментов — 2 / 3.5 / 3 (медиана уже опубликованного диапазона
    2–5 лет для Permanente; тот же приём, что и у _investor_timeline_chart — числа только для
    пропорции, отображаемые подписи — честные диапазоны из уже опубликованного текста, не новая
    точная цифра)."""
    SEGMENTS = {
        "ru": [("Residencia Temporal", "до 2 лет"), ("Residencia Permanente", "обычно 2–5 лет"),
               ("Ожидание перед натурализацией", "3 года, ст. 148")],
        "es": [("Residencia Temporal", "hasta 2 años"), ("Residencia Permanente", "normalmente 2–5 años"),
               ("Espera antes de la naturalización", "3 años, art. 148")],
        "en": [("Residencia Temporal", "up to 2 years"), ("Residencia Permanente", "usually 2–5 years"),
               ("Wait before naturalization", "3 years, Art. 148")],
        "de": [("Residencia Temporal", "bis zu 2 Jahre"), ("Residencia Permanente", "meist 2–5 Jahre"),
               ("Wartezeit vor der Einbürgerung", "3 Jahre, Art. 148")],
    }
    ARIA = {
        "ru": "Таймлайн: Residencia Temporal до 2 лет, затем Residencia Permanente обычно 2–5 лет, затем ожидание 3 года перед натурализацией.",
        "es": "Cronología: Residencia Temporal hasta 2 años, luego Residencia Permanente normalmente 2–5 años, luego 3 años de espera antes de la naturalización.",
        "en": "Timeline: Residencia Temporal up to 2 years, then Residencia Permanente usually 2–5 years, then a 3-year wait before naturalization.",
        "de": "Zeitachse: Residencia Temporal bis zu 2 Jahre, dann Residencia Permanente meist 2–5 Jahre, dann 3 Jahre Wartezeit vor der Einbürgerung.",
    }
    segs = SEGMENTS[lang]
    fracs = [2, 3.5, 3]
    total_frac = sum(fracs)
    W, H = 620, 170
    pad_l, pad_r = 20, 20
    bar_w = W - pad_l - pad_r
    bar_y, bar_h = 70, 40
    svg = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{ARIA[lang]}">']
    x = pad_l
    colors = ["var(--red-on-dark)", "var(--ink-dim-on-dark)", "var(--red-on-dark)"]
    opacities = [1, 0.55, 1]
    for i, ((name, dur), frac) in enumerate(zip(segs, fracs)):
        w = frac / total_frac * bar_w
        svg.append(f'<rect x="{x:.1f}" y="{bar_y}" width="{w:.1f}" height="{bar_h}" '
                   f'fill="{colors[i]}" opacity="{opacities[i]}"/>')
        cx = x + w / 2
        svg.append(f'<text x="{cx:.1f}" y="{bar_y-12}" text-anchor="middle" font-size="12" font-weight="600">{name}</text>')
        svg.append(f'<text x="{cx:.1f}" y="{bar_y+bar_h+20}" text-anchor="middle" class="dim" font-size="12">{dur}</text>')
        if i > 0:
            svg.append(f'<line x1="{x:.1f}" y1="{bar_y-4}" x2="{x:.1f}" y2="{bar_y+bar_h+4}" stroke="var(--surface-dark)" stroke-width="2"/>')
        x += w
    svg.append('</svg>')
    return "".join(svg)


def _company_timing_svg(lang):
    """bar_chart сравнения сроков регистрации (design/plan-razvernutye-stranitsy-uslug.md, идея
    для услуги №6): EAS / S.A. / S.R.L. Значения — рабочие дни, служат только для пропорции
    столбцов (EAS ≈72 рабочих часа ≈ 2 рабочих дня; S.A. и S.R.L. — медианы уже опубликованных
    диапазонов 8–30 и 15–30 дней); отображаемые подписи — честные диапазоны, не точная цифра."""
    cats = {"ru": ["EAS", "S.A.", "S.R.L."], "es": ["EAS", "S.A.", "S.R.L."],
            "en": ["EAS", "S.A.", "S.R.L."], "de": ["EAS", "S.A.", "S.R.L."]}[lang]
    disps = {
        "ru": ["≈72 раб. часа", "8–30 дней", "15–30 дней"],
        "es": ["≈72 h hábiles", "8–30 días", "15–30 días"],
        "en": ["≈72 business hrs", "8–30 days", "15–30 days"],
        "de": ["≈72 Werkstd.", "8–30 Tage", "15–30 Tage"],
    }[lang]
    y_unit = {"ru": "дн.", "es": "días", "en": "days", "de": "Tage"}[lang]
    values = [2, 19, 22.5]
    svg = bar_chart(cats, values, disps, y_fmt=lambda v: f'{v:.0f} {y_unit}')
    ARIA = {
        "ru": "Столбчатая диаграмма сроков регистрации: EAS — около 72 рабочих часов, S.A. — 8–30 дней, S.R.L. — 15–30 дней.",
        "es": "Gráfico de barras de los plazos de registro: EAS — unas 72 horas hábiles, S.A. — 8–30 días, S.R.L. — 15–30 días.",
        "en": "Bar chart of registration timelines: EAS — about 72 business hours, S.A. — 8–30 days, S.R.L. — 15–30 days.",
        "de": "Balkendiagramm der Registrierungsfristen: EAS — etwa 72 Werkstunden, S.A. — 8–30 Tage, S.R.L. — 15–30 Tage.",
    }[lang]
    return svg.replace('aria-label=""', f'aria-label="{ARIA}"', 1)


# Рендерим все графики один раз (не зависят от l, только от lang) — избегаем повторного рендера
# внутри f-string ниже.
_DNM_SVG, _DNM_CAPTION = _dnm_chart()
_INVESTOR_SVG = _investor_timeline_chart()
_COMPLIANCE_SVG = {lang: _compliance_cycle_svg(lang) for lang in ["ru", "es", "en", "de"]}
_CITIZENSHIP_SVG = {lang: _citizenship_timeline_svg(lang) for lang in ["ru", "es", "en", "de"]}
_COMPANY_SVG = {lang: _company_timing_svg(lang) for lang in ["ru", "es", "en", "de"]}


PAGES = {
"usluga-residencia": {
"ru": dict(
    title="Резидентура в Парагвае: Temporal → Permanente | Grund Paraguay",
    description="Как получить временную и постоянную резиденцию в Парагвае: документы по ст. 50 Ley 6984/22, 12 категорий DNM № 407/2026, статистика выданных резиденций и что нужно после получения статуса.",
    h1="Резидентура в Парагвае: от Temporal до Permanente",
    lead='Резидентура — вид на жительство в Парагвае, дающий право законно жить и работать в стране. Это не разовая услуга, а первый этап более длительного процесса: сначала временная (<a href="{terminologiya}#residencia-temporal">Residencia Temporal</a>, до 2 лет с продлением на такой же срок), затем — обычно через 2–5 лет — постоянная (<a href="{terminologiya}#residencia-permanente">Residencia Permanente</a>, на 10 лет с продлением). Мы проверяем комплект документов до подачи, а не после отказа.',
    body=lambda l: f'''
    <p>Сама по себе резидентура не решает вопрос легальной жизни в стране — это входной пакет,
    за которым следует обязательное сопровождение и комплаенс (см. раздел ниже). Рынок оформления
    временной и постоянной резиденции в Парагвае уже заполнен посредниками, и конкурировать на
    нём одной ценой бессмысленно — настоящая работа начинается после получения статуса.</p>

    <h2>Что нужно подготовить</h2>
    <p>Комплект документов — по ст. 50 Ley N° 6984/22 «De Migraciones» — мы проверяем ещё до подачи:
    загранпаспорт, консульская виза, свидетельство о рождении, справка о семейном положении,
    международная справка о несудимости и ряд других документов по конкретной категории заявителя.</p>
    <p>Полный чек-лист — с требованиями к апостилю и переводу — на страницах
    <a href="{l['dok-temporal']}">«Временная резидентура: документы»</a> и
    <a href="{l['dok-permanente']}">«Постоянная резидентура: документы»</a> в разделе «Документы».</p>

    <h2>12 категорий заявителей — резолюция DNM № 407/2026</h2>
    <p>С 6 июля 2026 года действует новая резолюция миграционной службы
    (<a href="{l['terminologiya']}#dnm">DNM</a>) № 407/2026 — 12 категорий заявителей, у каждой
    свои требования. Точные денежные пороги по категориям на момент публикации официально не
    раскрыты, поэтому стоимость и условия по вашей категории мы уточняем индивидуально.</p>

    <h2>Сколько резиденций выдаётся</h2>
    <div class="diagram">
      {_DNM_SVG}
      <p class="diagram-caption">{_DNM_CAPTION}</p>
    </div>
    <p>Рост числа выданных резиденций — не повод расслабиться по срокам: та же логика роста
    притока обычно предшествует ужесточению условий (подробнее — на странице
    <a href="{l['pochemu-paragvay']}">«Почему Парагвай»</a>, на примере Аргентины, которая уже
    прошла этот цикл).</p>

    <h2>После Temporal: обязательный комплаенс</h2>
    <p>После получения Residencia Temporal возникает обязанность зарегистрировать
    <a href="{l['terminologiya']}#ruc">RUC</a> (привязан к
    <a href="{l['terminologiya']}#cedula">Cédula</a>) и регулярно подавать налоговую отчётность,
    включая нулевую, если деятельности не было — это отдельная услуга (см. карточку
    «Сопровождение и комплаенс» на странице <a href="{l['uslugi']}">«Услуги»</a>), без которой
    перевод в постоянную резиденцию рискует растянуться или сорваться.</p>

    <h2>Что дальше — гражданство</h2>
    <p>Натурализация возможна не раньше чем через 3 года после получения Residencia Permanente
    (ст. 148 Конституции Парагвая) — реалистичный полный срок от переезда до паспорта обычно
    складывается в 7–8 лет. Дело ведёт Верховный суд
    (<a href="{l['terminologiya']}#corte-suprema">Corte Suprema de Justicia</a>), не миграционная
    служба; полный список документов — на странице
    <a href="{l['dok-grazhdanstvo']}">«Гражданство: документы»</a>.</p>

    <h2>Смотрите также</h2>
    <ul>
      <li><a href="{l['protsess']}">«Процесс и сроки»</a> — полный таймлайн от заявки до паспорта</li>
      <li><a href="{l['riski']}">«Честно о рисках»</a> — как меняются условия входа со временем</li>
      <li><a href="{l['keisy']}">«Кейсы и отзывы»</a> — типичные истории клиентов</li>
      <li><a href="{l['usluga-investor']}">«Инвесторский путь»</a> — более быстрый маршрут к
      постоянной резиденции при инвестициях от 70 000 USD</li>
    </ul>
    ''',
    final_h2="Готовы обсудить свою ситуацию?",
    final_p="Проверим комплект документов и честно оценим сроки конкретно по вашей категории.",
    final_cta="Оставить заявку на консультацию",
),
},
"usluga-investor": {
"ru": dict(
    title="Инвесторский путь в Парагвае: SUACE / Investor Pass | Grund Paraguay",
    description="Прямой доступ к постоянной резиденции в Парагвае через инвестиции от 70 000 USD: сертификат инвестора (CIE) за 5 рабочих дней, резолюция MIC № 0283/2026, сравнение сроков со стандартным путём.",
    h1="Инвесторский путь: SUACE / Investor Pass",
    lead='Инвесторский путь — способ получить постоянную резиденцию напрямую, минуя временную: для инвестиций от 70 000 USD (производственная ветка, при бизнес-плане и создании 5 официальных рабочих мест) до 200 000 USD (недвижимость или финансовые инструменты) возможен прямой доступ к <a href="{terminologiya}#residencia-permanente">Residencia Permanente</a> без прохождения <a href="{terminologiya}#residencia-temporal">Residencia Temporal</a>.',
    body=lambda l: f'''
    <p>Режим действует по резолюции Министерства промышленности и торговли
    (<a href="{l['terminologiya']}#mic">MIC</a>) N° 0283/2026 (с 21 апреля 2026 года) и
    администрируется через <a href="{l['terminologiya']}#suace">SUACE</a>. Это отдельный путь для
    более состоятельного сегмента — мы не смешиваем его с массовой резидентурой.</p>

    <h2>Как это работает</h2>
    <p>Сертификат инвестора (<a href="{l['terminologiya']}#cie">CIE</a>) оформляется официально за
    5 рабочих дней после подачи полного пакета документов. Сама постоянная резиденция, по оценке
    отраслевых изданий, занимает ещё около 3–6 месяцев сверху — итого примерно 4–7 месяцев от
    подачи до Residencia Permanente.</p>

    <h2>Стандартный путь vs инвесторский</h2>
    <div class="diagram">
      {_INVESTOR_SVG}
      <p class="diagram-caption">Стандартный путь (Temporal → Permanente) обычно занимает от 2 до
      5 лет — против примерно 4–7 месяцев на инвесторском пути. Обе оценки — уже опубликованные на
      сайте диапазоны, не новая цифра.</p>
    </div>

    <h2>Для кого этот путь</h2>
    <p>Порог входа заметно ниже, чем у ближайшего быстрого аналога в регионе: отдельная налоговая
    резидентура для инвесторов в Уругвае требует вложений от ≈377 000 USD — на порядок больше
    входного порога инвесторского пути Парагвая (от 70 000 USD). Подробнее о том, как это
    сравнение выглядит на фоне соседних стран — на странице
    <a href="{l['pochemu-paragvay']}">«Почему Парагвай»</a>.</p>

    <h2>Документы</h2>
    <p>Официальный перечень документов на сертификат инвестора — на странице
    <a href="{l['dok-investor']}">«Инвесторский путь: документы»</a> в разделе «Документы».</p>

    <h2>Смотрите также</h2>
    <ul>
      <li><a href="{l['usluga-residencia']}">«Резидентура (ВНЖ)»</a> — стандартный путь через
      Temporal → Permanente</li>
      <li><a href="{l['stoimost']}">«Стоимость и тарифы»</a> — полная стоимость услуг</li>
      <li><a href="{l['keisy']}">«Кейсы и отзывы»</a> — пример клиента, выбравшего этот путь</li>
    </ul>
    ''',
    final_h2="Рассматриваете инвесторский путь?",
    final_p="Оценим, подходит ли ваш случай под производственную или инвестиционную ветку, и что нужно для подачи.",
    final_cta="Оставить заявку на консультацию",
),
},
"usluga-relocation": {
"ru": dict(
    title="Релокация организаций в Парагвай: компания, Maquila, резидентура команды | Grund Paraguay",
    description="Комплекс услуг по переезду бизнеса в Парагвай: регистрация компании, льготный налоговый режим Maquila (1%) для экспортёров услуг, резидентура для команды, корпоративный счёт и комплаенс.",
    h1="Релокация организаций в Парагвай",
    lead='Релокация организации — не одна процедура, а пакет из нескольких уже отработанных услуг, собранных под задачу компании, а не физлица: регистрация юрлица, при необходимости — льготный налоговый режим <a href="{terminologiya}#maquila">Maquila</a>, резидентура для переезжающих сотрудников и открытие корпоративного счёта. Отдельной государственной процедуры «переезд компании» в Парагвае не существует — мы собираем её из механизмов, которые уже описаны на этом сайте по отдельности.',
    body=lambda l: f'''
    <p>Разница с обычным открытием компании — в масштабе и последовательности: вместо одного
    учредителя и одной резидентуры здесь, как правило, несколько сотрудников, которым нужен
    легальный статус одновременно с работающим юрлицом и счётом. Мы ведём это как один проект,
    а не как несколько независимых заказов.</p>

    <h2>Из чего состоит пакет</h2>
    <ul>
      <li><strong>Регистрация юрлица</strong> — <a href="{l['terminologiya']}#eas">EAS</a>,
      <a href="{l['terminologiya']}#sa">S.A.</a> или <a href="{l['terminologiya']}#srl">S.R.L.</a>,
      та же услуга «Открытие компании» (см. карточку на странице
      <a href="{l['uslugi']}">«Услуги»</a>).</li>
      <li><strong>Регистрация в режиме Maquila</strong> — если бизнес относится к производству
      или экспортируемым услугам (подробнее — ниже).</li>
      <li><strong>Резидентура для команды</strong> — пакет из нескольких дел по уже существующей
      услуге <a href="{l['usluga-residencia']}">«Резидентура»</a>, по одному на каждого
      переезжающего сотрудника.</li>
      <li><strong>Открытие корпоративного банковского счёта</strong> — с учётом требований,
      которые банки предъявляют именно к юрлицам (см. раздел ниже).</li>
      <li><strong>Сопровождение и комплаенс</strong> — та же логика, что и для физлиц, но на
      уровне компании: RUC юрлица и регулярная отчётность.</li>
    </ul>

    <h2>Режим Maquila — вероятно, главное преимущество для сервисных компаний</h2>
    <p>Официальный режим (Ley N° 1064/97), администрируется через
    <a href="{l['terminologiya']}#rediex">REDIEX</a> и MIC: единый налог 1% — либо от
    добавленной стоимости, созданной в Парагвае, либо от суммы счёта-фактуры, смотря что больше
    — вместо стандартных 10% IRE. Право на режим есть у любого юрлица, легально
    зарегистрированного в Парагвае и работающего по контракту с иностранной компанией; в числе
    льгот — приостановка пошлин на ввоз сырья и оборудования, освобождение от таможенных и
    портовых сборов, возврат НДС. Режим явно открыт не только для производства: по данным
    официального документа MIC, среди действующих операторов режима есть отдельная категория
    «Exportadores de Servicios» — то есть он подходит и для релокации IT- или аутсорс-компании,
    а не только завода.</p>
    <div class="callout"><span class="callout-label">Что не уточнено</span>Конкретная процедура
    и сроки получения статуса Maquila отдельно от самой регистрации компании — на момент
    публикации не исследованы; перед тем как называть точный срок и чек-лист, мы уточняем это
    индивидуально через REDIEX по вашему кейсу.</div>

    <h2>Компания как юрлицо</h2>
    <p>Сроки регистрации — те же, что и у обычного открытия компании: EAS через SUACE — до 72
    рабочих часов по типовому уставу, S.A. — 8–30 рабочих дней, S.R.L. — 15–30 рабочих дней. Для
    EAS законный представитель обязан иметь парагвайское гражданство или Cédula «без
    исключений» — при релокации, где ни один сотрудник ещё не имеет резидентства, эту роль на
    старте берёт на себя представитель по доверенности, пока кто-то из команды не получит
    Cédula.</p>

    <h2>Корпоративный банковский счёт</h2>
    <p>Компании нужна полностью оформленная корпоративная структура; физическое присутствие для
    открытия счёта обязательно — дистанционно это практически невозможно. EAS как относительно
    новая правовая форма иногда создаёт банкам дополнительные вопросы и требует более
    внимательного сопровождения при подаче.</p>
    <p class="confidence-note">Прямых подтверждений (или опровержений) того, что банки
    предъявляют дополнительные требования именно к капиталу или владельцам российского
    происхождения, в собранных источниках нет — это не значит, что таких сложностей
    гарантированно не будет, только что мы не нашли этому прямого подтверждения. Уточняем
    конкретно по вашему случаю до начала работы, а не постфактум.</p>

    <h2>Резидентура для сотрудников — без отдельной «корпоративной визы»</h2>
    <p>Специальной визы для релоцирующихся сотрудников или цифровых кочевников в Парагвае нет:
    весь поток идёт через тот же механизм, что уже описан на странице
    <a href="{l['usluga-residencia']}">«Резидентура»</a>, — <a href="{l['terminologiya']}#residencia-temporal">Residencia
    Temporal</a> по общему закону о миграции, где удалённая работа и контракт с иностранным
    (в данном случае — с релоцируемым) работодателем входят в пакет документов, подтверждающих
    источник дохода. Официального минимального порога дохода не установлено — миграционная
    служба оценивает платёжеспособность по выпискам и контрактам. Рассмотрение занимает
    60–90 дней. На практике это означает, что «релокация команды» — не одна процедура, а
    несколько параллельных дел по резидентуре, только с корпоративными документами (контракт,
    выписки компании) вместо части личных.</p>

    <h2>Стоимость</h2>
    <p>Пакет складывается из уже существующих услуг — открытия компании, резидентуры на каждого
    сотрудника и абонемента на комплаенс — плюс отдельный компонент по Maquila при
    необходимости. Итоговую стоимость и состав пакета мы считаем индивидуально: она зависит от
    выбранной организационно-правовой формы, числа переезжающих сотрудников и того, нужен ли
    режим Maquila. Полный прайс по отдельным компонентам — на странице
    <a href="{l['stoimost']}">«Стоимость и тарифы»</a>.</p>

    <h2>Смотрите также</h2>
    <ul>
      <li><a href="{l['usluga-residencia']}">«Резидентура (ВНЖ)»</a> — услуга, из которой
      собирается резидентура для каждого сотрудника команды</li>
      <li><a href="{l['uslugi']}">«Услуги»</a> — полный список, включая открытие компании и
      сопровождение бизнеса</li>
      <li><a href="{l['stoimost']}">«Стоимость и тарифы»</a> — стоимость отдельных компонентов
      пакета</li>
    </ul>
    ''',
    final_h2="Планируете релокацию компании в Парагвай?",
    final_p="Разберём состав пакета под вашу ситуацию — форму юрлица, число сотрудников и то, подходит ли вам режим Maquila.",
    final_cta="Оставить заявку на консультацию",
),
"es": dict(
    title="Relocalización de empresas a Paraguay: empresa, Maquila, residencia del equipo | Grund Paraguay",
    description="Paquete de servicios para trasladar un negocio a Paraguay: registro de la empresa, régimen fiscal preferencial Maquila (1%) para exportadores de servicios, residencia para el equipo, cuenta corporativa y cumplimiento.",
    h1="Relocalización de empresas a Paraguay",
    lead='La relocalización de una empresa no es un único trámite, sino un paquete de varios servicios ya probados, armado para la necesidad de una empresa y no de una persona física: la inscripción de la persona jurídica, si corresponde, el régimen fiscal preferencial <a href="{terminologiya}#maquila">Maquila</a>, la residencia para los empleados que se trasladan y la apertura de una cuenta corporativa. En Paraguay no existe un trámite estatal independiente de «traslado de empresa» — lo armamos combinando mecanismos que ya están descritos por separado en este sitio.',
    body=lambda l: f'''
    <p>La diferencia con la apertura de empresa habitual está en la escala y la secuencia: en lugar
    de un solo fundador y una sola residencia, aquí normalmente hay varios empleados que necesitan un
    estatus legal al mismo tiempo que una persona jurídica en funcionamiento y una cuenta. Llevamos
    esto como un solo proyecto, no como varios encargos independientes.</p>

    <h2>De qué se compone el paquete</h2>
    <ul>
      <li><strong>Inscripción de la persona jurídica</strong> — <a href="{l['terminologiya']}#eas">EAS</a>,
      <a href="{l['terminologiya']}#sa">S.A.</a> o <a href="{l['terminologiya']}#srl">S.R.L.</a>, el
      mismo servicio «Apertura de empresa» (ver la tarjeta en la página
      <a href="{l['uslugi']}">«Servicios»</a>).</li>
      <li><strong>Inscripción en el régimen Maquila</strong> — si el negocio corresponde a manufactura
      o a servicios exportables (más detalles más abajo).</li>
      <li><strong>Residencia para el equipo</strong> — un paquete de varios expedientes bajo el
      servicio ya existente <a href="{l['usluga-residencia']}">«Residencia»</a>, uno por cada
      empleado que se traslada.</li>
      <li><strong>Apertura de una cuenta bancaria corporativa</strong> — teniendo en cuenta los
      requisitos que los bancos exigen específicamente a las personas jurídicas (ver la sección más
      abajo).</li>
      <li><strong>Acompañamiento y cumplimiento</strong> — la misma lógica que para personas físicas,
      pero a nivel de empresa: RUC de la persona jurídica y declaraciones periódicas.</li>
    </ul>

    <h2>Régimen Maquila — probablemente la principal ventaja para empresas de servicios</h2>
    <p>Un régimen oficial (Ley N.° 1064/97), administrado a través de
    <a href="{l['terminologiya']}#rediex">REDIEX</a> y el MIC: un impuesto único del 1% — sobre el
    valor agregado generado en Paraguay o sobre el monto de la factura, lo que sea mayor — en lugar
    del 10% estándar de IRE. Tienen derecho al régimen cualquier persona jurídica legalmente
    registrada en Paraguay que trabaje bajo contrato con una empresa extranjera; entre los beneficios
    están la suspensión de aranceles a la importación de materia prima y equipos, la exención de
    tasas aduaneras y portuarias, y la devolución del IVA. El régimen está explícitamente abierto no
    solo a la manufactura: según el documento oficial del MIC, entre los operadores vigentes del
    régimen existe una categoría separada de «Exportadores de Servicios» — es decir, también es apto
    para la relocalización de una empresa de IT o de tercerización (outsourcing), no solo de una
    fábrica.</p>
    <div class="callout"><span class="callout-label">Qué no está aclarado</span>El procedimiento
    concreto y los plazos para obtener el estatus de Maquila, aparte del propio registro de la
    empresa, no se han investigado al momento de esta publicación; antes de indicar un plazo exacto y
    una lista de requisitos, lo confirmamos de forma individual a través de REDIEX según su caso.</div>

    <h2>La empresa como persona jurídica</h2>
    <p>Los plazos de inscripción son los mismos que para una apertura de empresa habitual: la EAS a
    través de SUACE — hasta 72 horas hábiles con estatuto tipo, la S.A. — de 8 a 30 días hábiles, la
    S.R.L. — de 15 a 30 días hábiles. Para la EAS, el representante legal debe tener obligatoriamente
    ciudadanía paraguaya o Cédula paraguaya «sin excepciones» — en una relocalización donde ningún
    empleado tiene todavía residencia, este papel lo asume al principio un apoderado, hasta que
    alguien del equipo obtenga la Cédula.</p>

    <h2>Cuenta bancaria corporativa</h2>
    <p>La empresa necesita una estructura corporativa completamente formalizada; la presencia física
    para abrir la cuenta es obligatoria — hacerlo a distancia es prácticamente imposible. La EAS, al
    ser una forma jurídica relativamente nueva, a veces genera preguntas adicionales en los bancos y
    requiere un acompañamiento más cuidadoso al momento de presentar la solicitud.</p>
    <p class="confidence-note">No hay confirmaciones directas (ni desmentidos) en las fuentes
    recopiladas de que los bancos exijan requisitos adicionales específicamente al capital o a los
    propietarios de origen ruso — esto no significa que tales dificultades estén garantizadas de no
    existir, solo que no encontramos una confirmación directa de ello. Lo confirmamos concretamente
    según su caso antes de comenzar el trabajo, no después de los hechos.</p>

    <h2>Residencia para los empleados — sin una «visa corporativa» aparte</h2>
    <p>No existe en Paraguay una visa especial para empleados que se relocalizan o para nómadas
    digitales: todo el flujo pasa por el mismo mecanismo ya descrito en la página
    <a href="{l['usluga-residencia']}">«Residencia»</a> — la
    <a href="{l['terminologiya']}#residencia-temporal">Residencia Temporal</a> según la ley general
    de migraciones, donde el trabajo remoto y el contrato con el empleador extranjero (en este caso,
    la empresa que se relocaliza) forman parte del paquete de documentos que acreditan la fuente de
    ingresos. No existe un umbral mínimo de ingresos oficialmente establecido — el servicio de
    migraciones evalúa la solvencia según los extractos y los contratos. La revisión toma de 60 a 90
    días. En la práctica, esto significa que la «relocalización del equipo» no es un único trámite,
    sino varios expedientes paralelos de residencia, solo que con documentos corporativos (contrato,
    extractos de la empresa) en lugar de parte de los documentos personales.</p>

    <h2>Costo</h2>
    <p>El paquete se compone de servicios ya existentes — apertura de empresa, residencia por cada
    empleado y la suscripción de cumplimiento — más un componente aparte por Maquila si corresponde.
    Calculamos el costo final y la composición del paquete de forma individual: depende de la forma
    jurídica elegida, del número de empleados que se trasladan y de si se necesita el régimen
    Maquila. El precio completo de cada componente por separado está en la página
    <a href="{l['stoimost']}">«Costos y tarifas»</a>.</p>

    <h2>Vea también</h2>
    <ul>
      <li><a href="{l['usluga-residencia']}">«Residencia»</a> — el servicio con el que se arma la
      residencia de cada integrante del equipo</li>
      <li><a href="{l['uslugi']}">«Servicios»</a> — la lista completa, incluida la apertura de
      empresa y el acompañamiento de negocios</li>
      <li><a href="{l['stoimost']}">«Costos y tarifas»</a> — el costo de los componentes
      individuales del paquete</li>
    </ul>
    ''',
    final_h2="¿Planea relocalizar su empresa a Paraguay?",
    final_p="Analizamos la composición del paquete según su situación — la forma jurídica, el número de empleados y si el régimen Maquila le conviene.",
    final_cta="Solicitar una consulta",
),
"en": dict(
    title="Relocating a business to Paraguay: company, Maquila, team residency | Grund Paraguay",
    description="A package of services for moving a business to Paraguay: company registration, the preferential Maquila tax regime (1%) for service exporters, residency for the team, a corporate account, and compliance.",
    h1="Relocating a business to Paraguay",
    lead='Relocating an organization isn\'t a single procedure — it\'s a package of several already-established services, put together for a company\'s needs rather than an individual\'s: registering the legal entity, the preferential <a href="{terminologiya}#maquila">Maquila</a> tax regime where it applies, residency for relocating employees, and opening a corporate bank account. There\'s no separate government procedure for "company relocation" in Paraguay — we assemble it from mechanisms already described separately on this site.',
    body=lambda l: f'''
    <p>The difference from ordinary company formation is one of scale and sequencing: instead of a
    single founder and a single residency case, there are usually several employees who need legal
    status at the same time as a functioning legal entity and account. We run this as one project,
    not as several independent orders.</p>

    <h2>What the package includes</h2>
    <ul>
      <li><strong>Registering the legal entity</strong> — <a href="{l['terminologiya']}#eas">EAS</a>,
      <a href="{l['terminologiya']}#sa">S.A.</a>, or <a href="{l['terminologiya']}#srl">S.R.L.</a>,
      the same "Company formation" service (see the card on the
      <a href="{l['uslugi']}">"Services"</a> page).</li>
      <li><strong>Registering under the Maquila regime</strong> — if the business is manufacturing or
      exportable services (more below).</li>
      <li><strong>Residency for the team</strong> — a package of several cases under the
      already-existing <a href="{l['usluga-residencia']}">"Residency"</a> service, one per relocating
      employee.</li>
      <li><strong>Opening a corporate bank account</strong> — accounting for the requirements banks
      specifically apply to legal entities (see the section below).</li>
      <li><strong>Ongoing compliance</strong> — the same logic as for individuals, but at the company
      level: the legal entity's RUC and regular filings.</li>
    </ul>

    <h2>The Maquila regime — likely the main advantage for service companies</h2>
    <p>An official regime (Ley N° 1064/97), administered through
    <a href="{l['terminologiya']}#rediex">REDIEX</a> and the MIC: a single 1% tax — on either the
    value added created in Paraguay or the invoice amount, whichever is greater — instead of the
    standard 10% IRE. Any legal entity legally registered in Paraguay and working under contract with
    a foreign company qualifies; benefits include suspension of duties on imported raw materials and
    equipment, exemption from customs and port fees, and VAT refunds. The regime is explicitly open
    to more than manufacturing: per an official MIC document, current operators under the regime
    include a separate "Exportadores de Servicios" (service exporters) category — meaning it also
    fits relocating an IT or outsourcing company, not just a factory.</p>
    <div class="callout"><span class="callout-label">What isn't confirmed</span>The specific
    procedure and timeline for obtaining Maquila status, separate from the company registration
    itself, hasn't been researched as of this writing; before quoting an exact timeline and
    checklist, we confirm this individually through REDIEX for your specific case.</div>

    <h2>The company as a legal entity</h2>
    <p>Registration timelines are the same as for ordinary company formation: EAS through SUACE — up
    to 72 business hours with a standard charter, S.A. — 8–30 business days, S.R.L. — 15–30 business
    days. For an EAS, the legal representative must hold Paraguayan citizenship or a Paraguayan
    Cédula "with no exceptions" — in a relocation where no employee yet has residency, a proxy
    representative takes on this role at the start, until someone on the team obtains a Cédula.</p>

    <h2>Corporate bank account</h2>
    <p>The company needs a fully formalized corporate structure; physical presence to open the
    account is mandatory — doing it remotely is practically impossible. As a relatively new legal
    form, an EAS sometimes raises additional questions for banks and requires more careful support
    when filing.</p>
    <p class="confidence-note">Nothing in the sources we gathered directly confirms — or rules out —
    banks applying additional requirements specifically to capital or owners of Russian origin. That
    doesn't mean such complications are guaranteed not to happen, only that we found no direct
    confirmation of them. We confirm this specifically for your case before starting work, not after
    the fact.</p>

    <h2>Residency for employees — no separate "corporate visa"</h2>
    <p>There's no special visa in Paraguay for relocating employees or digital nomads: the whole flow
    runs through the same mechanism already described on the
    <a href="{l['usluga-residencia']}">"Residency"</a> page —
    <a href="{l['terminologiya']}#residencia-temporal">Residencia Temporal</a> under the general
    migration law, where remote work and a contract with the foreign (in this case, relocating)
    employer are part of the document package proving income source. There's no officially set
    minimum income threshold — the migration service assesses solvency from bank statements and
    contracts. Review takes 60–90 days. In practice, this means "relocating the team" isn't one
    procedure but several parallel residency cases, just with corporate documents (contract, company
    statements) instead of some of the personal ones.</p>

    <h2>Cost</h2>
    <p>The package is built from already-existing services — company formation, residency for each
    employee, and the compliance subscription — plus a separate Maquila component where needed. We
    calculate the final cost and package composition individually: it depends on the legal form
    chosen, the number of relocating employees, and whether the Maquila regime is needed. Full
    pricing for the individual components is on the <a href="{l['stoimost']}">"Pricing"</a> page.</p>

    <h2>See also</h2>
    <ul>
      <li><a href="{l['usluga-residencia']}">"Residency"</a> — the service each team member's
      residency case is built from</li>
      <li><a href="{l['uslugi']}">"Services"</a> — the full list, including company formation and
      business support</li>
      <li><a href="{l['stoimost']}">"Pricing"</a> — the cost of the package's individual
      components</li>
    </ul>
    ''',
    final_h2="Planning to relocate a company to Paraguay?",
    final_p="We'll work out the package for your situation — legal form, number of employees, and whether the Maquila regime fits.",
    final_cta="Request a consultation",
),
"de": dict(
    title="Unternehmensrelokation nach Paraguay: Firma, Maquila, Aufenthaltstitel fürs Team | Grund Paraguay",
    description="Leistungspaket für den Umzug eines Unternehmens nach Paraguay: Firmengründung, steuerliches Vorzugsregime Maquila (1%) für Dienstleistungsexporteure, Aufenthaltstitel fürs Team, Firmenkonto und Compliance.",
    h1="Unternehmensrelokation nach Paraguay",
    lead='Die Relokation eines Unternehmens ist kein einzelnes Verfahren, sondern ein Paket aus mehreren bereits bewährten Leistungen, zusammengestellt für die Bedürfnisse eines Unternehmens, nicht einer Privatperson: die Eintragung der juristischen Person, bei Bedarf das steuerliche Vorzugsregime <a href="{terminologiya}#maquila">Maquila</a>, der Aufenthaltstitel für die umziehenden Mitarbeiter und die Eröffnung eines Firmenkontos. Ein eigenständiges staatliches Verfahren „Unternehmensumzug" gibt es in Paraguay nicht — wir stellen es aus Mechanismen zusammen, die auf dieser Website bereits einzeln beschrieben sind.',
    body=lambda l: f'''
    <p>Der Unterschied zur gewöhnlichen Firmengründung liegt im Umfang und in der Abfolge: Statt
    eines einzelnen Gründers und eines einzelnen Aufenthaltstitels gibt es hier in der Regel mehrere
    Mitarbeiter, die gleichzeitig mit einer arbeitsfähigen juristischen Person und einem Konto einen
    legalen Status benötigen. Wir führen das als ein Projekt, nicht als mehrere unabhängige
    Aufträge.</p>

    <h2>Woraus das Paket besteht</h2>
    <ul>
      <li><strong>Eintragung der juristischen Person</strong> —
      <a href="{l['terminologiya']}#eas">EAS</a>, <a href="{l['terminologiya']}#sa">S.A.</a> oder
      <a href="{l['terminologiya']}#srl">S.R.L.</a>, dieselbe Leistung „Unternehmensgründung" (siehe
      die Karte auf der Seite <a href="{l['uslugi']}">„Leistungen"</a>).</li>
      <li><strong>Eintragung im Maquila-Regime</strong> — wenn das Geschäft zur Fertigung oder zu
      exportierbaren Dienstleistungen gehört (mehr dazu weiter unten).</li>
      <li><strong>Aufenthaltstitel fürs Team</strong> — ein Paket aus mehreren Verfahren im Rahmen
      der bereits bestehenden Leistung <a href="{l['usluga-residencia']}">„Aufenthaltstitel"</a>,
      eines pro umziehendem Mitarbeiter.</li>
      <li><strong>Eröffnung eines Firmenkontos</strong> — unter Berücksichtigung der Anforderungen,
      die Banken speziell an juristische Personen stellen (siehe Abschnitt unten).</li>
      <li><strong>Begleitung und Compliance</strong> — dieselbe Logik wie bei Privatpersonen, aber
      auf Unternehmensebene: RUC der juristischen Person und regelmäßige Meldungen.</li>
    </ul>

    <h2>Das Maquila-Regime — wahrscheinlich der wichtigste Vorteil für Dienstleistungsunternehmen</h2>
    <p>Ein offizielles Regime (Ley N° 1064/97), verwaltet über
    <a href="{l['terminologiya']}#rediex">REDIEX</a> und das MIC: eine einheitliche Steuer von 1% —
    auf die in Paraguay geschaffene Wertschöpfung oder auf den Rechnungsbetrag, je nachdem, was höher
    ist — anstelle der regulären 10% IRE. Anspruch auf das Regime hat jede in Paraguay legal
    registrierte juristische Person, die im Auftrag eines ausländischen Unternehmens arbeitet; zu den
    Vergünstigungen zählen die Aussetzung von Zöllen auf Rohstoff- und Ausrüstungseinfuhren, die
    Befreiung von Zoll- und Hafengebühren sowie die Mehrwertsteuerrückerstattung. Das Regime steht
    ausdrücklich nicht nur der Fertigung offen: Laut einem offiziellen MIC-Dokument gibt es unter den
    aktuellen Nutzern des Regimes eine eigene Kategorie „Exportadores de Servicios"
    (Dienstleistungsexporteure) — das Regime eignet sich also auch für die Relokation eines IT- oder
    Outsourcing-Unternehmens, nicht nur einer Fabrik.</p>
    <div class="callout"><span class="callout-label">Was nicht geklärt ist</span>Das konkrete
    Verfahren und die Fristen für den Erhalt des Maquila-Status, getrennt von der eigentlichen
    Firmenregistrierung, wurden zum Zeitpunkt der Veröffentlichung nicht untersucht; bevor wir eine
    genaue Frist und Checkliste nennen, klären wir dies individuell über REDIEX für Ihren konkreten
    Fall.</div>

    <h2>Das Unternehmen als juristische Person</h2>
    <p>Die Registrierungsfristen entsprechen denen einer gewöhnlichen Firmengründung: EAS über
    SUACE — bis zu 72 Werkstunden bei Standardsatzung, S.A. — 8–30 Werktage, S.R.L. — 15–30 Werktage.
    Für die EAS muss der gesetzliche Vertreter zwingend die paraguayische Staatsbürgerschaft oder
    eine paraguayische Cédula besitzen — „ohne Ausnahmen" —; bei einer Relokation, bei der noch kein
    Mitarbeiter über einen Aufenthaltstitel verfügt, übernimmt zu Beginn ein Bevollmächtigter diese
    Rolle, bis jemand aus dem Team eine Cédula erhält.</p>

    <h2>Firmenkonto</h2>
    <p>Das Unternehmen benötigt eine vollständig formalisierte Unternehmensstruktur; die physische
    Anwesenheit zur Kontoeröffnung ist zwingend erforderlich — aus der Ferne ist dies praktisch
    unmöglich. Die EAS wirft als relativ neue Rechtsform bei Banken mitunter zusätzliche Fragen auf
    und erfordert bei der Antragstellung eine sorgfältigere Begleitung.</p>
    <p class="confidence-note">In den gesammelten Quellen gibt es keine direkten Bestätigungen (oder
    Widerlegungen) dafür, dass Banken speziell an Kapital oder Eigentümer russischer Herkunft
    zusätzliche Anforderungen stellen — das bedeutet nicht, dass solche Schwierigkeiten garantiert
    nicht auftreten, sondern nur, dass wir dafür keine direkte Bestätigung gefunden haben. Wir klären
    dies konkret für Ihren Fall vor Beginn der Arbeit, nicht im Nachhinein.</p>

    <h2>Aufenthaltstitel für Mitarbeiter — ohne gesondertes „Unternehmensvisum"</h2>
    <p>Ein spezielles Visum für umziehende Mitarbeiter oder digitale Nomaden gibt es in Paraguay
    nicht: Der gesamte Ablauf läuft über denselben Mechanismus, der bereits auf der Seite
    <a href="{l['usluga-residencia']}">„Aufenthaltstitel"</a> beschrieben ist — die
    <a href="{l['terminologiya']}#residencia-temporal">Residencia Temporal</a> nach dem allgemeinen
    Migrationsgesetz, bei der Remote-Arbeit und ein Vertrag mit dem ausländischen (in diesem Fall dem
    relokierenden) Arbeitgeber Teil des Dokumentenpakets sind, das die Einkommensquelle belegt. Eine
    offiziell festgelegte Mindesteinkommensgrenze gibt es nicht — die Migrationsbehörde bewertet die
    Zahlungsfähigkeit anhand von Kontoauszügen und Verträgen. Die Bearbeitung dauert 60–90 Tage. In
    der Praxis bedeutet das: Die „Relokation des Teams" ist kein einzelnes Verfahren, sondern mehrere
    parallele Aufenthaltstitel-Verfahren, nur mit Unternehmensdokumenten (Vertrag, Kontoauszüge der
    Firma) anstelle eines Teils der persönlichen Unterlagen.</p>

    <h2>Kosten</h2>
    <p>Das Paket setzt sich aus bereits bestehenden Leistungen zusammen — Firmengründung,
    Aufenthaltstitel für jeden Mitarbeiter und das Compliance-Abonnement — plus einer gesonderten
    Komponente für Maquila bei Bedarf. Den endgültigen Preis und die Zusammensetzung des Pakets
    berechnen wir individuell: Er hängt von der gewählten Rechtsform, der Anzahl der umziehenden
    Mitarbeiter und davon ab, ob das Maquila-Regime benötigt wird. Die vollständigen Preise der
    einzelnen Komponenten stehen auf der Seite <a href="{l['stoimost']}">„Preise"</a>.</p>

    <h2>Siehe auch</h2>
    <ul>
      <li><a href="{l['usluga-residencia']}">„Aufenthaltstitel"</a> — die Leistung, aus der der
      Aufenthaltstitel jedes Teammitglieds zusammengestellt wird</li>
      <li><a href="{l['uslugi']}">„Leistungen"</a> — die vollständige Liste, einschließlich
      Unternehmensgründung und Geschäftsbegleitung</li>
      <li><a href="{l['stoimost']}">„Preise"</a> — die Kosten der einzelnen Paketkomponenten</li>
    </ul>
    ''',
    final_h2="Planen Sie die Relokation eines Unternehmens nach Paraguay?",
    final_p="Wir erarbeiten die Zusammensetzung des Pakets für Ihre Situation — Rechtsform, Anzahl der Mitarbeiter und ob das Maquila-Regime für Sie passt.",
    final_cta="Beratung anfragen",
),
},
"usluga-medicina": {
"ru": dict(
    title="Медицинское сопровождение в Парагвае: страховка и помощь на приёме | Grund Paraguay",
    description="Подбор медицинской страховки в Парагвае, разбор условий (сроки ожидания, декларация о здоровье) и сопровождение на приёме — для тех, кто переезжает и не готов разбираться в этом на испанском в одиночку.",
    h1="Медицинское сопровождение в Парагвае",
    lead='Медицинское сопровождение — не полис сам по себе, а помощь на всех шагах вокруг него: подобрать план под свой статус, не упустить критичное условие в договоре и не остаться один на один с приёмной клиники на испанском. Отдельной государственной услуги «страховка для иностранца» в Парагвае не существует — мы собираем результат из уже существующих на рынке планов и своей работы вокруг них.',
    body=lambda l: f'''
    <p>Систему медицины в Парагвае мы разбираем подробно на отдельной странице
    <a href="{l['meditsina-v-paragvae']}">«Медицина в Парагвае»</a> — здесь коротко: три уровня
    (базовая помощь MSPBS, привязанное к занятости соцстрахование IPS, частная медицина) и
    для большинства переезжающих реальный вопрос — не «бесплатно или платно», а какой частный
    план выбрать и на каких условиях.</p>

    <h2>Из чего состоит сопровождение</h2>
    <ul>
      <li><strong>Подбор плана</strong> — сверяем предложения локальных страховщиков (например,
      MAPFRE Paraguay, Asismed) и международных полисов с вашим статусом и бюджетом. У части
      локальных планов есть условия, которые сразу отсекают часть заявителей — например, MAPFRE
      Paraguay требует статус постоянного резидента; на этапе временной резиденции такой план
      просто недоступен, и лучше знать это заранее, а не после отказа.</li>
      <li><strong>Разбор мелкого шрифта</strong> — сроки ожидания («carencias») перед покрытием
      конкретных состояний, обязательная декларация о здоровье при оформлении, список исключений.
      У локальных планов эти условия могут быть весьма жёсткими: например, у одного из
      распространённых планов — необходимость задекларировать хронические заболевания заранее (6
      месяцев ожидания на задекларированные, минимум 12 — на онкологию и болезни почек/печени, а
      незадекларированные не покрываются вообще).</li>
      <li><strong>Сопровождение на приёме</strong> — перевод, помощь с документами на месте и
      объяснение счёта: частные клиники в Парагвае обычно требуют оплату сразу, без ожидания
      возмещения от страховой.</li>
      <li><strong>Помощь с обращением за выплатой</strong> — сроки подачи документов по страховому
      случаю могут быть короткими (у отдельных планов — 48 часов), и мы следим, чтобы вы не
      пропустили этот срок в чужой стране на незнакомом языке.</li>
    </ul>

    <h2>Почему это вообще нужно</h2>
    <p>Денге — реальный сезонный риск, а не редкость (подробнее и с источниками — на странице
    <a href="{l['mify-voprosy']}">«Мифы и вопросы»</a>, раздел «Здоровье и климат»). Официальный
    портал Великобритании для путешественников прямо отмечает: качественная частная медпомощь в
    Парагвае доступна в основном в крупных городах, а частные клиники обычно требуют немедленной
    оплаты на месте — то есть страховка нужна не «на всякий случай», а как рабочий инструмент,
    которым придётся пользоваться в первый же год.</p>

    <h2>Что не входит на старте</h2>
    <p>Оформление IPS (для тех, кто официально трудоустроен в Парагвае или регистрирует
    микропредприятие) — отдельный процесс через работодателя, который выходит за рамки этой
    услуги на старте; при необходимости обсуждаем это отдельно, а не включаем в пакет по
    умолчанию.</p>

    <h2>Стоимость</h2>
    <p>Мы не нашли на рынке предложения, где организация страховки и сопровождение продавались
    бы как одна услуга специально для переезжающих в Парагвай, — устоявшегося рыночного
    ориентира по цене такой услуги попросту нет. Стоимость самих страховых планов у локальных и
    международных страховщиков публично не раскрывается (индивидуальный расчёт по возрасту и
    состоянию здоровья) — состав и стоимость нашего сопровождения тоже считаем индивидуально,
    после того как понятен ваш статус и то, какой план рассматривается.</p>

    <h2>Смотрите также</h2>
    <ul>
      <li><a href="{l['meditsina-v-paragvae']}">«Медицина в Парагвае»</a> — подробно об
      устройстве системы: MSPBS, IPS, частная медицина, клиники</li>
      <li><a href="{l['usluga-residencia']}">«Резидентура (ВНЖ)»</a> — статус, от которого
      зависит доступность части страховых планов</li>
      <li><a href="{l['mify-voprosy']}">«Мифы и вопросы»</a> — денге и другие риски здоровья при
      переезде</li>
    </ul>
    ''',
    final_h2="Разбираетесь, какая страховка вам подходит?",
    final_p="Сверим варианты с вашим статусом резидентства и бюджетом и объясним условия, которые легко упустить в договоре на испанском.",
    final_cta="Оставить заявку на консультацию",
),
"es": dict(
    title="Asistencia médica en Paraguay: seguro y acompañamiento en la consulta | Grund Paraguay",
    description="Selección de seguro médico en Paraguay, análisis de las condiciones (períodos de carencia, declaración jurada de salud) y acompañamiento en la consulta — para quienes se mudan y no quieren enfrentar esto en español por su cuenta.",
    h1="Asistencia médica en Paraguay",
    lead='La asistencia médica no es la póliza en sí, sino la ayuda en todos los pasos alrededor de ella: elegir el plan adecuado a su estatus, no pasar por alto una condición crítica del contrato y no quedarse solo frente a la recepción de una clínica en español. En Paraguay no existe un trámite estatal independiente de «seguro para extranjeros» — armamos el resultado a partir de los planes que ya existen en el mercado y de nuestro trabajo alrededor de ellos.',
    body=lambda l: f'''
    <p>Analizamos en detalle el sistema de salud en Paraguay en una página aparte,
    <a href="{l['meditsina-v-paragvae']}">«Medicina en Paraguay»</a> — aquí, en breve: tres
    niveles (atención básica del MSPBS, el seguro social IPS vinculado al empleo, la medicina
    privada) y para la mayoría de quienes se mudan la pregunta real no es «gratis o pago», sino
    qué plan privado elegir y en qué condiciones.</p>

    <h2>De qué se compone la asistencia</h2>
    <ul>
      <li><strong>Selección del plan</strong> — comparamos las ofertas de aseguradoras locales
      (por ejemplo, MAPFRE Paraguay, Asismed) y de pólizas internacionales con su estatus y
      presupuesto. Algunos planes locales tienen condiciones que descartan de entrada a parte de
      los solicitantes — por ejemplo, MAPFRE Paraguay exige el estatus de residente permanente;
      en la etapa de residencia temporal ese plan simplemente no está disponible, y es mejor
      saberlo con anticipación, no después de un rechazo.</li>
      <li><strong>Análisis de la letra pequeña</strong> — los períodos de carencia antes de
      cubrir condiciones concretas, la declaración jurada de salud obligatoria al contratar, la
      lista de exclusiones. En los planes locales estas condiciones pueden ser bastante
      estrictas: por ejemplo, en uno de los planes más difundidos hay que declarar por
      anticipado las enfermedades crónicas (6 meses de carencia para las declaradas, mínimo 12
      para cáncer y enfermedades renales/hepáticas, y las no declaradas no se cubren en
      absoluto).</li>
      <li><strong>Acompañamiento en la consulta</strong> — traducción, ayuda con los documentos
      en el lugar y explicación de la factura: las clínicas privadas en Paraguay suelen exigir
      el pago de inmediato, sin esperar el reembolso de la aseguradora.</li>
      <li><strong>Ayuda para reclamar el reembolso</strong> — los plazos para presentar los
      documentos de un siniestro pueden ser cortos (en algunos planes, 48 horas), y nos
      aseguramos de que no pierda ese plazo en un país extranjero y en un idioma que no
      domina.</li>
    </ul>

    <h2>Por qué esto es realmente necesario</h2>
    <p>El dengue es un riesgo estacional real, no una rareza (más detalles y fuentes en la página
    <a href="{l['mify-voprosy']}">«Mitos y preguntas»</a>, sección «Salud y clima»). El portal
    oficial del Reino Unido para viajeros señala directamente: la atención médica privada de
    calidad en Paraguay está disponible sobre todo en las grandes ciudades, y las clínicas
    privadas suelen exigir el pago inmediato en el lugar — es decir, el seguro no es «por si
    acaso», sino una herramienta de trabajo que tendrá que usar ya en el primer año.</p>

    <h2>Qué no incluye al principio</h2>
    <p>La gestión del IPS (para quienes están formalmente empleados en Paraguay o registran una
    microempresa) es un trámite aparte a través del empleador, que queda fuera del alcance de
    este servicio al principio; si hace falta, lo tratamos por separado, no lo incluimos en el
    paquete por defecto.</p>

    <h2>Costo</h2>
    <p>No encontramos en el mercado una oferta donde la gestión del seguro y el acompañamiento
    se vendieran como un solo servicio específicamente para quienes se mudan a Paraguay —
    sencillamente no existe un punto de referencia de precio consolidado para ese servicio. El
    costo de los propios planes de seguro de las aseguradoras locales e internacionales no se
    publica de forma pública (cálculo individual según la edad y el estado de salud) — la
    composición y el costo de nuestro acompañamiento también los calculamos de forma individual,
    una vez que su estatus está claro y qué plan se está considerando.</p>

    <h2>Vea también</h2>
    <ul>
      <li><a href="{l['meditsina-v-paragvae']}">«Medicina en Paraguay»</a> — en detalle sobre
      cómo está organizado el sistema: MSPBS, IPS, medicina privada, clínicas</li>
      <li><a href="{l['usluga-residencia']}">«Residencia»</a> — el estatus del que depende la
      disponibilidad de parte de los planes de seguro</li>
      <li><a href="{l['mify-voprosy']}">«Mitos y preguntas»</a> — el dengue y otros riesgos de
      salud al mudarse</li>
    </ul>
    ''',
    final_h2="¿Está evaluando qué seguro le conviene?",
    final_p="Comparamos las opciones con su estatus de residencia y presupuesto, y le explicamos las condiciones que son fáciles de pasar por alto en un contrato en español.",
    final_cta="Solicitar una consulta",
),
"en": dict(
    title="Medical support in Paraguay: insurance and support at the doctor's office | Grund Paraguay",
    description="Choosing medical insurance in Paraguay, working through the terms (waiting periods, health declaration), and support at appointments — for anyone relocating who isn't ready to handle this in Spanish alone.",
    h1="Medical support in Paraguay",
    lead='Medical support isn\'t the policy itself — it\'s help with everything around it: choosing a plan that fits your status, not missing a critical condition in the contract, and not being left alone at a clinic\'s front desk in Spanish. There\'s no separate government service for "insurance for foreigners" in Paraguay — we put the result together from the plans already on the market and our own work around them.',
    body=lambda l: f'''
    <p>We cover Paraguay's healthcare system in detail on a separate page,
    <a href="{l['meditsina-v-paragvae']}">"Healthcare in Paraguay"</a> — here, in short: three
    levels (basic MSPBS care, the employment-linked IPS social insurance, private medicine), and
    for most people relocating the real question isn't "free or paid" but which private plan to
    choose and on what terms.</p>

    <h2>What the support includes</h2>
    <ul>
      <li><strong>Plan selection</strong> — we compare offers from local insurers (e.g., MAPFRE
      Paraguay, Asismed) and international policies against your status and budget. Some local
      plans have conditions that rule out part of applicants right away — for example, MAPFRE
      Paraguay requires permanent-resident status; at the temporary-residency stage that plan
      simply isn't available, and it's better to know that in advance, not after a rejection.</li>
      <li><strong>Reading the fine print</strong> — waiting periods ("carencias") before specific
      conditions are covered, the mandatory health declaration at signup, the list of
      exclusions. Local plans' terms can be quite strict: for example, one widespread plan
      requires declaring chronic conditions in advance (6 months' waiting period for declared
      ones, at least 12 for cancer and kidney/liver disease, and undeclared conditions aren't
      covered at all).</li>
      <li><strong>Support at appointments</strong> — translation, help with paperwork on the
      spot, and explaining the bill: private clinics in Paraguay usually require payment right
      away, without waiting for reimbursement from the insurer.</li>
      <li><strong>Help filing a claim</strong> — deadlines for submitting claim documents can be
      short (48 hours for some plans), and we make sure you don't miss that deadline in a
      foreign country in an unfamiliar language.</li>
    </ul>

    <h2>Why this actually matters</h2>
    <p>Dengue is a real seasonal risk, not a rarity (more detail and sources on the
    <a href="{l['mify-voprosy']}">"Myths & Questions"</a> page, "Health & Climate" section). The
    UK's official travel portal notes directly that quality private medical care in Paraguay is
    mostly available in major cities, and private clinics usually require immediate
    on-the-spot payment — meaning insurance isn't "just in case," it's a working tool you'll
    likely need in your first year.</p>

    <h2>What's not included at the start</h2>
    <p>Setting up IPS (for those formally employed in Paraguay or registering a microenterprise)
    is a separate process through the employer, outside the scope of this service at the
    outset; we discuss it separately if needed, rather than bundling it in by default.</p>

    <h2>Cost</h2>
    <p>We didn't find an offer on the market where insurance arrangement and support are sold as
    one service specifically for people relocating to Paraguay — there simply isn't an
    established price benchmark for that. Pricing for the insurance plans themselves, from both
    local and international insurers, isn't published publicly (it's calculated individually by
    age and health status) — we calculate the scope and cost of our own support individually
    too, once your status is clear and which plan is under consideration.</p>

    <h2>See also</h2>
    <ul>
      <li><a href="{l['meditsina-v-paragvae']}">"Healthcare in Paraguay"</a> — a detailed look
      at how the system works: MSPBS, IPS, private medicine, clinics</li>
      <li><a href="{l['usluga-residencia']}">"Residency"</a> — the status that determines which
      insurance plans are available to you</li>
      <li><a href="{l['mify-voprosy']}">"Myths & Questions"</a> — dengue and other health risks
      when relocating</li>
    </ul>
    ''',
    final_h2="Working out which insurance fits you?",
    final_p="We'll compare your options against your residency status and budget and explain the terms that are easy to miss in a Spanish-language contract.",
    final_cta="Request a consultation",
),
"de": dict(
    title="Medizinische Begleitung in Paraguay: Versicherung und Unterstützung beim Arztbesuch | Grund Paraguay",
    description="Auswahl einer Krankenversicherung in Paraguay, Klärung der Bedingungen (Wartezeiten, Gesundheitserklärung) und Begleitung beim Arztbesuch — für alle, die umziehen und das nicht allein auf Spanisch klären möchten.",
    h1="Medizinische Begleitung in Paraguay",
    lead='Medizinische Begleitung ist nicht die Police selbst, sondern Hilfe bei allen Schritten drumherum: den passenden Plan für den eigenen Status wählen, eine entscheidende Vertragsbedingung nicht übersehen und am Empfang einer Klinik nicht allein auf Spanisch dastehen. Ein eigenständiges staatliches Verfahren „Versicherung für Ausländer" gibt es in Paraguay nicht — wir setzen das Ergebnis aus den bereits am Markt vorhandenen Plänen und unserer Arbeit darum herum zusammen.',
    body=lambda l: f'''
    <p>Das Gesundheitssystem Paraguays behandeln wir ausführlich auf einer eigenen Seite,
    <a href="{l['meditsina-v-paragvae']}">„Medizin in Paraguay"</a> — hier kurz: drei Ebenen
    (Grundversorgung über MSPBS, das an Beschäftigung gekoppelte Sozialversicherungssystem IPS,
    Privatmedizin), und für die meisten Umziehenden lautet die eigentliche Frage nicht
    „kostenlos oder kostenpflichtig", sondern welcher private Plan zu welchen Bedingungen
    infrage kommt.</p>

    <h2>Woraus die Begleitung besteht</h2>
    <ul>
      <li><strong>Planauswahl</strong> — wir gleichen die Angebote lokaler Versicherer (z. B.
      MAPFRE Paraguay, Asismed) und internationaler Policen mit Ihrem Status und Budget ab. Ein
      Teil der lokalen Pläne hat Bedingungen, die einen Teil der Antragsteller sofort
      ausschließen — MAPFRE Paraguay etwa verlangt den Status eines unbefristeten Residenten; in
      der Phase des befristeten Aufenthalts ist ein solcher Plan schlicht nicht verfügbar, und
      das sollte man vorher wissen, nicht erst nach einer Ablehnung.</li>
      <li><strong>Prüfung des Kleingedruckten</strong> — Wartezeiten („carencias") vor der
      Deckung bestimmter Zustände, die bei Vertragsabschluss verpflichtende
      Gesundheitserklärung, die Liste der Ausschlüsse. Bei lokalen Plänen können diese
      Bedingungen recht streng sein: Bei einem der verbreiteten Pläne müssen chronische
      Erkrankungen zum Beispiel im Voraus angegeben werden (6 Monate Wartezeit für angegebene,
      mindestens 12 für Krebs- sowie Nieren-/Lebererkrankungen, nicht angegebene Zustände werden
      überhaupt nicht gedeckt).</li>
      <li><strong>Begleitung beim Arztbesuch</strong> — Übersetzung, Hilfe mit Unterlagen vor Ort
      und Erklärung der Rechnung: Private Kliniken in Paraguay verlangen die Zahlung in der
      Regel sofort, ohne auf die Erstattung durch die Versicherung zu warten.</li>
      <li><strong>Hilfe bei der Schadensmeldung</strong> — die Fristen für die Einreichung von
      Unterlagen zu einem Versicherungsfall können kurz sein (bei manchen Plänen 48 Stunden),
      und wir achten darauf, dass Sie diese Frist im fremden Land und in einer fremden Sprache
      nicht verpassen.</li>
    </ul>

    <h2>Warum das überhaupt nötig ist</h2>
    <p>Dengue ist ein reales saisonales Risiko, keine Seltenheit (mehr dazu mit Quellen auf der
    Seite <a href="{l['mify-voprosy']}">„Mythen und Fragen"</a>, Abschnitt „Gesundheit und
    Klima"). Das offizielle britische Reiseportal weist ausdrücklich darauf hin: gute private
    medizinische Versorgung ist in Paraguay vor allem in Großstädten verfügbar, und private
    Kliniken verlangen in der Regel sofortige Zahlung vor Ort — die Versicherung ist also kein
    „für den Fall der Fälle", sondern ein Arbeitswerkzeug, das man bereits im ersten Jahr
    braucht.</p>

    <h2>Was zu Beginn nicht enthalten ist</h2>
    <p>Die Anmeldung bei der IPS (für formell in Paraguay Beschäftigte oder bei der Registrierung
    eines Kleinunternehmens) ist ein eigenständiges Verfahren über den Arbeitgeber, das zu
    Beginn außerhalb des Umfangs dieser Leistung liegt; bei Bedarf klären wir das gesondert,
    statt es standardmäßig ins Paket aufzunehmen.</p>

    <h2>Kosten</h2>
    <p>Wir haben am Markt kein Angebot gefunden, bei dem die Organisation der Versicherung und
    die Begleitung als eine Leistung speziell für Umziehende nach Paraguay verkauft würden —
    einen etablierten Preisrichtwert für eine solche Leistung gibt es schlicht nicht. Die Kosten
    der Versicherungspläne selbst geben weder lokale noch internationale Versicherer öffentlich
    bekannt (individuelle Berechnung nach Alter und Gesundheitszustand) — Umfang und Kosten
    unserer eigenen Begleitung berechnen wir ebenfalls individuell, sobald Ihr Status und der ins
    Auge gefasste Plan feststehen.</p>

    <h2>Siehe auch</h2>
    <ul>
      <li><a href="{l['meditsina-v-paragvae']}">„Medizin in Paraguay"</a> — ausführlich zum
      Aufbau des Systems: MSPBS, IPS, Privatmedizin, Kliniken</li>
      <li><a href="{l['usluga-residencia']}">„Aufenthaltstitel"</a> — der Status, von dem die
      Verfügbarkeit eines Teils der Versicherungspläne abhängt</li>
      <li><a href="{l['mify-voprosy']}">„Mythen und Fragen"</a> — Dengue und andere
      Gesundheitsrisiken beim Umzug</li>
    </ul>
    ''',
    final_h2="Sie klären, welche Versicherung zu Ihnen passt?",
    final_p="Wir gleichen die Optionen mit Ihrem Aufenthaltsstatus und Budget ab und erklären die Bedingungen, die man in einem spanischsprachigen Vertrag leicht übersieht.",
    final_cta="Beratung anfragen",
),
},
"usluga-compliance": {
"ru": dict(
    title="Сопровождение и комплаенс в Парагвае: RUC и отчётность | Grund Paraguay",
    description="Абонентская услуга, которая держит статус резидента Парагвая в силе: регистрация RUC, регулярная налоговая отчётность и контроль срока перехода с Residencia Temporal на Permanente.",
    h1="Сопровождение и комплаенс",
    lead='Сопровождение и комплаенс — абонентская услуга, которая поддерживает статус резидента в силе на всём пути от временной резиденции к постоянной, чтобы он не был потерян из-за пропущенной отчётности.',
    body=lambda l: f'''
    <p>Это продолжение <a href="{l['usluga-residencia']}">«Резидентуры»</a>, а не альтернатива ей:
    резидентура открывает статус, а комплаенс держит его в силе всё то время, что статус
    действует, — обычно от 2 до 5 лет до перехода на Permanente.</p>

    <h2>Что запускает эту обязанность</h2>
    <p>После получения <a href="{l['terminologiya']}#residencia-temporal">Residencia Temporal</a>
    у иностранца возникает обязанность зарегистрировать <a href="{l['terminologiya']}#ruc">RUC</a>
    (единый номер налогоплательщика, привязанный к <a href="{l['terminologiya']}#cedula">Cédula</a>)
    и регулярно — как правило, ежемесячно — подавать налоговую отчётность, включая нулевую, если
    деятельности не было.</p>

    <h2>Как это выглядит на практике</h2>
    <div class="diagram">
      {_COMPLIANCE_SVG['ru']}
      <p class="diagram-caption">Условная схема цикла, который повторяется каждый месяц, пока
      статус резидента действует.</p>
    </div>

    <h2>Что входит в абонемент</h2>
    <ul>
      <li><strong>Ведение отчётности</strong> — включая нулевую, если в отчётном периоде не было
      деятельности.</li>
      <li><strong>Контроль сроков</strong> — чтобы ни одна подача не была пропущена.</li>
      <li><strong>Контроль статуса дела</strong> на всём пути от Temporal к Permanente, который
      обычно занимает от 2 до 5 лет.</li>
    </ul>

    <h2>Почему это отдельная услуга, а не бонус к резидентуре</h2>
    <p>Без действующего комплаенса перевод в постоянную резиденцию рискует растянуться или
    сорваться — накопленные пропуски по отчётности становятся проблемой именно в момент подачи на
    Permanente, а не раньше. Полная стоимость абонемента — на странице
    <a href="{l['stoimost']}">«Стоимость и тарифы»</a>.</p>

    <h2>Смотрите также</h2>
    <ul>
      <li><a href="{l['usluga-residencia']}">«Резидентура (ВНЖ)»</a> — предыдущий этап, который
      запускает эту обязанность</li>
      <li><a href="{l['nalogi-inostrantsev']}">«Налоги для иностранцев»</a> — что именно входит в
      отчётность (IRE, IVA, IRP)</li>
      <li><a href="{l['stoimost']}">«Стоимость и тарифы»</a> — полная стоимость абонемента</li>
    </ul>
    ''',
    final_h2="Хотите, чтобы отчётность не отвлекала от остального?",
    final_p="Возьмём на себя RUC, регулярную отчётность и контроль статуса дела — обращаемся к вам, только когда нужно ваше решение.",
    final_cta="Оставить заявку на консультацию",
),
"es": dict(
    title="Acompañamiento y cumplimiento en Paraguay: RUC y declaraciones | Grund Paraguay",
    description="Servicio por suscripción que mantiene vigente el estatus de residente en Paraguay: inscripción del RUC, declaraciones tributarias regulares y seguimiento del plazo de Temporal a Permanente.",
    h1="Acompañamiento y cumplimiento",
    lead='El acompañamiento y cumplimiento es un servicio por suscripción que mantiene vigente el estatus de residente durante todo el camino de la temporal a la permanente, para que no se pierda por una declaración omitida.',
    body=lambda l: f'''
    <p>Es la continuación de <a href="{l['usluga-residencia']}">«Residencia»</a>, no una
    alternativa: la residencia abre el estatus, y el cumplimiento lo mantiene vigente durante todo
    el tiempo en que está en curso — normalmente de 2 a 5 años hasta pasar a la Permanente.</p>

    <h2>Qué origina esta obligación</h2>
    <p>Tras obtener la <a href="{l['terminologiya']}#residencia-temporal">Residencia Temporal</a>,
    el extranjero debe inscribir el <a href="{l['terminologiya']}#ruc">RUC</a> (número único de
    contribuyente, vinculado a la <a href="{l['terminologiya']}#cedula">Cédula</a>) y presentar
    declaraciones tributarias de forma regular — por lo general mensual —, incluidas las
    declaraciones en cero si no hubo actividad.</p>

    <h2>Cómo funciona en la práctica</h2>
    <div class="diagram">
      {_COMPLIANCE_SVG['es']}
      <p class="diagram-caption">Esquema ilustrativo del ciclo que se repite cada mes mientras el
      estatus de residente está vigente.</p>
    </div>

    <h2>Qué incluye la suscripción</h2>
    <ul>
      <li><strong>Gestión de las declaraciones</strong> — incluidas las de cero si no hubo
      actividad en el período.</li>
      <li><strong>Control de plazos</strong> — para que no se omita ninguna presentación.</li>
      <li><strong>Seguimiento del estado del trámite</strong> durante todo el camino de Temporal a
      Permanente, que suele durar de 2 a 5 años.</li>
    </ul>

    <h2>Por qué es un servicio aparte y no un bono de la residencia</h2>
    <p>Sin un cumplimiento activo, la conversión a residencia permanente corre el riesgo de
    demorarse o fracasar — las omisiones acumuladas en las declaraciones se vuelven un problema
    justo en el momento de solicitar la Permanente, no antes. El costo completo de la suscripción
    está en la página <a href="{l['stoimost']}">«Costos y tarifas»</a>.</p>

    <h2>Vea también</h2>
    <ul>
      <li><a href="{l['usluga-residencia']}">«Residencia»</a> — la etapa anterior que origina esta
      obligación</li>
      <li><a href="{l['nalogi-inostrantsev']}">«Impuestos para extranjeros»</a> — qué incluye
      exactamente la declaración (IRE, IVA, IRP)</li>
      <li><a href="{l['stoimost']}">«Costos y tarifas»</a> — el costo completo de la suscripción</li>
    </ul>
    ''',
    final_h2="¿Quiere que las declaraciones no le quiten tiempo de lo demás?",
    final_p="Nos hacemos cargo del RUC, las declaraciones regulares y el seguimiento del trámite — le contactamos solo cuando su decisión es necesaria.",
    final_cta="Solicitar una consulta",
),
"en": dict(
    title="Ongoing Compliance in Paraguay: RUC and Tax Filings | Grund Paraguay",
    description="A subscription service that keeps your Paraguayan resident status valid: RUC registration, regular tax filings, and tracking your timeline from Residencia Temporal to Permanente.",
    h1="Ongoing Compliance",
    lead="Ongoing compliance is a subscription service that keeps your resident status valid all the way from temporary to permanent, so it isn't lost over a missed filing.",
    body=lambda l: f'''
    <p>This is a continuation of <a href="{l['usluga-residencia']}">"Residency"</a>, not an
    alternative to it: residency opens the status, and compliance keeps it valid for as long as it
    runs — usually 2 to 5 years before converting to Permanente.</p>

    <h2>What triggers this obligation</h2>
    <p>After getting <a href="{l['terminologiya']}#residencia-temporal">Residencia Temporal</a>, a
    foreigner must register a <a href="{l['terminologiya']}#ruc">RUC</a> (a unique taxpayer number
    tied to the <a href="{l['terminologiya']}#cedula">Cédula</a>) and file tax returns regularly —
    usually monthly — including zero filings when there was no activity.</p>

    <h2>What this looks like in practice</h2>
    <div class="diagram">
      {_COMPLIANCE_SVG['en']}
      <p class="diagram-caption">An illustrative diagram of the cycle that repeats every month
      while your resident status is active.</p>
    </div>

    <h2>What the subscription covers</h2>
    <ul>
      <li><strong>Bookkeeping</strong> — including zero filings when there was no activity in the
      period.</li>
      <li><strong>Deadline tracking</strong> — so no filing gets missed.</li>
      <li><strong>Case status monitoring</strong> all the way from Temporal to Permanente, which
      usually takes 2 to 5 years.</li>
    </ul>

    <h2>Why this is a separate service, not a bonus to residency</h2>
    <p>Without active compliance, converting to permanent residency risks dragging on or falling
    through — missed filings pile up and become a problem exactly when you apply for Permanente,
    not before. Full subscription pricing is on the
    <a href="{l['stoimost']}">"Pricing"</a> page.</p>

    <h2>See also</h2>
    <ul>
      <li><a href="{l['usluga-residencia']}">"Residency"</a> — the earlier stage that triggers
      this obligation</li>
      <li><a href="{l['nalogi-inostrantsev']}">"Taxes for Foreigners"</a> — exactly what the
      filings cover (IRE, IVA, IRP)</li>
      <li><a href="{l['stoimost']}">"Pricing"</a> — full subscription pricing</li>
    </ul>
    ''',
    final_h2="Want tax filings off your plate?",
    final_p="We take on the RUC, regular filings, and case status tracking — we only reach out when your decision is actually needed.",
    final_cta="Request a consultation",
),
"de": dict(
    title="Begleitung und Compliance in Paraguay: RUC und Meldungen | Grund Paraguay",
    description="Abonnement-Leistung, die den Aufenthaltsstatus in Paraguay aufrechterhält: RUC-Registrierung, regelmäßige Steuermeldungen und Fristenkontrolle von Temporal zu Permanente.",
    h1="Begleitung und Compliance",
    lead="Begleitung und Compliance ist eine Abonnement-Leistung, die den Aufenthaltsstatus auf dem gesamten Weg von befristet zu unbefristet aufrechterhält, damit er nicht wegen einer versäumten Meldung verloren geht.",
    body=lambda l: f'''
    <p>Das ist die Fortsetzung von <a href="{l['usluga-residencia']}">„Aufenthaltstitel"</a>, keine
    Alternative dazu: Der Aufenthaltstitel eröffnet den Status, Compliance hält ihn die ganze Zeit
    aufrecht, in der er läuft — meist 2 bis 5 Jahre bis zur Umwandlung in Permanente.</p>

    <h2>Was diese Pflicht auslöst</h2>
    <p>Nach Erhalt der <a href="{l['terminologiya']}#residencia-temporal">Residencia Temporal</a>
    muss der Ausländer eine <a href="{l['terminologiya']}#ruc">RUC</a> (einheitliche Steuernummer,
    gekoppelt an die <a href="{l['terminologiya']}#cedula">Cédula</a>) registrieren und regelmäßig
    — in der Regel monatlich — Steuererklärungen einreichen, einschließlich Nullmeldungen bei
    fehlender Tätigkeit.</p>

    <h2>Wie das in der Praxis aussieht</h2>
    <div class="diagram">
      {_COMPLIANCE_SVG['de']}
      <p class="diagram-caption">Schematische Darstellung des Zyklus, der sich jeden Monat
      wiederholt, solange der Aufenthaltsstatus gilt.</p>
    </div>

    <h2>Was das Abonnement abdeckt</h2>
    <ul>
      <li><strong>Buchführung</strong> — einschließlich Nullmeldungen bei fehlender Tätigkeit im
      Zeitraum.</li>
      <li><strong>Fristenkontrolle</strong> — damit keine Meldung versäumt wird.</li>
      <li><strong>Statusüberwachung des Verfahrens</strong> auf dem gesamten Weg von Temporal zu
      Permanente, der meist 2 bis 5 Jahre dauert.</li>
    </ul>

    <h2>Warum das eine eigenständige Leistung ist, kein Bonus zum Aufenthaltstitel</h2>
    <p>Ohne laufende Compliance riskiert die Umwandlung in den unbefristeten Aufenthaltstitel,
    sich zu verzögern oder zu scheitern — versäumte Meldungen summieren sich und werden genau im
    Moment der Beantragung der Permanente zum Problem, nicht früher. Die vollständigen Kosten des
    Abonnements stehen auf der Seite <a href="{l['stoimost']}">„Preise"</a>.</p>

    <h2>Siehe auch</h2>
    <ul>
      <li><a href="{l['usluga-residencia']}">„Aufenthaltstitel"</a> — die vorherige Etappe, die
      diese Pflicht auslöst</li>
      <li><a href="{l['nalogi-inostrantsev']}">„Steuern für Ausländer"</a> — was die Meldungen
      genau umfassen (IRE, IVA, IRP)</li>
      <li><a href="{l['stoimost']}">„Preise"</a> — die vollständigen Kosten des Abonnements</li>
    </ul>
    ''',
    final_h2="Sollen Meldungen Sie nicht vom Wesentlichen ablenken?",
    final_p="Wir übernehmen RUC, regelmäßige Meldungen und Statuskontrolle — wir melden uns nur, wenn Ihre Entscheidung tatsächlich gebraucht wird.",
    final_cta="Beratung anfragen",
),
},
"usluga-citizenship": {
"ru": dict(
    title="Гражданство Парагвая: сроки, документы, Corte Suprema | Grund Paraguay",
    description="Натурализация в Парагвае: 3 года после Residencia Permanente (ст. 148 Конституции), дело ведёт Верховный суд, реалистичный полный срок от переезда до паспорта — 7–8 лет.",
    h1="Гражданство Парагвая",
    lead='Гражданство Парагвая — статус, который даёт паспорт с безвизовым доступом примерно в 145 стран (Henley Passport Index) и более устойчивое правовое положение, чем резиденция.',
    body=lambda l: f'''
    <p>Натурализация — не альтернатива резидентуре, а её логичное продолжение для тех, кто хочет
    более устойчивый статус, чем Residencia Permanente, и готов ждать ещё несколько лет сверху.</p>

    <h2>Когда это становится возможно</h2>
    <p>Натурализация возможна не раньше чем через 3 года после получения
    <a href="{l['terminologiya']}#residencia-permanente">Residencia Permanente</a> (ст. 148
    Конституции Парагвая) — то есть реалистичный полный срок от переезда до паспорта складывается
    в 7–8 лет, а не «год», как иногда обещают на рынке.</p>

    <h2>Путь от переезда до паспорта</h2>
    <div class="diagram">
      {_CITIZENSHIP_SVG['ru']}
      <p class="diagram-caption">Таймлайн из уже опубликованных диапазонов: Temporal (до 2 лет) →
      Permanente (обычно 2–5 лет) → обязательное ожидание 3 года перед подачей на натурализацию.</p>
    </div>

    <h2>Кто ведёт дело</h2>
    <p>Дело о натурализации ведёт не миграционная служба, а Верховный суд
    (<a href="{l['terminologiya']}#corte-suprema">Corte Suprema de Justicia</a>); процедура
    требует личной явки и сопровождения адвоката — это отдельный процесс со своими сроками, не
    продолжение резидентского дела по инерции.</p>

    <h2>Документы</h2>
    <p>Полный список документов на натурализацию — на странице
    <a href="{l['dok-grazhdanstvo']}">«Гражданство: документы»</a> в разделе «Документы».</p>

    <h2>Смотрите также</h2>
    <ul>
      <li><a href="{l['usluga-residencia']}">«Резидентура (ВНЖ)»</a> — обязательный
      предшествующий этап</li>
      <li><a href="{l['riski']}">«Честно о рисках»</a> — почему «гражданство за год» не
      соответствует действительности</li>
      <li><a href="{l['keisy']}">«Кейсы и отзывы»</a> — типичные истории клиентов</li>
    </ul>
    ''',
    final_h2="Планируете дойти до гражданства?",
    final_p="Оценим сроки конкретно по вашей ситуации и проверим документы до подачи в Corte Suprema.",
    final_cta="Оставить заявку на консультацию",
),
"es": dict(
    title="Ciudadanía paraguaya: plazos, documentos, Corte Suprema | Grund Paraguay",
    description="Naturalización en Paraguay: 3 años después de la Residencia Permanente (art. 148 de la Constitución), la tramita la Corte Suprema, plazo real completo desde la mudanza hasta el pasaporte — 7–8 años.",
    h1="Ciudadanía paraguaya",
    lead='La ciudadanía paraguaya otorga un pasaporte con acceso sin visa a unos 145 países (Henley Passport Index) y un estatus jurídico más estable que la residencia.',
    body=lambda l: f'''
    <p>La naturalización no es una alternativa a la residencia, sino su continuación lógica para
    quienes quieren un estatus más estable que la Residencia Permanente y están dispuestos a
    esperar algunos años más.</p>

    <h2>Cuándo es posible</h2>
    <p>La naturalización es posible recién 3 años después de obtener la
    <a href="{l['terminologiya']}#residencia-permanente">Residencia Permanente</a> (art. 148 de la
    Constitución de Paraguay) — es decir, el plazo real completo desde la mudanza hasta el
    pasaporte es de 7 a 8 años, no «un año» como a veces se promete en el mercado.</p>

    <h2>El camino desde la mudanza hasta el pasaporte</h2>
    <div class="diagram">
      {_CITIZENSHIP_SVG['es']}
      <p class="diagram-caption">Cronología basada en rangos ya publicados: Temporal (hasta 2
      años) → Permanente (normalmente 2–5 años) → espera obligatoria de 3 años antes de solicitar
      la naturalización.</p>
    </div>

    <h2>Quién tramita el caso</h2>
    <p>El trámite de naturalización lo lleva la Corte Suprema
    (<a href="{l['terminologiya']}#corte-suprema">Corte Suprema de Justicia</a>), no la DNM; el
    procedimiento requiere comparecencia personal y el acompañamiento de un abogado — es un
    proceso aparte con sus propios plazos, no una continuación automática del trámite de
    residencia.</p>

    <h2>Documentos</h2>
    <p>La lista completa de documentos para la naturalización está en la página
    <a href="{l['dok-grazhdanstvo']}">«Ciudadanía: documentos»</a> de la sección «Documentos».</p>

    <h2>Vea también</h2>
    <ul>
      <li><a href="{l['usluga-residencia']}">«Residencia»</a> — la etapa previa obligatoria</li>
      <li><a href="{l['riski']}">«Riesgos y dificultades»</a> — por qué «ciudadanía en un año» no
      corresponde a la realidad</li>
      <li><a href="{l['keisy']}">«Casos y testimonios»</a> — historias típicas de clientes</li>
    </ul>
    ''',
    final_h2="¿Piensa llegar hasta la ciudadanía?",
    final_p="Evaluamos los plazos según su situación concreta y verificamos los documentos antes de presentarlos ante la Corte Suprema.",
    final_cta="Solicitar una consulta",
),
"en": dict(
    title="Paraguayan Citizenship: Timeline, Documents, the Supreme Court | Grund Paraguay",
    description="Naturalization in Paraguay: 3 years after Residencia Permanente (Art. 148 of the Constitution), the case is handled by the Supreme Court, realistic full timeline from moving to a passport — 7–8 years.",
    h1="Paraguayan Citizenship",
    lead="Paraguayan citizenship grants a passport with visa-free access to roughly 145 countries (Henley Passport Index) and a more stable legal status than residency.",
    body=lambda l: f'''
    <p>Naturalization isn't an alternative to residency — it's its logical continuation for those
    who want a more stable status than Residencia Permanente and are willing to wait a few more
    years for it.</p>

    <h2>When it becomes possible</h2>
    <p>Naturalization is only possible 3 years after getting
    <a href="{l['terminologiya']}#residencia-permanente">Residencia Permanente</a> (Art. 148 of
    Paraguay's Constitution) — meaning the realistic full timeline from moving to holding a
    passport works out to 7–8 years, not "a year" as some agencies promise.</p>

    <h2>The path from moving to a passport</h2>
    <div class="diagram">
      {_CITIZENSHIP_SVG['en']}
      <p class="diagram-caption">A timeline built from already-published ranges: Temporal (up to
      2 years) → Permanente (usually 2–5 years) → a mandatory 3-year wait before applying for
      naturalization.</p>
    </div>

    <h2>Who handles the case</h2>
    <p>The naturalization case is handled by the Supreme Court
    (<a href="{l['terminologiya']}#corte-suprema">Corte Suprema de Justicia</a>), not the
    migration service; the procedure requires appearing in person and legal representation — it's
    a separate process with its own timeline, not an automatic continuation of the residency
    case.</p>

    <h2>Documents</h2>
    <p>The full document list for naturalization is on the
    <a href="{l['dok-grazhdanstvo']}">"Citizenship: Documents"</a> page in the "Documents"
    section.</p>

    <h2>See also</h2>
    <ul>
      <li><a href="{l['usluga-residencia']}">"Residency"</a> — the mandatory earlier stage</li>
      <li><a href="{l['riski']}">"Risks & Difficulties"</a> — why "citizenship in a year" isn't
      realistic</li>
      <li><a href="{l['keisy']}">"Case Studies"</a> — typical client stories</li>
    </ul>
    ''',
    final_h2="Planning to go all the way to citizenship?",
    final_p="We'll estimate the timeline for your specific situation and check your documents before filing with the Supreme Court.",
    final_cta="Request a consultation",
),
"de": dict(
    title="Paraguayische Staatsbürgerschaft: Fristen, Dokumente, Oberster Gerichtshof | Grund Paraguay",
    description="Einbürgerung in Paraguay: 3 Jahre nach der Residencia Permanente (Art. 148 der Verfassung), das Verfahren führt der Oberste Gerichtshof, realistische Gesamtfrist vom Umzug bis zum Pass — 7–8 Jahre.",
    h1="Paraguayische Staatsbürgerschaft",
    lead="Die paraguayische Staatsbürgerschaft verleiht einen Reisepass mit visumfreiem Zugang zu rund 145 Ländern (Henley Passport Index) und einen stabileren Rechtsstatus als der Aufenthaltstitel.",
    body=lambda l: f'''
    <p>Die Einbürgerung ist keine Alternative zum Aufenthaltstitel, sondern dessen logische
    Fortsetzung für alle, die einen stabileren Status als die Residencia Permanente wollen und
    bereit sind, dafür noch einige Jahre zu warten.</p>

    <h2>Wann sie möglich wird</h2>
    <p>Die Einbürgerung ist erst 3 Jahre nach Erhalt der
    <a href="{l['terminologiya']}#residencia-permanente">Residencia Permanente</a> möglich (Art.
    148 der paraguayischen Verfassung) — das heißt, die realistische Gesamtfrist vom Umzug bis zum
    Pass beträgt 7–8 Jahre, nicht „ein Jahr", wie manchmal auf dem Markt versprochen wird.</p>

    <h2>Der Weg vom Umzug zum Pass</h2>
    <div class="diagram">
      {_CITIZENSHIP_SVG['de']}
      <p class="diagram-caption">Eine Zeitachse aus bereits veröffentlichten Spannen: Temporal
      (bis zu 2 Jahre) → Permanente (meist 2–5 Jahre) → verpflichtende Wartezeit von 3 Jahren vor
      dem Einbürgerungsantrag.</p>
    </div>

    <h2>Wer das Verfahren führt</h2>
    <p>Das Einbürgerungsverfahren führt nicht die Migrationsbehörde, sondern der Oberste
    Gerichtshof (<a href="{l['terminologiya']}#corte-suprema">Corte Suprema de Justicia</a>); das
    Verfahren erfordert persönliches Erscheinen und anwaltliche Begleitung — ein eigenständiger
    Prozess mit eigenen Fristen, keine automatische Fortsetzung des Aufenthaltsverfahrens.</p>

    <h2>Dokumente</h2>
    <p>Die vollständige Dokumentenliste für die Einbürgerung steht auf der Seite
    <a href="{l['dok-grazhdanstvo']}">„Staatsbürgerschaft: Dokumente"</a> im Bereich „Dokumente".</p>

    <h2>Siehe auch</h2>
    <ul>
      <li><a href="{l['usluga-residencia']}">„Aufenthaltstitel"</a> — die verpflichtende
      vorherige Etappe</li>
      <li><a href="{l['riski']}">„Risiken und Schwierigkeiten"</a> — warum „Staatsbürgerschaft in
      einem Jahr" nicht der Realität entspricht</li>
      <li><a href="{l['keisy']}">„Fallstudien"</a> — typische Mandantengeschichten</li>
    </ul>
    ''',
    final_h2="Planen Sie, bis zur Staatsbürgerschaft zu gehen?",
    final_p="Wir schätzen die Fristen speziell für Ihre Situation ein und prüfen Ihre Dokumente vor der Einreichung beim Obersten Gerichtshof.",
    final_cta="Beratung anfragen",
),
},
"usluga-realestate": {
"ru": dict(
    title="Проверка и покупка недвижимости в Парагвае: due diligence | Grund Paraguay",
    description="Due diligence по конкретному объекту недвижимости в Парагвае: цепочка документов, риск lote agrario, escribano, удалённая доверенность и ежегодный Impuesto Inmobiliario.",
    h1="Проверка и покупка недвижимости",
    lead='Проверка и покупка недвижимости — услуга due diligence по конкретному объекту, которая защищает от переплаты и от скрытых рисков сделки. Мы не ведём каталог объектов — вместо этого проверяем конкретную сделку.',
    body=lambda l: f'''
    <p>Итог услуги — не список «хороших предложений», а отчёт по конкретному объекту: можно ли
    его безопасно покупать и на что обратить внимание до подписания.</p>

    <h2>Что мы проверяем</h2>
    <ul>
      <li><strong>Цепочку правоустанавливающих документов</strong> — кто и на каком основании
      владел объектом до продавца.</li>
      <li><strong>Статус земли</strong> — в частности, риск отнесения к категории «lote agrario»
      (неотчуждаемые земли аграрной реформы <a href="{l['terminologiya']}#indert">INDERT</a>),
      которые нельзя свободно продать иностранцу.</li>
      <li><strong>Работу через независимого нотариуса</strong>
      (<a href="{l['terminologiya']}#escribano">escribano</a>) — а не через того, кого предложил
      продавец.</li>
      <li><strong>Удалённую доверенность</strong> — для тех, кто ещё не переехал и не может
      присутствовать на сделке лично.</li>
    </ul>

    <h2>Расход, о котором часто забывают: ежегодный налог на владение</h2>
    <div class="callout"><span class="callout-label">Impuesto Inmobiliario</span>Ежегодный налог
    на недвижимость — 1% от фискальной (кадастровой, не рыночной) стоимости объекта, которая
    пересчитывается каждый год по ИПЦ. На 2026 год фискальная стоимость проиндексирована на 4,1%.
    Срок уплаты зависит от муниципалитета (для Асунсьона — до 31 марта). Это расход на владение, а
    не только на саму сделку — его стоит закладывать в бюджет заранее, а не узнавать о нём
    постфактум.</div>

    <h2>Разовые расходы на сделку</h2>
    <p>Помимо ежегодного налога на владение, при самой покупке есть отдельные разовые издержки —
    гонорар нотариуса, регистрационный сбор, муниципальный налог на передачу и НДС на передачу,
    если продавец — плательщик НДС. Подробная структура этих расходов — на странице
    <a href="{l['stoimost']}">«Стоимость и тарифы»</a>.</p>

    <h2>Стоимость проверки</h2>
    <p>Цена due diligence фиксированная за отчёт — независимо от того, состоится сделка или нет;
    точная сумма — на странице <a href="{l['stoimost']}">«Стоимость и тарифы»</a>.</p>

    <h2>Смотрите также</h2>
    <ul>
      <li><a href="{l['stoimost']}">«Стоимость и тарифы»</a> — разовые расходы на сделку и
      стоимость проверки</li>
      <li><a href="{l['terminologiya']}#escribano">«Терминология»: escribano</a> — роль
      независимого нотариуса в сделке</li>
      <li><a href="{l['keisy']}">«Кейсы и отзывы»</a> — типичные истории клиентов</li>
    </ul>
    ''',
    final_h2="Рассматриваете конкретный объект?",
    final_p="Проверим цепочку документов, статус земли и структуру сделки до того, как вы что-то подпишете.",
    final_cta="Оставить заявку на консультацию",
),
"es": dict(
    title="Verificación y compra de inmuebles en Paraguay: due diligence | Grund Paraguay",
    description="Due diligence sobre un inmueble concreto en Paraguay: cadena de títulos, riesgo de lote agrario, escribano, poder a distancia e Impuesto Inmobiliario anual.",
    h1="Verificación y compra de inmuebles",
    lead='La verificación y compra de inmuebles es un servicio de due diligence sobre una propiedad concreta, que protege de sobrepagar o de riesgos ocultos en la operación. No manejamos un catálogo de propiedades — en cambio, verificamos la operación concreta.',
    body=lambda l: f'''
    <p>El resultado del servicio no es una lista de «buenas ofertas», sino un informe sobre un
    inmueble concreto: si se puede comprar con seguridad y qué revisar antes de firmar.</p>

    <h2>Qué verificamos</h2>
    <ul>
      <li><strong>La cadena de títulos de propiedad</strong> — quién fue propietario y con qué
      base, antes del vendedor.</li>
      <li><strong>El estatus de la tierra</strong> — en particular, el riesgo de que se trate de
      un «lote agrario» (tierras inalienables de la reforma agraria del
      <a href="{l['terminologiya']}#indert">INDERT</a>), que no se pueden vender libremente a un
      extranjero.</li>
      <li><strong>El trabajo a través de un escribano independiente</strong>
      (<a href="{l['terminologiya']}#escribano">escribano</a>) — no del que proponga el
      vendedor.</li>
      <li><strong>El poder a distancia</strong> — para quienes aún no se han mudado y no pueden
      estar presentes en la operación.</li>
    </ul>

    <h2>Un gasto que suele olvidarse: el impuesto anual por tener la propiedad</h2>
    <div class="callout"><span class="callout-label">Impuesto Inmobiliario</span>Impuesto anual
    sobre bienes raíces — 1% del valor fiscal (catastral, no de mercado) del inmueble, que se
    reajusta cada año según el IPC. Para 2026, el valor fiscal se indexó en 4,1%. El plazo de pago
    depende del municipio (en Asunción, hasta el 31 de marzo). Es un gasto por tener la propiedad,
    no solo por la operación — conviene preverlo en el presupuesto de antemano, no descubrirlo
    después.</div>

    <h2>Gastos únicos de la operación</h2>
    <p>Además del impuesto anual por tener la propiedad, la compra en sí implica gastos únicos
    aparte — honorarios del escribano, tasa de registro, impuesto municipal a la transferencia e
    IVA sobre la transferencia si el vendedor es contribuyente de IVA. La estructura detallada de
    estos gastos está en la página <a href="{l['stoimost']}">«Costos y tarifas»</a>.</p>

    <h2>Costo de la verificación</h2>
    <p>El precio del due diligence es fijo por informe — sin importar si la operación se concreta
    o no; el monto exacto está en la página <a href="{l['stoimost']}">«Costos y tarifas»</a>.</p>

    <h2>Vea también</h2>
    <ul>
      <li><a href="{l['stoimost']}">«Costos y tarifas»</a> — gastos únicos de la operación y
      costo de la verificación</li>
      <li><a href="{l['terminologiya']}#escribano">«Terminología»: escribano</a> — el papel del
      notario independiente en la operación</li>
      <li><a href="{l['keisy']}">«Casos y testimonios»</a> — historias típicas de clientes</li>
    </ul>
    ''',
    final_h2="¿Está evaluando un inmueble concreto?",
    final_p="Verificamos la cadena de títulos, el estatus de la tierra y la estructura de la operación antes de que firme nada.",
    final_cta="Solicitar una consulta",
),
"en": dict(
    title="Real Estate Verification & Purchase in Paraguay: Due Diligence | Grund Paraguay",
    description="Due diligence on a specific property in Paraguay: chain of title, lote agrario risk, escribano, remote power of attorney, and the annual Impuesto Inmobiliario.",
    h1="Real Estate Verification & Purchase",
    lead="Real estate verification & purchase is a due-diligence service on a specific property, protecting you from overpaying or from hidden risks in the deal. We don't run a listings catalog — instead we verify the specific deal.",
    body=lambda l: f'''
    <p>The outcome isn't a list of "good deals" — it's a report on one specific property: whether
    it's safe to buy and what to check before you sign.</p>

    <h2>What we check</h2>
    <ul>
      <li><strong>The chain of title documents</strong> — who owned the property and on what
      basis, before the seller.</li>
      <li><strong>The land's status</strong> — in particular, the risk of it being classed as
      "lote agrario" (inalienable land reform land under
      <a href="{l['terminologiya']}#indert">INDERT</a>), which can't be freely sold to a
      foreigner.</li>
      <li><strong>Working through an independent notary</strong>
      (<a href="{l['terminologiya']}#escribano">escribano</a>) — not whoever the seller
      suggests.</li>
      <li><strong>A remote power of attorney</strong> — for those who haven't moved yet and can't
      attend the closing in person.</li>
    </ul>

    <h2>A cost that's easy to overlook: the annual ownership tax</h2>
    <div class="callout"><span class="callout-label">Impuesto Inmobiliario</span>An annual
    property tax — 1% of the fiscal (assessed, not market) value of the property, which is
    re-indexed every year to inflation. For 2026, the fiscal value was indexed up by 4.1%. The
    payment deadline depends on the municipality (in Asunción, by March 31). This is an ongoing
    ownership cost, not just a transaction cost — worth budgeting for upfront, not discovering
    later.</div>

    <h2>One-off transaction costs</h2>
    <p>Beyond the annual ownership tax, the purchase itself carries separate one-off costs —
    notary fees, a registration fee, a municipal transfer tax, and VAT on the transfer if the
    seller is a VAT payer. The detailed cost breakdown is on the
    <a href="{l['stoimost']}">"Pricing"</a> page.</p>

    <h2>Cost of the verification</h2>
    <p>The due-diligence fee is fixed per report, regardless of whether the deal closes; the exact
    amount is on the <a href="{l['stoimost']}">"Pricing"</a> page.</p>

    <h2>See also</h2>
    <ul>
      <li><a href="{l['stoimost']}">"Pricing"</a> — one-off transaction costs and the
      verification fee</li>
      <li><a href="{l['terminologiya']}#escribano">"Terminology": escribano</a> — the independent
      notary's role in the deal</li>
      <li><a href="{l['keisy']}">"Case Studies"</a> — typical client stories</li>
    </ul>
    ''',
    final_h2="Considering a specific property?",
    final_p="We'll check the chain of title, the land's status, and the deal structure before you sign anything.",
    final_cta="Request a consultation",
),
"de": dict(
    title="Prüfung und Kauf von Immobilien in Paraguay: Due Diligence | Grund Paraguay",
    description="Due Diligence für ein konkretes Objekt in Paraguay: Eigentumskette, Risiko lote agrario, escribano, Fernvollmacht und die jährliche Impuesto Inmobiliario.",
    h1="Prüfung und Kauf von Immobilien",
    lead="Prüfung und Kauf von Immobilien ist eine Due-Diligence-Leistung für ein konkretes Objekt, die vor Überzahlung und vor verdeckten Risiken des Geschäfts schützt. Wir führen keinen Objektkatalog — stattdessen prüfen wir das konkrete Geschäft.",
    body=lambda l: f'''
    <p>Das Ergebnis ist keine Liste „guter Angebote", sondern ein Bericht zu einem konkreten
    Objekt: ob es sich sicher kaufen lässt und worauf vor der Unterschrift zu achten ist.</p>

    <h2>Was wir prüfen</h2>
    <ul>
      <li><strong>Die Kette der Eigentumsdokumente</strong> — wer das Objekt vor dem Verkäufer
      besaß und auf welcher Grundlage.</li>
      <li><strong>Den Status des Grundstücks</strong> — insbesondere das Risiko einer Einstufung
      als „lote agrario" (unveräußerliches Agrarreformland des
      <a href="{l['terminologiya']}#indert">INDERT</a>), das nicht frei an Ausländer verkauft
      werden darf.</li>
      <li><strong>Die Abwicklung über einen unabhängigen Notar</strong>
      (<a href="{l['terminologiya']}#escribano">escribano</a>) — nicht über den vom Verkäufer
      vorgeschlagenen.</li>
      <li><strong>Die Fernvollmacht</strong> — für alle, die noch nicht umgezogen sind und beim
      Abschluss nicht persönlich anwesend sein können.</li>
    </ul>

    <h2>Ein leicht übersehener Posten: die jährliche Eigentumssteuer</h2>
    <div class="callout"><span class="callout-label">Impuesto Inmobiliario</span>Eine jährliche
    Grundsteuer — 1% des steuerlichen (nicht des Markt-)Werts des Objekts, der jedes Jahr an die
    Inflation angepasst wird. Für 2026 wurde der steuerliche Wert um 4,1% angehoben. Die
    Zahlungsfrist hängt von der Gemeinde ab (in Asunción bis zum 31. März). Das ist eine laufende
    Kostenposition durch den Besitz, nicht nur durch die Transaktion — sie gehört von Anfang an ins
    Budget, nicht als nachträgliche Überraschung.</div>

    <h2>Einmalige Transaktionskosten</h2>
    <p>Neben der jährlichen Eigentumssteuer fallen beim Kauf selbst separate einmalige Kosten an —
    Notargebühren, eine Registrierungsgebühr, eine kommunale Übertragungssteuer und Mehrwertsteuer
    auf die Übertragung, falls der Verkäufer mehrwertsteuerpflichtig ist. Die detaillierte
    Kostenaufstellung steht auf der Seite <a href="{l['stoimost']}">„Preise"</a>.</p>

    <h2>Kosten der Prüfung</h2>
    <p>Der Preis der Due Diligence ist ein Festpreis pro Bericht — unabhängig davon, ob das
    Geschäft zustande kommt; der genaue Betrag steht auf der Seite
    <a href="{l['stoimost']}">„Preise"</a>.</p>

    <h2>Siehe auch</h2>
    <ul>
      <li><a href="{l['stoimost']}">„Preise"</a> — einmalige Transaktionskosten und die Kosten
      der Prüfung</li>
      <li><a href="{l['terminologiya']}#escribano">„Terminologie": escribano</a> — die Rolle des
      unabhängigen Notars im Geschäft</li>
      <li><a href="{l['keisy']}">„Fallstudien"</a> — typische Mandantengeschichten</li>
    </ul>
    ''',
    final_h2="Haben Sie ein konkretes Objekt im Blick?",
    final_p="Wir prüfen die Eigentumskette, den Status des Grundstücks und die Struktur des Geschäfts, bevor Sie etwas unterschreiben.",
    final_cta="Beratung anfragen",
),
},
"usluga-company": {
"ru": dict(
    title="Открытие компании в Парагвае: EAS, S.A., S.R.L. | Grund Paraguay",
    description="Регистрация юрлица в Парагвае: EAS через SUACE до 72 рабочих часов, S.A. 8–30 дней, S.R.L. 15–30 дней, требование Cédula для представителя EAS.",
    h1="Открытие компании (EAS/SRL)",
    lead='Открытие компании — регистрация юридического лица в Парагвае, которое даёт возможность вести бизнес легально: выставлять счета, нанимать сотрудников и открывать банковский счёт на компанию.',
    body=lambda l: f'''
    <p>Мы предлагаем открытие компании в комплекте с резидентурой, а не как отдельный премиум-
    продукт: для большинства клиентов это шаги одного проекта, а не два независимых заказа.</p>

    <h2>Три формы, три срока регистрации</h2>
    <div class="diagram">
      {_COMPANY_SVG['ru']}
      <p class="diagram-caption">Столбчатая диаграмма сроков регистрации: EAS через SUACE — около
      72 рабочих часов по типовому уставу, S.A. — 8–30 рабочих дней, S.R.L. — 15–30 рабочих
      дней.</p>
    </div>
    <p><a href="{l['terminologiya']}#eas">EAS</a> (упрощённое акционерное общество) —
    самая быстрая форма, но с одним жёстким условием: законный представитель обязательно должен
    иметь парагвайское гражданство или парагвайскую <a href="{l['terminologiya']}#cedula">Cédula</a>
    «без исключений». Если резидентства пока нет, эту роль на старте берёт на себя представитель
    по доверенности. <a href="{l['terminologiya']}#sa">S.A.</a> и
    <a href="{l['terminologiya']}#srl">S.R.L.</a> регистрируются дольше, но без этого требования к
    представителю.</p>

    <h2>Стоимость</h2>
    <p>Расходы на регистрацию и полная стоимость услуги в комплекте с резидентурой — на странице
    <a href="{l['stoimost']}">«Стоимость и тарифы»</a>.</p>

    <h2>После регистрации: RUC и отчётность</h2>
    <p>У зарегистрированной компании — та же логика, что и у физлица после получения резиденции:
    нужен RUC и регулярная отчётность, чтобы статус компании оставался в силе. Это отдельная
    услуга — см. <a href="{l['usluga-compliance']}">«Сопровождение и комплаенс»</a>.</p>

    <h2>Смотрите также</h2>
    <ul>
      <li><a href="{l['usluga-residencia']}">«Резидентура (ВНЖ)»</a> — обычно идёт в комплекте с
      открытием компании</li>
      <li><a href="{l['usluga-compliance']}">«Сопровождение и комплаенс»</a> — что нужно после
      регистрации</li>
      <li><a href="{l['usluga-relocation']}">«Релокация организаций»</a> — если переезжает не один
      учредитель, а вся команда</li>
    </ul>
    ''',
    final_h2="Готовы зарегистрировать компанию?",
    final_p="Поможем выбрать форму под вашу задачу и оценим реальный срок регистрации.",
    final_cta="Оставить заявку на консультацию",
),
"es": dict(
    title="Apertura de empresa en Paraguay: EAS, S.A., S.R.L. | Grund Paraguay",
    description="Constitución de una persona jurídica en Paraguay: EAS por SUACE hasta 72 horas hábiles, S.A. 8–30 días, S.R.L. 15–30 días, requisito de Cédula para el representante de la EAS.",
    h1="Apertura de empresa (EAS/SRL)",
    lead='La apertura de empresa es la inscripción de una persona jurídica en Paraguay, que permite operar legalmente: facturar, contratar personal y abrir una cuenta bancaria a nombre de la empresa.',
    body=lambda l: f'''
    <p>Ofrecemos la apertura de empresa junto con la residencia, no como un producto premium
    aparte: para la mayoría de los clientes son pasos de un mismo proyecto, no dos encargos
    independientes.</p>

    <h2>Tres formas, tres plazos de registro</h2>
    <div class="diagram">
      {_COMPANY_SVG['es']}
      <p class="diagram-caption">Gráfico de barras de los plazos de registro: EAS por SUACE —
      unas 72 horas hábiles con estatuto tipo, S.A. — 8–30 días hábiles, S.R.L. — 15–30 días
      hábiles.</p>
    </div>
    <p>La <a href="{l['terminologiya']}#eas">EAS</a> (empresa por acciones simplificada) es la
    forma más rápida, pero con una condición estricta: el representante legal debe tener
    obligatoriamente ciudadanía paraguaya o <a href="{l['terminologiya']}#cedula">Cédula</a>
    paraguaya «sin excepciones». Si aún no hay residencia, esta función la asume al inicio un
    apoderado. La <a href="{l['terminologiya']}#sa">S.A.</a> y la
    <a href="{l['terminologiya']}#srl">S.R.L.</a> se registran más lento, pero sin ese requisito
    para el representante.</p>

    <h2>Costo</h2>
    <p>Los gastos de registro y el costo completo del servicio junto con la residencia están en la
    página <a href="{l['stoimost']}">«Costos y tarifas»</a>.</p>

    <h2>Después del registro: RUC y declaraciones</h2>
    <p>Una empresa registrada sigue la misma lógica que una persona física tras obtener la
    residencia: necesita un RUC y declaraciones regulares para que su estatus siga vigente. Es un
    servicio aparte — ver <a href="{l['usluga-compliance']}">«Acompañamiento y cumplimiento»</a>.</p>

    <h2>Vea también</h2>
    <ul>
      <li><a href="{l['usluga-residencia']}">«Residencia»</a> — normalmente va junto con la
      apertura de la empresa</li>
      <li><a href="{l['usluga-compliance']}">«Acompañamiento y cumplimiento»</a> — qué se necesita
      después del registro</li>
      <li><a href="{l['usluga-relocation']}">«Relocalización de empresas»</a> — si no se muda un
      solo fundador, sino todo el equipo</li>
    </ul>
    ''',
    final_h2="¿Listo para registrar su empresa?",
    final_p="Le ayudamos a elegir la forma según su objetivo y evaluamos el plazo real de registro.",
    final_cta="Solicitar una consulta",
),
"en": dict(
    title="Company Formation in Paraguay: EAS, S.A., S.R.L. | Grund Paraguay",
    description="Registering a legal entity in Paraguay: EAS via SUACE in up to 72 business hours, S.A. 8–30 days, S.R.L. 15–30 days, the Cédula requirement for an EAS representative.",
    h1="Company Formation (EAS/SRL)",
    lead="Company formation is registering a legal entity in Paraguay, which lets you do business legally: issue invoices, hire staff, and open a bank account in the company's name.",
    body=lambda l: f'''
    <p>We offer company formation bundled with residency, not as a separate premium product — for
    most clients these are steps in one project, not two independent orders.</p>

    <h2>Three forms, three registration timelines</h2>
    <div class="diagram">
      {_COMPANY_SVG['en']}
      <p class="diagram-caption">Bar chart of registration timelines: EAS via SUACE — about 72
      business hours with a standard charter, S.A. — 8–30 business days, S.R.L. — 15–30 business
      days.</p>
    </div>
    <p>An <a href="{l['terminologiya']}#eas">EAS</a> (simplified joint-stock company) is the
    fastest form, but with one strict condition: the legal representative must hold Paraguayan
    citizenship or a Paraguayan <a href="{l['terminologiya']}#cedula">Cédula</a> "with no
    exceptions." If you don't have residency yet, a proxy representative takes on this role at
    the start. An <a href="{l['terminologiya']}#sa">S.A.</a> and an
    <a href="{l['terminologiya']}#srl">S.R.L.</a> take longer to register, but without that
    requirement for the representative.</p>

    <h2>Cost</h2>
    <p>Registration costs and the full price of the service bundled with residency are on the
    <a href="{l['stoimost']}">"Pricing"</a> page.</p>

    <h2>After registration: RUC and filings</h2>
    <p>A registered company follows the same logic as an individual after getting residency: it
    needs a RUC and regular filings to keep its status valid. This is a separate service — see
    <a href="{l['usluga-compliance']}">"Ongoing Compliance"</a>.</p>

    <h2>See also</h2>
    <ul>
      <li><a href="{l['usluga-residencia']}">"Residency"</a> — usually bundled with company
      formation</li>
      <li><a href="{l['usluga-compliance']}">"Ongoing Compliance"</a> — what's needed after
      registration</li>
      <li><a href="{l['usluga-relocation']}">"Business Relocation"</a> — for when it's a whole
      team moving, not just one founder</li>
    </ul>
    ''',
    final_h2="Ready to register your company?",
    final_p="We'll help you choose the right form for your goal and give you a realistic registration timeline.",
    final_cta="Request a consultation",
),
"de": dict(
    title="Unternehmensgründung in Paraguay: EAS, S.A., S.R.L. | Grund Paraguay",
    description="Eintragung einer juristischen Person in Paraguay: EAS über SUACE bis zu 72 Werkstunden, S.A. 8–30 Tage, S.R.L. 15–30 Tage, Cédula-Pflicht für den EAS-Vertreter.",
    h1="Unternehmensgründung (EAS/SRL)",
    lead="Die Unternehmensgründung ist die Eintragung einer juristischen Person in Paraguay, die es ermöglicht, legal Geschäfte zu tätigen: Rechnungen zu stellen, Personal einzustellen und ein Firmenkonto zu eröffnen.",
    body=lambda l: f'''
    <p>Wir bieten die Unternehmensgründung im Paket mit dem Aufenthaltstitel an, nicht als
    separates Premiumprodukt — für die meisten Mandanten sind das Schritte eines Projekts, keine
    zwei unabhängigen Aufträge.</p>

    <h2>Drei Formen, drei Registrierungsfristen</h2>
    <div class="diagram">
      {_COMPANY_SVG['de']}
      <p class="diagram-caption">Balkendiagramm der Registrierungsfristen: EAS über SUACE — etwa
      72 Werkstunden bei Standardsatzung, S.A. — 8–30 Werktage, S.R.L. — 15–30 Werktage.</p>
    </div>
    <p>Die <a href="{l['terminologiya']}#eas">EAS</a> (vereinfachte Aktiengesellschaft) ist die
    schnellste Form, aber mit einer strengen Bedingung: Der gesetzliche Vertreter muss zwingend
    die paraguayische Staatsbürgerschaft oder eine paraguayische
    <a href="{l['terminologiya']}#cedula">Cédula</a> besitzen — „ohne Ausnahmen". Liegt noch kein
    Aufenthaltstitel vor, übernimmt zu Beginn ein Bevollmächtigter diese Rolle. Die
    <a href="{l['terminologiya']}#sa">S.A.</a> und die
    <a href="{l['terminologiya']}#srl">S.R.L.</a> werden langsamer registriert, aber ohne diese
    Anforderung an den Vertreter.</p>

    <h2>Kosten</h2>
    <p>Die Registrierungskosten und der vollständige Preis der Leistung im Paket mit dem
    Aufenthaltstitel stehen auf der Seite <a href="{l['stoimost']}">„Preise"</a>.</p>

    <h2>Nach der Registrierung: RUC und Meldungen</h2>
    <p>Für ein registriertes Unternehmen gilt dieselbe Logik wie für eine Privatperson nach Erhalt
    des Aufenthaltstitels: Es braucht eine RUC und regelmäßige Meldungen, damit sein Status gültig
    bleibt. Das ist eine eigene Leistung — siehe
    <a href="{l['usluga-compliance']}">„Begleitung und Compliance"</a>.</p>

    <h2>Siehe auch</h2>
    <ul>
      <li><a href="{l['usluga-residencia']}">„Aufenthaltstitel"</a> — meist im Paket mit der
      Unternehmensgründung</li>
      <li><a href="{l['usluga-compliance']}">„Begleitung und Compliance"</a> — was nach der
      Registrierung nötig ist</li>
      <li><a href="{l['usluga-relocation']}">„Unternehmensrelokation"</a> — wenn nicht nur ein
      Gründer umzieht, sondern das ganze Team</li>
    </ul>
    ''',
    final_h2="Bereit, Ihr Unternehmen zu registrieren?",
    final_p="Wir helfen bei der Wahl der passenden Form und schätzen die realistische Registrierungsfrist ein.",
    final_cta="Beratung anfragen",
),
},
"usluga-business": {
"ru": dict(
    title="Покупка и продажа бизнеса в Парагвае | Grund Paraguay",
    description="Сопровождение сделки купли-продажи готового бизнеса в Парагвае: независимая оценка, проверка предложения, сопровождение передачи — на непрозрачном рынке без стандартной статистики.",
    h1="Покупка и продажа бизнеса",
    lead='Покупка и продажа бизнеса — сопровождение сделки для тех, кто хочет войти в дело через готовую компанию или выйти из своей, а не запускать регистрацию с нуля.',
    body=lambda l: f'''
    <h2>Рынок, где нет стандартной статистики</h2>
    <p>Рынок сделок купли-продажи бизнеса в Парагвае небольшой и непрозрачный: крупные
    международные трекеры сделок (например, TTR Data) вообще не включают Парагвай в число
    охваченных стран — в отличие от соседних Аргентины и Уругвая. Это означает, что стандартной
    статистики по мультипликаторам оценки и объёму сделок просто не существует, а проверенных
    предложений на открытом рынке немного.</p>

    <h2>Как мы работаем без готового бенчмарка</h2>
    <p>Раз опереться на статистику рынка нельзя, каждую сделку мы сопровождаем индивидуально —
    по трём этапам:</p>
    <ul>
      <li><strong>Независимая оценка</strong> — по фактическим показателям конкретной компании,
      а не по рыночному мультипликатору, которого для Парагвая просто нет.</li>
      <li><strong>Проверка предложения</strong> — due diligence по документам, обязательствам и
      реальному состоянию дел компании, а не только по тому, что говорит продавец.</li>
      <li><strong>Сопровождение передачи</strong> — юридическое оформление перехода бизнеса от
      одного владельца к другому.</li>
    </ul>

    <h2>Смотрите также</h2>
    <ul>
      <li><a href="{l['usluga-company']}">«Открытие компании (EAS/SRL)»</a> — если проще и
      быстрее зарегистрировать новую компанию, чем покупать готовую</li>
      <li><a href="{l['keisy']}">«Кейсы и отзывы»</a> — типичные истории клиентов</li>
      <li><a href="{l['stoimost']}">«Стоимость и тарифы»</a> — как оцениваются индивидуальные
      услуги без фиксированного прайса</li>
    </ul>
    ''',
    final_h2="Рассматриваете сделку с готовым бизнесом?",
    final_p="Оценим предложение независимо и проверим его до того, как вы примете решение.",
    final_cta="Оставить заявку на консультацию",
),
"es": dict(
    title="Compra y venta de empresas en Paraguay | Grund Paraguay",
    description="Acompañamiento de la compraventa de una empresa en marcha en Paraguay: valuación independiente, verificación de la oferta, acompañamiento en la transferencia — en un mercado opaco sin estadística estándar.",
    h1="Compra y venta de empresas",
    lead='La compra y venta de empresas es el acompañamiento de una operación para quienes prefieren entrar a un negocio ya en marcha o salir del propio, en lugar de registrar uno desde cero.',
    body=lambda l: f'''
    <h2>Un mercado sin estadística estándar</h2>
    <p>El mercado de compraventa de empresas en Paraguay es pequeño y poco transparente: los
    grandes rastreadores internacionales de operaciones (por ejemplo, TTR Data) directamente no
    incluyen a Paraguay entre los países cubiertos, a diferencia de la vecina Argentina y Uruguay.
    Esto significa que no existe estadística estándar sobre múltiplos de valuación ni volumen de
    operaciones, y hay pocas ofertas verificadas en el mercado abierto.</p>

    <h2>Cómo trabajamos sin un benchmark ya disponible</h2>
    <p>Como no se puede apoyar en estadísticas de mercado, acompañamos cada operación de forma
    individual — en tres etapas:</p>
    <ul>
      <li><strong>Valuación independiente</strong> — según los indicadores reales de la empresa
      concreta, no según un múltiplo de mercado que simplemente no existe para Paraguay.</li>
      <li><strong>Verificación de la oferta</strong> — due diligence sobre documentos,
      obligaciones y el estado real de la empresa, no solo lo que dice el vendedor.</li>
      <li><strong>Acompañamiento en la transferencia</strong> — la formalización jurídica del
      traspaso del negocio de un propietario a otro.</li>
    </ul>

    <h2>Vea también</h2>
    <ul>
      <li><a href="{l['usluga-company']}">«Apertura de empresa (EAS/SRL)»</a> — si es más simple
      y rápido registrar una empresa nueva que comprar una ya existente</li>
      <li><a href="{l['keisy']}">«Casos y testimonios»</a> — historias típicas de clientes</li>
      <li><a href="{l['stoimost']}">«Costos y tarifas»</a> — cómo se evalúan los servicios
      individuales sin un precio fijo</li>
    </ul>
    ''',
    final_h2="¿Está evaluando una operación con una empresa en marcha?",
    final_p="Evaluamos la oferta de forma independiente y la verificamos antes de que tome una decisión.",
    final_cta="Solicitar una consulta",
),
"en": dict(
    title="Buying & Selling a Business in Paraguay | Grund Paraguay",
    description="Deal support for buying or selling a running business in Paraguay: independent valuation, offer verification, handover support — in an opaque market with no standard statistics.",
    h1="Buying & Selling a Business",
    lead="Buying & selling a business is deal support for those who'd rather step into a running company or exit their own, instead of registering one from scratch.",
    body=lambda l: f'''
    <h2>A market with no standard statistics</h2>
    <p>The market for buying and selling businesses in Paraguay is small and opaque: major
    international deal trackers (e.g., TTR Data) don't cover Paraguay at all, unlike neighboring
    Argentina and Uruguay. That means there's no standard statistics on valuation multiples or
    deal volume, and few verified offers on the open market.</p>

    <h2>How we work without a ready-made benchmark</h2>
    <p>Since there's no market statistic to lean on, we support each deal individually — across
    three stages:</p>
    <ul>
      <li><strong>Independent valuation</strong> — based on the specific company's actual
      numbers, not a market multiple that simply doesn't exist for Paraguay.</li>
      <li><strong>Offer verification</strong> — due diligence on documents, liabilities, and the
      company's real state of affairs, not just what the seller says.</li>
      <li><strong>Handover support</strong> — the legal formalization of the business passing from
      one owner to another.</li>
    </ul>

    <h2>See also</h2>
    <ul>
      <li><a href="{l['usluga-company']}">"Company Formation (EAS/SRL)"</a> — if it's simpler and
      faster to register a new company than to buy an existing one</li>
      <li><a href="{l['keisy']}">"Case Studies"</a> — typical client stories</li>
      <li><a href="{l['stoimost']}">"Pricing"</a> — how individually scoped services are priced
      without a fixed rate</li>
    </ul>
    ''',
    final_h2="Considering a deal with a running business?",
    final_p="We'll value the offer independently and verify it before you make a decision.",
    final_cta="Request a consultation",
),
"de": dict(
    title="Kauf und Verkauf von Unternehmen in Paraguay | Grund Paraguay",
    description="Begleitung beim Kauf oder Verkauf eines laufenden Unternehmens in Paraguay: unabhängige Bewertung, Prüfung des Angebots, Begleitung der Übergabe — auf einem intransparenten Markt ohne Standardstatistik.",
    h1="Kauf und Verkauf von Unternehmen",
    lead="Kauf und Verkauf von Unternehmen ist die Begleitung einer Transaktion für alle, die lieber in ein laufendes Unternehmen einsteigen oder aus dem eigenen aussteigen möchten, statt eines von Grund auf neu zu registrieren.",
    body=lambda l: f'''
    <h2>Ein Markt ohne Standardstatistik</h2>
    <p>Der Markt für den Kauf und Verkauf von Unternehmen in Paraguay ist klein und wenig
    transparent: Große internationale Deal-Tracker (z. B. TTR Data) erfassen Paraguay überhaupt
    nicht — anders als die Nachbarländer Argentinien und Uruguay. Das bedeutet, dass es keine
    Standardstatistik zu Bewertungsmultiplikatoren oder Transaktionsvolumen gibt und nur wenige
    geprüfte Angebote auf dem offenen Markt existieren.</p>

    <h2>Wie wir ohne fertigen Vergleichswert arbeiten</h2>
    <p>Da sich das nicht auf Marktstatistiken stützen lässt, begleiten wir jede Transaktion
    individuell — in drei Schritten:</p>
    <ul>
      <li><strong>Unabhängige Bewertung</strong> — anhand der tatsächlichen Kennzahlen des
      konkreten Unternehmens, nicht anhand eines Marktmultiplikators, den es für Paraguay schlicht
      nicht gibt.</li>
      <li><strong>Prüfung des Angebots</strong> — Due Diligence zu Dokumenten, Verbindlichkeiten
      und der tatsächlichen Lage des Unternehmens, nicht nur zu dem, was der Verkäufer sagt.</li>
      <li><strong>Begleitung der Übergabe</strong> — die rechtliche Abwicklung des Übergangs des
      Unternehmens von einem Eigentümer zum anderen.</li>
    </ul>

    <h2>Siehe auch</h2>
    <ul>
      <li><a href="{l['usluga-company']}">„Unternehmensgründung (EAS/SRL)"</a> — falls es
      einfacher und schneller ist, ein neues Unternehmen zu registrieren, statt ein bestehendes zu
      kaufen</li>
      <li><a href="{l['keisy']}">„Fallstudien"</a> — typische Mandantengeschichten</li>
      <li><a href="{l['stoimost']}">„Preise"</a> — wie individuell zugeschnittene Leistungen ohne
      Festpreis bewertet werden</li>
    </ul>
    ''',
    final_h2="Denken Sie über ein Geschäft mit einem laufenden Unternehmen nach?",
    final_p="Wir bewerten das Angebot unabhängig und prüfen es, bevor Sie eine Entscheidung treffen.",
    final_cta="Beratung anfragen",
),
},
}


for page_id, by_lang in PAGES.items():
    for lang, t in by_lang.items():
        l = L(lang)
        body = f'''
{crumbs(lang, page_id)}
<section class="hero" style="padding-top:24px;">
  <div class="wrap"><h1>{t["h1"]}</h1>
  <p class="lead">{t["lead"].format(**l)}</p>
  </div>
</section>
<section style="padding-top:0;">
  <div class="prose">
    {t["body"](l)}
  </div>
</section>
<div class="prose">
  <div class="final-cta">
    <h2>{t["final_h2"]}</h2>
    <p>{t["final_p"]}</p>
    <a class="btn" href="{l['kontakty']}">{t["final_cta"]}</a>
  </div>
</div>
'''
        schema = {"@context": "https://schema.org", "@type": "Service", "name": t["h1"],
                  "provider": {"@type": "Organization", "name": "Fortuna Vida E.A.S."}, "areaServed": "Paraguay"}
        page(page_id, lang, t["title"], t["description"], body,
             extra_schema=[schema_crumbs(lang, page_id), schema])
