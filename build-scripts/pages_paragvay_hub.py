#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Хаб «Парагвай для переезда» — landing + 7 подстраниц.

11.08.2026: собран как RU-only раздел (решение заказчика «Сначала только на русском»).
11.08.2026 (вечер): переведён на ES/EN/DE по прямому решению заказчика — черновой перевод,
без юридической/носительской вычитки, тем же порядком, что и остальной черновой ES/EN/DE-
контент сайта. Официальные испано-парагвайские термины (DNM, RUC, IRE, IVA, IRP, IDU, DNIT,
BCP, Marangatú, Corte Suprema de Justicia, FATF, Traductor Público matriculado и т.д.) не
переводятся ни на одном языке. Факты и уровни уверенности не менялись — только язык.
Исходник перевода — design/teksty-khab-paragvay-dlya-pereezda-es-en-de.md (проект Cowork).

Термины BCP, DNIT, IDU и (для ES/EN/DE) Numbeo/Expatistan упоминаются инлайн без ссылки на
«Терминологию» — на этих трёх языках карточек для них в глоссарии пока нет (решение по
добавлению карточек — открытый вопрос, см. design/poyasneniya-redaktora.md). На RU-версии
Numbeo/Expatistan ссылаются на #numbeo/#expatistan, т.к. там эти карточки уже есть.

Источники, уровни уверенности фактов и открытые вопросы — design/poyasneniya-redaktora.md
(раздел «Хаб «Парагвай для переезда»»), по той же схеме разделения текста и пояснений, что и
для исходных 12 страниц.
"""
from build import page, breadcrumbs, schema_breadcrumb, href_to, NAV_LABELS, chart_slider, LANGS
from chart_data import build_topics, render_topic, UI_LABELS


def L(lang):
    ids = ["home", "uslugi", "stoimost", "riski", "protsess", "terminologiya",
           "paragvay-hub", "pochemu-paragvay", "zhizn-v-paragvae", "stoimost-zhizni",
           "nalogi-inostrantsev", "banki-perevody", "viza-vyezd", "mify-voprosy",
           "dokumenty", "dok-temporal", "turizm", "meditsina-v-paragvae", "usluga-medicina",
           "usluga-compliance", "rabota-v-paragvae"]
    return {pid: href_to(pid, lang) for pid in ids}


HUB_LABEL = {
    "ru": "Парагвай для переезда",
    "es": "Paraguay para mudarse",
    "en": "Paraguay for Relocation",
    "de": "Paraguay für Auswanderer",
}

MORE = {"ru": "Подробнее →", "es": "Más →", "en": "Learn more →", "de": "Mehr erfahren →"}

# Карточка «Туризм» на лендинге хаба (21.08.2026, переведена на ES/EN/DE вместе со всей секцией
# «Туризм» — см. pages_turizm.py). (title, description) по языкам.
TOUR_CARD = {
    "ru": ("Туризм: что посмотреть в Парагвае",
           "20 достопримечательностей по всей стране — от исторического центра Асунсьона и "
           "иезуитских миссий ЮНЕСКО до плотины Итайпу и меннонитских колоний Чако, с фактами и "
           "источниками по каждой."),
    "es": ("Turismo: qué ver en Paraguay",
           "20 atractivos turísticos en todo el país — desde el centro histórico de Asunción y las "
           "misiones jesuíticas de la UNESCO hasta la represa de Itaipú y las colonias menonitas del "
           "Chaco, con datos y fuentes para cada uno."),
    "en": ("Tourism: what to see in Paraguay",
           "20 attractions across the country — from historic downtown Asunción and the UNESCO "
           "Jesuit missions to the Itaipú dam and the Mennonite colonies of the Chaco, with facts "
           "and sources for each one."),
    "de": ("Tourismus: Was man in Paraguay sehen sollte",
           "20 Sehenswürdigkeiten im ganzen Land — vom historischen Zentrum Asuncións und den "
           "UNESCO-Jesuitenmissionen bis zum Staudamm Itaipú und den mennonitischen Kolonien des "
           "Chaco, mit Fakten und Quellen zu jeder einzelnen."),
}


def crumbs(lang, current_label, current_href=None):
    """Хлебные крошки: Главная › Парагвай для переезда [› текущая подстраница]."""
    l = L(lang)
    items = [(NAV_LABELS[lang]["home"], l["home"])]
    if current_href is None:
        items.append((HUB_LABEL[lang], None))
    else:
        items.append((HUB_LABEL[lang], l["paragvay-hub"]))
        items.append((current_label, None))
    return breadcrumbs(items)


def schema_crumbs(lang, name, page_id):
    l = L(lang)
    items = [(NAV_LABELS[lang]["home"], f"/{lang}/")]
    if page_id != "paragvay-hub":
        items.append((HUB_LABEL[lang], f"/{lang}/{l['paragvay-hub']}"))
    items.append((name, f"/{lang}/{l[page_id]}"))
    return schema_breadcrumb(items)


def hero(h1, lead, compact=False):
    cls = "hero hero--compact" if compact else "hero"
    return f'''<section class="{cls}" style="padding-top:24px;">
  <div class="wrap">
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>
  </div>
</section>'''


# ============================================================= 0. HUB LANDING

CARD_TITLE = {
    "ru": {"pochemu-paragvay": "Почему Парагвай", "zhizn-v-paragvae": "Жизнь в Парагвае",
           "stoimost-zhizni": "Стоимость жизни", "nalogi-inostrantsev": "Налоги для иностранцев",
           "banki-perevody": "Банки, счета и переводы денег", "viza-vyezd": "Виза, документы и въезд",
           "mify-voprosy": "Мифы о переезде"},
    "es": {"pochemu-paragvay": "Por qué Paraguay", "zhizn-v-paragvae": "Vida en Paraguay",
           "stoimost-zhizni": "Costo de vida", "nalogi-inostrantsev": "Impuestos para extranjeros",
           "banki-perevody": "Bancos, cuentas y transferencias de dinero", "viza-vyezd": "Visa, documentos y entrada",
           "mify-voprosy": "Mitos sobre la mudanza"},
    "en": {"pochemu-paragvay": "Why Paraguay", "zhizn-v-paragvae": "Life in Paraguay",
           "stoimost-zhizni": "Cost of Living", "nalogi-inostrantsev": "Taxes for Foreigners",
           "banki-perevody": "Banking, Accounts, and Money Transfers", "viza-vyezd": "Visa, Documents, and Entry",
           "mify-voprosy": "Myths About Relocating"},
    "de": {"pochemu-paragvay": "Warum Paraguay", "zhizn-v-paragvae": "Leben in Paraguay",
           "stoimost-zhizni": "Lebenshaltungskosten", "nalogi-inostrantsev": "Steuern für Ausländer",
           "banki-perevody": "Banken, Konten und Geldtransfers", "viza-vyezd": "Visum, Dokumente und Einreise",
           "mify-voprosy": "Mythen über den Umzug"},
}

# Короткие лейблы для хлебных крошек — где короче CARD_TITLE, повторяют паттерн RU-оригинала
# (banki-perevody/viza-vyezd там ещё короче, чем в карточках лендинга).
BREADCRUMB_LABEL = {
    "ru": dict(CARD_TITLE["ru"], **{"banki-perevody": "Банки и переводы", "viza-vyezd": "Виза и въезд"}),
    "es": dict(CARD_TITLE["es"], **{"banki-perevody": "Bancos y transferencias", "viza-vyezd": "Visa y entrada"}),
    "en": dict(CARD_TITLE["en"], **{"banki-perevody": "Banking and Transfers", "viza-vyezd": "Visa and Entry"}),
    "de": dict(CARD_TITLE["de"], **{"banki-perevody": "Banken und Transfers", "viza-vyezd": "Visum und Einreise"}),
}

DESC = {
    "ru": {
        "pochemu-paragvay": 'Честное сравнение условий переезда: почему заявленные короткие сроки гражданства в '
                             'соседних странах почти никогда не относятся к типичному переезжающему — и чем на этом '
                             'фоне выделяется Парагвай.',
        "zhizn-v-paragvae": 'Климат Асунсьона по месяцам, районы столицы и агломерации, немецкие колонии юга страны '
                             'и меннониты из России в Чако — практическая картина повседневности, не туристический глянец.',
        "stoimost-zhizni": 'Ориентировочные месячные расходы в Асунсьоне — аренда, продукты и коммунальные услуги '
                            'по данным Numbeo и Expatistan, с честной оговоркой о точности этих источников.',
        "nalogi-inostrantsev": 'Территориальный принцип налогообложения и ставки IRE, IVA, IRP, IDU в Парагвае простыми '
                                'словами — и честно о том, что соглашения об избежании двойного налогообложения с Россией '
                                'найти не удалось.',
        "banki-perevody": 'Как открыть счёт в Парагвае, что известно про санкционные ограничения переводов из '
                           'России и почему криптовалюта — не безрисковый обходной путь.',
        "viza-vyezd": 'Безвизовый режим Россия–Парагвай, апостиль, перевод документов и категории пребывания — '
                      'практический чек-лист перед поездкой.',
        "mify-voprosy": 'Разбираем пять частых утверждений о переезде в Парагвай — от «гражданства за год» до '
                         'мифов про визу и криптопереводы — с указанием источника по каждому пункту.',
    },
    "es": {
        "pochemu-paragvay": 'Comparación honesta de condiciones de mudanza: por qué los plazos cortos de ciudadanía '
                             'anunciados en países vecinos casi nunca se aplican a la persona típica que se muda — y '
                             'qué distingue a Paraguay frente a esto.',
        "zhizn-v-paragvae": 'Clima de Asunción mes a mes, barrios de la capital y su aglomeración, colonias alemanas '
                             'del sur del país y menonitas venidos de Rusia al Chaco — un panorama práctico de la vida '
                             'cotidiana, sin glamour turístico.',
        "stoimost-zhizni": 'Gastos mensuales aproximados en Asunción — alquiler, alimentos y servicios según datos de '
                            'Numbeo y Expatistan, con una aclaración honesta sobre la precisión de estas fuentes.',
        "nalogi-inostrantsev": 'Principio territorial de tributación y tasas de IRE, IVA, IRP e IDU en Paraguay '
                                'explicados de forma sencilla — y con honestidad sobre que no se encontró un convenio '
                                'para evitar la doble imposición con Rusia.',
        "banki-perevody": 'Cómo abrir una cuenta en Paraguay, qué se sabe sobre las restricciones por sanciones a las '
                           'transferencias desde Rusia y por qué la criptomoneda no es una vía sin riesgo.',
        "viza-vyezd": 'Régimen sin visado Rusia–Paraguay, apostilla, traducción de documentos y categorías de '
                      'estadía — una lista práctica antes del viaje.',
        "mify-voprosy": 'Analizamos cinco afirmaciones frecuentes sobre mudarse a Paraguay — desde la «ciudadanía en '
                         'un año» hasta los mitos sobre la visa y las criptotransferencias — con la fuente indicada '
                         'en cada punto.',
    },
    "en": {
        "pochemu-paragvay": 'An honest comparison of relocation conditions: why the short citizenship timelines '
                             'advertised in neighboring countries almost never apply to a typical person relocating — '
                             'and what sets Paraguay apart against that backdrop.',
        "zhizn-v-paragvae": "Asunción's climate month by month, neighborhoods of the capital and its metro area, the "
                             'German colonies in the south of the country, and Mennonites from Russia in the Chaco — a '
                             'practical picture of everyday life, not a tourist brochure.',
        "stoimost-zhizni": 'Approximate monthly expenses in Asunción — rent, groceries, and utilities based on Numbeo '
                            'and Expatistan data, with an honest caveat about how accurate these sources are.',
        "nalogi-inostrantsev": "Paraguay's territorial tax principle and IRE, IVA, IRP, and IDU rates explained in "
                                'plain terms — and an honest note that no double taxation treaty with Russia could be '
                                'found.',
        "banki-perevody": "How to open an account in Paraguay, what's known about sanctions restrictions on transfers "
                           "from Russia, and why crypto isn't a risk-free workaround.",
        "viza-vyezd": 'The Russia–Paraguay visa-free regime, apostilles, document translation, and categories of '
                      'stay — a practical checklist before the trip.',
        "mify-voprosy": 'We break down five common claims about relocating to Paraguay — from "citizenship in a '
                         'year" to myths about visas and crypto transfers — with a source cited for each point.',
    },
    "de": {
        "pochemu-paragvay": 'Ehrlicher Vergleich der Auswanderungsbedingungen: warum die beworbenen kurzen Fristen '
                             'bis zur Staatsbürgerschaft in Nachbarländern fast nie auf die typische auswandernde '
                             'Person zutreffen — und was Paraguay davon abhebt.',
        "zhizn-v-paragvae": 'Asunciones Klima im Monatsverlauf, Stadtviertel der Hauptstadt und ihres Ballungsraums, '
                             'die deutschen Kolonien im Süden des Landes und Mennoniten aus Russland im Chaco — ein '
                             'praktisches Bild des Alltags, kein touristischer Hochglanz.',
        "stoimost-zhizni": 'Ungefähre monatliche Ausgaben in Asunción — Miete, Lebensmittel und Nebenkosten laut '
                            'Numbeo und Expatistan, mit einem ehrlichen Hinweis zur Genauigkeit dieser Quellen.',
        "nalogi-inostrantsev": 'Das Territorialprinzip der Besteuerung und die Sätze von IRE, IVA, IRP und IDU in '
                                'Paraguay einfach erklärt — und ehrlich dazu, dass kein Doppelbesteuerungsabkommen mit '
                                'Russland gefunden werden konnte.',
        "banki-perevody": 'Wie man in Paraguay ein Konto eröffnet, was über sanktionsbedingte Beschränkungen bei '
                           'Überweisungen aus Russland bekannt ist und warum Kryptowährung kein risikofreier Umweg ist.',
        "viza-vyezd": 'Das visumfreie Regime zwischen Russland und Paraguay, Apostille, Dokumentenübersetzung und '
                      'Aufenthaltskategorien — eine praktische Checkliste vor der Reise.',
        "mify-voprosy": 'Wir prüfen fünf häufige Behauptungen über den Umzug nach Paraguay — von '
                         '„Staatsbürgerschaft in einem Jahr" bis zu Mythen über Visum und Kryptotransfers — mit '
                         'Quellenangabe zu jedem Punkt.',
    },
}

HUB_PAGE_ORDER = ["pochemu-paragvay", "zhizn-v-paragvae", "stoimost-zhizni", "nalogi-inostrantsev",
                   "banki-perevody", "viza-vyezd", "mify-voprosy"]

LANDING = {
    "ru": dict(
        h1="Парагвай для переезда",
        lead="Справочник о жизни в Парагвае для тех, кто рассматривает переезд: климат и районы, "
             "налоги, банки и переводы денег, визы и документы, честное сравнение с соседними странами.",
        stats_heading="Парагвай в цифрах",
        intro="Прежде чем разбираться, какая услуга нужна именно вам, обычно возникает вопрос проще и "
              "шире — а что вообще собой представляет жизнь в этой стране. Русскоязычного контента о "
              "Парагвае почти нет: телеграм-сообщества переехавших и интересующихся исчисляются тысячами, "
              "а внятных текстов и видео на русском — единицы. Этот раздел закрывает разрыв — рабочий "
              "справочник, к которому можно возвращаться на разных этапах решения.",
        title_tag="Парагвай для переезда: климат, налоги, банки, визы, мифы | Grund Paraguay",
    ),
    "es": dict(
        h1="Paraguay para mudarse",
        lead="Guía sobre la vida en Paraguay para quienes evalúan mudarse: clima y barrios, impuestos, "
             "bancos y transferencias de dinero, visado y documentos, comparación honesta con los países vecinos.",
        stats_heading="Paraguay en cifras",
        intro="Antes de decidir qué servicio necesita exactamente, suele surgir una pregunta más simple y "
              "más amplia: cómo es en realidad la vida en este país. Casi no existe contenido en ruso sobre "
              "Paraguay: las comunidades de Telegram de quienes ya se mudaron o están interesados se cuentan "
              "por miles, mientras que los textos y videos claros en ruso son escasos. Esta sección cubre ese "
              "vacío — un recurso de referencia al que se puede volver en distintas etapas de la decisión.",
        title_tag="Paraguay para mudarse: clima, impuestos, bancos, visados, mitos | Grund Paraguay",
    ),
    "en": dict(
        h1="Paraguay for Relocation",
        lead="A guide to life in Paraguay for anyone considering relocating: climate and neighborhoods, "
             "taxes, banking and money transfers, visas and documents, an honest comparison with neighboring countries.",
        stats_heading="Paraguay in Numbers",
        intro="Before figuring out which service you actually need, a simpler and broader question usually "
              "comes up first — what everyday life in this country is actually like. There's almost no "
              "Russian-language content about Paraguay: Telegram communities of people who have already moved "
              "or are just curious run into the thousands, while clear, well-researched texts and videos in "
              "Russian are rare. This section closes that gap — a working reference you can come back to at "
              "different stages of the decision.",
        title_tag="Paraguay for Relocation: Climate, Taxes, Banks, Visas, Myths | Grund Paraguay",
    ),
    "de": dict(
        h1="Paraguay für Auswanderer",
        lead="Ratgeber zum Leben in Paraguay für alle, die einen Umzug erwägen: Klima und Stadtviertel, "
             "Steuern, Banken und Geldtransfers, Visum und Dokumente, ehrlicher Vergleich mit den Nachbarländern.",
        stats_heading="Paraguay in Zahlen",
        intro="Bevor man klärt, welche Dienstleistung man eigentlich braucht, stellt sich meist zuerst eine "
              "einfachere und umfassendere Frage — wie das Leben in diesem Land überhaupt aussieht. "
              "Russischsprachige Inhalte über Paraguay gibt es kaum: Telegram-Communities von Ausgewanderten "
              "und Interessierten zählen in die Tausende, verständliche Texte und Videos auf Russisch dagegen "
              "sind rar. Dieser Abschnitt schließt diese Lücke — ein Nachschlagewerk, zu dem man in "
              "verschiedenen Phasen der Entscheidung zurückkehren kann.",
        title_tag="Paraguay für Auswanderer: Klima, Steuern, Banken, Visa, Mythen | Grund Paraguay",
    ),
}


def stat_href(lang):
    l = L(lang)
    return {
        "life": l["zhizn-v-paragvae"],
        "gpi": l["mify-voprosy"],
        "passport": l["viza-vyezd"],
        "dnm": l["protsess"],
        "argentina": l["pochemu-paragvay"],
        "tax": l["nalogi-inostrantsev"],
    }


def build_hub_landing():
    for lang in LANGS:
        l = L(lang)
        t = LANDING[lang]

        blocks_html = ""
        for page_id in HUB_PAGE_ORDER:
            blocks_html += f'''
    <article class="card" style="margin-bottom:24px;">
      <h3>{CARD_TITLE[lang][page_id]}</h3>
      <p style="font-size:16px;">{DESC[lang][page_id]}</p>
      <a class="card-link" href="{l[page_id]}">{MORE[lang]}</a>
    </article>'''

        # 21.08.2026 — «Туризм» (20 достопримечательностей + анонс-страница, pages_turizm.py),
        # старт RU-only; 21.08.2026 вечер — переведена на ES/EN/DE (тем же запросом заказчика,
        # что и «Релокация организаций»). Не входит в HUB_PAGE_ORDER (тот список — про сами
        # страницы хаба «Парагвай для переезда»), добавлена отдельной карточкой ниже для всех
        # 4 языков, тем же приёмом, что и «Релокация организаций» на «Услугах» (RELOCATION_CARD
        # в pages_home_uslugi.py).
        tour_title, tour_desc = TOUR_CARD[lang]
        blocks_html += f'''
    <article class="card" style="margin-bottom:24px;">
      <h3>{tour_title}</h3>
      <p style="font-size:16px;">{tour_desc}</p>
      <a class="card-link" href="{l['turizm']}">{MORE[lang]}</a>
    </article>'''

        # «Медицина в Парагвае» — подстраница хаба (24.08.2026, старт RU-only; 27.08.2026 —
        # переведена на ES/EN/DE), карточка на лендинге тем же приёмом, что и «Туризм» выше.
        meditsina_title, meditsina_desc = MEDITSINA_CARD[lang]
        blocks_html += f'''
    <article class="card" style="margin-bottom:24px;">
      <h3>{meditsina_title}</h3>
      <p style="font-size:16px;">{meditsina_desc}</p>
      <a class="card-link" href="{l['meditsina-v-paragvae']}">{MORE[lang]}</a>
    </article>'''

        # «Работа в Парагвае» — подстраница хаба (28.08.2026), карточка тем же приёмом, что и
        # «Туризм»/«Медицина в Парагвае» выше.
        rabota_title, rabota_desc = RABOTA_CARD[lang]
        blocks_html += f'''
    <article class="card" style="margin-bottom:24px;">
      <h3>{rabota_title}</h3>
      <p style="font-size:16px;">{rabota_desc}</p>
      <a class="card-link" href="{l['rabota-v-paragvae']}">{MORE[lang]}</a>
    </article>'''

        body = f'''
{crumbs(lang, HUB_LABEL[lang])}
{hero(t["h1"], t["lead"], compact=True)}
<section style="padding-top:0;">
  <div class="wrap">
    <h2 style="margin-top:0">{t["stats_heading"]}</h2>
    {chart_slider(
        [dict(svg=render_topic(ct), title=ct["title"], caption=ct["caption"], href=ct["href"])
         for ct in build_topics(lang, href=stat_href(lang))],
        UI_LABELS[lang], slider_id="hub-stats-slider", more_label=MORE[lang],
    )}
  </div>
</section>
<section class="section-alt">
  <div class="prose">
    <p>{t["intro"]}</p>

    {blocks_html}
  </div>
</section>
'''
        page("paragvay-hub", lang, t["title_tag"], t["lead"], body,
             extra_schema=schema_crumbs(lang, HUB_LABEL[lang], "paragvay-hub"))

# ============================================================ 1. ПОЧЕМУ ПАРАГВАЙ

POCHEMU_HEAD = {
    "ru": ("Страна", "Стандартный срок гражданства", "Условие для более короткого срока"),
    "es": ("País", "Plazo estándar de ciudadanía", "Condición para un plazo más corto"),
    "en": ("Country", "Standard time to citizenship", "Condition for a shorter time"),
    "de": ("Land", "Standardfrist bis zur Staatsbürgerschaft", "Bedingung für eine kürzere Frist"),
}

POCHEMU_ROWS = {
    "ru": [
        ("Аргентина", "2 года", "— это и есть стандартный срок, без дополнительных условий"),
        ("Чили", "5 лет", "2 года — только при браке с гражданином/гражданкой Чили"),
        ("Бразилия", "4 года", "1 год — только для граждан португалоязычных стран или при браке с бразильцем/бразильянкой"),
        ("Уругвай", "3 года (при «сформированной семье» в стране) / 5 лет", "отдельная налоговая резидентура для инвесторов — от ≈377 000 USD"),
        ("Парагвай", "7–8 лет (реалистичный срок)", "путь открыт без брака с местным гражданином, без гражданства третьей страны и без депозита в сотни тысяч долларов"),
    ],
    "es": [
        ("Argentina", "2 años", "— este es el plazo estándar, sin condiciones adicionales"),
        ("Chile", "5 años", "2 años — solo en caso de matrimonio con un ciudadano o ciudadana chilena"),
        ("Brasil", "4 años", "1 año — solo para ciudadanos de países de habla portuguesa o en caso de matrimonio con un brasileño o brasileña"),
        ("Uruguay", "3 años (con «familia constituida» en el país) / 5 años", "residencia fiscal aparte para inversionistas — desde ≈377.000 USD"),
        ("Paraguay", "7–8 años (plazo realista)", "el camino está abierto sin matrimonio con un ciudadano local, sin ciudadanía de un tercer país y sin depósitos de cientos de miles de dólares"),
    ],
    "en": [
        ("Argentina", "2 years", "— this is the standard time, no extra conditions"),
        ("Chile", "5 years", "2 years — only when married to a Chilean citizen"),
        ("Brazil", "4 years", "1 year — only for citizens of Portuguese-speaking countries or when married to a Brazilian citizen"),
        ("Uruguay", "3 years (with a \"family established\" in the country) / 5 years", "a separate tax residency for investors — from ≈$377,000"),
        ("Paraguay", "7–8 years (realistic timeline)", "the path is open without marrying a local citizen, without third-country citizenship, and without a deposit of hundreds of thousands of dollars"),
    ],
    "de": [
        ("Argentinien", "2 Jahre", "— das ist bereits die Standardfrist, ohne zusätzliche Bedingungen"),
        ("Chile", "5 Jahre", "2 Jahre — nur bei Ehe mit einem chilenischen Staatsbürger/einer chilenischen Staatsbürgerin"),
        ("Brasilien", "4 Jahre", "1 Jahr — nur für Staatsangehörige portugiesischsprachiger Länder oder bei Ehe mit einem/einer Brasilianer(in)"),
        ("Uruguay", "3 Jahre (bei „gegründeter Familie\" im Land) / 5 Jahre", "eigener Steuerwohnsitz für Investoren — ab ≈377.000 USD"),
        ("Paraguay", "7–8 Jahre (realistische Frist)", "der Weg steht offen ohne Ehe mit einem einheimischen Staatsbürger, ohne Staatsbürgerschaft eines Drittlands und ohne Einlage in Höhe von Hunderttausenden Dollar"),
    ],
}


def build_pochemu():
    for lang in LANGS:
        l = L(lang)
        h1 = LANDING  # placeholder, overwritten below per-lang h1 dict
        H1 = {
            "ru": "Почему Парагвай, а не Аргентина, Уругвай, Чили или Бразилия",
            "es": "Por qué Paraguay y no Argentina, Uruguay, Chile o Brasil",
            "en": "Why Paraguay, and Not Argentina, Uruguay, Chile, or Brazil",
            "de": "Warum Paraguay und nicht Argentinien, Uruguay, Chile oder Brasilien",
        }[lang]
        lead = DESC[lang]["pochemu-paragvay"]
        title_tag = {
            "ru": "Почему Парагвай, а не Аргентина, Уругвай, Чили, Бразилия | Grund Paraguay",
            "es": "Por qué Paraguay y no Argentina, Uruguay, Chile, Brasil | Grund Paraguay",
            "en": "Why Paraguay, Not Argentina, Uruguay, Chile, Brazil | Grund Paraguay",
            "de": "Warum Paraguay statt Argentinien, Uruguay, Chile, Brasilien | Grund Paraguay",
        }[lang]

        head = POCHEMU_HEAD[lang]
        table_html = f'<table>\n<thead><tr><th>{head[0]}</th><th>{head[1]}</th><th>{head[2]}</th></tr></thead>\n<tbody>\n'
        for country, term, cond in POCHEMU_ROWS[lang]:
            table_html += f'<tr><td>{country}</td><td>{term}</td><td>{cond}</td></tr>\n'
        table_html += '</tbody>\n</table>'

        if lang == "ru":
            prose = f'''
    <p>Если сравнивать страны региона по одной цифре — «через сколько лет гражданство», —
    выбор кажется очевидным не в пользу Парагвая:</p>

    {table_html}

    <p>На бумаге Аргентина, Уругвай, Чили и Бразилия выглядят быстрее. На практике у трёх из
    четырёх коротких сроков есть условие, которое отсекает большую часть переезжающих людей.</p>

    <p>У Чили и Бразилии короткий срок — не общий путь, а исключение. Два года у Чили — это
    сокращение только «при квалифицирующих связях», на практике — брак с гражданином страны;
    стандартный путь занимает 5 лет. Год у Бразилии — только для граждан португалоязычных
    стран или при браке с бразильцем/бразильянкой; без этого — 4 года, то есть даже не
    принципиально быстрее Парагвая. Если у переезжающего нет местного супруга или гражданства
    Португалии/Анголы/Мозамбика — эти цифры к нему просто не применяются.</p>

    <p>У Уругвая ситуация другая: три года при «сформированной семье» в стране (пять — без
    неё) звучат привлекательно сами по себе, но версия «быстрого Уругвая», которая обычно и
    мелькает в рекламе, — это отдельная налоговая резидентура для инвесторов, начинающаяся от
    ≈377 000 USD (порог действует с реформы 2020 года). Для сравнения — инвесторский путь в
    Парагвае (подробнее — среди <a href="{l['uslugi']}">наших услуг</a>) открыт от 70 000 USD.
    Для человека с доходом от удалённой работы, а не с крупным капиталом, уругвайский вариант —
    не «более дорогая альтернатива», а фактически недоступный вариант.</p>

    <p>Аргентина — самый сильный конкурент по этой таблице, и здесь нечего разоблачать по
    существу условий: два года непрерывного проживания — один из самых коротких сроков в
    мире, без скрытых оговорок. Но у формального преимущества есть оборотная сторона: с
    приходом к власти Хавьера Милея в конце 2023 года миграционная политика Аргентины
    последовательно ужесточается. С 29 мая 2025 года действует декрет № 366/2025: он ввёл
    требование о двух годах непрерывного проживания без выездов для гражданства вместо прежней
    практики накопления срока через продления временных виз, сократил срок действия временного
    статуса («precaria») со 180 до 90 дней, ограничил бесплатную медицину и высшее образование
    только постоянными резидентами и расширил основания для депортации. С 31 июля 2026 года
    действует ещё один декрет (№ 681/2026) — он позволяет отказывать во въезде и выдворять
    иностранцев за публичные высказывания, которые сочтут враждебными по отношению к
    Аргентине; на момент проверки декрет ещё проходит обязательное рассмотрение в
    парламентской комиссии. Статистика подтверждает ужесточение на практике: отказы во въезде
    на границе показывают многократный скачок в последних двух месяцах — только за декабрь
    2025 – январь 2026 года власти отчитались почти о 5000 отказов и выдворений, заметно
    больше обычного месячного темпа. Депортации осуждённых иностранцев выросли в полтора раза.
    Если решающий критерий при выборе страны — именно скорость получения гражданства сама по
    себе на бумаге, честный ответ по этой конкретной метрике — Аргентина, а не Парагвай; но
    эта же бумага на практике становится менее предсказуемой год от года.</p>

    <p>Вот что реально получает человек, который выбирает Парагвай. Во-первых, доступность без
    обходных условий: стандартный путь не привязан ни к браку с местным гражданином, ни к
    чужому гражданству, ни к крупному капиталу, а более быстрый инвесторский трек открыт уже
    от 70 000 USD. Во-вторых, уже заметное и растущее русскоязычное присутствие: в 2025 году
    резидентство в Парагвае получили 509 граждан России, а только за I квартал 2026 года — уже
    194, почти столько же, сколько за весь предыдущий год. В-третьих — рынок услуг вокруг
    переезда здесь ещё не насыщен: для рынка сделок по <a href="{l['uslugi']}">покупке и
    продаже бизнеса</a>, например, крупные региональные трекеры сделок вообще не включают
    Парагвай в своё покрытие. Это можно прочитать не как признак неразвитости, а как то, что
    здесь меньше посредников, конкурирующих за клиента, и меньше уже устоявшихся,
    закостеневших практик.</p>

    <p>У этой доступности есть цена — время. Реалистичный срок «от приезда до паспорта» —
    7–8 лет, а не один год, как иногда обещают недобросовестные агентства; это прямая оценка
    директора миграционной службы Парагвая (DNM), Хорхе Кронаветтера (ABC Color, 04.05.2026) —
    та же цифра уже упоминалась на <a href="{l['home']}">Главной</a>. Даже после выполнения
    формального трёхлетнего срока после получения постоянной резиденции решение о гражданстве
    принимает не миграционная служба, а
    <a href="{l['terminologiya']}#corte-suprema">Верховный суд</a> (Corte Suprema de Justicia) —
    с обязательной личной явкой и юридическим сопровождением.</p>'''
        elif lang == "es":
            prose = f'''
    <p>Si se comparan los países de la región por una sola cifra — «en cuántos años se obtiene la
    ciudadanía» —, la elección no parece favorecer a Paraguay a simple vista:</p>

    {table_html}

    <p>Sobre el papel, Argentina, Uruguay, Chile y Brasil parecen más rápidos. En la práctica, tres de
    los cuatro plazos cortos tienen una condición que excluye a la mayoría de las personas que se
    mudan.</p>

    <p>En Chile y Brasil, el plazo corto no es el camino general, sino la excepción. Los dos años de
    Chile son una reducción solo «por vínculos calificados» — en la práctica, matrimonio con un
    ciudadano del país; el camino estándar toma 5 años. El año de Brasil es solo para ciudadanos de
    países de habla portuguesa o en caso de matrimonio con un brasileño o brasileña; sin eso, son 4
    años, es decir, ni siquiera sustancialmente más rápido que Paraguay. Si la persona que se muda no
    tiene cónyuge local ni ciudadanía de Portugal, Angola o Mozambique, estas cifras simplemente no
    se le aplican.</p>

    <p>Con Uruguay la situación es distinta: tres años con «familia constituida» en el país (cinco sin
    ella) suenan atractivos de por sí, pero la versión de «Uruguay rápido» que suele aparecer en la
    publicidad es una residencia fiscal aparte para inversionistas, que empieza desde ≈377.000 USD
    (el umbral rige desde la reforma de 2020). En comparación, el camino de inversionista en Paraguay
    (más detalles entre <a href="{l['uslugi']}">nuestros servicios</a>) está abierto desde 70.000 USD.
    Para una persona con ingresos de trabajo remoto, y no con un capital grande, la opción uruguaya no
    es «una alternativa más cara», sino en la práctica inalcanzable.</p>

    <p>Argentina es el competidor más fuerte en esta tabla, y aquí no hay nada que desmentir en cuanto
    al fondo de las condiciones: dos años de residencia continua es uno de los plazos más cortos del
    mundo, sin condiciones ocultas. Pero esta ventaja formal tiene su contracara: desde la llegada al
    poder de Javier Milei a fines de 2023, la política migratoria de Argentina se ha endurecido de
    forma constante. Desde el 29 de mayo de 2025 rige el decreto N.º 366/2025: introdujo el requisito
    de dos años de residencia continua sin salidas del país para la ciudadanía, en lugar de la
    práctica anterior de acumular el plazo mediante renovaciones de visas temporales, redujo la
    vigencia del estatus temporal («precaria») de 180 a 90 días, limitó la salud pública gratuita y
    la educación superior solo a residentes permanentes y amplió los motivos para la deportación.
    Desde el 31 de julio de 2026 rige otro decreto (N.º 681/2026) que permite negar la entrada y
    expulsar a extranjeros por declaraciones públicas que se consideren hostiles hacia Argentina; al
    momento de la revisión, el decreto todavía está bajo revisión obligatoria de una comisión
    parlamentaria. Las estadísticas confirman el endurecimiento en la práctica: los rechazos de
    entrada en la frontera muestran un salto muy marcado en los últimos dos meses — solo entre
    diciembre de 2025 y enero de 2026 las autoridades reportaron casi 5.000 rechazos y expulsiones,
    notablemente por encima del ritmo mensual habitual. Las deportaciones de extranjeros condenados
    aumentaron una vez y media. Si el criterio decisivo al elegir un país es la velocidad de la
    ciudadanía en sí, sobre el papel, la respuesta honesta según esta métrica concreta es Argentina,
    no Paraguay; pero ese mismo papel se vuelve, en la práctica, menos predecible año tras año.</p>

    <p>Esto es lo que realmente obtiene una persona que elige Paraguay. Primero, accesibilidad sin
    condiciones indirectas: el camino estándar no está condicionado ni al matrimonio con un
    ciudadano local, ni a la ciudadanía de otro país, ni a un capital grande, y la vía de
    inversionista, más rápida, está abierta ya desde 70.000 USD. Segundo, una presencia de habla rusa
    ya notable y en crecimiento: en 2025, 509 ciudadanos de Rusia obtuvieron la residencia en
    Paraguay, y solo en el primer trimestre de 2026 ya fueron 194 — casi tantos como en todo el año
    anterior. Tercero — el mercado de servicios en torno a la mudanza todavía no está saturado: en el
    mercado de <a href="{l['uslugi']}">compra y venta de negocios</a>, por ejemplo, los grandes
    rastreadores regionales de transacciones ni siquiera incluyen a Paraguay en su cobertura. Esto
    puede leerse no como señal de subdesarrollo, sino como que aquí hay menos intermediarios
    compitiendo por el cliente y menos prácticas ya asentadas y rígidas.</p>

    <p>Esta accesibilidad tiene un precio — el tiempo. El plazo realista «desde la llegada hasta el
    pasaporte» es de 7 a 8 años, no un año, como a veces prometen agencias poco serias; es la
    estimación directa del director del servicio de migraciones de Paraguay (DNM), Jorge Kronawetter
    (ABC Color, 04.05.2026) — la misma cifra ya se mencionó en la <a href="{l['home']}">Página
    principal</a>. Incluso después de cumplir el plazo formal de tres años tras obtener la residencia
    permanente, la decisión sobre la ciudadanía no la toma el servicio de migraciones, sino la
    <a href="{l['terminologiya']}#corte-suprema">Corte Suprema</a> (Corte Suprema de Justicia) — con
    comparecencia personal obligatoria y acompañamiento jurídico.</p>'''
        elif lang == "en":
            prose = f'''
    <p>If you compare the countries of the region using a single figure — "how many years until
    citizenship" — the choice doesn't look like it favors Paraguay at first glance:</p>

    {table_html}

    <p>On paper, Argentina, Uruguay, Chile, and Brazil look faster. In practice, three of the four short
    timelines come with a condition that rules out most people who relocate.</p>

    <p>For Chile and Brazil, the short timeline isn't the general path — it's the exception. Chile's two
    years is a reduction only "for qualifying ties," which in practice means marriage to a citizen of
    the country; the standard path takes 5 years. Brazil's one year applies only to citizens of
    Portuguese-speaking countries or those married to a Brazilian citizen; without that, it's 4
    years — not meaningfully faster than Paraguay at all. If the person relocating has no local
    spouse and no citizenship of Portugal, Angola, or Mozambique, these figures simply don't apply to
    them.</p>

    <p>Uruguay's situation is different: three years with a "family established" in the country (five
    without one) sound appealing on their own, but the "fast Uruguay" version that usually shows up
    in advertising is a separate tax residency for investors, starting at roughly $377,000 (the
    threshold has been in place since the 2020 reform). By comparison, the investor track in Paraguay
    (more in our <a href="{l['uslugi']}">services</a>) opens at $70,000. For someone with income from remote work
    rather than substantial capital, the Uruguayan option isn't "a pricier alternative" — it's
    effectively out of reach.</p>

    <p>Argentina is the strongest competitor in this table, and there's nothing to debunk about the
    substance of its conditions: two years of continuous residence is one of the shortest timelines
    in the world, with no hidden catches. But that formal advantage has a flip side: since Javier
    Milei came to power in late 2023, Argentina's migration policy has been tightening steadily.
    Decree No. 366/2025, in force since May 29, 2025, introduced a requirement of two years of
    continuous residence without leaving the country for citizenship — replacing the previous
    practice of accumulating time through temporary visa renewals — shortened the validity of
    temporary status ("precaria") from 180 to 90 days, restricted free healthcare and higher
    education to permanent residents only, and expanded the grounds for deportation. Another decree
    (No. 681/2026), in force since July 31, 2026, allows denying entry to and expelling foreigners
    for public statements deemed hostile toward Argentina; at the time of checking, the decree was
    still going through mandatory review by a parliamentary committee. The statistics confirm the
    tightening in practice: border entry refusals show a sharp jump over the last two months — in
    December 2025–January 2026 alone, authorities reported almost 5,000 refusals and expulsions,
    noticeably above the usual monthly pace. Deportations of convicted foreigners rose by half. If
    the deciding factor in choosing a country is the speed of citizenship on paper by itself, the
    honest answer on that specific metric is Argentina, not Paraguay — but that same paper is
    becoming less predictable in practice, year by year.</p>

    <p>Here's what a person choosing Paraguay actually gets. First, accessibility without workarounds:
    the standard path isn't tied to marrying a local citizen, holding another country's citizenship,
    or having substantial capital, and the faster investor track is already open from $70,000.
    Second, an already noticeable and growing Russian-speaking presence: in 2025, 509 Russian
    citizens received residency in Paraguay, and in the first quarter of 2026 alone, already 194 —
    almost as many as in the entire previous year. Third, the market for relocation-related services
    here isn't saturated yet: for the <a href="{l['uslugi']}">business purchase and sale</a> market, for instance,
    the major regional deal trackers don't even include Paraguay in their coverage. That can be read
    not as a sign of underdevelopment, but as meaning fewer intermediaries competing for clients and
    fewer already-entrenched, rigid practices.</p>

    <p>This accessibility comes at a cost — time. The realistic timeline "from arrival to passport" is 7
    to 8 years, not one year, as some unscrupulous agencies sometimes promise; that's the direct
    assessment of the director of Paraguay's migration authority (DNM), Jorge Kronawetter (ABC
    Color, 05/04/2026) — the same figure already mentioned on the <a href="{l['home']}">Home page</a>. Even after
    meeting the formal three-year requirement following permanent residency, the decision on
    citizenship isn't made by the migration authority but by the
    <a href="{l['terminologiya']}#corte-suprema">Supreme Court</a> (Corte Suprema de Justicia) — with mandatory personal
    appearance and legal representation.</p>'''
        else:  # de
            prose = f'''
    <p>Vergleicht man die Länder der Region anhand einer einzigen Zahl — „nach wie vielen Jahren gibt es
    die Staatsbürgerschaft" —, scheint die Wahl auf den ersten Blick nicht für Paraguay zu sprechen:</p>

    {table_html}

    <p>Auf dem Papier wirken Argentinien, Uruguay, Chile und Brasilien schneller. In der Praxis ist bei
    drei der vier kurzen Fristen eine Bedingung geknüpft, die den größten Teil der Auswandernden
    ausschließt.</p>

    <p>Bei Chile und Brasilien ist die kurze Frist nicht der allgemeine Weg, sondern die Ausnahme. Die
    zwei Jahre in Chile sind eine Verkürzung nur „bei qualifizierenden Bindungen" — in der Praxis eine
    Ehe mit einem Staatsbürger des Landes; der Standardweg dauert 5 Jahre. Das eine Jahr in Brasilien
    gilt nur für Staatsangehörige portugiesischsprachiger Länder oder bei Ehe mit einem/einer
    Brasilianer(in); ohne das sind es 4 Jahre — also nicht einmal wesentlich schneller als Paraguay.
    Hat die auswandernde Person keinen einheimischen Ehepartner und keine Staatsbürgerschaft
    Portugals, Angolas oder Mosambiks, gelten diese Zahlen für sie schlicht nicht.</p>

    <p>Bei Uruguay liegt der Fall anders: drei Jahre bei „gegründeter Familie" im Land (fünf ohne sie)
    klingen für sich genommen attraktiv, aber die Version des „schnellen Uruguay", die meist in der
    Werbung auftaucht, ist ein eigener Steuerwohnsitz für Investoren, der bei ≈377.000 USD beginnt
    (die Schwelle gilt seit der Reform von 2020). Zum Vergleich: Der Investorenweg in Paraguay (mehr
    dazu bei unseren <a href="{l['uslugi']}">Dienstleistungen</a>) steht bereits ab 70.000 USD offen. Für jemanden
    mit Einkommen aus Remote-Arbeit statt großem Kapital ist die uruguayische Option nicht „eine
    teurere Alternative", sondern faktisch unerreichbar.</p>

    <p>Argentinien ist der stärkste Konkurrent in dieser Tabelle, und hier gibt es inhaltlich nichts an
    den Bedingungen zu entlarven: zwei Jahre ununterbrochener Aufenthalt sind eine der kürzesten
    Fristen weltweit, ohne versteckte Vorbehalte. Doch dieser formale Vorteil hat eine Kehrseite: Seit
    dem Amtsantritt von Javier Milei Ende 2023 wird die Migrationspolitik Argentiniens konsequent
    verschärft. Seit dem 29. Mai 2025 gilt das Dekret Nr. 366/2025: Es führte die Anforderung von zwei
    Jahren ununterbrochenen Aufenthalts ohne Ausreisen für die Staatsbürgerschaft ein — anstelle der
    bisherigen Praxis, die Frist über Verlängerungen befristeter Visa anzusammeln —, verkürzte die
    Gültigkeit des befristeten Status („precaria") von 180 auf 90 Tage, beschränkte die kostenlose
    Gesundheitsversorgung und Hochschulbildung auf Daueraufenthaltsberechtigte und erweiterte die
    Gründe für eine Abschiebung. Seit dem 31. Juli 2026 gilt ein weiteres Dekret (Nr. 681/2026) — es
    erlaubt, Ausländern die Einreise zu verweigern und sie auszuweisen wegen öffentlicher Äußerungen,
    die als feindselig gegenüber Argentinien eingestuft werden; zum Zeitpunkt der Prüfung durchlief
    das Dekret noch die obligatorische Prüfung durch einen Parlamentsausschuss. Die Statistik
    bestätigt die Verschärfung in der Praxis: Die Zahl der Einreiseverweigerungen an der Grenze zeigt
    in den letzten zwei Monaten einen deutlichen Sprung — allein von Dezember 2025 bis Januar 2026
    meldeten die Behörden fast 5.000 Verweigerungen und Ausweisungen, spürbar über dem üblichen
    monatlichen Tempo. Die Abschiebungen verurteilter Ausländer stiegen um das Anderthalbfache. Wenn
    das entscheidende Kriterium bei der Länderwahl allein das Tempo der Staatsbürgerschaft auf dem
    Papier ist, lautet die ehrliche Antwort bei dieser konkreten Kennzahl Argentinien, nicht Paraguay —
    doch eben dieses Papier wird in der Praxis von Jahr zu Jahr weniger vorhersehbar.</p>

    <p>Das bekommt eine Person, die sich für Paraguay entscheidet, tatsächlich. Erstens: Zugänglichkeit
    ohne Umwege — der Standardweg ist weder an eine Ehe mit einem einheimischen Staatsbürger noch an
    eine fremde Staatsbürgerschaft noch an großes Kapital gebunden, und der schnellere Investorenweg
    steht bereits ab 70.000 USD offen. Zweitens: eine bereits spürbare und wachsende
    russischsprachige Präsenz — 2025 erhielten 509 russische Staatsbürger die Residenz in Paraguay,
    und allein im ersten Quartal 2026 waren es bereits 194 — fast so viele wie im gesamten Vorjahr.
    Drittens: Der Markt für Dienstleistungen rund um den Umzug ist hier noch nicht gesättigt — für den
    Markt für den <a href="{l['uslugi']}">Kauf und Verkauf von Unternehmen</a> etwa erfassen große regionale
    Deal-Tracker Paraguay überhaupt nicht in ihrer Abdeckung. Das lässt sich nicht als Zeichen von
    Unterentwicklung lesen, sondern als Hinweis darauf, dass es hier weniger Vermittler gibt, die um
    Kunden konkurrieren, und weniger bereits erstarrte, festgefahrene Praktiken.</p>

    <p>Diese Zugänglichkeit hat einen Preis — Zeit. Die realistische Frist „von der Ankunft bis zum Pass"
    beträgt 7 bis 8 Jahre, nicht ein Jahr, wie es unseriöse Agenturen mitunter versprechen; das ist
    die direkte Einschätzung des Direktors der paraguayischen Migrationsbehörde (DNM), Jorge
    Kronawetter (04.05.2026, ABC Color) — dieselbe Zahl wurde bereits auf der
    <a href="{l['home']}">Startseite</a> erwähnt. Selbst nach Erfüllung der formalen Dreijahresfrist nach Erhalt
    der Daueraufenthaltsberechtigung trifft nicht die Migrationsbehörde die Entscheidung über die
    Staatsbürgerschaft, sondern der <a href="{l['terminologiya']}#corte-suprema">Oberste Gerichtshof</a> (Corte
    Suprema de Justicia) — mit obligatorischem persönlichem Erscheinen und anwaltlicher Begleitung.</p>'''

        body = f'''
{crumbs(lang, BREADCRUMB_LABEL[lang]["pochemu-paragvay"])}
{hero(H1, lead)}
<section style="padding-top:0;">
  <div class="prose">
    {prose}
  </div>
</section>
'''
        page("pochemu-paragvay", lang, title_tag, lead, body,
             extra_schema=schema_crumbs(lang, BREADCRUMB_LABEL[lang]["pochemu-paragvay"], "pochemu-paragvay"))

# ================================================== 2. ЖИЗНЬ В ПАРАГВАЕ

H1_ZHIZN = {"ru": "Жизнь в Парагвае", "es": "Vida en Paraguay", "en": "Life in Paraguay", "de": "Leben in Paraguay"}
TITLE_ZHIZN = {
    "ru": "Жизнь в Парагвае: климат, Асунсьон, немецкие колонии юга | Grund Paraguay",
    "es": "Vida en Paraguay: clima, Asunción, colonias alemanas del sur | Grund Paraguay",
    "en": "Life in Paraguay: Climate, Asunción, German Colonies South | Grund Paraguay",
    "de": "Leben in Paraguay: Klima, Asunción, deutsche Kolonien im Süden | Grund Paraguay",
}

ZHIZN_PROSE = {
    "ru": '''
    <p>Климат Асунсьона — субтропический, с выраженным контрастом лета и зимы. По усреднённым
    данным метеорологических агрегаторов, летние месяцы (январь) держат дневной максимум около
    32–33°C, зимние (июль, самый холодный месяц) — 14–22°C днём с более прохладными ночами;
    годовая норма осадков — около 1629 мм. Разные агрегаторы дают чуть отличающиеся цифры,
    поэтому здесь и стоит держать диапазон, а не единственное число.</p>

    <p>Сам Асунсьон делится на 68 официальных районов (barrios); население города по переписи
    2022 года — 462 241 человек, агломерации Гран-Асунсьон — свыше 2,4 млн, это около 40%
    всего населения страны. Независимого (не риелторского) обзора конкретных районов по
    качеству жизни найти не удалось — весь подобный контент в открытом доступе оказался
    маркетингом агентств недвижимости и экспат-сервисов, поэтому рейтинга «топ-5 районов для
    жизни» здесь нет.</p>

    <p>Юг страны — отдельная и не туристическая причина, почему Парагвай может звучать роднее,
    чем кажется на первый взгляд. Немецкая колонизация региона Итапуа началась с посёлка
    Хоэнау, основанного в 1900 году (решение о выделении земли принято ещё в 1898-м), позже —
    Облигадо (1912); оба входят в кластер «Colonias Unidas». В 1930–40-х к немецким
    переселенцам добавились польские, украинские и русские колонисты, с 1958 года — японские.
    Это одна сложившаяся община с почти вековой историей смешанной европейской иммиграции, а
    не абстрактная «Германия в Южной Америке».</p>

    <p>Отдельная и более многочисленная община — около 25 000 меннонитов в департаменте
    Бокерон, в регионе Чако. Это потомки голландско-прусских переселенцев, которые попали в
    Парагвай именно из России — сначала бежав от отмены освобождения от воинской службы в
    XIX веке, затем от сталинской коллективизации в XX веке. Важно не путать эти два
    немецкоязычных сообщества между собой в разговоре с клиентом: колонии юга (Итапуа) — это
    столетняя смешанная европейская колонизация, а меннониты Чако — отдельная община с
    собственной, именно российской предысторией.</p>

    <p>Эта страница — стартовая карта, а не гид по аренде жилья: за конкретным районом,
    климатом конкретного месяца переезда или укладом жизни в интересующем регионе разумнее
    обращаться на бесплатную консультацию, а не полагаться на усреднённые цифры
    агрегаторов.</p>''',
    "es": '''
    <p>El clima de Asunción es subtropical, con un contraste marcado entre verano e invierno. Según los
    promedios de los agregadores meteorológicos, los meses de verano (enero) tienen una máxima
    diurna de alrededor de 32–33°C, y los de invierno (julio, el mes más frío) de 14–22°C durante el
    día, con noches más frescas; la norma anual de precipitaciones es de unos 1.629 mm. Distintos
    agregadores dan cifras algo diferentes, por eso aquí conviene manejar un rango y no una cifra
    única.</p>

    <p>La propia Asunción se divide en 68 barrios oficiales; la población de la ciudad según el censo de
    2022 es de 462.241 habitantes, y la de la aglomeración del Gran Asunción supera los 2,4 millones,
    alrededor del 40% de toda la población del país. No fue posible encontrar una reseña independiente
    (no inmobiliaria) de barrios concretos por calidad de vida — todo ese tipo de contenido en acceso
    abierto resultó ser marketing de agencias inmobiliarias y servicios para expatriados, por lo que
    aquí no hay un ranking de «los 5 mejores barrios para vivir».</p>

    <p>El sur del país es una razón aparte, y nada turística, por la que Paraguay puede sonar más
    familiar de lo que parece a primera vista. La colonización alemana de la región de Itapúa comenzó
    con el pueblo de Hohenau, fundado en 1900 (la decisión de asignar las tierras se tomó ya en
    1898); más tarde, Obligado (1912); ambos forman parte del clúster «Colonias Unidas». En los años
    1930–40 se sumaron a los colonos alemanes colonos polacos, ucranianos y rusos, y desde 1958,
    japoneses. Es una comunidad consolidada con casi un siglo de historia de inmigración europea
    mixta, no una «Alemania abstracta en Sudamérica».</p>

    <p>Otra comunidad, aparte y más numerosa, son los cerca de 25.000 menonitas del departamento de
    Boquerón, en la región del Chaco. Son descendientes de colonos neerlandés-prusianos que llegaron
    a Paraguay precisamente desde Rusia — primero huyendo de la abolición de la exención del servicio
    militar en el siglo XIX, y luego de la colectivización estalinista en el siglo XX. Es importante
    no confundir estas dos comunidades de habla alemana al hablar con un cliente: las colonias del sur
    (Itapúa) son una colonización europea mixta de un siglo, y los menonitas del Chaco son una
    comunidad aparte con su propia prehistoria, precisamente rusa.</p>

    <p>Esta página es un mapa de partida, no una guía de alquiler de vivienda: para conocer un barrio
    concreto, el clima de un mes concreto de la mudanza o las costumbres de la región que interesa, lo
    más razonable es acudir a una consulta gratuita, no depender de cifras promediadas de agregadores.</p>''',
    "en": '''
    <p>Asunción's climate is subtropical, with a marked contrast between summer and winter. According to
    averaged data from weather aggregators, the summer months (January) hold a daytime high of around
    32–33°C, while winter (July, the coldest month) runs 14–22°C during the day with cooler nights;
    annual rainfall averages around 1,629 mm. Different aggregators give slightly different figures,
    which is why it makes sense to give a range here rather than a single number.</p>

    <p>Asunción itself is divided into 68 official neighborhoods (barrios); the city's population per
    the 2022 census is 462,241, and Greater Asunción's is over 2.4 million — about 40% of the
    country's entire population. We couldn't find an independent (non-realtor) review of specific
    neighborhoods by quality of life — all similar content in the open web turned out to be marketing
    from real estate agencies and expat services, so there's no "top 5 neighborhoods to live in"
    ranking here.</p>

    <p>The south of the country is a separate, non-touristy reason why Paraguay might sound more
    familiar than it first appears. German colonization of the Itapúa region began with the town of
    Hohenau, founded in 1900 (the land-grant decision was made back in 1898); later, Obligado (1912);
    both are part of the "Colonias Unidas" cluster. In the 1930s–40s, Polish, Ukrainian, and Russian
    settlers joined the German colonists, followed by Japanese settlers from 1958. This is one
    established community with nearly a century of mixed European immigration history, not an
    abstract "Germany in South America."</p>

    <p>A separate and larger community is the roughly 25,000 Mennonites in Boquerón department, in the
    Chaco region. They're descendants of Dutch-Prussian settlers who arrived in Paraguay specifically
    from Russia — first fleeing the abolition of military service exemptions in the 19th century,
    then Stalinist collectivization in the 20th. It's important not to mix up these two
    German-speaking communities when talking with a client: the southern colonies (Itapúa) are a
    century-old mixed European colonization, while the Mennonites of the Chaco are a separate
    community with their own, specifically Russian, backstory.</p>

    <p>This page is a starting map, not a housing rental guide: for a specific neighborhood, the climate
    of a specific month of relocation, or the way of life in a region you're interested in, it makes
    more sense to book a free consultation than to rely on averaged aggregator figures.</p>''',
    "de": '''
    <p>Das Klima von Asunción ist subtropisch, mit einem ausgeprägten Kontrast zwischen Sommer und
    Winter. Nach gemittelten Daten von Wetteraggregatoren liegt das Tageshöchst in den Sommermonaten
    (Januar) bei etwa 32–33 °C, im Winter (Juli, der kälteste Monat) tagsüber bei 14–22 °C mit
    kühleren Nächten; die jährliche Niederschlagsmenge beträgt im Schnitt etwa 1.629 mm. Verschiedene
    Aggregatoren liefern leicht abweichende Zahlen, deshalb lohnt sich hier eine Spanne statt einer
    einzelnen Zahl.</p>

    <p>Asunción selbst gliedert sich in 68 offizielle Stadtviertel (Barrios); die Einwohnerzahl der Stadt
    liegt laut Volkszählung 2022 bei 462.241, die des Ballungsraums Groß-Asunción bei über 2,4
    Millionen — rund 40 % der gesamten Landesbevölkerung. Eine unabhängige (nicht von
    Immobilienmaklern stammende) Übersicht konkreter Stadtviertel nach Lebensqualität ließ sich nicht
    finden — sämtliche entsprechenden frei zugänglichen Inhalte erwiesen sich als Marketing von
    Immobilienagenturen und Expat-Diensten, deshalb gibt es hier kein Ranking „Top 5 Stadtviertel zum
    Leben".</p>

    <p>Der Süden des Landes ist ein eigener, nicht touristischer Grund, warum Paraguay vertrauter klingen
    kann, als es auf den ersten Blick scheint. Die deutsche Kolonisierung der Region Itapúa begann mit
    dem Ort Hohenau, gegründet 1900 (die Entscheidung zur Landzuteilung fiel bereits 1898); später kam
    Obligado (1912) hinzu; beide gehören zum Cluster „Colonias Unidas". In den 1930er–40er-Jahren kamen
    zu den deutschen Siedlern polnische, ukrainische und russische Kolonisten hinzu, ab 1958
    japanische. Das ist eine gewachsene Gemeinschaft mit fast einem Jahrhundert gemischter
    europäischer Einwanderungsgeschichte, nicht ein abstraktes „Deutschland in Südamerika".</p>

    <p>Eine eigenständige und zahlenmäßig größere Gemeinschaft sind die rund 25.000 Mennoniten im
    Departement Boquerón, in der Region Chaco. Sie sind Nachkommen niederländisch-preußischer Siedler,
    die genau aus Russland nach Paraguay kamen — zunächst auf der Flucht vor der Abschaffung der
    Befreiung vom Wehrdienst im 19. Jahrhundert, dann vor der stalinistischen Kollektivierung im 20.
    Jahrhundert. Im Gespräch mit einem Mandanten ist es wichtig, diese beiden deutschsprachigen
    Gemeinschaften nicht zu verwechseln: Die Kolonien im Süden (Itapúa) sind eine jahrhundertealte
    gemischte europäische Kolonisierung, die Mennoniten im Chaco dagegen eine eigenständige
    Gemeinschaft mit einer eigenen, genau russischen Vorgeschichte.</p>

    <p>Diese Seite ist eine Startkarte, kein Ratgeber für die Wohnungssuche: Für ein konkretes
    Stadtviertel, das Klima eines bestimmten Umzugsmonats oder die Lebensweise in der interessierenden
    Region ist es sinnvoller, eine kostenlose Beratung in Anspruch zu nehmen, als sich auf gemittelte
    Aggregator-Zahlen zu verlassen.</p>''',
}


def build_zhizn():
    for lang in LANGS:
        lead = DESC[lang]["zhizn-v-paragvae"]
        body = f'''
{crumbs(lang, BREADCRUMB_LABEL[lang]["zhizn-v-paragvae"])}
{hero(H1_ZHIZN[lang], lead)}
<section style="padding-top:0;">
  <div class="prose">
    {ZHIZN_PROSE[lang]}
  </div>
</section>
'''
        page("zhizn-v-paragvae", lang, TITLE_ZHIZN[lang], lead, body,
             extra_schema=schema_crumbs(lang, BREADCRUMB_LABEL[lang]["zhizn-v-paragvae"], "zhizn-v-paragvae"))

# ==================================================== 3. СТОИМОСТЬ ЖИЗНИ

H1_STZH = {
    "ru": "Сколько стоит жить в Парагвае", "es": "Cuánto cuesta vivir en Paraguay",
    "en": "How Much It Costs to Live in Paraguay", "de": "Was das Leben in Paraguay kostet",
}
TITLE_STZH = {
    "ru": "Стоимость жизни в Парагвае: аренда, продукты, коммуналка | Grund Paraguay",
    "es": "Costo de vida en Paraguay: alquiler, comida, servicios | Grund Paraguay",
    "en": "Cost of Living in Paraguay: Rent, Food, Utilities | Grund Paraguay",
    "de": "Lebenshaltungskosten in Paraguay: Miete, Essen, Nebenkosten | Grund Paraguay",
}
CALLOUT_LABEL = {"ru": "Методологическая оговорка", "es": "Aclaración metodológica",
                  "en": "Methodological note", "de": "Methodischer Hinweis"}


def build_stoimost_zhizni():
    for lang in LANGS:
        l = L(lang)
        lead = DESC[lang]["stoimost-zhizni"]

        if lang == "ru":
            callout = (f'<a href="{l["terminologiya"]}#numbeo">Numbeo</a> и '
                        f'<a href="{l["terminologiya"]}#expatistan">Expatistan</a>, на которые ссылается эта '
                        'страница, — это не официальная статистика, а краудсорсинговые данные с небольшой '
                        'выборкой по Асунсьону: пользователи сами вносят цены, которые видят. Относитесь к '
                        'цифрам ниже как к ориентиру для планирования бюджета, а не как к точному прайс-листу.')
            prose = f'''
    <p>По данным Numbeo (снимок на начало августа 2026 года, 57 авторов): аренда
    однокомнатной квартиры в центре Асунсьона — около 3,65 млн гуарани в месяц, за пределами
    центра — около 2,21 млн; расходы одного человека без учёта аренды — около 599 USD в
    месяц, семьи из четырёх человек — около 2242 USD.</p>

    <p>По данным Expatistan: месячные расходы семьи из четырёх человек — около 15,9 млн
    гуарани, одного человека — около 7,8 млн; сам сервис отмечает, что его оценки основаны на
    «небольшом объёме данных». По этому же источнику, Асунсьон примерно на 16% дешевле
    Буэнос-Айреса.</p>

    <p>Официальной государственной статистики о стоимости потребительской корзины (со стороны
    Центробанка Парагвая или национального статистического ведомства) в открытом доступе
    найти не удалось — такие данные были бы надёжнее Numbeo и Expatistan.</p>

    <p>Важно не путать эту страницу с <a href="{l['stoimost']}">«Стоимостью и тарифами»</a> на
    сайте — там речь о цене наших услуг и о государственных пошлинах DNM, здесь — о
    повседневных расходах на жизнь в стране, это две разные «стоимости». Цифры в гуарани
    удобнее сверять с актуальным курсом на странице
    <a href="{l['terminologiya']}#kurs-valyuty">«Терминология»</a>.</p>'''
        elif lang == "es":
            callout = ('Numbeo y Expatistan, en los que se basa esta página, no son estadísticas '
                       'oficiales, sino datos colaborativos («crowdsourcing») con una muestra pequeña para '
                       'Asunción: los propios usuarios cargan los precios que observan. Tome las cifras de '
                       'abajo como una referencia para planificar el presupuesto, no como una lista de '
                       'precios exacta.')
            prose = f'''
    <p>Según Numbeo (captura de principios de agosto de 2026, 57 colaboradores): el alquiler de un
    apartamento de un ambiente en el centro de Asunción ronda los 3,65 millones de guaraníes al mes, y
    fuera del centro, unos 2,21 millones; el gasto de una persona sin contar el alquiler ronda los 599
    USD al mes, y el de una familia de cuatro, unos 2.242 USD.</p>

    <p>Según Expatistan: el gasto mensual de una familia de cuatro personas ronda los 15,9 millones de
    guaraníes, y el de una persona, unos 7,8 millones; el propio servicio señala que sus estimaciones
    se basan en «un volumen reducido de datos». Según esta misma fuente, Asunción es aproximadamente
    un 16% más barata que Buenos Aires.</p>

    <p>No fue posible encontrar en acceso abierto estadísticas oficiales del Estado sobre el costo de la
    canasta básica de consumo (del Banco Central de Paraguay o del organismo estadístico nacional) —
    este tipo de datos sería más confiable que Numbeo y Expatistan.</p>

    <p>Es importante no confundir esta página con <a href="{l['stoimost']}">«Costos y tarifas»</a> del sitio — allí
    se habla del precio de nuestros servicios y de las tasas estatales de la DNM; aquí, de los gastos
    cotidianos de vivir en el país — son dos «costos» distintos. Las cifras en guaraníes conviene
    cotejarlas con el tipo de cambio actual en la página <a href="{l['terminologiya']}#kurs-valyuty">«Terminología»</a>.</p>'''
        elif lang == "en":
            callout = ('Numbeo and Expatistan, which this page draws on, aren\'t official statistics — '
                       'they\'re crowdsourced data with a small sample for Asunción: users enter the '
                       'prices they see themselves. Treat the figures below as a budgeting guide, not an '
                       'exact price list.')
            prose = f'''
    <p>Per Numbeo (snapshot from early August 2026, 57 contributors): renting a one-bedroom apartment in
    central Asunción runs around 3.65 million guaraníes a month, and outside the center, around 2.21
    million; one person's expenses excluding rent run around $599 a month, and a family of four's
    around $2,242.</p>

    <p>Per Expatistan: a family of four's monthly expenses run around 15.9 million guaraníes, and one
    person's around 7.8 million; the service itself notes its estimates are based on "a small amount
    of data." By the same source, Asunción is roughly 16% cheaper than Buenos Aires.</p>

    <p>We couldn't find official government statistics on the cost of the basic consumer basket (from
    Paraguay's Central Bank or the national statistics agency) in the open web — such data would be
    more reliable than Numbeo and Expatistan.</p>

    <p>It's important not to confuse this page with <a href="{l['stoimost']}">Pricing</a> on the site — that page
    covers the price of our services and DNM government fees, while this one covers everyday living
    expenses in the country — two different kinds of "cost." Figures in guaraníes are easiest to check
    against the current exchange rate on the <a href="{l['terminologiya']}#kurs-valyuty">Terminology</a> page.</p>'''
        else:  # de
            callout = ('Numbeo und Expatistan, auf die sich diese Seite stützt, sind keine amtliche '
                       'Statistik, sondern Crowdsourcing-Daten mit einer kleinen Stichprobe für Asunción: '
                       'Die Nutzer tragen die Preise, die sie selbst sehen, eigenständig ein. Betrachten '
                       'Sie die Zahlen unten als Orientierung für die Budgetplanung, nicht als exakte '
                       'Preisliste.')
            prose = f'''
    <p>Nach Numbeo (Stand Anfang August 2026, 57 Beitragende): Die Miete für eine Einzimmerwohnung im
    Zentrum von Asunción liegt bei etwa 3,65 Millionen Guaraní im Monat, außerhalb des Zentrums bei
    etwa 2,21 Millionen; die Ausgaben einer Person ohne Miete liegen bei etwa 599 USD im Monat, die
    einer vierköpfigen Familie bei etwa 2.242 USD.</p>

    <p>Nach Expatistan: Die monatlichen Ausgaben einer vierköpfigen Familie liegen bei etwa 15,9
    Millionen Guaraní, die einer Einzelperson bei etwa 7,8 Millionen; der Dienst selbst weist darauf
    hin, dass seine Schätzungen auf „einer geringen Datenmenge" beruhen. Nach derselben Quelle ist
    Asunción etwa 16 % günstiger als Buenos Aires.</p>

    <p>Amtliche staatliche Statistiken zu den Kosten eines Warenkorbs (von der Zentralbank Paraguays oder
    der nationalen Statistikbehörde) waren frei zugänglich nicht auffindbar — solche Daten wären
    zuverlässiger als Numbeo und Expatistan.</p>

    <p>Diese Seite sollte nicht mit <a href="{l['stoimost']}">„Kosten und Tarife"</a> auf der Website verwechselt
    werden — dort geht es um den Preis unserer Dienstleistungen und die staatlichen Gebühren der DNM,
    hier um die laufenden Lebenshaltungskosten im Land — das sind zwei unterschiedliche „Kosten".
    Beträge in Guaraní lassen sich am besten mit dem aktuellen Wechselkurs auf der Seite
    <a href="{l['terminologiya']}#kurs-valyuty">„Terminologie"</a> abgleichen.</p>'''

        body = f'''
{crumbs(lang, BREADCRUMB_LABEL[lang]["stoimost-zhizni"])}
{hero(H1_STZH[lang], lead)}
<section style="padding-top:0;">
  <div class="prose">
    <div class="callout">
      <span class="callout-label">{CALLOUT_LABEL[lang]}</span>
      {callout}
    </div>

    {prose}
  </div>
</section>
'''
        page("stoimost-zhizni", lang, TITLE_STZH[lang], lead, body,
             extra_schema=schema_crumbs(lang, BREADCRUMB_LABEL[lang]["stoimost-zhizni"], "stoimost-zhizni"))

# ============================================ 4. НАЛОГИ ДЛЯ ИНОСТРАНЦЕВ

H1_NALOGI = {
    "ru": "Налоги для иностранцев в Парагвае", "es": "Impuestos para extranjeros en Paraguay",
    "en": "Taxes for Foreigners in Paraguay", "de": "Steuern für Ausländer in Paraguay",
}
TITLE_NALOGI = {
    "ru": "Налоги в Парагвае для иностранцев: ставки IRE, IVA, IRP | Grund Paraguay",
    "es": "Impuestos en Paraguay para extranjeros: IRE, IVA, IRP | Grund Paraguay",
    "en": "Taxes in Paraguay for Foreigners: IRE, IVA, IRP Rates | Grund Paraguay",
    "de": "Steuern in Paraguay für Ausländer: IRE, IVA, IRP | Grund Paraguay",
}

NALOGI_PROSE = {
    "ru": '''
    <p>Налоговая система Парагвая основана на законе Ley N° 6380/2019; сам налоговый орган с
    недавнего времени официально называется DNIT (правопреемник прежней SET) — это то
    учреждение, куда физически подаются декларации и с которым взаимодействует бухгалтер
    после получения <a href="{terminologiya}#ruc">RUC</a>.</p>

    <p>Основные ставки на середину 2026 года: налог на прибыль предприятий,
    <a href="{terminologiya}#ire">IRE</a>, — 10%; НДС,
    <a href="{terminologiya}#iva">IVA</a>, — 10% по общей ставке и 5% по льготной; налог
    на дивиденды (IDU) — 8% для налоговых резидентов Парагвая и 15% для нерезидентов; налог на
    доходы физических лиц, <a href="{terminologiya}#irp">IRP</a>, от личных услуг —
    ступенчато 8/9/10% в зависимости от суммы, с годовой декларацией в марте.</p>

    <p>Один принцип стоит понимать заранее, потому что он напрямую касается тех, кто
    продолжает получать доход из-за рубежа после переезда: налогообложение в Парагвае в целом
    устроено по территориальному принципу — доходы физических лиц-резидентов из зарубежных
    источников, как правило, не входят в налоговую базу IRP. Прямого подтверждения этой нормы
    в первичном тексте закона мы не нашли — воспринимать как вероятную практику, а не как
    гарантию, и уточнять применительно к своей ситуации отдельно.</p>

    <p>Отдельно — вопрос о соглашении об избежании двойного налогообложения: между Парагваем
    и Россией на момент проверки в открытых источниках обнаружить его не удалось. Это не
    означает гарантированно, что его не существует — но при его отсутствии доход российского
    происхождения у резидента Парагвая по умолчанию может облагаться налогом в обеих
    юрисдикциях без взаимного зачёта. Для Парагвая подтверждены соглашения как минимум с
    Чили, Уругваем, Германией, Бельгией, Тайванем, ОАЭ и Катаром — по каждому конкретному
    случаю имеет смысл отдельная консультация, а не общий вывод по этой странице.</p>''',
    "es": '''
    <p>El sistema tributario de Paraguay se basa en la Ley N.° 6380/2019; el propio organismo
    tributario se llama oficialmente, desde hace poco, DNIT (sucesor de la antigua SET) — es la
    entidad ante la que físicamente se presentan las declaraciones y con la que trata el contador
    después de obtener el <a href="{terminologiya}#ruc">RUC</a>.</p>

    <p>Tasas principales a mediados de 2026: el impuesto a la renta empresarial,
    <a href="{terminologiya}#ire">IRE</a>, — 10%; el IVA, <a href="{terminologiya}#iva">IVA</a>, — 10% en la tasa
    general y 5% en la reducida; el impuesto a los dividendos (IDU) — 8% para residentes fiscales de
    Paraguay y 15% para no residentes; el impuesto a la renta de las personas físicas,
    <a href="{terminologiya}#irp">IRP</a>, sobre servicios personales — escalonado en 8/9/10% según el monto,
    con declaración anual en marzo.</p>

    <p>Conviene entender un principio de antemano, porque afecta directamente a quienes siguen
    percibiendo ingresos del exterior después de mudarse: la tributación en Paraguay en general se
    rige por el principio territorial — los ingresos de personas físicas residentes provenientes de
    fuentes extranjeras, por regla general, no forman parte de la base imponible del IRP. No
    encontramos una confirmación directa de esta norma en el texto primario de la ley — hay que
    tomarlo como una práctica probable, no como una garantía, y consultarlo por separado según la
    situación de cada uno.</p>

    <p>Aparte — la cuestión del convenio para evitar la doble imposición: entre Paraguay y Rusia, al
    momento de la revisión, no fue posible encontrarlo en fuentes abiertas. Esto no significa con
    certeza que no exista — pero, en su ausencia, los ingresos de origen ruso de un residente en
    Paraguay pueden, por defecto, estar sujetos a impuestos en ambas jurisdicciones sin compensación
    mutua. Para Paraguay están confirmados convenios al menos con Chile, Uruguay, Alemania, Bélgica,
    Taiwán, los EAU y Catar — para cada caso concreto tiene sentido una consulta particular, no una
    conclusión general de esta página.</p>''',
    "en": '''
    <p>Paraguay's tax system is based on Law No. 6380/2019; the tax authority itself has recently been
    officially renamed DNIT (successor to the former SET) — this is the agency where returns are
    physically filed and that an accountant deals with after obtaining an <a href="{terminologiya}#ruc">RUC</a>.</p>

    <p>Main rates as of mid-2026: corporate income tax, <a href="{terminologiya}#ire">IRE</a>, — 10%; VAT,
    <a href="{terminologiya}#iva">IVA</a>, — 10% standard rate and 5% reduced rate; dividend tax (IDU) — 8% for
    Paraguayan tax residents and 15% for non-residents; personal income tax,
    <a href="{terminologiya}#irp">IRP</a>, on personal services — tiered at 8/9/10% depending on the amount,
    with an annual return due in March.</p>

    <p>One principle is worth understanding up front, because it directly affects anyone who keeps
    earning income from abroad after relocating: taxation in Paraguay generally follows the
    territorial principle — foreign-source income of individual residents generally isn't included in
    the IRP tax base. We didn't find direct confirmation of this rule in the primary text of the
    law — treat it as likely practice rather than a guarantee, and check it separately for your
    specific situation.</p>

    <p>Separately — the question of a double taxation treaty: between Paraguay and Russia, at the time
    of checking, none could be found in open sources. That doesn't guarantee one doesn't exist — but
    in its absence, income of Russian origin for a Paraguayan resident may by default be taxed in
    both jurisdictions without mutual offset. For Paraguay, treaties are confirmed with at least
    Chile, Uruguay, Germany, Belgium, Taiwan, the UAE, and Qatar — for any specific case, a separate
    consultation makes more sense than a general conclusion drawn from this page.</p>''',
    "de": '''
    <p>Das paraguayische Steuersystem beruht auf dem Gesetz Ley N.° 6380/2019; die Steuerbehörde selbst
    heißt seit Kurzem offiziell DNIT (Nachfolgerin der früheren SET) — das ist die Stelle, bei der
    Erklärungen physisch eingereicht werden und mit der der Buchhalter nach Erhalt der
    <a href="{terminologiya}#ruc">RUC</a> zu tun hat.</p>

    <p>Wichtigste Sätze Mitte 2026: die Unternehmenssteuer, <a href="{terminologiya}#ire">IRE</a>, — 10 %; die
    Mehrwertsteuer, <a href="{terminologiya}#iva">IVA</a>, — 10 % zum allgemeinen Satz und 5 % zum ermäßigten
    Satz; die Dividendensteuer (IDU) — 8 % für Steueransässige Paraguays und 15 % für Nichtansässige;
    die Einkommensteuer natürlicher Personen, <a href="{terminologiya}#irp">IRP</a>, auf persönliche
    Dienstleistungen — gestaffelt bei 8/9/10 % je nach Betrag, mit jährlicher Erklärung im März.</p>

    <p>Ein Prinzip lohnt sich, im Voraus zu verstehen, weil es diejenigen direkt betrifft, die nach dem
    Umzug weiterhin Einkommen aus dem Ausland beziehen: Die Besteuerung in Paraguay folgt insgesamt
    dem Territorialprinzip — Einkünfte natürlicher Personen mit Wohnsitz in Paraguay aus
    ausländischen Quellen gehören in der Regel nicht zur Bemessungsgrundlage der IRP. Eine direkte
    Bestätigung dieser Regel im Primärtext des Gesetzes haben wir nicht gefunden — als wahrscheinliche
    Praxis zu verstehen, nicht als Garantie, und für die eigene Situation gesondert zu klären.</p>

    <p>Gesondert — die Frage eines Doppelbesteuerungsabkommens: Zwischen Paraguay und Russland ließ sich
    zum Zeitpunkt der Prüfung in offenen Quellen keines finden. Das bedeutet nicht mit Sicherheit,
    dass keines existiert — aber ohne ein solches Abkommen kann Einkommen russischer Herkunft bei
    einem in Paraguay Ansässigen standardmäßig in beiden Rechtsordnungen besteuert werden, ohne
    gegenseitige Anrechnung. Für Paraguay sind Abkommen mindestens mit Chile, Uruguay, Deutschland,
    Belgien, Taiwan, den VAE und Katar bestätigt — für jeden konkreten Fall lohnt sich eine gesonderte
    Beratung, keine allgemeine Schlussfolgerung aus dieser Seite.</p>''',
}


def build_nalogi():
    for lang in LANGS:
        l = L(lang)
        lead = DESC[lang]["nalogi-inostrantsev"]
        body = f'''
{crumbs(lang, BREADCRUMB_LABEL[lang]["nalogi-inostrantsev"])}
{hero(H1_NALOGI[lang], lead)}
<section style="padding-top:0;">
  <div class="prose">
    {NALOGI_PROSE[lang].format(terminologiya=l["terminologiya"])}
  </div>
</section>
'''
        page("nalogi-inostrantsev", lang, TITLE_NALOGI[lang], lead, body,
             extra_schema=schema_crumbs(lang, BREADCRUMB_LABEL[lang]["nalogi-inostrantsev"], "nalogi-inostrantsev"))

# ====================================== 5. БАНКИ, СЧЕТА И ПЕРЕВОДЫ ДЕНЕГ

H1_BANKI = {
    "ru": "Банки, счета и переводы денег", "es": "Bancos, cuentas y transferencias de dinero",
    "en": "Banking, Accounts, and Money Transfers", "de": "Banken, Konten und Geldtransfers",
}
TITLE_BANKI = {
    "ru": "Банки и переводы денег в Парагвае для россиян | Grund Paraguay",
    "es": "Bancos y transferencias de dinero en Paraguay para rusos | Grund Paraguay",
    "en": "Banking and Money Transfers in Paraguay for Russians | Grund Paraguay",
    "de": "Banken und Geldtransfers in Paraguay für Russen | Grund Paraguay",
}

BANKI_PROSE = {
    "ru": '''
    <p>Банковские ограничения, связанные с санкциями, продолжают меняться в течение всего
    2026 года — при планировании стоит сверяться с актуальным статусом отдельно.</p>

    <p>Начать стоит с позиции самого Центробанка Парагвая (BCP): криптовалюты там официально
    не имеют статуса законного платёжного средства, не регистрируются и не авторизуются
    регулятором и прямо называются высокорисковыми активами. С 2026 фискального года в стране
    действует обязательная отчётность по криптоактивам: платформы обязаны отчитываться через
    налоговую систему <a href="{terminologiya}#marangatu">Marangatú</a>, а резиденты и
    юрлица обязаны декларировать операции, если их годовой оборот превышает 5000 USD; первые
    такие декларации нужно будет подать за 2026 год в начале 2027-го, штраф за просрочку —
    около 130 USD. Вывод из этого прямой: крипта и стейблкоины — не безрисковый обходной путь
    перевода денег, а сама область, которая попадает под всё более плотное регулирование.</p>

    <p>Отдельно стоит закрыть репутационный вопрос: по состоянию на середину 2026 года
    Парагвай не входит в «серый список» FATF (международной группы по противодействию
    отмыванию денег) — это прямо опровергает возможные опасения о повышенных банковских
    рисках именно из-за статуса страны.</p>

    <p>Что касается открытия счёта — по примеру одного из банков (Itaú Paraguay, через данные
    финтех-сервиса Wise, не первоисточник банка) для валютного счёта на момент проверки
    упоминался минимальный средний остаток около 6000 USD для расчётного счёта и 2500 USD для
    сберегательного. Это стоит воспринимать именно как пример условий одного банка, а не как
    общее правило для всех — у разных банков Парагвая требования отличаются, и точный список
    нужно уточнять непосредственно перед открытием счёта.</p>

    <p>Отдельный практический контекст — санкционные ограничения на переводы из России. SWIFT
    официально отключил Сбербанк ещё 3 июня 2022 года. Дальше ограничения расширялись: 19-й
    пакет санкций ЕС (23.10.2025) добавил под транзакционный запрет ещё пять российских
    банков, включая Альфа-Банк и МТС Банк, а с 25 января 2026 года ограничения распространились
    также на систему СБП и платёжную систему «Мир»; 20-й пакет санкций ЕС (23.04.2026) ввёл
    полный запрет на рублёвый стейблкоин и на поддержку разработки цифрового рубля Центробанка
    России, добавив ещё двадцать российских банков под ограничения. Перевод денег из России в
    Парагвай — тема, которая требует индивидуального разбора конкретной ситуации на
    консультации, а не общей инструкции, применимой ко всем.</p>''',
    "es": '''
    <p>Las restricciones bancarias vinculadas a las sanciones siguen cambiando a lo largo de todo 2026 —
    al planificar, conviene verificar por separado el estado actual.</p>

    <p>Conviene empezar por la postura del propio Banco Central de Paraguay (BCP): allí, las
    criptomonedas no tienen oficialmente estatus de medio de pago legal, no se registran ni son
    autorizadas por el regulador, y se las califica directamente como activos de alto riesgo. Desde
    el año fiscal 2026 rige en el país la declaración obligatoria de criptoactivos: las plataformas
    deben reportar a través del sistema tributario <a href="{terminologiya}#marangatu">Marangatú</a>, y los
    residentes y personas jurídicas deben declarar las operaciones cuando su volumen anual supere los
    5.000 USD; las primeras declaraciones de este tipo deberán presentarse por el año 2026 a
    comienzos de 2027, con una multa por demora de unos 130 USD. La conclusión es directa: las
    criptomonedas y las stablecoins no son una vía sin riesgo para transferir dinero, sino
    precisamente el área que queda bajo una regulación cada vez más estricta.</p>

    <p>Aparte, vale la pena cerrar la cuestión de reputación: a mediados de 2026, Paraguay no figura en
    la «lista gris» del GAFI/FATF (el grupo internacional contra el lavado de dinero) — esto desmiente
    directamente posibles temores sobre un riesgo bancario elevado precisamente por el estatus del
    país.</p>

    <p>En cuanto a abrir una cuenta — según el ejemplo de un banco (Itaú Paraguay, a través de datos del
    servicio fintech Wise, no la fuente primaria del banco), para una cuenta en moneda extranjera se
    mencionaba, al momento de la revisión, un saldo medio mínimo de unos 6.000 USD para la cuenta
    corriente y 2.500 USD para la cuenta de ahorro. Esto hay que tomarlo justamente como ejemplo de
    las condiciones de un banco, no como una regla general para todos — los distintos bancos de
    Paraguay tienen requisitos diferentes, y la lista exacta debe confirmarse justo antes de abrir la
    cuenta.</p>

    <p>Otro contexto práctico aparte son las restricciones por sanciones a las transferencias desde
    Rusia. SWIFT desconectó oficialmente a Sberbank ya el 3 de junio de 2022. Después las
    restricciones se ampliaron: el 19.º paquete de sanciones de la UE (23.10.2025) sumó a otros cinco
    bancos rusos a la prohibición transaccional, incluidos Alfa-Bank y MTS Bank, y desde el 25 de
    enero de 2026 las restricciones se extendieron también al sistema SBP y al sistema de pagos
    «Mir»; el 20.º paquete de sanciones de la UE (23.04.2026) impuso una prohibición total a la
    stablecoin en rublos y al apoyo al desarrollo del rublo digital del Banco Central de Rusia,
    sumando otros veinte bancos rusos a las restricciones. Transferir dinero desde Rusia a Paraguay es
    un tema que requiere un análisis individual de la situación concreta en la consulta, no una
    instrucción general aplicable a todos.</p>''',
    "en": '''
    <p>Sanctions-related banking restrictions keep changing throughout 2026 — when planning, it's worth
    checking the current status separately.</p>

    <p>It's worth starting with the position of the Central Bank of Paraguay (BCP) itself:
    cryptocurrencies there officially have no status as legal tender, aren't registered or authorized
    by the regulator, and are explicitly labeled high-risk assets. Since fiscal year 2026, mandatory
    reporting on crypto assets has applied in the country: platforms must report through the tax
    system <a href="{terminologiya}#marangatu">Marangatú</a>, and residents and legal entities must declare
    transactions if their annual turnover exceeds $5,000; the first such returns will need to be
    filed for 2026, in early 2027, with a late-filing penalty of about $130. The takeaway is direct:
    crypto and stablecoins aren't a risk-free workaround for moving money — they're an area falling
    under increasingly tight regulation.</p>

    <p>Separately, it's worth settling the reputational question: as of mid-2026, Paraguay isn't on the
    FATF (the international anti-money-laundering group) "grey list" — this directly refutes any
    concerns about elevated banking risk specifically because of the country's status.</p>

    <p>As for opening an account — going by one bank's example (Itaú Paraguay, via data from the fintech
    service Wise, not the bank's own primary source), at the time of checking, a foreign-currency
    account required a minimum average balance of around $6,000 for a checking account and $2,500 for
    a savings account. Treat this specifically as an example of one bank's terms, not a general rule
    for all — different banks in Paraguay have different requirements, and the exact list needs to be
    confirmed right before opening an account.</p>

    <p>A separate practical context is sanctions-related restrictions on transfers from Russia. SWIFT
    officially disconnected Sberbank back on June 3, 2022. Restrictions have since expanded: the EU's
    19th sanctions package (10/23/2025) added five more Russian banks to the transaction ban,
    including Alfa-Bank and MTS Bank, and from January 25, 2026, restrictions also extended to the
    SPFS/SBP system and the "Mir" payment system; the EU's 20th sanctions package (04/23/2026)
    introduced a full ban on the ruble stablecoin and on support for developing the Russian Central
    Bank's digital ruble, adding another twenty Russian banks to the restrictions. Transferring money
    from Russia to Paraguay is a topic that calls for an individual review of the specific situation
    during a consultation, not a general instruction that applies to everyone.</p>''',
    "de": '''
    <p>Sanktionsbedingte Bankbeschränkungen ändern sich das ganze Jahr 2026 über weiter — bei der
    Planung lohnt es sich, den aktuellen Stand gesondert zu prüfen.</p>

    <p>Man sollte mit der Position der Zentralbank Paraguays (BCP) selbst beginnen: Kryptowährungen haben
    dort offiziell keinen Status als gesetzliches Zahlungsmittel, werden vom Regulator nicht
    registriert oder autorisiert und ausdrücklich als hochriskante Vermögenswerte bezeichnet. Seit dem
    Steuerjahr 2026 gilt im Land eine Meldepflicht für Kryptowerte: Plattformen müssen über das
    Steuersystem <a href="{terminologiya}#marangatu">Marangatú</a> berichten, und Ansässige sowie juristische
    Personen müssen Transaktionen deklarieren, wenn ihr Jahresumsatz 5.000 USD übersteigt; die ersten
    derartigen Erklärungen müssen für das Jahr 2026 Anfang 2027 eingereicht werden, die Strafe bei
    Verspätung liegt bei etwa 130 USD. Die Schlussfolgerung daraus ist direkt: Krypto und Stablecoins
    sind kein risikofreier Umweg für Geldtransfers, sondern genau der Bereich, der zunehmend strenger
    reguliert wird.</p>

    <p>Gesondert lohnt sich, die Reputationsfrage zu klären: Mitte 2026 steht Paraguay nicht auf der
    „grauen Liste" der FATF (der internationalen Gruppe gegen Geldwäsche) — das widerlegt direkt
    mögliche Bedenken zu einem erhöhten Bankrisiko allein aufgrund des Status des Landes.</p>

    <p>Was die Kontoeröffnung betrifft — am Beispiel einer Bank (Itaú Paraguay, über Daten des
    Fintech-Dienstes Wise, nicht die Primärquelle der Bank selbst) wurde zum Zeitpunkt der Prüfung für
    ein Fremdwährungskonto ein Mindestdurchschnittssaldo von etwa 6.000 USD für ein Girokonto und
    2.500 USD für ein Sparkonto genannt. Das sollte genau als Beispiel für die Bedingungen einer Bank
    verstanden werden, nicht als allgemeine Regel für alle — verschiedene Banken in Paraguay haben
    unterschiedliche Anforderungen, und die genaue Liste muss unmittelbar vor der Kontoeröffnung
    geklärt werden.</p>

    <p>Ein gesonderter praktischer Kontext sind sanktionsbedingte Beschränkungen bei Überweisungen aus
    Russland. SWIFT hat die Sberbank bereits am 3. Juni 2022 offiziell abgeklemmt. Danach wurden die
    Beschränkungen erweitert: Das 19. Sanktionspaket der EU (23.10.2025) nahm fünf weitere russische
    Banken in das Transaktionsverbot auf, darunter Alfa-Bank und MTS Bank, und seit dem 25. Januar
    2026 erstrecken sich die Beschränkungen auch auf das System SBP und das Zahlungssystem „Mir"; das
    20. Sanktionspaket der EU (23.04.2026) führte ein vollständiges Verbot des Rubel-Stablecoins und
    der Unterstützung der Entwicklung des digitalen Rubels der russischen Zentralbank ein und nahm
    weitere zwanzig russische Banken in die Beschränkungen auf. Geldtransfers aus Russland nach
    Paraguay sind ein Thema, das eine individuelle Prüfung der konkreten Situation im
    Beratungsgespräch erfordert, keine allgemeine, für alle geltende Anleitung.</p>''',
}


def build_banki():
    for lang in LANGS:
        l = L(lang)
        lead = DESC[lang]["banki-perevody"]
        body = f'''
{crumbs(lang, BREADCRUMB_LABEL[lang]["banki-perevody"])}
{hero(H1_BANKI[lang], lead)}
<section style="padding-top:0;">
  <div class="prose">
    {BANKI_PROSE[lang].format(terminologiya=l["terminologiya"])}
  </div>
</section>
'''
        page("banki-perevody", lang, TITLE_BANKI[lang], lead, body,
             extra_schema=schema_crumbs(lang, BREADCRUMB_LABEL[lang]["banki-perevody"], "banki-perevody"))

# =============================================== 6. ВИЗА, ДОКУМЕНТЫ И ВЪЕЗД

H1_VIZA = {
    "ru": "Виза, документы и въезд", "es": "Visa, documentos y entrada",
    "en": "Visa, Documents, and Entry", "de": "Visum, Dokumente und Einreise",
}
TITLE_VIZA = {
    "ru": "Виза и документы для въезда в Парагвай из России | Grund Paraguay",
    "es": "Visa y documentos para entrar a Paraguay desde Rusia | Grund Paraguay",
    "en": "Visa and Documents to Enter Paraguay from Russia | Grund Paraguay",
    "de": "Visum und Dokumente für die Einreise nach Paraguay | Grund Paraguay",
}

VIZA_PROSE = {
    "ru": '''
    <p>Между Россией и Парагваем действует безвизовый режим с 20 октября 2014 года: граждане
    России могут находиться в стране до 90 дней в течение каждых 180 дней без визы (соглашение
    утверждено Парагваем как Ley Nº 5227).</p>

    <p>Обе страны — участники Гаагской конвенции об апостиле: Россия с 1992 года, Парагвай с
    2014-го. Это значит, что документы, выданные в России (в первую очередь — справка о
    несудимости), заверяются апостилем в самой России и не требуют дополнительной консульской
    легализации. Электронный апостиль через портал Госуслуг существует, но насколько
    парагвайская миграционная служба (<a href="{terminologiya}#dnm">DNM</a>) принимает
    его без сопровождающего бумажного документа — прямого подтверждения найти не удалось; на
    практике надёжнее подготовить и бумажный вариант.</p>

    <p>Апостилированные документы, которые не на испанском языке, должны переводиться
    зарегистрированным в Парагвае присяжным переводчиком («Traductor Público matriculado») —
    это не любой переводчик, а специалист с местной регистрацией, и именно такой перевод
    принимают органы.</p>

    <p>По действующему закону в стране три категории пребывания: «спонтанное» (occasional,
    туризм — до 90 дней), временное резидентство и постоянное резидентство. Постоянные
    резиденты, которые получили статус после реформы 2022 года, обязаны продлевать его каждые
    10 лет — это не разовое решение навсегда, а статус, который нужно поддерживать.</p>

    <p>Один практический вопрос официально не урегулирован в открытом доступе: сколько дней
    заявитель на постоянную резиденцию может находиться за пределами Парагвая, пока его дело
    ещё рассматривается. На консультации мы разбираем это индивидуально по фактической
    ситуации клиента.</p>

    <p>Полные чек-листы документов по каждой программе — временная и постоянная резидентура,
    инвесторский путь, гражданство — собраны в разделе <a href="{dokumenty}">«Документы по
    программам»</a>.</p>''',
    "es": '''
    <p>Entre Rusia y Paraguay rige un régimen sin visado desde el 20 de octubre de 2014: los ciudadanos
    rusos pueden permanecer en el país hasta 90 días dentro de cada período de 180 días sin visado
    (el acuerdo fue aprobado por Paraguay como la Ley N.º 5227).</p>

    <p>Ambos países son parte del Convenio de La Haya sobre la Apostilla: Rusia desde 1992, Paraguay
    desde 2014. Esto significa que los documentos emitidos en Rusia (ante todo, el certificado de
    antecedentes penales) se legalizan con apostilla en la propia Rusia y no requieren legalización
    consular adicional. Existe la apostilla electrónica a través del portal Gosuslugi, pero no fue
    posible encontrar una confirmación directa de en qué medida el servicio de migraciones paraguayo
    (<a href="{terminologiya}#dnm">DNM</a>) la acepta sin un documento en papel que la acompañe; en la
    práctica, es más seguro preparar también la versión en papel.</p>

    <p>Los documentos apostillados que no están en español deben traducirse por un traductor público
    matriculado en Paraguay («Traductor Público matriculado») — no es cualquier traductor, sino un
    profesional con matrícula local, y solo ese tipo de traducción es aceptada por las autoridades.</p>

    <p>Según la ley vigente, en el país hay tres categorías de estadía: «ocasional» (occasional,
    turismo — hasta 90 días), residencia temporal y residencia permanente. Los residentes permanentes
    que obtuvieron el estatus después de la reforma de 2022 deben renovarlo cada 10 años — no es una
    decisión única para siempre, sino un estatus que hay que mantener.</p>

    <p>Una cuestión práctica no está resuelta oficialmente en fuentes abiertas: cuántos días puede estar
    un solicitante de la residencia permanente fuera de Paraguay mientras su trámite sigue en curso.
    En la consulta analizamos esto de forma individual según la situación real del cliente.</p>

    <p>Las listas completas de documentos para cada programa — residencia temporal y permanente,
    vía de inversor, ciudadanía — están reunidas en la sección <a href="{dokumenty}">«Documentos
    por programa»</a>.</p>''',
    "en": '''
    <p>Russia and Paraguay have had a visa-free regime since October 20, 2014: Russian citizens can stay
    in the country for up to 90 days within any 180-day period without a visa (the agreement was
    ratified by Paraguay as Ley Nº 5227).</p>

    <p>Both countries are parties to the Hague Apostille Convention: Russia since 1992, Paraguay since
    2014. That means documents issued in Russia (chiefly a criminal record certificate) are
    apostilled within Russia itself and don't need additional consular legalization. An electronic
    apostille via the Gosuslugi portal exists, but we couldn't find direct confirmation of whether
    Paraguay's migration authority (<a href="{terminologiya}#dnm">DNM</a>) accepts it without an accompanying
    paper document; in practice, it's safer to also prepare a paper copy.</p>

    <p>Apostilled documents not in Spanish must be translated by a sworn translator registered in
    Paraguay ("Traductor Público matriculado") — not just any translator, but a specialist with local
    registration, and it's specifically this kind of translation that authorities accept.</p>

    <p>Under current law, the country has three categories of stay: "occasional" (tourism — up to 90
    days), temporary residency, and permanent residency. Permanent residents who obtained their
    status after the 2022 reform are required to renew it every 10 years — it's not a one-time
    decision forever, but a status that needs to be maintained.</p>

    <p>One practical question isn't officially settled in open sources: how many days an applicant for
    permanent residency can spend outside Paraguay while their case is still being processed. During
    a consultation, we go through this individually based on the client's actual situation.</p>

    <p>Full document checklists for every program — temporary and permanent residency, the investor
    route, citizenship — are collected in the <a href="{dokumenty}">"Documents by Program"</a>
    section.</p>''',
    "de": '''
    <p>Zwischen Russland und Paraguay gilt seit dem 20. Oktober 2014 ein visumfreies Regime: Russische
    Staatsbürger dürfen sich bis zu 90 Tage innerhalb jeweils 180 Tage ohne Visum im Land aufhalten
    (das Abkommen wurde von Paraguay als Ley Nº 5227 verabschiedet).</p>

    <p>Beide Länder sind Vertragsparteien des Haager Apostille-Übereinkommens: Russland seit 1992,
    Paraguay seit 2014. Das bedeutet, dass in Russland ausgestellte Dokumente (vor allem das
    Führungszeugnis) bereits in Russland selbst mit einer Apostille versehen werden und keine
    zusätzliche konsularische Legalisierung benötigen. Eine elektronische Apostille über das Portal
    Gosuslugi gibt es, aber ob die paraguayische Migrationsbehörde (<a href="{terminologiya}#dnm">DNM</a>) sie
    ohne begleitendes Papierdokument akzeptiert, ließ sich nicht direkt bestätigen; in der Praxis ist
    es sicherer, zusätzlich auch eine Papierversion vorzubereiten.</p>

    <p>Apostillierte Dokumente, die nicht auf Spanisch verfasst sind, müssen von einem in Paraguay
    registrierten vereidigten Übersetzer («Traductor Público matriculado») übersetzt werden — das ist
    nicht irgendein Übersetzer, sondern ein Fachmann mit lokaler Zulassung, und nur eine solche
    Übersetzung wird von den Behörden akzeptiert.</p>

    <p>Nach geltendem Recht gibt es im Land drei Aufenthaltskategorien: „spontan" (occasional, Tourismus —
    bis zu 90 Tage), befristete Residenz und Daueraufenthalt. Daueraufenthaltsberechtigte, die ihren
    Status nach der Reform von 2022 erhalten haben, müssen ihn alle 10 Jahre verlängern — das ist
    keine einmalige Entscheidung für immer, sondern ein Status, der aufrechterhalten werden muss.</p>

    <p>Eine praktische Frage ist in offen zugänglichen Quellen amtlich nicht geregelt: wie viele Tage
    sich ein Antragsteller auf Daueraufenthalt außerhalb Paraguays aufhalten darf, während sein
    Verfahren noch läuft. Im Beratungsgespräch klären wir das individuell anhand der tatsächlichen
    Situation des Mandanten.</p>

    <p>Vollständige Dokumenten-Checklisten für jedes Programm — befristeter und unbefristeter
    Aufenthalt, Investorenweg, Staatsbürgerschaft — sind im Bereich <a href="{dokumenty}">„Dokumente
    nach Programm"</a> zusammengestellt.</p>''',
}


def build_viza():
    for lang in LANGS:
        l = L(lang)
        lead = DESC[lang]["viza-vyezd"]
        body = f'''
{crumbs(lang, BREADCRUMB_LABEL[lang]["viza-vyezd"])}
{hero(H1_VIZA[lang], lead)}
<section style="padding-top:0;">
  <div class="prose">
    {VIZA_PROSE[lang].format(terminologiya=l["terminologiya"], dokumenty=l["dokumenty"])}
  </div>
</section>
'''
        page("viza-vyezd", lang, TITLE_VIZA[lang], lead, body,
             extra_schema=schema_crumbs(lang, BREADCRUMB_LABEL[lang]["viza-vyezd"], "viza-vyezd"))

# ==================================================== 7. МИФЫ И ВОПРОСЫ

H1_MIFY = {
    "ru": "Мифы о переезде в Парагвай", "es": "Mitos sobre mudarse a Paraguay",
    "en": "Myths About Relocating to Paraguay", "de": "Mythen über den Umzug nach Paraguay",
}
TITLE_MIFY = {
    "ru": "Мифы о переезде в Парагвай: 5 частых заблуждений | Grund Paraguay",
    "es": "Mitos sobre mudarse a Paraguay: 5 ideas erróneas | Grund Paraguay",
    "en": "Myths About Moving to Paraguay: 5 Common Misconceptions | Grund Paraguay",
    "de": "Mythen über den Umzug nach Paraguay: 5 Irrtümer | Grund Paraguay",
}
QUOTE = {"ru": ("«", "»"), "es": ("«", "»"), "en": ("“", "”"), "de": ("„", "“")}
MIFY_INTRO = {
    "ru": "На рынке релокационных услуг в Парагвай встречается набор утверждений, которые "
          "повторяются достаточно часто, чтобы разобрать их отдельно и с указанием источника по каждому.",
    "es": "En el mercado de servicios de relocación a Paraguay circula un conjunto de afirmaciones que "
          "se repiten con la frecuencia suficiente como para analizarlas por separado, indicando la "
          "fuente en cada caso.",
    "en": "In the market for relocation services to Paraguay, a set of claims keeps coming up often "
          "enough to be worth examining separately, with a source noted for each one.",
    "de": "Auf dem Markt für Umzugsdienstleistungen nach Paraguay kursiert eine Reihe von Behauptungen, "
          "die häufig genug wiederholt werden, um sie gesondert zu betrachten — mit Quellenangabe zu "
          "jedem Punkt.",
}
MIFY_CLOSING = {
    "ru": 'Официального документированного предупреждения миграционной службы Парагвая именно о '
          'мошеннических агентах и посредниках (по образцу аналогичных предупреждений, которые '
          'публиковали миграционные службы Чили и Перу) найти не удалось — это не значит, что такого '
          'предупреждения не существует, оно может быть недоступно в открытых источниках. Общая '
          'осторожность в выборе агентства на этом рынке подробнее разобрана на странице '
          '<a href="{riski}">«Честно о рисках»</a>.',
    "es": 'No fue posible encontrar una advertencia oficial documentada del servicio de migraciones de '
          'Paraguay específicamente sobre agentes e intermediarios fraudulentos (según el modelo de '
          'advertencias similares publicadas por los servicios de migraciones de Chile y Perú) — esto no '
          'significa que tal advertencia no exista, puede que no esté disponible en fuentes abiertas. La '
          'precaución general al elegir una agencia en este mercado se analiza con más detalle en la página '
          '<a href="{riski}">«Honestamente sobre los riesgos»</a>.',
    "en": "We couldn't find a documented official warning from Paraguay's migration authority specifically "
          'about fraudulent agents and intermediaries (along the lines of similar warnings published by the '
          "migration authorities of Chile and Peru) — that doesn't mean such a warning doesn't exist; it may "
          'simply not be available in open sources. General caution when choosing an agency in this market is '
          'discussed in more detail on the <a href="{riski}">"Honestly, About the Risks"</a> page.',
    "de": 'Eine dokumentierte offizielle Warnung der paraguayischen Migrationsbehörde speziell vor '
          'betrügerischen Agenten und Vermittlern (nach dem Vorbild ähnlicher Warnungen, die die '
          'Migrationsbehörden Chiles und Perus veröffentlicht haben) ließ sich nicht finden — das bedeutet '
          'nicht, dass es eine solche Warnung nicht gibt, sie ist in offenen Quellen möglicherweise einfach '
          'nicht verfügbar. Allgemeine Vorsicht bei der Wahl einer Agentur auf diesem Markt wird '
          'ausführlicher auf der Seite <a href="{riski}">„Ehrlich über die Risiken"</a> behandelt.',
}

# Каждый миф: (bare_question, answer_html_template, plain_answer)
MYTHS = {
    "ru": [
        ("Гражданство за один год",
         'Не соответствует действительности. Конституция Парагвая (ст. 148) требует минимум три '
         'года «radicación» — и этот срок отсчитывается с даты получения постоянной резиденции, '
         'а не с момента въезда в страну. Официальная страница судебной системы Парагвая (Poder '
         'Judicial) это подтверждает. С учётом времени на получение самой резиденции реальный '
         'общий срок обычно существенно превышает год — подробнее об этом на странице '
         '<a href="{pochemu}">«Почему Парагвай»</a>.',
         'Конституция Парагвая (ст. 148) требует минимум три года «radicación», отсчитываемых с даты получения постоянной резиденции, а не с момента въезда в страну; реальный общий срок обычно существенно превышает год.'),
        ("Резидентность через депозит 5000 USD",
         'Эта схема действительно существовала, но была отменена ещё в октябре 2022 года вместе с '
         'принятием нового миграционного закона (Ley 6984/22). Вместо фиксированного депозита '
         'сейчас действует система, привязанная к конкретному подтверждению платёжеспособности или '
         'инвестиционному проекту заявителя, а не к единой универсальной сумме.',
         'Схема фиксированного депозита была отменена в октябре 2022 года (Ley 6984/22); сейчас действует система, привязанная к подтверждению платёжеспособности или инвестиционному проекту, а не к единой сумме.'),
        ("Россиянам нужна виза, чтобы подать заявление на резиденцию",
         'Не соответствует действительности в части въезда — между Россией и Парагваем действует '
         'безвизовый режим с 2014 года (подробнее — на странице '
         '<a href="{viza}">«Виза и въезд»</a>). Отдельный процедурный нюанс — можно ли формально '
         'подавать документы на резидентство, уже находясь в Парагвае в безвизовом туристическом '
         'статусе — прямой официальной цитатой DNM не подтверждён.',
         'Между Россией и Парагваем действует безвизовый режим с 2014 года; отдельный процедурный нюанс о подаче документов на резидентство уже находясь в стране прямой официальной цитатой DNM не подтверждён.'),
        ("Парагвай в чёрном или сером списке FATF, банковские операции особенно рискованны",
         'Не соответствует действительности: по состоянию на середину 2026 года страна не входит в '
         'этот список (подробнее — на странице <a href="{banki}">«Банки и переводы»</a>).',
         'По состоянию на середину 2026 года Парагвай не входит в «серый список» FATF.'),
        ("Крипта и стейблкоины — безрисковый способ перевести деньги в обход ограничений",
         'Не соответствует действительности: с 2026 фискального года в Парагвае введена '
         'обязательная налоговая отчётность по криптоактивам, а Центробанк страны официально '
         'называет криптовалюты высокорисковыми активами без статуса законного платёжного '
         'средства.',
         'С 2026 фискального года в Парагвае введена обязательная налоговая отчётность по криптоактивам, а Центробанк страны официально называет криптовалюты высокорисковыми активами без статуса законного платёжного средства.'),
    ],
    "es": [
        ("Ciudadanía en un año",
         'No corresponde a la realidad. La Constitución de Paraguay (art. 148) exige un mínimo de tres '
         'años de «radicación» — y este plazo se cuenta desde la fecha de obtención de la residencia '
         'permanente, no desde el momento de entrar al país. La página oficial del Poder Judicial de '
         'Paraguay lo confirma. Sumando el tiempo para obtener la propia residencia, el plazo total real '
         'suele superar ampliamente el año — más detalles en la página '
         '<a href="{pochemu}">«Por qué Paraguay»</a>.',
         'La Constitución de Paraguay (art. 148) exige un mínimo de tres años de «radicación», contados desde la fecha de obtención de la residencia permanente, no desde el momento de entrar al país; el plazo total real suele superar ampliamente el año.'),
        ("Residencia mediante un depósito de 5.000 USD",
         'Este esquema efectivamente existió, pero fue eliminado ya en octubre de 2022 junto con la '
         'nueva ley migratoria (Ley 6984/22). En lugar de un depósito fijo, ahora rige un sistema '
         'vinculado a una comprobación concreta de solvencia o a un proyecto de inversión del '
         'solicitante, y no a una suma única universal.',
         'El esquema de depósito fijo fue eliminado en octubre de 2022 (Ley 6984/22); ahora rige un sistema vinculado a la comprobación de solvencia o a un proyecto de inversión, no a una suma única.'),
        ("Los rusos necesitan visa para presentar la solicitud de residencia",
         'No corresponde a la realidad en cuanto a la entrada — entre Rusia y Paraguay rige un régimen '
         'sin visado desde 2014 (más detalles en la página <a href="{viza}">«Visa y entrada»</a>). Un '
         'matiz procedimental aparte — si formalmente se pueden presentar los documentos de residencia '
         'estando ya en Paraguay en estatus turístico sin visado — no está confirmado con una cita '
         'oficial directa de la DNM.',
         'Entre Rusia y Paraguay rige un régimen sin visado desde 2014; un matiz procedimental aparte sobre presentar documentos de residencia estando ya en el país no está confirmado con una cita oficial directa de la DNM.'),
        ("Paraguay está en la lista negra o gris del GAFI/FATF, las operaciones bancarias son especialmente riesgosas",
         'No corresponde a la realidad: a mediados de 2026, el país no figura en esa lista (más '
         'detalles en la página <a href="{banki}">«Bancos y transferencias»</a>).',
         'A mediados de 2026, Paraguay no figura en la «lista gris» del GAFI/FATF.'),
        ("La cripto y las stablecoins son una forma sin riesgo de transferir dinero evitando las restricciones",
         'No corresponde a la realidad: desde el año fiscal 2026, en Paraguay rige la declaración '
         'tributaria obligatoria de criptoactivos, y el Banco Central del país califica oficialmente a '
         'las criptomonedas como activos de alto riesgo sin estatus de medio de pago legal.',
         'Desde el año fiscal 2026, en Paraguay rige la declaración tributaria obligatoria de criptoactivos, y el Banco Central del país califica oficialmente a las criptomonedas como activos de alto riesgo sin estatus de medio de pago legal.'),
    ],
    "en": [
        ("Citizenship in one year",
         'Not true. Paraguay\'s Constitution (Art. 148) requires a minimum of three years of '
         '"radicación" — and this period is counted from the date permanent residency is granted, not '
         'from the moment of entering the country. The official page of Paraguay\'s judiciary (Poder '
         'Judicial) confirms this. Once you add the time needed to obtain residency itself, the real '
         'overall timeline is usually well beyond a year — more on this on the '
         '<a href="{pochemu}">"Why Paraguay"</a> page.',
         'Paraguay\'s Constitution (Art. 148) requires a minimum of three years of "radicación," counted from the date permanent residency is granted, not from entry into the country; the real overall timeline is usually well beyond a year.'),
        ("Residency through a $5,000 deposit",
         'This scheme really did exist, but it was abolished back in October 2022 along with the new '
         'migration law (Ley 6984/22). Instead of a fixed deposit, a system now applies that\'s tied to '
         'specific proof of solvency or to the applicant\'s investment project, rather than to one '
         'universal amount.',
         'The fixed-deposit scheme was abolished in October 2022 (Ley 6984/22); a system now applies tied to proof of solvency or an investment project, not a single universal amount.'),
        ("Russians need a visa to apply for residency",
         'Not true regarding entry — Russia and Paraguay have had a visa-free regime since 2014 (more '
         'on the <a href="{viza}">"Visa and Entry"</a> page). A separate procedural nuance — whether you '
         'can formally file residency paperwork while already in Paraguay on visa-free tourist status — '
         'isn\'t confirmed by a direct official DNM statement.',
         'Russia and Paraguay have had a visa-free regime since 2014; a separate procedural nuance about filing residency paperwork while already in the country isn\'t confirmed by a direct official DNM statement.'),
        ("Paraguay is on the FATF black or grey list, so banking is especially risky",
         'Not true: as of mid-2026, the country isn\'t on that list (more on the '
         '<a href="{banki}">"Banking and Money Transfers"</a> page).',
         'As of mid-2026, Paraguay isn\'t on the FATF "grey list."'),
        ("Crypto and stablecoins are a risk-free way to move money around restrictions",
         'Not true: since fiscal year 2026, mandatory tax reporting on crypto assets has applied in '
         'Paraguay, and the country\'s Central Bank officially labels cryptocurrencies as high-risk '
         'assets with no status as legal tender.',
         'Since fiscal year 2026, mandatory tax reporting on crypto assets has applied in Paraguay, and the country\'s Central Bank officially labels cryptocurrencies as high-risk assets with no status as legal tender.'),
    ],
    "de": [
        ("Staatsbürgerschaft in einem Jahr",
         'Entspricht nicht der Realität. Die Verfassung Paraguays (Art. 148) verlangt mindestens drei '
         'Jahre „radicación" — und diese Frist wird ab dem Datum des Erhalts der '
         'Daueraufenthaltsberechtigung gerechnet, nicht ab der Einreise ins Land. Die offizielle Seite '
         'der paraguayischen Justiz (Poder Judicial) bestätigt dies. Rechnet man die Zeit für den Erhalt '
         'der Residenz selbst hinzu, liegt die tatsächliche Gesamtfrist in der Regel deutlich über einem '
         'Jahr — mehr dazu auf der Seite <a href="{pochemu}">„Warum Paraguay"</a>.',
         'Die Verfassung Paraguays (Art. 148) verlangt mindestens drei Jahre „radicación", gerechnet ab dem Datum des Erhalts der Daueraufenthaltsberechtigung, nicht ab der Einreise; die tatsächliche Gesamtfrist liegt in der Regel deutlich über einem Jahr.'),
        ("Residenz durch eine Einlage von 5.000 USD",
         'Dieses Modell gab es tatsächlich, wurde aber bereits im Oktober 2022 zusammen mit dem neuen '
         'Migrationsgesetz (Ley 6984/22) abgeschafft. Anstelle einer festen Einlage gilt jetzt ein '
         'System, das an einen konkreten Zahlungsfähigkeitsnachweis oder ein Investitionsprojekt des '
         'Antragstellers gebunden ist, nicht an einen einheitlichen universellen Betrag.',
         'Das Modell der festen Einlage wurde im Oktober 2022 abgeschafft (Ley 6984/22); jetzt gilt ein System, das an einen Zahlungsfähigkeitsnachweis oder ein Investitionsprojekt gebunden ist, nicht an einen einheitlichen Betrag.'),
        ("Russen brauchen ein Visum, um einen Residenzantrag zu stellen",
         'Entspricht in Bezug auf die Einreise nicht der Realität — zwischen Russland und Paraguay gilt '
         'seit 2014 ein visumfreies Regime (mehr auf der Seite <a href="{viza}">„Visum und '
         'Einreise"</a>). Eine gesonderte verfahrenstechnische Nuance — ob man formal '
         'Residenzunterlagen einreichen kann, während man sich bereits visumfrei im touristischen Status '
         'in Paraguay befindet — ist nicht durch ein direktes offizielles Zitat der DNM bestätigt.',
         'Zwischen Russland und Paraguay gilt seit 2014 ein visumfreies Regime; eine gesonderte Nuance zur Einreichung von Residenzunterlagen innerhalb des Landes ist nicht durch ein direktes offizielles Zitat der DNM bestätigt.'),
        ("Paraguay steht auf der schwarzen oder grauen Liste der FATF, Bankgeschäfte sind besonders riskant",
         'Entspricht nicht der Realität: Mitte 2026 steht das Land nicht auf dieser Liste (mehr auf der '
         'Seite <a href="{banki}">„Banken und Geldtransfers"</a>).',
         'Mitte 2026 steht Paraguay nicht auf der „grauen Liste" der FATF.'),
        ("Krypto und Stablecoins sind ein risikofreier Weg, um Geld unter Umgehung von Beschränkungen zu transferieren",
         'Entspricht nicht der Realität: Seit dem Steuerjahr 2026 gilt in Paraguay eine steuerliche '
         'Meldepflicht für Kryptowerte, und die Zentralbank des Landes bezeichnet Kryptowährungen '
         'offiziell als hochriskante Vermögenswerte ohne Status als gesetzliches Zahlungsmittel.',
         'Seit dem Steuerjahr 2026 gilt in Paraguay eine steuerliche Meldepflicht für Kryptowerte, und die Zentralbank des Landes bezeichnet Kryptowährungen offiziell als hochriskante Vermögenswerte ohne Status als gesetzliches Zahlungsmittel.'),
    ],
}


def build_mify():
    for lang in LANGS:
        l = L(lang)
        lead = DESC[lang]["mify-voprosy"]
        qo, qc = QUOTE[lang]

        myths_html = ""
        for question, answer_html, _ in MYTHS[lang]:
            answer = answer_html.format(pochemu=l["pochemu-paragvay"], viza=l["viza-vyezd"], banki=l["banki-perevody"])
            myths_html += f'<h3>{qo}{question}{qc}</h3>\n<p>{answer}</p>\n'

        faq_schema = {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": q,
                    "acceptedAnswer": {"@type": "Answer", "text": plain_answer}
                } for q, _, plain_answer in MYTHS[lang]
            ]
        }

        closing = MIFY_CLOSING[lang].format(riski=l["riski"])

        body = f'''
{crumbs(lang, BREADCRUMB_LABEL[lang]["mify-voprosy"])}
{hero(H1_MIFY[lang], lead)}
<section style="padding-top:0;">
  <div class="prose">
    <p>{MIFY_INTRO[lang]}</p>

    {myths_html}

    <p>{closing}</p>
  </div>
</section>
'''
        page("mify-voprosy", lang, TITLE_MIFY[lang], lead, body,
             extra_schema=[schema_crumbs(lang, BREADCRUMB_LABEL[lang]["mify-voprosy"], "mify-voprosy"), faq_schema])

# ================================================== 8. МЕДИЦИНА В ПАРАГВАЕ

# Новая подстраница (24.08.2026, старт RU-only; 27.08.2026 — переведена на ES/EN/DE по запросу
# заказчика «Делай мультиязычность и правь карту сайта») — не часть HUB_PAGE_ORDER/CARD_TITLE/DESC
# (те словари собраны для исходных 7 подстраниц хаба), карточка на лендинге — MEDITSINA_CARD ниже,
# тем же приёмом, что и TOUR_CARD. Источник фактуры — design/meditsina-strakhovanie-issledovanie.md
# (проект Cowork).

H1_MEDITSINA = {"ru": "Медицина в Парагвае", "es": "Medicina en Paraguay",
                "en": "Healthcare in Paraguay", "de": "Medizin in Paraguay"}
TITLE_MEDITSINA = {
    "ru": "Медицина в Парагвае: IPS, частная страховка, клиники | Grund Paraguay",
    "es": "Medicina en Paraguay: IPS, seguro privado, clínicas | Grund Paraguay",
    "en": "Healthcare in Paraguay: IPS, private insurance, clinics | Grund Paraguay",
    "de": "Medizin in Paraguay: IPS, private Versicherung, Kliniken | Grund Paraguay",
}
LEAD_MEDITSINA = {
    "ru": ("Как устроено здравоохранение в Парагвае для иностранца: три уровня системы, "
           "во сколько обходится частная страховка и на что смотреть в договоре, прежде "
           "чем его подписывать."),
    "es": ("Cómo está organizada la atención médica en Paraguay para un extranjero: los tres "
           "niveles del sistema, cuánto cuesta un seguro privado y qué hay que revisar en el "
           "contrato antes de firmarlo."),
    "en": ("How healthcare works in Paraguay for a foreigner: the system's three levels, what "
           "private insurance costs, and what to check in the contract before signing it."),
    "de": ("Wie die Gesundheitsversorgung in Paraguay für Ausländer funktioniert: die drei "
           "Ebenen des Systems, was eine private Versicherung kostet und worauf man im Vertrag "
           "achten sollte, bevor man ihn unterschreibt."),
}

# Карточка «Медицина в Парагвае» на лендинге хаба — тем же приёмом, что и TOUR_CARD выше.
MEDITSINA_CARD = {
    "ru": ("Медицина в Парагвае",
           "Как устроено здравоохранение — IPS, MSPBS и частная медицина, во сколько "
           "обходится страховка и на что смотреть в договоре, прежде чем его подписывать."),
    "es": ("Medicina en Paraguay",
           "Cómo está organizada la atención médica — IPS, MSPBS y medicina privada, cuánto "
           "cuesta un seguro y qué hay que revisar en el contrato antes de firmarlo."),
    "en": ("Healthcare in Paraguay",
           "How healthcare works — IPS, MSPBS, and private medicine, what insurance costs, "
           "and what to check in the contract before signing it."),
    "de": ("Medizin in Paraguay",
           "Wie die Gesundheitsversorgung funktioniert — IPS, MSPBS und Privatmedizin, was "
           "eine Versicherung kostet und worauf man im Vertrag achten sollte, bevor man ihn "
           "unterschreibt."),
}

# Карточка «Работа в Парагвае» на лендинге хаба (28.08.2026) — тем же приёмом, что TOUR_CARD/
# MEDITSINA_CARD выше.
RABOTA_CARD = {
    "ru": ("Работа в Парагвае",
           "Нужна ли резиденция для трудоустройства, что даёт cédula, когда регистрировать RUC "
           "и IPS — пошагово, с честной оценкой того, что подтвердить не удалось."),
    "es": ("Trabajo en Paraguay",
           "Si se necesita la residencia para trabajar, qué da la cédula, cuándo inscribirse en "
           "el RUC y en el IPS — paso a paso, con una evaluación honesta de lo que no se pudo "
           "confirmar."),
    "en": ("Working in Paraguay",
           "Whether you need residency to work, what the cédula gets you, and when to register "
           "for RUC and IPS — step by step, with an honest note on what couldn't be confirmed."),
    "de": ("Arbeiten in Paraguay",
           "Ob man für die Arbeit eine Aufenthaltserlaubnis braucht, was die Cédula bringt und "
           "wann man sich bei RUC und IPS anmelden muss — Schritt für Schritt, mit einem "
           "ehrlichen Hinweis darauf, was sich nicht bestätigen ließ."),
}


def build_meditsina():
  for lang in LANGS:
    l = L(lang)
    if lang == "ru":
        prose = f'''
    <p>Русскоязычного контента о медицине в Парагвае почти нет, а то, что есть, — либо
    туристический глянец, либо реклама конкретной страховой компании. Здесь — рабочий разбор:
    что вы получаете бесплатно, за что придётся платить, и какие условия в договоре со
    страховой легко упустить, если читаете его не на родном языке.</p>

    <h2>Три уровня системы</h2>
    <p>В Парагвае одновременно работают три уровня медицины, и их легко перепутать между собой.
    <strong>MSPBS</strong> (Министерство здравоохранения) — публичные больницы и поликлиники,
    базовая помощь, доступная широко, без привязки к статусу резидентства как условию входа в
    двери. <strong>IPS</strong> (Instituto de Previsión Social) — не публичная медицина вообще, а
    отдельная система социального страхования, привязанная к формальной занятости: даёт
    комплексную бесплатную помощь (базовые консультации, сложные операции, помощь при ДТП,
    лечение уже имеющихся заболеваний), но вход в неё — через взносы с зарплаты, а не через факт
    нахождения в стране. Третий уровень — частная медицина: клиники и страховые планы, которыми
    в итоге пользуется большинство иностранцев независимо от статуса. Разница между MSPBS и IPS —
    самое частое место путаницы в англоязычных источниках, и именно она объясняет, почему разные
    сайты по-разному отвечают на вопрос «бесплатна ли медицина для иностранца».</p>

    <h2>IPS: кому доступен и что даёт</h2>
    <p>Взнос в IPS — 25,5% от зарплаты, из них 9% — доля работника, 16,5% — доля работодателя.
    Для регистрации нужны cédula (парагвайский ID), подтверждение занятости и регистрация
    работодателя в системе соцстрахования — то есть доступ появляется вместе с официальным
    трудоустройством, а не автоматически по факту резидентства. У временных резидентов
    автоматического доступа к IPS нет: они могут пользоваться MSPBS для базовой помощи, но для
    надёжного доступа к специалистам обычно нужна частная страховка или prepaid-план. Отдельно:
    фрилансер может добровольно подключиться к пенсионной части IPS, но не к медицинской —
    добровольное подключение именно к медицинскому страхованию для самозанятых не предусмотрено;
    регистрация как микропредприниматель для этого станет обязательной только с 2028 года, то
    есть на 2026 год это не действующее правило, а будущее.</p>
    <p class="confidence-note">Разные источники по-разному описывают доступ туристов к публичным
    больницам — от «только неотложная помощь» до «полностью бесплатно для всех с документом».
    Прямого и однозначного ответа именно для туристического статуса найти не удалось — если это
    критично для вашей ситуации, уточняем отдельно, а не полагаемся на общую формулировку.</p>

    <h2>Частная медицина: локальные и международные планы</h2>
    <p>На испанском рынке для полиса типа ДМС используется термин <em>medicina prepaga</em>
    (предоплаченный медицинский план) — отдельная от «seguro médico» (страховки классического
    типа с возмещением) категория. У локальных страховщиков есть нюансы, которые стоит знать
    заранее. Например, у MAPFRE Paraguay (план «Trébol Salud Global») два варианта — с
    возмещением 80% или 100% (включая роды до 7 000 USD), но требуется статус <strong>постоянного
    резидента</strong>: на этапе временной резиденции такой план просто недоступен. У другого
    крупного локального игрока, Asismed, — жёсткие сроки ожидания («carencias»): 6 месяцев на
    задекларированные хронические состояния, минимум 12 месяцев — на онкологию и болезни
    почек/печени, а незадекларированные состояния не покрываются вообще; при оформлении
    обязательна декларация о здоровье, а документы по страховому случаю нужно подать в течение
    48 часов. Цены на локальные prepaid-планы страховщики публично не публикуют, но по трём
    независимым источникам они сходятся к ориентиру примерно 70–150 USD в месяц для среднего/
    премиального плана (отдельные источники называют более широкий разброс — от 25 до 300 USD, но
    это уже не пересекающиеся между источниками цифры). Международные страховки (Cigna Global,
    Allianz Care, April International и другие) обходятся дороже — примерно 150–800 USD в месяц в
    зависимости от покрытия, зато дают доступ к более широкой сети клиник и не требуют
    резидентства. Если выбираете международный план, разумно сверяться по шести пунктам: перевод
    медицинских заключений на понятный вам язык, покрытие эвакуации, покрытие «весь мир» против
    «только регион», условия по уже существующим заболеваниям, структура франшизы и покрытие
    неотложной помощи и стационара.</p>

    <h2>Клиники</h2>
    <p>Официальный список Великобритании для путешественников называет по имени и с контактами
    два частных учреждения в Асунсьоне с англоговорящим персоналом: <strong>Centro Médico
    Bautista</strong> (Avda. República Argentina 635 y Campos Cervera, +595 21 6889000) и
    <strong>Centro Médico La Costa</strong> (Av. Artigas 1500 y María Concepción Leyes de Chávez,
    +595 21 2171000) — с оговоркой, что список не исчерпывающий и не является рекомендацией
    конкретной клиники. Также в Асунсьоне работает частный стационар Sanatorio Británico (Av.
    Gaspar Rodríguez de Francia 910) — состав его услуг и работа со страховыми сетями отдельно не
    проверялись.</p>

    <h2>Риски, из-за которых страховка — не формальность</h2>
    <p>Денге — реальный сезонный риск, а не редкость; подробности и источники — на странице
    <a href="{l['mify-voprosy']}">«Мифы и вопросы»</a>, раздел «Здоровье и климат». Отдельно
    официальный портал Великобритании для путешественников отмечает: частные клиники в Парагвае
    обычно требуют оплату сразу на месте, без ожидания возмещения от страховой, — то есть
    страховка нужна не «на всякий случай», а как рабочий инструмент на первый же год.</p>

    <h2>Если нужна помощь с выбором</h2>
    <p>Подбор плана под ваш статус резидентства, разбор мелкого шрифта в договоре и
    сопровождение на приёме — отдельная услуга,
    <a href="{l['usluga-medicina']}">«Медицинское сопровождение»</a>.</p>

    <h2>Смотрите также</h2>
    <ul>
      <li><a href="{l['usluga-medicina']}">«Медицинское сопровождение»</a> — подбор страховки и
      помощь на приёме</li>
      <li><a href="{l['mify-voprosy']}">«Мифы и вопросы»</a> — денге и другие риски здоровья</li>
      <li><a href="{l['terminologiya']}#ips">«Терминология»: IPS</a> — короткое определение с
      привязкой к занятости и статусу резидента</li>
    </ul>'''
    elif lang == "es":
        prose = f'''
    <p>Casi no hay contenido en ruso sobre medicina en Paraguay, y lo poco que existe es o bien
    glamour turístico, o publicidad de una aseguradora concreta. Aquí va un análisis práctico:
    qué recibe gratis, por qué tendrá que pagar y qué condiciones del contrato con la
    aseguradora son fáciles de pasar por alto si no lo lee en su idioma nativo.</p>

    <h2>Tres niveles del sistema</h2>
    <p>En Paraguay funcionan simultáneamente tres niveles de medicina, y es fácil confundirlos
    entre sí. El <strong>MSPBS</strong> (Ministerio de Salud Pública) son los hospitales y
    centros de salud públicos, atención básica, ampliamente disponible, sin que el estatus de
    residencia sea una condición para entrar por la puerta. El <strong>IPS</strong> (Instituto
    de Previsión Social) no es la medicina pública en general, sino un sistema aparte de
    seguridad social vinculado al empleo formal: brinda atención integral gratuita (consultas
    básicas, cirugías complejas, atención en accidentes de tránsito, tratamiento de
    enfermedades ya existentes), pero el acceso es a través de los aportes del salario, no por
    el simple hecho de estar en el país. El tercer nivel es la medicina privada: clínicas y
    planes de seguro que, al final, usa la mayoría de los extranjeros independientemente de su
    estatus. La diferencia entre MSPBS e IPS es el punto de confusión más frecuente en las
    fuentes en inglés, y es justamente ella la que explica por qué distintos sitios responden
    de forma diferente a la pregunta «¿es gratis la medicina para un extranjero?».</p>

    <h2>IPS: quién tiene acceso y qué ofrece</h2>
    <p>El aporte al IPS es del 25,5% del salario, de los cuales 9% es la parte del trabajador y
    16,5% la del empleador. Para inscribirse se necesita la cédula paraguaya, comprobante de
    empleo y la inscripción del empleador en el sistema de seguridad social — es decir, el
    acceso llega junto con el empleo formal, no automáticamente por el hecho de tener
    residencia. Los residentes temporales no tienen acceso automático al IPS: pueden usar el
    MSPBS para atención básica, pero para un acceso confiable a especialistas normalmente hace
    falta un seguro privado o un plan prepago. Por separado: un freelance puede afiliarse
    voluntariamente a la parte jubilatoria del IPS, pero no a la parte médica — la afiliación
    voluntaria específicamente al seguro médico para independientes no está prevista; el
    registro como microempresario para esto recién será obligatorio a partir de 2028, es decir,
    para 2026 esta no es una regla vigente, sino algo a futuro.</p>
    <p class="confidence-note">Distintas fuentes describen de forma diferente el acceso de los
    turistas a los hospitales públicos — desde «solo atención de urgencia» hasta «completamente
    gratis para todos con un documento». No se pudo encontrar una respuesta directa e
    inequívoca específicamente para el estatus de turista — si esto es crítico para su
    situación, lo confirmamos por separado, en lugar de basarnos en una formulación general.</p>

    <h2>Medicina privada: planes locales e internacionales</h2>
    <p>En el mercado en español se usa el término <em>medicina prepaga</em> (plan médico
    prepago) para un seguro de tipo integral — una categoría aparte de «seguro médico» (seguro
    clásico con reembolso). Las aseguradoras locales tienen matices que conviene conocer de
    antemano. Por ejemplo, MAPFRE Paraguay (plan «Trébol Salud Global») ofrece dos variantes —
    con reembolso del 80% o del 100% (incluido el parto, hasta 7.000 USD) —, pero exige el
    estatus de <strong>residente permanente</strong>: en la etapa de residencia temporal ese
    plan simplemente no está disponible. Otro actor local importante, Asismed, tiene períodos
    de carencia estrictos: 6 meses para enfermedades crónicas declaradas, mínimo 12 meses para
    cáncer y enfermedades renales/hepáticas, y las condiciones no declaradas no se cubren en
    absoluto; al contratar es obligatoria la declaración jurada de salud, y los documentos de
    un siniestro deben presentarse en un plazo de 48 horas. Las aseguradoras no publican
    públicamente los precios de los planes prepagos locales, pero según tres fuentes
    independientes convergen en un valor de referencia de aproximadamente 70–150 USD al mes
    para un plan medio/premium (fuentes individuales mencionan un rango más amplio — de 25 a
    300 USD, pero esas cifras ya no coinciden entre fuentes). Los seguros internacionales
    (Cigna Global, Allianz Care, April International y otros) cuestan más — entre 150 y 800 USD
    al mes según la cobertura, pero a cambio dan acceso a una red de clínicas más amplia y no
    exigen residencia. Si elige un plan internacional, conviene revisar seis puntos: traducción
    de los informes médicos a un idioma que entienda, cobertura de evacuación, cobertura «todo
    el mundo» frente a «solo la región», condiciones para enfermedades preexistentes,
    estructura de la franquicia y cobertura de urgencias y hospitalización.</p>

    <h2>Clínicas</h2>
    <p>La lista oficial del Reino Unido para viajeros menciona por nombre y con datos de
    contacto dos centros privados en Asunción con personal que habla inglés: <strong>Centro
    Médico Bautista</strong> (Avda. República Argentina 635 y Campos Cervera, +595 21 6889000)
    y <strong>Centro Médico La Costa</strong> (Av. Artigas 1500 y María Concepción Leyes de
    Chávez, +595 21 2171000) — con la aclaración de que la lista no es exhaustiva ni constituye
    una recomendación de una clínica en particular. También funciona en Asunción el sanatorio
    privado Sanatorio Británico (Av. Gaspar Rodríguez de Francia 910) — su cartera de servicios
    y su trabajo con redes de seguros no se verificaron por separado.</p>

    <h2>Riesgos por los que el seguro no es una formalidad</h2>
    <p>El dengue es un riesgo estacional real, no una rareza; detalles y fuentes en la página
    <a href="{l['mify-voprosy']}">«Mitos y preguntas»</a>, sección «Salud y clima». Por
    separado, el portal oficial del Reino Unido para viajeros señala: las clínicas privadas en
    Paraguay suelen exigir el pago de inmediato en el lugar, sin esperar el reembolso de la
    aseguradora — es decir, el seguro no es «por si acaso», sino una herramienta de trabajo
    desde el primer año.</p>

    <h2>Si necesita ayuda para elegir</h2>
    <p>La selección del plan según su estatus de residencia, el análisis de la letra pequeña
    del contrato y el acompañamiento en la consulta son un servicio aparte,
    <a href="{l['usluga-medicina']}">«Asistencia médica»</a>.</p>

    <h2>Vea también</h2>
    <ul>
      <li><a href="{l['usluga-medicina']}">«Asistencia médica»</a> — selección de seguro y
      acompañamiento en la consulta</li>
      <li><a href="{l['mify-voprosy']}">«Mitos y preguntas»</a> — el dengue y otros riesgos de
      salud</li>
      <li><a href="{l['terminologiya']}#ips">«Terminología»: IPS</a> — definición breve
      vinculada al empleo y al estatus de residente</li>
    </ul>'''
    elif lang == "en":
        prose = f'''
    <p>There's almost no Russian-language content about healthcare in Paraguay, and what exists
    is either tourist gloss or advertising for a specific insurer. Here's a practical
    breakdown: what you get for free, what you'll have to pay for, and which contract terms
    with an insurer are easy to miss if you're not reading it in your native language.</p>

    <h2>Three levels of the system</h2>
    <p>Paraguay runs three levels of healthcare at once, and it's easy to confuse them.
    <strong>MSPBS</strong> (the Ministry of Public Health) runs public hospitals and clinics —
    basic care, widely available, with residency status not a condition for walking through
    the door. <strong>IPS</strong> (Instituto de Previsión Social) isn't public healthcare in
    general — it's a separate social insurance system tied to formal employment: it provides
    comprehensive free care (basic consultations, complex surgeries, treatment after traffic
    accidents, treatment of existing conditions), but access comes through payroll
    contributions, not simply from being in the country. The third level is private medicine —
    clinics and insurance plans that most foreigners end up using regardless of status. The
    difference between MSPBS and IPS is the single most common point of confusion in
    English-language sources, and it's exactly what explains why different sites answer "is
    healthcare free for a foreigner?" so differently.</p>

    <h2>IPS: who has access and what it covers</h2>
    <p>The IPS contribution is 25.5% of salary, split 9% employee / 16.5% employer.
    Registration requires a Paraguayan cédula, proof of employment, and the employer's
    registration in the social security system — meaning access comes together with formal
    employment, not automatically from residency status. Temporary residents don't have
    automatic access to IPS: they can use MSPBS for basic care, but reliable access to
    specialists usually requires private insurance or a prepaid plan. Separately: a freelancer
    can voluntarily join the pension side of IPS, but not the medical side — voluntary
    enrollment specifically in medical coverage isn't available to the self-employed;
    registering as a microentrepreneur for this will only become mandatory starting in 2028,
    meaning as of 2026 this isn't a rule in effect yet, just a future one.</p>
    <p class="confidence-note">Sources describe tourists' access to public hospitals
    differently — anywhere from "emergency care only" to "completely free for anyone with an
    ID." We couldn't find a direct, unambiguous answer specifically for tourist status — if
    this matters for your situation, we confirm it separately rather than relying on a general
    statement.</p>

    <h2>Private medicine: local and international plans</h2>
    <p>The Spanish-language market uses the term <em>medicina prepaga</em> (prepaid medical
    plan) for an HMO-style policy — a category distinct from "seguro médico" (a classic
    reimbursement-type policy). Local insurers have quirks worth knowing in advance. For
    example, MAPFRE Paraguay (the "Trébol Salud Global" plan) offers two options — 80% or 100%
    reimbursement (including maternity, up to $7,000) — but requires
    <strong>permanent-resident</strong> status: at the temporary-residency stage, that plan
    simply isn't available. Another major local player, Asismed, has strict waiting periods
    ("carencias"): 6 months for declared chronic conditions, at least 12 months for cancer and
    kidney/liver disease, and undeclared conditions aren't covered at all; a health declaration
    is mandatory when signing up, and claim documents must be submitted within 48 hours.
    Insurers don't publicly disclose pricing for local prepaid plans, but three independent
    sources converge on a rough benchmark of about $70–150/month for a mid-to-premium plan
    (individual sources cite a wider range — $25 to $300 — but those figures don't overlap
    across sources). International insurance (Cigna Global, Allianz Care, April International,
    and others) costs more — roughly $150–800/month depending on coverage — but in exchange
    gives access to a broader clinic network and doesn't require residency. If you're choosing
    an international plan, it's worth checking six things: translation of medical reports into
    a language you understand, evacuation coverage, worldwide vs. region-only coverage, terms
    on pre-existing conditions, the deductible structure, and coverage for emergency care and
    hospitalization.</p>

    <h2>Clinics</h2>
    <p>The UK's official traveler list names, with contact details, two private facilities in
    Asunción with English-speaking staff: <strong>Centro Médico Bautista</strong> (Avda.
    República Argentina 635 y Campos Cervera, +595 21 6889000) and <strong>Centro Médico La
    Costa</strong> (Av. Artigas 1500 y María Concepción Leyes de Chávez, +595 21 2171000) —
    with the caveat that the list isn't exhaustive and isn't a recommendation of any specific
    clinic. Asunción is also home to the private hospital Sanatorio Británico (Av. Gaspar
    Rodríguez de Francia 910) — its range of services and its work with insurance networks
    weren't separately verified.</p>

    <h2>Risks that make insurance more than a formality</h2>
    <p>Dengue is a real seasonal risk, not a rarity; details and sources are on the
    <a href="{l['mify-voprosy']}">"Myths & Questions"</a> page, "Health & Climate" section.
    Separately, the UK's official travel portal notes that private clinics in Paraguay usually
    require payment on the spot, without waiting for reimbursement from the insurer — meaning
    insurance isn't "just in case," it's a working tool for year one.</p>

    <h2>If you need help choosing</h2>
    <p>Choosing a plan for your residency status, reading the fine print in the contract, and
    support at appointments are a separate service, <a href="{l['usluga-medicina']}">"Medical
    Support"</a>.</p>

    <h2>See also</h2>
    <ul>
      <li><a href="{l['usluga-medicina']}">"Medical Support"</a> — choosing insurance and
      support at appointments</li>
      <li><a href="{l['mify-voprosy']}">"Myths & Questions"</a> — dengue and other health
      risks</li>
      <li><a href="{l['terminologiya']}#ips">"Terminology": IPS</a> — a short definition tied to
      employment and resident status</li>
    </ul>'''
    else:  # de
        prose = f'''
    <p>Russischsprachige Inhalte zur Medizin in Paraguay gibt es kaum, und was es gibt, ist
    entweder touristischer Hochglanz oder Werbung einer bestimmten Versicherungsgesellschaft.
    Hier ein praktischer Überblick: was Sie kostenlos bekommen, wofür Sie zahlen müssen und
    welche Vertragsbedingungen mit der Versicherung leicht zu übersehen sind, wenn man sie
    nicht in der eigenen Muttersprache liest.</p>

    <h2>Drei Ebenen des Systems</h2>
    <p>In Paraguay bestehen gleichzeitig drei Ebenen der Medizin, die sich leicht verwechseln
    lassen. <strong>MSPBS</strong> (Gesundheitsministerium) betreibt öffentliche Krankenhäuser
    und Gesundheitszentren — Grundversorgung, breit verfügbar, ohne dass der Aufenthaltsstatus
    eine Bedingung für den Zugang wäre. <strong>IPS</strong> (Instituto de Previsión Social)
    ist nicht die öffentliche Medizin im Allgemeinen, sondern ein eigenständiges
    Sozialversicherungssystem, das an formale Beschäftigung gekoppelt ist: Es bietet
    umfassende kostenlose Versorgung (Basiskonsultationen, komplexe Operationen, Behandlung
    nach Verkehrsunfällen, Behandlung bereits bestehender Erkrankungen), aber der Zugang
    erfolgt über Beiträge vom Gehalt, nicht allein durch den Aufenthalt im Land. Die dritte
    Ebene ist die Privatmedizin — Kliniken und Versicherungspläne, die am Ende die meisten
    Ausländer unabhängig von ihrem Status nutzen. Der Unterschied zwischen MSPBS und IPS ist
    der häufigste Verwechslungspunkt in englischsprachigen Quellen, und genau er erklärt,
    warum verschiedene Webseiten die Frage „ist die Medizin für Ausländer kostenlos?"
    unterschiedlich beantworten.</p>

    <h2>IPS: Wer hat Zugang und was bietet es</h2>
    <p>Der IPS-Beitrag beträgt 25,5% des Gehalts, davon 9% Arbeitnehmer- und 16,5%
    Arbeitgeberanteil. Für die Anmeldung sind eine paraguayische Cédula, ein
    Beschäftigungsnachweis und die Registrierung des Arbeitgebers im
    Sozialversicherungssystem nötig — der Zugang entsteht also zusammen mit der formellen
    Beschäftigung, nicht automatisch durch den Aufenthaltsstatus. Befristete Residenten haben
    keinen automatischen Zugang zur IPS: Sie können MSPBS für die Grundversorgung nutzen, doch
    für einen zuverlässigen Zugang zu Fachärzten braucht es meist eine private Versicherung
    oder einen Prepaid-Plan. Gesondert: Ein Freelancer kann sich freiwillig dem Rentenanteil
    der IPS anschließen, nicht aber dem medizinischen Anteil — eine freiwillige Anmeldung
    speziell zur Krankenversicherung ist für Selbstständige nicht vorgesehen; die Registrierung
    als Kleinunternehmer wird dafür erst ab 2028 verpflichtend, das heißt, für 2026 ist das
    noch keine geltende Regel, sondern Zukunftsmusik.</p>
    <p class="confidence-note">Verschiedene Quellen beschreiben den Zugang von Touristen zu
    öffentlichen Krankenhäusern unterschiedlich — von „nur Notfallversorgung" bis „mit Ausweis
    für alle vollständig kostenlos". Eine direkte, eindeutige Antwort speziell für den
    Touristenstatus ließ sich nicht finden — falls das für Ihre Situation entscheidend ist,
    klären wir das gesondert, statt uns auf eine allgemeine Formulierung zu verlassen.</p>

    <h2>Privatmedizin: lokale und internationale Pläne</h2>
    <p>Auf dem spanischsprachigen Markt wird für eine Police vom Typ einer
    Krankenzusatzversicherung der Begriff <em>medicina prepaga</em> (vorausbezahlter
    medizinischer Plan) verwendet — eine eigene Kategorie neben „seguro médico" (klassische
    Versicherung mit Kostenerstattung). Lokale Versicherer haben Besonderheiten, die man
    vorher kennen sollte. MAPFRE Paraguay (Plan „Trébol Salud Global") bietet zum Beispiel zwei
    Varianten — mit 80% oder 100% Erstattung (einschließlich Geburt, bis zu 7.000 USD) —,
    verlangt aber den Status eines <strong>unbefristeten Residenten</strong>: In der Phase des
    befristeten Aufenthalts ist dieser Plan schlicht nicht verfügbar. Ein weiterer großer
    lokaler Anbieter, Asismed, hat strenge Wartezeiten („carencias"): 6 Monate für angegebene
    chronische Erkrankungen, mindestens 12 Monate für Krebs- und Nieren-/Lebererkrankungen, und
    nicht angegebene Zustände werden überhaupt nicht gedeckt; bei Vertragsabschluss ist eine
    Gesundheitserklärung verpflichtend, und Unterlagen zu einem Versicherungsfall müssen
    innerhalb von 48 Stunden eingereicht werden. Die Preise lokaler Prepaid-Pläne
    veröffentlichen die Versicherer nicht öffentlich, doch drei unabhängige Quellen laufen auf
    einen Richtwert von etwa 70–150 USD im Monat für einen mittleren/Premium-Plan hinaus
    (einzelne Quellen nennen eine breitere Spanne — 25 bis 300 USD, doch diese Zahlen
    überschneiden sich zwischen den Quellen nicht mehr). Internationale Versicherungen (Cigna
    Global, Allianz Care, April International und andere) kosten mehr — etwa 150–800 USD im
    Monat je nach Deckung —, bieten dafür aber Zugang zu einem breiteren Klinik-Netzwerk und
    verlangen keinen Aufenthaltstitel. Wer sich für einen internationalen Plan entscheidet,
    sollte sinnvollerweise sechs Punkte prüfen: Übersetzung medizinischer Befunde in eine
    verständliche Sprache, Deckung der Evakuierung, weltweite Deckung gegenüber „nur Region",
    Bedingungen für Vorerkrankungen, die Struktur der Selbstbeteiligung und die Deckung von
    Notfallversorgung und Krankenhausaufenthalt.</p>

    <h2>Kliniken</h2>
    <p>Die offizielle britische Liste für Reisende nennt namentlich und mit Kontaktdaten zwei
    private Einrichtungen in Asunción mit englischsprachigem Personal: <strong>Centro Médico
    Bautista</strong> (Avda. República Argentina 635 y Campos Cervera, +595 21 6889000) und
    <strong>Centro Médico La Costa</strong> (Av. Artigas 1500 y María Concepción Leyes de
    Chávez, +595 21 2171000) — mit dem Hinweis, dass die Liste nicht vollständig ist und keine
    Empfehlung für eine bestimmte Klinik darstellt. In Asunción arbeitet außerdem das private
    Krankenhaus Sanatorio Británico (Av. Gaspar Rodríguez de Francia 910) — sein
    Leistungsspektrum und die Zusammenarbeit mit Versicherungsnetzwerken wurden nicht gesondert
    überprüft.</p>

    <h2>Risiken, wegen derer eine Versicherung keine Formalität ist</h2>
    <p>Dengue ist ein reales saisonales Risiko, keine Seltenheit; Details und Quellen auf der
    Seite <a href="{l['mify-voprosy']}">„Mythen und Fragen"</a>, Abschnitt „Gesundheit und
    Klima". Das offizielle britische Reiseportal weist gesondert darauf hin: Private Kliniken
    in Paraguay verlangen die Zahlung in der Regel sofort vor Ort, ohne auf die Erstattung
    durch die Versicherung zu warten — die Versicherung ist also kein „für den Fall der
    Fälle", sondern ein Arbeitswerkzeug für das erste Jahr.</p>

    <h2>Wenn Sie Hilfe bei der Wahl brauchen</h2>
    <p>Die Planauswahl passend zu Ihrem Aufenthaltsstatus, die Prüfung des Kleingedruckten im
    Vertrag und die Begleitung beim Arztbesuch sind eine eigene Leistung,
    <a href="{l['usluga-medicina']}">„Medizinische Begleitung"</a>.</p>

    <h2>Siehe auch</h2>
    <ul>
      <li><a href="{l['usluga-medicina']}">„Medizinische Begleitung"</a> —
      Versicherungsauswahl und Begleitung beim Arztbesuch</li>
      <li><a href="{l['mify-voprosy']}">„Mythen und Fragen"</a> — Dengue und andere
      Gesundheitsrisiken</li>
      <li><a href="{l['terminologiya']}#ips">„Terminologie": IPS</a> — kurze Definition mit
      Bezug zu Beschäftigung und Residentenstatus</li>
    </ul>'''

    body = f'''
{crumbs(lang, H1_MEDITSINA[lang])}
{hero(H1_MEDITSINA[lang], LEAD_MEDITSINA[lang])}
<section style="padding-top:0;">
  <div class="prose">
    {prose}
  </div>
</section>
'''
    page("meditsina-v-paragvae", lang, TITLE_MEDITSINA[lang], LEAD_MEDITSINA[lang], body,
         extra_schema=schema_crumbs(lang, H1_MEDITSINA[lang], "meditsina-v-paragvae"))


# ============================================================ 9. РАБОТА В ПАРАГВАЕ
#
# 28.08.2026, сразу мультиязычная (по запросу заказчика «Сделай страницу Работа в Парагвае»,
# тем же порядком, что и предыдущие добавления в разделе — RU/ES/EN/DE одним заходом).
# Источник фактуры — веб-поиск в этой же сессии Cowork: официальные и профильные испаноязычные
# источники (портал IPS, ABC Color, действующая Ley N° 213/93 «Código del Trabajo», Ley
# N° 3452/2008) плюс уже подтверждённый ранее в проекте факт об обязанности RUC после Residencia
# Temporal (design/teksty-mvp-stranits.md). Полная сводка источников и уровней уверенности —
# design/rabota-v-paragvae-issledovanie.md (проект Cowork).

TITLE_RABOTA = {
    "ru": "Работа в Парагвае: документы для трудоустройства | Grund Paraguay",
    "es": "Trabajo en Paraguay: documentos para el empleo | Grund Paraguay",
    "en": "Working in Paraguay: Documents for Employment | Grund Paraguay",
    "de": "Arbeiten in Paraguay: Dokumente für die Beschäftigung | Grund Paraguay",
}
H1_RABOTA = {
    "ru": "Работа в Парагвае: как устроено официальное трудоустройство",
    "es": "Trabajo en Paraguay: cómo funciona el empleo formal",
    "en": "Working in Paraguay: how formal employment works",
    "de": "Arbeiten in Paraguay: Wie die formelle Beschäftigung funktioniert",
}
LEAD_RABOTA = {
    "ru": ("Нужна ли резиденция, чтобы работать легально, что даёт cédula, когда регистрировать "
           "RUC и IPS — по шагам, с источниками и честной оценкой того, что подтвердить не удалось."),
    "es": ("Si se necesita la residencia para trabajar legalmente, qué da la cédula, cuándo "
           "inscribirse en el RUC y en el IPS — paso a paso, con fuentes y una evaluación "
           "honesta de lo que no se pudo confirmar."),
    "en": ("Whether you need residency to work legally, what the cédula gets you, and when to "
           "register for RUC and IPS — step by step, with sources and an honest note on what "
           "couldn't be confirmed."),
    "de": ("Ob man für legale Arbeit eine Aufenthaltserlaubnis braucht, was die Cédula bringt "
           "und wann man sich bei RUC und IPS anmelden muss — Schritt für Schritt, mit Quellen "
           "und einem ehrlichen Hinweis darauf, was sich nicht bestätigen ließ."),
}


def build_rabota():
  for lang in LANGS:
    l = L(lang)
    if lang == "ru":
        prose = f'''
    <p>Отдельного «разрешения на работу», не привязанного к статусу в стране, в Парагвае нет —
    юридическое право работать даёт сама резиденция. Дальше вопрос не «какое разрешение
    оформить», а какие документы и регистрации нужны на каждом шаге — от резидентуры до
    трудового договора. Привычной в России «трудовой книжки» в Парагвае тоже нет: занятость
    подтверждается трудовым договором и записью в системе социального страхования.</p>

    <h2>Резидентура — обязательное условие</h2>
    <p>Право легально работать даёт временная
    (<a href="{l['terminologiya']}#residencia-temporal">Residencia Temporal</a>) или постоянная
    (<a href="{l['terminologiya']}#residencia-permanente">Residencia Permanente</a>) резиденция —
    отдельного трека «рабочей визы» в стороне от резидентуры источники не описывают. Без
    действующей резиденции легальное трудоустройство невозможно. Чек-лист документов для
    оформления — на странице <a href="{l['dok-temporal']}">«Документы для временной
    резиденции»</a>.</p>

    <h2>Cédula de identidad paraguaya</h2>
    <p>С августа 2024 года парагвайскую <a href="{l['terminologiya']}#cedula">cédula</a> можно
    получить уже на статусе временного резидента — раньше это было доступно только постоянным
    резидентам. Свежий (на момент проверки) список требований для иностранца:</p>
    <ol>
      <li>Certificado de Radicación (Permanente или Temporal) от миграционной службы
      (<a href="{l['terminologiya']}#dnm">DNM</a>)</li>
      <li>заверенная копия Carnet de Admisión</li>
      <li>заверенная копия документа страны происхождения с визой МИД</li>
      <li>свидетельство о рождении — оригинал с консульской визой и
      <a href="{l['terminologiya']}#apostil">апостилем</a></li>
      <li>документы о семейном положении, если применимо</li>
      <li>Certificado de Vida y Residencia от комиссариата или мирового суда</li>
      <li>справка об отсутствии судимости из страны происхождения (для лиц от 14 лет)</li>
      <li>справка Интерпола</li>
      <li>справка об отсутствии судимости в самом Парагвае</li>
      <li>заверенная копия карты регистрации (registro)</li>
    </ol>
    <p>Документы не на испанском — через
    <a href="{l['terminologiya']}#traductor-publico">присяжного переводчика (Traductor Público
    matriculado)</a>.</p>

    <h2>RUC — постановка на налоговый учёт</h2>
    <p>После получения Residencia Temporal возникает обязанность зарегистрировать
    <a href="{l['terminologiya']}#ruc">RUC</a> и подавать налоговую отчётность — это касается и
    наёмных работников, и предпринимателей, только состав подтверждающих занятость документов
    разный. Ставки и логика налогообложения — на странице
    <a href="{l['nalogi-inostrantsev']}">«Налоги для иностранцев»</a>.</p>

    <h2>IPS и трудовой договор у работодателя</h2>
    <p>Формализация трудовых отношений договором обязательна по Código del Trabajo (Ley
    N° 213/93) и Ley N° 3452/2008 — как для граждан, так и для иностранцев. Отдельно обязательна
    регистрация в <a href="{l['terminologiya']}#ips">IPS</a> (ст. 95 Конституции Парагвая):
    взнос — 25,5% от зарплаты, 9% — доля работника, 16,5% — доля работодателя. Со стороны
    работника для регистрации нужны carnet de migraciones и документ, удостоверяющий личность
    (до получения cédula — документ страны происхождения). Со стороны работодателя для
    постановки на учёт в IPS нужны его cédula и RUC/Constancia de RUC (для физлица) либо
    учредительные документы, акт последнего собрания и cédula представителя (для юрлица).</p>

    <p class="confidence-note">Единого официального чек-листа документов именно для самого
    трудового договора (в отличие от чётких списков для cédula и регистрации в IPS выше) найти
    не удалось — судя по всему, его содержание (условия, оплата, функции) регулируется Código
    del Trabajo содержательно, а не отдельным перечнем бумаг. Отдельного межправительственного
    соглашения о трудовой миграции между Россией и Парагваем подтвердить тоже не удалось —
    занятость оформляется по общему для всех иностранцев режиму, описанному выше.</p>

    <h2>Если нужна помощь</h2>
    <p>Ведение отчётности после регистрации RUC, контроль сроков и сопровождение переписки с
    ведомствами — отдельная услуга,
    <a href="{l['usluga-compliance']}">«Сопровождение и комплаенс»</a>.</p>

    <h2>Смотрите также</h2>
    <ul>
      <li><a href="{l['dok-temporal']}">Документы для временной резиденции</a> — с чего
      начинается легальный статус</li>
      <li><a href="{l['nalogi-inostrantsev']}">«Налоги для иностранцев»</a> — ставки IRE, IVA,
      IRP и обязанность RUC</li>
      <li><a href="{l['terminologiya']}#ips">«Терминология»: IPS</a>,
      <a href="{l['terminologiya']}#cedula">Cédula</a> и
      <a href="{l['terminologiya']}#ruc">RUC</a> — короткие определения</li>
      <li><a href="{l['usluga-compliance']}">«Сопровождение и комплаенс»</a> — ведение
      отчётности после трудоустройства</li>
    </ul>'''
    elif lang == "es":
        prose = f'''
    <p>En Paraguay no existe un «permiso de trabajo» aparte, independiente del estatus
    migratorio — el derecho legal a trabajar lo otorga la propia residencia. La pregunta no es
    «qué permiso tramitar», sino qué documentos e inscripciones se necesitan en cada paso —
    desde la residencia hasta el contrato de trabajo. Tampoco existe en Paraguay la «libreta de
    trabajo» habitual en Rusia: el empleo se acredita con el contrato de trabajo y la
    inscripción en el sistema de seguridad social.</p>

    <h2>La residencia — condición obligatoria</h2>
    <p>El derecho a trabajar legalmente lo otorga la residencia temporal
    (<a href="{l['terminologiya']}#residencia-temporal">Residencia Temporal</a>) o la permanente
    (<a href="{l['terminologiya']}#residencia-permanente">Residencia Permanente</a>) —
    las fuentes no describen una vía aparte de «visa de trabajo» separada de la residencia. Sin
    una residencia vigente, el empleo formal no es posible. La lista de documentos para
    tramitarla está en la página <a href="{l['dok-temporal']}">«Documentos para la residencia
    temporal»</a>.</p>

    <h2>Cédula de identidad paraguaya</h2>
    <p>Desde agosto de 2024, la <a href="{l['terminologiya']}#cedula">cédula</a> paraguaya puede
    obtenerse ya con el estatus de residente temporal — antes solo estaba disponible para
    residentes permanentes. Lista reciente (al momento de la revisión) de requisitos para un
    extranjero:</p>
    <ol>
      <li>Certificado de Radicación (Permanente o Temporal) de la Dirección de Migraciones
      (<a href="{l['terminologiya']}#dnm">DNM</a>)</li>
      <li>copia autenticada del Carnet de Admisión</li>
      <li>copia autenticada del documento del país de origen con visación del MRE</li>
      <li>partida de nacimiento — original con visación consular y
      <a href="{l['terminologiya']}#apostil">apostilla</a></li>
      <li>documentos sobre el estado civil, si corresponde</li>
      <li>Certificado de Vida y Residencia de la comisaría o del juzgado de paz</li>
      <li>certificado de antecedentes penales del país de origen (para mayores de 14 años)</li>
      <li>certificado de Interpol</li>
      <li>certificado de antecedentes en el propio Paraguay</li>
      <li>copia autenticada de la tarjeta de registro (registro)</li>
    </ol>
    <p>Los documentos que no estén en español requieren traducción de un
    <a href="{l['terminologiya']}#traductor-publico">Traductor Público matriculado</a>.</p>

    <h2>RUC — inscripción en el registro tributario</h2>
    <p>Tras obtener la Residencia Temporal surge la obligación de inscribir el
    <a href="{l['terminologiya']}#ruc">RUC</a> y presentar declaraciones — esto aplica tanto a
    empleados en relación de dependencia como a emprendedores, solo cambia el conjunto de
    documentos que acreditan la actividad. Las tasas y la lógica tributaria están en la página
    <a href="{l['nalogi-inostrantsev']}">«Impuestos para extranjeros»</a>.</p>

    <h2>IPS y contrato de trabajo con el empleador</h2>
    <p>Formalizar la relación laboral mediante contrato es obligatorio según el Código del
    Trabajo (Ley N.° 213/93) y la Ley N.° 3452/2008 — tanto para ciudadanos como para
    extranjeros. Por separado es obligatoria la inscripción en el
    <a href="{l['terminologiya']}#ips">IPS</a> (art. 95 de la Constitución de Paraguay): el
    aporte es del 25,5% del salario, 9% a cargo del trabajador y 16,5% a cargo del empleador.
    Por el lado del trabajador se necesitan el carnet de migraciones y un documento de
    identidad (hasta obtener la cédula — el documento del país de origen). Por el lado del
    empleador, para inscribirse en el IPS se necesitan su cédula y RUC/Constancia de RUC (para
    persona física) o los documentos constitutivos, el acta de la última asamblea y la cédula
    del representante (para persona jurídica).</p>

    <p class="confidence-note">No se pudo encontrar una lista oficial única de documentos
    específicamente para el propio contrato de trabajo (a diferencia de las listas claras para
    la cédula y la inscripción en el IPS de arriba) — al parecer, su contenido (condiciones,
    remuneración, funciones) se regula de fondo por el Código del Trabajo, no por un listado de
    papeles aparte. Tampoco se pudo confirmar un convenio intergubernamental específico de
    migración laboral entre Rusia y Paraguay — el empleo se tramita bajo el régimen general
    descrito arriba, común a todos los extranjeros.</p>

    <h2>Si necesita ayuda</h2>
    <p>La gestión de las declaraciones tras inscribir el RUC, el control de plazos y el
    acompañamiento en la correspondencia con los organismos son un servicio aparte,
    <a href="{l['usluga-compliance']}">«Acompañamiento y cumplimiento»</a>.</p>

    <h2>Vea también</h2>
    <ul>
      <li><a href="{l['dok-temporal']}">Documentos para la residencia temporal</a> — por dónde
      empieza el estatus legal</li>
      <li><a href="{l['nalogi-inostrantsev']}">«Impuestos para extranjeros»</a> — tasas de IRE,
      IVA, IRP y la obligación del RUC</li>
      <li><a href="{l['terminologiya']}#ips">«Terminología»: IPS</a>,
      <a href="{l['terminologiya']}#cedula">Cédula</a> y
      <a href="{l['terminologiya']}#ruc">RUC</a> — definiciones breves</li>
      <li><a href="{l['usluga-compliance']}">«Acompañamiento y cumplimiento»</a> — gestión de
      declaraciones tras el empleo</li>
    </ul>'''
    elif lang == "en":
        prose = f'''
    <p>Paraguay doesn't have a separate "work permit" independent of immigration status — the
    legal right to work comes from residency itself. The question isn't "which permit to get,"
    it's which documents and registrations are needed at each step — from residency through to
    the labor contract. Paraguay also has no equivalent of a Russian-style "work record book":
    employment is evidenced by the labor contract and the social-insurance registration.</p>

    <h2>Residency — the mandatory precondition</h2>
    <p>The right to work legally comes from temporary
    (<a href="{l['terminologiya']}#residencia-temporal">Residencia Temporal</a>) or permanent
    (<a href="{l['terminologiya']}#residencia-permanente">Residencia Permanente</a>) residency —
    sources don't describe a separate "work visa" track apart from residency. Without valid
    residency, formal employment isn't possible. The document checklist for applying is on the
    <a href="{l['dok-temporal']}">"Documents for Temporary Residency"</a> page.</p>

    <h2>Paraguayan cédula de identidad</h2>
    <p>Since August 2024, the Paraguayan <a href="{l['terminologiya']}#cedula">cédula</a> has
    been available already at temporary-resident status — previously it was available only to
    permanent residents. A recent (as of this check) list of requirements for a foreigner:</p>
    <ol>
      <li>Certificado de Radicación (Permanent or Temporary) from the immigration service
      (<a href="{l['terminologiya']}#dnm">DNM</a>)</li>
      <li>a certified copy of the Carnet de Admisión</li>
      <li>a certified copy of the home-country ID document with a foreign-ministry visa stamp</li>
      <li>birth certificate — original, with consular legalization and an
      <a href="{l['terminologiya']}#apostil">apostille</a></li>
      <li>civil-status documents, where applicable</li>
      <li>Certificado de Vida y Residencia from the local police commissariat or justice of the
      peace</li>
      <li>a police-clearance certificate from the home country (for anyone age 14 or older)</li>
      <li>an Interpol clearance certificate</li>
      <li>a police-clearance certificate from Paraguay itself</li>
      <li>a certified copy of the registration card (registro)</li>
    </ol>
    <p>Documents not in Spanish need translation by a registered
    <a href="{l['terminologiya']}#traductor-publico">sworn translator (Traductor Público
    matriculado)</a>.</p>

    <h2>RUC — tax registration</h2>
    <p>Once Residencia Temporal is granted, registering an <a href="{l['terminologiya']}#ruc">RUC</a>
    and filing tax returns becomes mandatory — this applies to salaried employees and
    entrepreneurs alike, only the set of documents proving your occupation differs. Rates and
    the underlying tax logic are covered on the
    <a href="{l['nalogi-inostrantsev']}">"Taxes for Foreigners"</a> page.</p>

    <h2>IPS and the labor contract with an employer</h2>
    <p>Formalizing the employment relationship with a contract is mandatory under the Labor Code
    (Ley N° 213/93) and Ley N° 3452/2008 — for citizens and foreigners alike. Separately,
    registration with <a href="{l['terminologiya']}#ips">IPS</a> is mandatory (Art. 95 of
    Paraguay's Constitution): the contribution is 25.5% of salary, split 9% employee / 16.5%
    employer. On the employee's side, registration needs the carnet de migraciones plus an ID
    document (the home-country document, until the cédula is issued). On the employer's side,
    registering with IPS needs their cédula and RUC/Constancia de RUC (for an individual
    employer) or founding documents, minutes of the most recent shareholders' meeting, and the
    representative's cédula (for a legal entity).</p>

    <p class="confidence-note">We couldn't find a single official checklist of documents for the
    labor contract itself (unlike the clear lists for the cédula and IPS registration above) —
    its content (terms, pay, duties) appears to be governed substantively by the Labor Code
    rather than by a separate paperwork list. We also couldn't confirm a specific
    intergovernmental labor-migration agreement between Russia and Paraguay — employment is
    handled under the general regime described above, the same one that applies to all
    foreigners.</p>

    <h2>If you need help</h2>
    <p>Handling tax filings after RUC registration, tracking deadlines, and managing
    correspondence with government agencies is a separate service,
    <a href="{l['usluga-compliance']}">"Ongoing Compliance"</a>.</p>

    <h2>See also</h2>
    <ul>
      <li><a href="{l['dok-temporal']}">Documents for temporary residency</a> — where legal
      status starts</li>
      <li><a href="{l['nalogi-inostrantsev']}">"Taxes for Foreigners"</a> — IRE, IVA, and IRP
      rates, and the RUC obligation</li>
      <li><a href="{l['terminologiya']}#ips">"Terminology": IPS</a>,
      <a href="{l['terminologiya']}#cedula">Cédula</a>, and
      <a href="{l['terminologiya']}#ruc">RUC</a> — short definitions</li>
      <li><a href="{l['usluga-compliance']}">"Ongoing Compliance"</a> — handling filings after
      you start working</li>
    </ul>'''
    else:  # de
        prose = f'''
    <p>Eine gesonderte „Arbeitserlaubnis", unabhängig vom Aufenthaltsstatus, gibt es in Paraguay
    nicht — das Recht, legal zu arbeiten, entsteht durch die Aufenthaltserlaubnis selbst. Die
    Frage ist nicht „welche Erlaubnis beantragen", sondern welche Dokumente und Anmeldungen bei
    jedem Schritt nötig sind — von der Aufenthaltserlaubnis bis zum Arbeitsvertrag. Ein
    „Arbeitsbuch" wie in Russland üblich gibt es in Paraguay ebenfalls nicht: Die Beschäftigung
    wird durch den Arbeitsvertrag und die Anmeldung im Sozialversicherungssystem nachgewiesen.</p>

    <h2>Aufenthaltserlaubnis — zwingende Voraussetzung</h2>
    <p>Das Recht, legal zu arbeiten, entsteht durch die befristete
    (<a href="{l['terminologiya']}#residencia-temporal">Residencia Temporal</a>) oder
    unbefristete (<a href="{l['terminologiya']}#residencia-permanente">Residencia
    Permanente</a>) Aufenthaltserlaubnis — Quellen beschreiben keinen gesonderten
    „Arbeitsvisum"-Weg neben der Aufenthaltserlaubnis. Ohne gültige Aufenthaltserlaubnis ist eine
    formelle Beschäftigung nicht möglich. Die Dokumentenliste für die Beantragung steht auf der
    Seite <a href="{l['dok-temporal']}">„Dokumente für die befristete
    Aufenthaltserlaubnis"</a>.</p>

    <h2>Paraguayische Cédula de identidad</h2>
    <p>Seit August 2024 kann die paraguayische <a href="{l['terminologiya']}#cedula">Cédula</a>
    bereits mit dem Status eines befristeten Residenten beantragt werden — zuvor stand sie nur
    unbefristeten Residenten offen. Eine aktuelle (Stand der Prüfung) Liste der Anforderungen für
    Ausländer:</p>
    <ol>
      <li>Certificado de Radicación (unbefristet oder befristet) von der Migrationsbehörde
      (<a href="{l['terminologiya']}#dnm">DNM</a>)</li>
      <li>beglaubigte Kopie des Carnet de Admisión</li>
      <li>beglaubigte Kopie des Ausweisdokuments aus dem Herkunftsland mit Visasichtvermerk des
      Außenministeriums</li>
      <li>Geburtsurkunde — Original mit konsularischer Beglaubigung und
      <a href="{l['terminologiya']}#apostil">Apostille</a></li>
      <li>Dokumente zum Familienstand, sofern zutreffend</li>
      <li>Certificado de Vida y Residencia vom Kommissariat oder Friedensrichter</li>
      <li>polizeiliches Führungszeugnis aus dem Herkunftsland (ab 14 Jahren)</li>
      <li>Interpol-Unbedenklichkeitsbescheinigung</li>
      <li>polizeiliches Führungszeugnis aus Paraguay selbst</li>
      <li>beglaubigte Kopie der Registrierungskarte (registro)</li>
    </ol>
    <p>Nicht-spanischsprachige Dokumente benötigen eine Übersetzung durch einen
    <a href="{l['terminologiya']}#traductor-publico">vereidigten, beim Obersten Gerichtshof
    registrierten Übersetzer (Traductor Público matriculado)</a>.</p>

    <h2>RUC — steuerliche Erfassung</h2>
    <p>Nach Erhalt der Residencia Temporal entsteht die Pflicht, sich beim
    <a href="{l['terminologiya']}#ruc">RUC</a> anzumelden und Steuererklärungen einzureichen —
    das gilt gleichermaßen für Angestellte und Unternehmer, nur die Nachweisdokumente für die
    Tätigkeit unterscheiden sich. Sätze und die zugrunde liegende Logik der Besteuerung stehen
    auf der Seite <a href="{l['nalogi-inostrantsev']}">„Steuern für Ausländer"</a>.</p>

    <h2>IPS und Arbeitsvertrag beim Arbeitgeber</h2>
    <p>Die Formalisierung des Arbeitsverhältnisses durch einen Vertrag ist nach dem
    Arbeitsgesetzbuch (Ley N° 213/93) und der Ley N° 3452/2008 verpflichtend — sowohl für
    Staatsbürger als auch für Ausländer. Gesondert ist die Anmeldung bei
    <a href="{l['terminologiya']}#ips">IPS</a> verpflichtend (Art. 95 der Verfassung Paraguays):
    Der Beitrag beträgt 25,5% des Gehalts, davon 9% Arbeitnehmer- und 16,5% Arbeitgeberanteil.
    Auf Seiten des Arbeitnehmers sind für die Anmeldung das Carnet de Migraciones sowie ein
    Ausweisdokument nötig (bis zum Erhalt der Cédula — das Dokument des Herkunftslands). Auf
    Seiten des Arbeitgebers sind für die IPS-Anmeldung dessen Cédula und RUC/Constancia de RUC
    (bei einer natürlichen Person) bzw. Gründungsdokumente, das Protokoll der letzten
    Gesellschafterversammlung und die Cédula des Vertreters (bei einer juristischen Person)
    nötig.</p>

    <p class="confidence-note">Eine einzige offizielle Dokumentenliste speziell für den
    Arbeitsvertrag selbst (im Unterschied zu den klaren Listen für Cédula und IPS-Anmeldung
    oben) ließ sich nicht finden — sein Inhalt (Bedingungen, Vergütung, Aufgaben) wird
    offenbar inhaltlich durch das Arbeitsgesetzbuch geregelt, nicht durch eine gesonderte
    Dokumentenliste. Auch ein gesondertes zwischenstaatliches Abkommen zur Arbeitsmigration
    zwischen Russland und Paraguay ließ sich nicht bestätigen — die Beschäftigung erfolgt nach
    der oben beschriebenen allgemeinen Regelung, die für alle Ausländer gilt.</p>

    <h2>Wenn Sie Hilfe brauchen</h2>
    <p>Die laufende Erklärungsführung nach der RUC-Anmeldung, die Fristenkontrolle und die
    Begleitung im Schriftverkehr mit den Behörden sind eine eigene Leistung,
    <a href="{l['usluga-compliance']}">„Begleitung und Compliance"</a>.</p>

    <h2>Siehe auch</h2>
    <ul>
      <li><a href="{l['dok-temporal']}">Dokumente für die befristete Aufenthaltserlaubnis</a> —
      womit der rechtliche Status beginnt</li>
      <li><a href="{l['nalogi-inostrantsev']}">„Steuern für Ausländer"</a> — Sätze von IRE,
      IVA, IRP und die RUC-Pflicht</li>
      <li><a href="{l['terminologiya']}#ips">„Terminologie": IPS</a>,
      <a href="{l['terminologiya']}#cedula">Cédula</a> und
      <a href="{l['terminologiya']}#ruc">RUC</a> — kurze Definitionen</li>
      <li><a href="{l['usluga-compliance']}">„Begleitung und Compliance"</a> — laufende
      Erklärungsführung nach dem Arbeitsbeginn</li>
    </ul>'''

    body = f'''
{crumbs(lang, H1_RABOTA[lang])}
{hero(H1_RABOTA[lang], LEAD_RABOTA[lang])}
<section style="padding-top:0;">
  <div class="prose">
    {prose}
  </div>
</section>
'''
    page("rabota-v-paragvae", lang, TITLE_RABOTA[lang], LEAD_RABOTA[lang], body,
         extra_schema=schema_crumbs(lang, H1_RABOTA[lang], "rabota-v-paragvae"))

# ======================================================================= run

build_hub_landing()
build_pochemu()
build_zhizn()
build_stoimost_zhizni()
build_nalogi()
build_banki()
build_viza()
build_mify()
build_meditsina()
build_rabota()
