#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Раздел «Документы» (12.08.2026 — старт RU-only; 12.08.2026 вечер — переведён на ES/EN/DE по
запросу заказчика «делай мультиязычность по документам»).

Хаб-страница «Документы по программам» + 4 страницы с чек-листами документов по каждой
программе миграции: временная резидентура, постоянная резидентура (12 категорий Resolución DNM
N° 407/2026), инвесторский путь (SUACE / Investor Pass), гражданство (натурализация).

Источник фактуры — design/dokumenty-po-programmam-migratsii.md (проект Cowork, сбор 12.08.2026),
формат сохранён: факт → источник → уверенность, критичные пробелы вынесены в явные callout/
confidence-note блоки, а не сглажены. Правило проекта «не изобретай факты» соблюдается: там, где
источник только вторичный/коммерческий (не migraciones.gov.py напрямую), это прямо указано —
на всех 4 языках одинаково, перевод не меняет факты и уровни уверенности (см. промт
design/promt-seo-i-terminologiya.md, «главное правило»).

Стиль страниц — по образцу уже существующих content-страниц (protsess-i-sroki, stoimost):
<table> для табличных данных вне .prose (полная ширина .wrap), <div class="callout"> для
методологической оговорки в начале каждой страницы, <p class="confidence-note"> для сносок по
конкретным пунктам. Хаб — по образцу «kak-my-rabotaem»: один столбец карточек без иконок и без
сетки, 2–3 предложения + обязательная ссылка «Подробнее →».
"""
from build import page, breadcrumbs, schema_breadcrumb, href_to, NAV_LABELS, LANGS, icon


def L(lang):
    return {pid: href_to(pid, lang) for pid in [
        "home", "uslugi", "protsess", "riski", "kak-my-rabotaem", "terminologiya", "kontakty",
        "o-kompanii", "stoimost", "viza-vyezd",
        "dokumenty", "dok-temporal", "dok-permanente", "dok-investor", "dok-grazhdanstvo",
    ]}


METHOD_NOTE = {
    "ru": (
        'Официальные домены migraciones.gov.py, suace.gov.py и bacn.gov.py в основном недоступны для '
        'прямой проверки в рабочей среде, где собирались эти материалы, поэтому большая часть фактов '
        'ниже — из вторичных источников (юридические фирмы Парагвая, профильные иммиграционные '
        'сервисы), с пометкой уверенности по каждому пункту. Два документа на этой странице получены '
        'напрямую с официальных источников — это отмечено отдельно. Прежде чем использовать любой '
        'список ниже как окончательный при подаче документов, стоит свериться с юристом-партнёром в '
        'Парагвае — особенно там, где стоит пометка «средняя» или «низкая» уверенность.'
    ),
    "es": (
        'Los dominios oficiales migraciones.gov.py, suace.gov.py y bacn.gov.py en su mayoría no '
        'estaban disponibles para verificación directa en el entorno de trabajo donde se recopiló '
        'este material, por lo que la mayor parte de los datos siguientes provienen de fuentes '
        'secundarias (firmas jurídicas de Paraguay, servicios de inmigración especializados), con el '
        'nivel de confianza indicado en cada punto. Dos documentos de esta página se obtuvieron '
        'directamente de fuentes oficiales — esto se indica por separado. Antes de usar cualquiera de '
        'las listas siguientes como definitiva al presentar documentos, conviene consultarlo con un '
        'abogado socio en Paraguay — especialmente donde figure la marca de confianza «media» o «baja».'
    ),
    "en": (
        'The official domains migraciones.gov.py, suace.gov.py, and bacn.gov.py were mostly '
        'unreachable for direct verification in the working environment where this material was '
        'compiled, so most of the facts below come from secondary sources (Paraguayan law firms, '
        'specialized immigration services), with a confidence note on every point. Two documents on '
        'this page were obtained directly from official sources — this is noted separately. Before '
        'treating any list below as final when filing documents, it\'s worth checking with a partner '
        'lawyer in Paraguay — especially wherever the confidence is marked "medium" or "low".'
    ),
    "de": (
        'Die offiziellen Domains migraciones.gov.py, suace.gov.py und bacn.gov.py waren in der '
        'Arbeitsumgebung, in der dieses Material zusammengestellt wurde, größtenteils nicht für eine '
        'direkte Prüfung erreichbar, daher stammen die meisten der folgenden Fakten aus '
        'Sekundärquellen (paraguayische Anwaltskanzleien, spezialisierte Einwanderungsdienstleister), '
        'mit einem Vertrauensvermerk zu jedem Punkt. Zwei Dokumente auf dieser Seite stammen direkt '
        'aus offiziellen Quellen — dies ist gesondert vermerkt. Bevor eine der folgenden Listen bei '
        'der Einreichung von Dokumenten als endgültig verwendet wird, lohnt sich eine Rücksprache mit '
        'einem Partneranwalt in Paraguay — besonders dort, wo „mittleres" oder „niedriges" Vertrauen '
        'vermerkt ist.'
    ),
}

METHOD_LABEL = {
    "ru": "Как читать эти чек-листы", "es": "Cómo leer estas listas de verificación",
    "en": "How to read these checklists", "de": "Wie diese Checklisten zu lesen sind",
}


# Степ-индикатор «Документы» (12.08.2026, декор-фаза 2.2/2.3) — 4 программы одним рядом
# иконок: на хабе — рядом с заголовком каждой карточки (2.3), на каждой из 4 программных
# страниц — кликабельный ряд вверху, текущая программа выделена (не ссылка), остальные 3
# ведут друг на друга напрямую, без возврата на хаб (2.2). Один и тот же порядок и набор
# иконок everywhere — единая "лента программ" по всему разделу.
STEP_PIDS = ["dok-temporal", "dok-permanente", "dok-investor", "dok-grazhdanstvo"]
STEP_ICON = {
    "dok-temporal": "step-temporal", "dok-permanente": "step-permanente",
    "dok-investor": "step-investor", "dok-grazhdanstvo": "step-citizenship",
}
STEP_LABELS = {
    "ru": {"dok-temporal": "Врем. резидентура", "dok-permanente": "Пост. резидентура",
           "dok-investor": "Инвесторский путь", "dok-grazhdanstvo": "Гражданство"},
    "es": {"dok-temporal": "Res. temporal", "dok-permanente": "Res. permanente",
           "dok-investor": "Vía de inversor", "dok-grazhdanstvo": "Ciudadanía"},
    "en": {"dok-temporal": "Temp. residency", "dok-permanente": "Perm. residency",
           "dok-investor": "Investor route", "dok-grazhdanstvo": "Citizenship"},
    "de": {"dok-temporal": "Befr. Aufenthalt", "dok-permanente": "Daueraufenthalt",
           "dok-investor": "Investorenweg", "dok-grazhdanstvo": "Staatsbürgerschaft"},
}
STEP_NAV_ARIA = {
    "ru": "Программы раздела «Документы»", "es": "Programas de la sección «Documentos»",
    "en": "Programs in the Documents section", "de": 'Programme im Bereich „Dokumente"',
}


def step_indicator(lang, l, current_pid):
    items = []
    for pid in STEP_PIDS:
        icon_html = icon(STEP_ICON[pid], "doc-step-icon")
        label = STEP_LABELS[lang][pid]
        if pid == current_pid:
            items.append(f'<span class="doc-step is-current" aria-current="page">{icon_html}<span class="doc-step-label">{label}</span></span>')
        else:
            items.append(f'<a class="doc-step" href="{l[pid]}">{icon_html}<span class="doc-step-label">{label}</span></a>')
    nav = f'<nav class="doc-steps" aria-label="{STEP_NAV_ARIA[lang]}">\n      ' + "\n      ".join(items) + '\n    </nav>'
    # 20.08.2026: обёрнуто в .wrap — без него ряд шёл вплотную к краю экрана, без полей,
    # в отличие от остального контента страницы (найдено по скриншоту заказчика).
    return f'<div class="wrap">{nav}</div>'


# ============================================================== ХАБ-СТРАНИЦА

HUB = {
"ru": dict(
    title="Документы по программам: что нужно для резидентуры, гражданства и Investor Pass | Grund Paraguay",
    description="Чек-листы документов по каждой программе переезда в Парагвай: временная и постоянная резидентура (12 категорий), инвесторский путь, гражданство. С источниками и уровнем уверенности по каждому пункту.",
    h1="Документы по программам",
    lead="Разные пути легализации в Парагвае требуют разных комплектов документов. Здесь — чек-лист по каждой программе отдельно, с источником и уровнем уверенности по каждому пункту: где факт подтверждён официально, а где — только вторичным источником и его стоит перепроверить перед подачей.",
    more="Подробнее →",
    cards=[
        ("dok-temporal", "Временная резидентура (Residencia Temporal)",
         "Базовый комплект по ст. 50 Ley N° 6984/22: загранпаспорт, апостилированные свидетельство о рождении и справка о несудимости, присяжный перевод, личная явка в DNM. Действует 2 года, продлевается на такой же срок."),
        ("dok-permanente", "Постоянная резидентура (Residencia Permanente)",
         "Помимо общего перехода из временной — новая система из 12 категорий заявителей (Resolución DNM N° 407/2026, действует с 6 июля 2026 года): у каждой категории свой набор документов, подтверждающих доход или источник средств."),
        ("dok-investor", "Инвесторский путь (SUACE / Investor Pass)",
         "Прямой доступ к постоянной резиденции без временной, от 70 000 USD инвестиций. Документы на сертификат инвестора (CIE) — по официальному перечню SUACE."),
        ("dok-grazhdanstvo", "Гражданство (натурализация)",
         "Не раньше чем через 3 года после получения постоянной резиденции, дело ведёт не миграционная служба, а Верховный суд. Официальный перечень документов — по данным Poder Judicial."),
    ],
),
"es": dict(
    title="Documentos por programa: qué se necesita para la residencia, la ciudadanía y el Investor Pass | Grund Paraguay",
    description="Listas de verificación de documentos para cada programa de mudanza a Paraguay: residencia temporal y permanente (12 categorías), vía de inversor, ciudadanía. Con fuentes y nivel de confianza en cada punto.",
    h1="Documentos por programa",
    lead="Las distintas vías de legalización en Paraguay requieren distintos paquetes de documentos. Aquí, una lista de verificación por cada programa por separado, con la fuente y el nivel de confianza de cada punto: dónde el dato está confirmado oficialmente y dónde proviene solo de una fuente secundaria y conviene verificarlo antes de presentarlo.",
    more="Más información →",
    cards=[
        ("dok-temporal", "Residencia temporal (Residencia Temporal)",
         "Paquete básico según el art. 50 de la Ley N.° 6984/22: pasaporte, partida de nacimiento y certificado de antecedentes penales apostillados, traducción jurada, comparecencia personal en la DNM. Válida por 2 años, renovable por el mismo plazo."),
        ("dok-permanente", "Residencia permanente (Residencia Permanente)",
         "Además de la conversión general desde la temporal — el nuevo sistema de 12 categorías de solicitantes (Resolución DNM N.° 407/2026, vigente desde el 6 de julio de 2026): cada categoría tiene su propio conjunto de documentos que acreditan ingresos o fuente de fondos."),
        ("dok-investor", "Vía de inversor (SUACE / Investor Pass)",
         "Acceso directo a la residencia permanente sin pasar por la temporal, desde 70.000 USD de inversión. Documentos para el certificado de inversor (CIE) — según la lista oficial de SUACE."),
        ("dok-grazhdanstvo", "Ciudadanía (naturalización)",
         "No antes de 3 años después de obtener la residencia permanente; el trámite lo lleva la Corte Suprema, no el servicio de migraciones. Lista oficial de documentos — según datos del Poder Judicial."),
    ],
),
"en": dict(
    title="Documents by Program: What You Need for Residency, Citizenship & the Investor Pass | Grund Paraguay",
    description="Document checklists for every Paraguay relocation program: temporary and permanent residency (12 categories), the investor route, and citizenship — with sources and a confidence level for each point.",
    h1="Documents by Program",
    lead="Different legalization routes in Paraguay require different sets of documents. Here's a checklist for each program on its own, with a source and confidence level for every point — showing where a fact is officially confirmed and where it comes only from a secondary source and is worth double-checking before filing.",
    more="Learn more →",
    cards=[
        ("dok-temporal", "Temporary Residency (Residencia Temporal)",
         "The basic package under Art. 50 of Ley N° 6984/22: passport, apostilled birth certificate and criminal record certificate, sworn translation, in-person appearance at DNM. Valid for 2 years, renewable for the same term."),
        ("dok-permanente", "Permanent Residency (Residencia Permanente)",
         "Beyond the general conversion from temporary residency — a new system of 12 applicant categories (Resolución DNM N° 407/2026, in effect since July 6, 2026): each category has its own set of documents proving income or source of funds."),
        ("dok-investor", "Investor Route (SUACE / Investor Pass)",
         "Direct access to permanent residency without going through the temporary stage, from 70,000 USD in investment. Documents for the investor certificate (CIE) — per the official SUACE list."),
        ("dok-grazhdanstvo", "Citizenship (Naturalization)",
         "Not sooner than 3 years after getting permanent residency — the case is handled by the Supreme Court, not the migration service. The official document list — per Poder Judicial."),
    ],
),
"de": dict(
    title="Dokumente nach Programm: Was Sie für Aufenthalt, Staatsbürgerschaft und Investor Pass brauchen | Grund Paraguay",
    description="Dokumenten-Checklisten für jedes Umzugsprogramm nach Paraguay: befristeter und unbefristeter Aufenthalt (12 Kategorien), Investorenweg, Staatsbürgerschaft — mit Quellen und Vertrauensniveau zu jedem Punkt.",
    h1="Dokumente nach Programm",
    lead="Unterschiedliche Wege zur Legalisierung in Paraguay erfordern unterschiedliche Dokumentenpakete. Hier eine Checkliste für jedes Programm einzeln, mit Quelle und Vertrauensniveau zu jedem Punkt: wo eine Tatsache offiziell bestätigt ist und wo sie nur aus einer Sekundärquelle stammt und vor der Einreichung überprüft werden sollte.",
    more="Mehr erfahren →",
    cards=[
        ("dok-temporal", "Befristeter Aufenthalt (Residencia Temporal)",
         "Das Basispaket gemäß Art. 50 des Ley N° 6984/22: Reisepass, apostillierte Geburtsurkunde und Führungszeugnis, beglaubigte Übersetzung, persönliches Erscheinen bei der DNM. Gültig für 2 Jahre, verlängerbar um denselben Zeitraum."),
        ("dok-permanente", "Daueraufenthalt (Residencia Permanente)",
         "Neben dem allgemeinen Übergang vom befristeten Aufenthalt — das neue System aus 12 Antragstellerkategorien (Resolución DNM N° 407/2026, in Kraft seit 6. Juli 2026): jede Kategorie hat ihr eigenes Set an Dokumenten zum Nachweis von Einkommen oder Mittelherkunft."),
        ("dok-investor", "Investorenweg (SUACE / Investor Pass)",
         "Direkter Zugang zum Daueraufenthalt ohne befristete Phase, ab 70.000 USD Investition. Dokumente für das Investorenzertifikat (CIE) — nach der offiziellen SUACE-Liste."),
        ("dok-grazhdanstvo", "Staatsbürgerschaft (Einbürgerung)",
         "Frühestens 3 Jahre nach Erhalt des Daueraufenthalts — das Verfahren führt der Oberste Gerichtshof, nicht die Migrationsbehörde. Die offizielle Dokumentenliste — laut Poder Judicial."),
    ],
),
}


def build_hub():
    for lang in LANGS:
        l = L(lang)
        t = HUB[lang]
        cards_html = ""
        for pid, title, desc in t["cards"]:
            card_icon = icon(STEP_ICON[pid], "doc-card-icon") if pid in STEP_ICON else ""
            cards_html += f'''
    <article class="card" style="margin-bottom:24px;">
      <h3>{card_icon}{title}</h3>
      <p style="font-size:16px;">{desc}</p>
      <a class="card-link" href="{l[pid]}">{t["more"]}</a>
    </article>'''
        body = f'''
{breadcrumbs([(NAV_LABELS[lang]["home"], l['home']), (NAV_LABELS[lang]["dokumenty"], None)])}
<section class="hero" style="padding-top:24px;">
  <div class="wrap">
    <h1>{t["h1"]}</h1>
    <p class="lead">{t["lead"]}</p>
  </div>
</section>
<section style="padding-top:0;">
  <div class="prose">
    <div class="callout"><span class="callout-label">{METHOD_LABEL[lang]}</span>{METHOD_NOTE[lang]}</div>
  </div>
</section>
<section style="padding-top:0;">
  <div class="prose">
    {cards_html}
  </div>
</section>
'''
        page("dokumenty", lang, t["title"], t["description"], body,
             extra_schema=schema_breadcrumb([
                 (NAV_LABELS[lang]["home"], f"/{lang}/"),
                 (NAV_LABELS[lang]["dokumenty"], f"/{lang}/{href_to('dokumenty', lang)}"),
             ]))


build_hub()


# ======================================================= ВРЕМЕННАЯ РЕЗИДЕНТУРА

TEMPORAL = {
"ru": dict(
    title="Временная резидентура: список документов (Residencia Temporal) | Grund Paraguay",
    description="Полный список документов для временной резиденции в Парагвае по ст. 50 Ley N° 6984/22: апостиль, перевод, пошлина и сроки действия статуса.",
    h1="Временная резидентура: какие документы нужны",
    lead="Residencia Temporal — временная резиденция, которая даёт право законно жить в Парагвае: оформляется на 2 года с продлением на такой же срок и открывает путь к постоянной резиденции. Это первый шаг легализации, общий для любой из дальнейших программ; единый пакет документов для оформления закреплён в ст. 50 Ley N° 6984/22 «De Migraciones».",
    intro='Комплект документов на временную резиденцию не зависит от категории заявителя — в отличие от постоянной резиденции (см. страницу <a href="{dok-permanente}">«Постоянная резидентура»</a>), где с 2026 года действует отдельная система из 12 категорий. Нужны:',
    items=[
        "Загранпаспорт — действующий, с достаточным сроком действия на весь процесс.",
        'Консульская виза — не требуется гражданам России благодаря безвизовому режиму с 2014 года (подробнее — на странице <a href="{viza-vyezd}">«Виза, документы и въезд»</a>).',
        'Свидетельство о рождении — с апостилем, переведено на испанский зарегистрированным в Парагвае присяжным переводчиком (<a href="{terminologiya}#traductor-publico">Traductor Público matriculado</a>).',
        "Справка о семейном положении / свидетельство о браке — если применимо.",
        'Международная справка о несудимости — с <a href="{terminologiya}#apostil">апостилем</a>, переведена.',
        'Письменное обязательство соблюдать конституцию и законы Парагвая — оформляется уже в стране, в <a href="{terminologiya}#dnm">DNM</a>.',
        "Присяжное заявление о профессии и адресе проживания в Парагвае.",
        "Личная явка в DNM — обязательна, дистанционно оформить нельзя.",
    ],
    gap_label="Не подтверждено официально",
    gap='В источниках иммиграционных сервисов встречается требование о сроке действия справки о несудимости — 90 дней с даты выдачи; в официальном тексте закона это не закреплено. Мы не считаем этот срок окончательным и уточняем актуальные требования индивидуально перед подачей.',
    p_fee='Государственная пошлина по общему режиму — ₲ 2 787 550 (наличными) / ₲ 2 864 208 (картой), действует с 1 июля 2025 года. Статус выдаётся на 2 года с возможностью продления на такой же срок, утрачивается при непрерывном отсутствии в стране свыше 1 года.',
    p_confidence='Источники: Ley N° 6984/22 «De Migraciones» (ст. 50) — в пересказе юридических фирм, без прямой сверки с текстом закона на официальном портале; VF Paraguay Gestiones, Romero Machuca &amp; Asociados. Уверенность по списку документов — средняя-высокая; по сроку действия справки о несудимости — низкая-средняя.',
    p_next='Дальше — конверсия в <a href="{dok-permanente}">постоянную резидентуру</a>. Если вы уже определились с переездом, <a href="{kontakty}">оставьте заявку на консультацию</a> — мы проверяем комплект документов до подачи, а не после отказа.',
),
"es": dict(
    title="Residencia temporal: lista de documentos (Residencia Temporal) | Grund Paraguay",
    description="Lista completa de documentos para la residencia temporal en Paraguay según el art. 50 de la Ley N.° 6984/22: apostilla, traducción, arancel y vigencia del estatus.",
    h1="Residencia temporal: qué documentos se necesitan",
    lead="La Residencia Temporal es un permiso que otorga el derecho a vivir legalmente en Paraguay: se concede por 2 años, renovable por el mismo plazo, y abre el camino hacia la residencia permanente. Es el primer paso de la legalización, común a cualquiera de los programas posteriores; el paquete único de documentos para tramitarla está fijado en el art. 50 de la Ley N.° 6984/22 «De Migraciones».",
    intro='El paquete de documentos para la residencia temporal no depende de la categoría del solicitante — a diferencia de la residencia permanente (ver la página <a href="{dok-permanente}">«Residencia permanente»</a>), donde desde 2026 rige un sistema aparte de 12 categorías. Se necesitan:',
    items=[
        "Pasaporte — vigente, con validez suficiente para todo el trámite.",
        'Visa consular — no se exige a los ciudadanos rusos gracias al régimen sin visado desde 2014 (más detalles en la página <a href="{viza-vyezd}">«Visa, documentos y entrada»</a>).',
        'Partida de nacimiento — apostillada, traducida al español por un traductor público matriculado en Paraguay (<a href="{terminologiya}#traductor-publico">Traductor Público matriculado</a>).',
        "Certificado de estado civil / partida de matrimonio — si corresponde.",
        'Certificado de antecedentes penales internacional — con <a href="{terminologiya}#apostil">apostilla</a>, traducido.',
        'Declaración jurada de compromiso de respetar la constitución y las leyes de Paraguay — se realiza ya en el país, en la <a href="{terminologiya}#dnm">DNM</a>.',
        "Declaración jurada sobre la profesión y el domicilio de residencia en Paraguay.",
        "Comparecencia personal en la DNM — obligatoria, no se puede tramitar a distancia.",
    ],
    gap_label="No confirmado oficialmente",
    gap='En fuentes de servicios de inmigración aparece un requisito de vigencia de 90 días desde la fecha de emisión para el certificado de antecedentes penales; el texto oficial de la ley no lo establece. No consideramos este plazo definitivo y confirmamos los requisitos vigentes de forma individual antes de la presentación.',
    p_fee='El arancel estatal del régimen general es de ₲ 2.787.550 (en efectivo) / ₲ 2.864.208 (con tarjeta), vigente desde el 1 de julio de 2025. El estatus se otorga por 2 años con posibilidad de renovación por el mismo plazo, y se pierde si hay ausencia continua del país por más de 1 año.',
    p_confidence='Fuentes: Ley N.° 6984/22 «De Migraciones» (art. 50) — según lo relatado por firmas jurídicas de Paraguay, sin cotejo directo con el texto de la ley en el portal oficial; VF Paraguay Gestiones, Romero Machuca &amp; Asociados. Confianza sobre la lista de documentos — media-alta; sobre la vigencia del certificado de antecedentes penales — baja-media.',
    p_next='El siguiente paso es la conversión a la <a href="{dok-permanente}">residencia permanente</a>. Si ya decidió mudarse, <a href="{kontakty}">solicite una consulta</a> — verificamos el paquete de documentos antes de presentarlo, no después de un rechazo.',
),
"en": dict(
    title="Temporary Residency: Document Checklist (Residencia Temporal) | Grund Paraguay",
    description="The full document list for temporary residency in Paraguay under Art. 50 of Ley N° 6984/22: apostille, translation, fee, and how long the status lasts.",
    h1="Temporary Residency: What Documents You Need",
    lead='Residencia Temporal is a status that grants the right to live legally in Paraguay: it\'s issued for 2 years with the option to renew for the same term, and opens the path to permanent residency. It\'s the first step to legalization, common to any of the further programs; the single document package for it is set out in Art. 50 of Ley N° 6984/22 "De Migraciones".',
    intro='The document package for temporary residency doesn\'t depend on the applicant\'s category — unlike permanent residency (see the <a href="{dok-permanente}">"Permanent Residency"</a> page), where a separate system of 12 categories has been in effect since 2026. You\'ll need:',
    items=[
        "Passport — valid, with enough remaining validity to cover the whole process.",
        'Consular visa — not required for Russian citizens thanks to the visa-free regime in place since 2014 (more on the <a href="{viza-vyezd}">"Visa, Documents, and Entry"</a> page).',
        'Birth certificate — apostilled, translated into Spanish by a sworn translator registered in Paraguay (<a href="{terminologiya}#traductor-publico">Traductor Público matriculado</a>).',
        "Marital status certificate / marriage certificate — if applicable.",
        'International criminal record certificate — <a href="{terminologiya}#apostil">apostilled</a>, translated.',
        'A written undertaking to abide by Paraguay\'s constitution and laws — completed in-country, at <a href="{terminologiya}#dnm">DNM</a>.',
        "A sworn statement of your profession and residential address in Paraguay.",
        "In-person appearance at DNM — mandatory, cannot be done remotely.",
    ],
    gap_label="Not officially confirmed",
    gap='Immigration-service sources mention a requirement that the criminal record certificate be valid for 90 days from its issue date; the official text of the law doesn\'t set this out. We don\'t treat this as a final deadline and confirm the current requirements individually before filing.',
    p_fee='The government fee under the general regime is ₲2,787,550 (cash) / ₲2,864,208 (card), in effect since July 1, 2025. The status is granted for 2 years with the option to renew for the same term, and is forfeited after a continuous absence from the country of more than 1 year.',
    p_confidence='Sources: Ley N° 6984/22 "De Migraciones" (Art. 50) — as summarized by Paraguayan law firms, without direct cross-checking against the law\'s text on the official portal; VF Paraguay Gestiones, Romero Machuca &amp; Asociados. Confidence on the document list — medium-high; on the criminal record certificate\'s validity period — low-medium.',
    p_next='Next comes conversion to <a href="{dok-permanente}">permanent residency</a>. If you\'ve already decided to move, <a href="{kontakty}">request a consultation</a> — we check your document package before filing, not after a rejection.',
),
"de": dict(
    title="Befristeter Aufenthalt: Dokumentenliste (Residencia Temporal) | Grund Paraguay",
    description="Die vollständige Dokumentenliste für den befristeten Aufenthalt in Paraguay gemäß Art. 50 des Ley N° 6984/22: Apostille, Übersetzung, Gebühr und Gültigkeitsdauer des Status.",
    h1="Befristeter Aufenthalt: welche Dokumente nötig sind",
    lead='Die Residencia Temporal ist ein Status, der das Recht gibt, legal in Paraguay zu leben: Sie wird für 2 Jahre mit Verlängerungsoption erteilt und öffnet den Weg zum Daueraufenthalt. Sie ist der erste Schritt zur Legalisierung, gemeinsam für jedes der weiteren Programme; das einheitliche Dokumentenpaket dafür ist in Art. 50 des Ley N° 6984/22 „De Migraciones" festgelegt.',
    intro='Das Dokumentenpaket für den befristeten Aufenthalt hängt nicht von der Kategorie des Antragstellers ab — anders als beim Daueraufenthalt (siehe Seite <a href="{dok-permanente}">„Daueraufenthalt"</a>), wo seit 2026 ein eigenes System aus 12 Kategorien gilt. Benötigt werden:',
    items=[
        "Reisepass — gültig, mit ausreichender Restgültigkeit für den gesamten Prozess.",
        'Konsularisches Visum — für russische Staatsbürger dank der visumfreien Regelung seit 2014 nicht erforderlich (mehr auf der Seite <a href="{viza-vyezd}">„Visum, Dokumente und Einreise"</a>).',
        'Geburtsurkunde — apostilliert, ins Spanische übersetzt von einem in Paraguay registrierten vereidigten Übersetzer (<a href="{terminologiya}#traductor-publico">Traductor Público matriculado</a>).',
        "Familienstandsbescheinigung / Heiratsurkunde — falls zutreffend.",
        'Internationales Führungszeugnis — mit <a href="{terminologiya}#apostil">Apostille</a>, übersetzt.',
        'Schriftliche Verpflichtungserklärung zur Einhaltung der Verfassung und Gesetze Paraguays — wird bereits im Land bei der <a href="{terminologiya}#dnm">DNM</a> abgegeben.',
        "Eidesstattliche Erklärung zu Beruf und Wohnadresse in Paraguay.",
        "Persönliches Erscheinen bei der DNM — obligatorisch, keine Fernbearbeitung möglich.",
    ],
    gap_label="Nicht offiziell bestätigt",
    gap='In Quellen von Einwanderungsdienstleistern findet sich eine Anforderung, wonach das Führungszeugnis ab Ausstellungsdatum 90 Tage gültig sein muss; im offiziellen Gesetzestext ist das nicht festgelegt. Wir betrachten diese Frist nicht als endgültig und klären die aktuell geltenden Anforderungen vor der Einreichung individuell.',
    p_fee='Die staatliche Gebühr im allgemeinen Regime beträgt ₲2.787.550 (bar) / ₲2.864.208 (Karte), gültig seit dem 1. Juli 2025. Der Status wird für 2 Jahre erteilt, mit Verlängerungsoption um denselben Zeitraum, und erlischt bei ununterbrochener Abwesenheit vom Land von mehr als 1 Jahr.',
    p_confidence='Quellen: Ley N° 6984/22 „De Migraciones" (Art. 50) — wiedergegeben von paraguayischen Anwaltskanzleien, ohne direkten Abgleich mit dem Gesetzestext auf dem offiziellen Portal; VF Paraguay Gestiones, Romero Machuca &amp; Asociados. Vertrauen bezüglich der Dokumentenliste — mittel-hoch; bezüglich der Gültigkeitsdauer des Führungszeugnisses — niedrig-mittel.',
    p_next='Als Nächstes folgt die Umwandlung in den <a href="{dok-permanente}">Daueraufenthalt</a>. Wenn Sie sich bereits für den Umzug entschieden haben, <a href="{kontakty}">fordern Sie eine Beratung an</a> — wir prüfen Ihr Dokumentenpaket vor der Einreichung, nicht nach einer Ablehnung.',
),
}


def build_temporal():
    for lang in LANGS:
        l = L(lang)
        t = TEMPORAL[lang]
        items_html = "\n      ".join(f"<li>{it.format(**l)}</li>" for it in t["items"])
        body = f'''
{breadcrumbs([(NAV_LABELS[lang]["home"], l['home']), (NAV_LABELS[lang]["dokumenty"], l['dokumenty']), (NAV_LABELS[lang]["dok-temporal"], None)])}
<section class="hero" style="padding-top:24px;">
  <div class="wrap">
    <h1>{t["h1"]}</h1>
    <p class="lead">{t["lead"]}</p>
  </div>
</section>
{step_indicator(lang, l, "dok-temporal")}
<section style="padding-top:0;">
  <div class="prose">
    <p>{t["intro"].format(**l)}</p>
    <ol>
      {items_html}
    </ol>
    <div class="callout"><span class="callout-label">{t["gap_label"]}</span>{t["gap"]}</div>
    <p>{t["p_fee"]}</p>
    <p class="confidence-note">{t["p_confidence"]}</p>
    <p>{t["p_next"].format(**l)}</p>
  </div>
</section>
'''
        page("dok-temporal", lang, t["title"], t["description"], body,
             extra_schema=schema_breadcrumb([
                 (NAV_LABELS[lang]["home"], f"/{lang}/"),
                 (NAV_LABELS[lang]["dokumenty"], f"/{lang}/{href_to('dokumenty', lang)}"),
                 (NAV_LABELS[lang]["dok-temporal"], f"/{lang}/{href_to('dok-temporal', lang)}"),
             ]))


build_temporal()


# ====================================================== ПОСТОЯННАЯ РЕЗИДЕНТУРА

CATEGORIES_407 = {
"ru": [
    ("1", "Профессионал", "Диплом вуза, зарегистрированный в MEC, плюс запись в IPS, зарегистрированный трудовой договор или свежие декларации IVA/IRP со справкой о налоговой благонадёжности", "Одного диплома недостаточно — нужно подтвердить фактический доход/занятость"),
    ("2", "Техник", "Диплом техника, зарегистрированный в MEC, плюс та же альтернатива (занятость или налоговые декларации)", "Аналогично категории «Профессионал»"),
    ("3", "Наёмный работник", "Справка страхователя IPS либо трудовой договор, зарегистрированный в Минтруде", "Занятость должна быть формально подтверждаема"),
    ("4", "Самозанятый / независимый", "Регистрация как индивидуальный налогоплательщик плюс декларации IVA за последние 3 месяца либо последняя декларация IRP со справкой о налоговой благонадёжности", "Записи должны показывать реальное движение/активность"),
    ("5", "Удалённый работник / цифровой кочевник", "Справка о работе или подтверждение трудовых отношений с указанием дохода и способа его получения", "Иностранные документы — апостиль/легализация + перевод"),
    ("6", "Собственник недвижимости", "Право собственности, зарегистрированное в реестре, с выполнением условия о 2-летнем сроке регистрации", "DNM может запросить подтверждение дохода, приносимого недвижимостью"),
    ("7", "Акционер / партнёр компании", "Учредительный договор компании с указанием заявителя либо зарегистрированная книга акционеров / электронный реестр", "Доля участия должна быть официально зафиксирована"),
    ("8", "Фермер / животновод", "Título на продуктивную землю + справка о налоговой благонадёжности и регистрация как налогоплательщик, либо подтверждение продаж/закупок продукции или зарегистрированный бренд + налоговая благонадёжность", "Должна быть связь актива с производственной деятельностью"),
    ("9", "Служитель культа", "Регистрация конгрегации в MEC + письмо, подтверждающее роль заявителя и то, что организация покрывает расходы на проживание", "Финансовую ответственность несёт организация"),
    ("10", "Пенсионер", "Справка о пенсии с указанием суммы и способа выплаты", "Иностранные документы — легализация или апостиль"),
    ("11", "Иждивенец", "Свидетельство о браке, подтверждение родства (родитель/дедушка-бабушка, ребёнок/внук) или справка об инвалидности плюс парагвайское удостоверение личности / резидентская карта лица, предоставляющего содержание", "Допустимые степени родства и документы различаются по конкретному основанию"),
    ("12", "Совершеннолетний студент (18+)", "Справка об обучении на очной/заочной форме (регулярность, продолжение обучения, оплата) плюс собственный доход либо документально подтверждённая поддержка от родственника из допустимого круга", "Одного статуса студента недостаточно"),
],
"es": [
    ("1", "Profesional", "Título universitario registrado en el MEC, más inscripción en el IPS, contrato laboral registrado o declaraciones recientes de IVA/IRP con certificado de buena conducta tributaria", "Un título por sí solo no basta — hay que acreditar ingresos/empleo reales"),
    ("2", "Técnico", "Título técnico registrado en el MEC, más la misma alternativa (empleo o declaraciones tributarias)", "Igual que en la categoría «Profesional»"),
    ("3", "Trabajador en relación de dependencia", "Certificado del asegurador IPS o contrato laboral registrado en el Ministerio de Trabajo", "El empleo debe poder acreditarse formalmente"),
    ("4", "Autónomo / independiente", "Inscripción como contribuyente individual, más declaraciones de IVA de los últimos 3 meses o la última declaración de IRP con certificado de buena conducta tributaria", "Los registros deben mostrar movimiento/actividad real"),
    ("5", "Trabajador remoto / nómada digital", "Certificado laboral o confirmación de la relación de trabajo, indicando el ingreso y la forma de percibirlo", "Documentos extranjeros — apostilla/legalización + traducción"),
    ("6", "Propietario de inmuebles", "Título de propiedad inscripto en el registro, cumpliendo la condición de 2 años de antigüedad de la inscripción", "La DNM puede solicitar confirmación de los ingresos que genera el inmueble"),
    ("7", "Accionista / socio de empresa", "Contrato constitutivo de la empresa con mención del solicitante, o libro de accionistas registrado / registro electrónico", "La participación debe estar registrada oficialmente"),
    ("8", "Agricultor / ganadero", "Título sobre tierra productiva + certificado de buena conducta tributaria e inscripción como contribuyente, o confirmación de ventas/compras de producción o marca registrada + buena conducta tributaria", "Debe existir un vínculo entre el activo y la actividad productiva"),
    ("9", "Ministro de culto", "Inscripción de la congregación en el MEC + carta que confirme el rol del solicitante y que la organización cubre los gastos de manutención", "La responsabilidad financiera recae en la organización"),
    ("10", "Jubilado", "Certificado de jubilación con indicación del monto y la forma de pago", "Documentos extranjeros — legalización o apostilla"),
    ("11", "Dependiente", "Acta de matrimonio, comprobante de parentesco (padre/abuelo, hijo/nieto) o certificado de discapacidad, más la cédula paraguaya / carné de residente de la persona que brinda el sustento", "Los grados de parentesco admitidos y los documentos varían según el motivo concreto"),
    ("12", "Estudiante mayor de edad (18+)", "Certificado de estudios presenciales/a distancia (regularidad, continuidad, pago) más ingresos propios o apoyo documentado de un familiar dentro del círculo admitido", "El solo estatus de estudiante no es suficiente"),
],
"en": [
    ("1", "Professional", "University degree registered with MEC, plus IPS enrollment, a registered employment contract, or recent IVA/IRP tax filings with a tax-compliance certificate", "A degree alone isn't enough — actual income/employment must be confirmed"),
    ("2", "Technician", "Technical degree registered with MEC, plus the same alternative (employment or tax filings)", 'Same as the "Professional" category'),
    ("3", "Employee", "An IPS insured-party certificate or an employment contract registered with the Ministry of Labor", "Employment must be formally verifiable"),
    ("4", "Self-employed / independent", "Registration as an individual taxpayer, plus IVA filings for the last 3 months or the latest IRP filing with a tax-compliance certificate", "Records must show real activity/turnover"),
    ("5", "Remote worker / digital nomad", "A work certificate or confirmation of the employment relationship, stating income and how it's received", "Foreign documents — apostille/legalization + translation"),
    ("6", "Property owner", "Title of ownership registered in the registry, meeting the 2-year registration-age requirement", "DNM may request confirmation of income generated by the property"),
    ("7", "Shareholder / company partner", "The company's articles of incorporation naming the applicant, or a registered shareholder ledger / electronic registry", "The ownership stake must be officially recorded"),
    ("8", "Farmer / rancher", "Title to productive land + a tax-compliance certificate and taxpayer registration, or confirmation of production sales/purchases, or a registered brand + tax compliance", "There must be a link between the asset and the productive activity"),
    ("9", "Religious minister", "Registration of the congregation with MEC + a letter confirming the applicant's role and that the organization covers living expenses", "Financial responsibility rests with the organization"),
    ("10", "Retiree", "A pension certificate stating the amount and method of payment", "Foreign documents — legalization or apostille"),
    ("11", "Dependent", "Marriage certificate, proof of kinship (parent/grandparent, child/grandchild) or a disability certificate, plus the Paraguayan ID / residency card of the person providing support", "Eligible degrees of kinship and required documents vary by the specific basis"),
    ("12", "Adult student (18+)", "A certificate of full-time/distance enrollment (regular attendance, continued study, payment) plus own income or documented support from a relative within the eligible circle", "Student status alone isn't enough"),
],
"de": [
    ("1", "Fachkraft (Akademiker)", "Beim MEC registrierter Hochschulabschluss, zusätzlich IPS-Eintragung, registrierter Arbeitsvertrag oder aktuelle IVA/IRP-Steuererklärungen mit Steuerunbedenklichkeitsbescheinigung", "Ein Abschluss allein reicht nicht — tatsächliches Einkommen/Beschäftigung muss nachgewiesen werden"),
    ("2", "Techniker", "Beim MEC registrierter Technikerabschluss, zusätzlich dieselbe Alternative (Beschäftigung oder Steuererklärungen)", 'Analog zur Kategorie „Fachkraft"'),
    ("3", "Angestellter", "IPS-Versichertenbescheinigung oder beim Arbeitsministerium registrierter Arbeitsvertrag", "Die Beschäftigung muss formal nachweisbar sein"),
    ("4", "Selbstständiger / Unabhängiger", "Registrierung als Einzelsteuerpflichtiger, zusätzlich IVA-Erklärungen der letzten 3 Monate oder die letzte IRP-Erklärung mit Steuerunbedenklichkeitsbescheinigung", "Die Unterlagen müssen reale Bewegung/Aktivität zeigen"),
    ("5", "Remote-Arbeiter / digitaler Nomade", "Arbeitsbescheinigung oder Nachweis des Beschäftigungsverhältnisses mit Angabe des Einkommens und der Art seines Erhalts", "Ausländische Dokumente — Apostille/Legalisation + Übersetzung"),
    ("6", "Immobilieneigentümer", "Im Register eingetragenes Eigentumsrecht, unter Erfüllung der Bedingung einer 2-jährigen Eintragungsdauer", "Die DNM kann einen Nachweis der durch die Immobilie erzielten Einkünfte verlangen"),
    ("7", "Aktionär / Firmenpartner", "Gründungsvertrag des Unternehmens mit Nennung des Antragstellers oder registriertes Aktionärsbuch / elektronisches Register", "Der Beteiligungsanteil muss offiziell festgehalten sein"),
    ("8", "Landwirt / Viehzüchter", "Título für produktives Land + Steuerunbedenklichkeitsbescheinigung und Registrierung als Steuerpflichtiger, oder Nachweis von Verkäufen/Einkäufen von Produkten oder eingetragene Marke + Steuerunbedenklichkeit", "Es muss ein Zusammenhang zwischen dem Vermögenswert und der Produktionstätigkeit bestehen"),
    ("9", "Geistlicher", "Registrierung der Kongregation beim MEC + Schreiben, das die Rolle des Antragstellers bestätigt und dass die Organisation die Lebenshaltungskosten übernimmt", "Die finanzielle Verantwortung trägt die Organisation"),
    ("10", "Rentner", "Rentenbescheinigung mit Angabe des Betrags und der Zahlungsweise", "Ausländische Dokumente — Legalisation oder Apostille"),
    ("11", "Angehöriger (Unterhaltsberechtigter)", "Heiratsurkunde, Nachweis der Verwandtschaft (Elternteil/Großelternteil, Kind/Enkel) oder Behindertenausweis, plus paraguayischer Personalausweis / Aufenthaltskarte der unterhaltsgewährenden Person", "Zulässige Verwandtschaftsgrade und Dokumente unterscheiden sich je nach konkretem Grund"),
    ("12", "Volljähriger Student (18+)", "Studienbescheinigung (Präsenz-/Fernstudium — Regelmäßigkeit, Fortsetzung des Studiums, Zahlung) plus eigenes Einkommen oder dokumentierte Unterstützung durch einen Angehörigen aus dem zulässigen Kreis", "Der Studentenstatus allein reicht nicht aus"),
],
}

PERMANENTE = {
"ru": dict(
    title="Постоянная резидентура: документы и 12 категорий Resolución 407/2026 | Grund Paraguay",
    description="Документы для перехода в постоянную резиденцию Парагвая: общий порядок конверсии из временной и полная таблица документов по 12 категориям заявителей Resolución DNM N° 407/2026.",
    h1="Постоянная резидентура: документы и 12 категорий заявителей",
    lead="После двух лет временной резиденции — переход в постоянную (Residencia Permanente). С 6 июля 2026 года дополнительно действует система из 12 категорий заявителей с разными требованиями к документам, подтверждающим доход.",
    h2_transition="Общий переход из временной резиденции",
    p_transition="Заявление подаётся в течение 90 дней до истечения срока Residencia Temporal, при условии полных 2 лет статуса. Постоянная резиденция выдаётся на 10 лет с возможностью продления, утрачивается при непрерывном отсутствии свыше 3 лет.",
    h2_categories="12 категорий заявителей — Resolución DNM N° 407/2026",
    p_categories='Резолюция (<a href="{terminologiya}#resolucion-407">Resolución DNM N° 407/2026</a>) регулирует именно подтверждение экономической состоятельности — она не заменяет общий пакет документов для временной резиденции (см. страницу <a href="{dok-temporal}">«Временная резидентура»</a>), а добавляет к нему требования по конкретной категории. Действует для дел, поданных с 6 июля 2026 года.',
    gap_label="Уровень уверенности по таблице ниже",
    gap="Структура из 12 категорий подтверждена тремя независимыми источниками, но детальный список документов по каждой категории — только одним коммерческим иммиграционным сервисом, без построчной перепроверки. Перед подачей документов по конкретной категории стоит свериться с DNM напрямую или с юристом-партнёром — особенно по категориям «самозанятый», «акционер» и «иждивенец», наиболее вероятным для клиентов агентства.",
    table_caption="Документы по категориям Resolución DNM N° 407/2026",
    table_head=["Категория", "Требуемые документы", "Комментарий"],
    h2_general="Общие требования ко всем категориям",
    p_general='Документы должны соответствовать роду занятий, заявленному во время временной резиденции; позволять объективно проверить реальный доход или источник средств; быть актуальными. Иностранные документы — с апостилем (<a href="{terminologiya}#apostil">апостиль</a>) и переводом присяжного переводчика. Резолюция не устанавливает единый минимальный порог дохода для всех категорий — акцент на достаточности и проверяемости подтверждения, а не на фиксированной сумме.',
    p_confidence='Источники: Paraguay Sovereign («Resolution 407 Explained»), MERSAN, ADN Digital (25.06.2026). Уверенность по факту существования резолюции, дате и структуре из 12 категорий — высокая; по документам внутри каждой категории — средняя.',
    p_next='Более быстрый путь к постоянной резиденции — без прохождения временной — описан на странице <a href="{dok-investor}">«Инвесторский путь»</a>. Следующий этап легализации после постоянной резиденции — <a href="{dok-grazhdanstvo}">гражданство</a>. Если нужна оценка вашей категории — <a href="{kontakty}">оставьте заявку на консультацию</a>.',
),
"es": dict(
    title="Residencia permanente: documentos y las 12 categorías de la Resolución 407/2026 | Grund Paraguay",
    description="Documentos para la conversión a la residencia permanente en Paraguay: el procedimiento general de conversión desde la temporal y la tabla completa de documentos para las 12 categorías de solicitantes de la Resolución DNM N.° 407/2026.",
    h1="Residencia permanente: documentos y las 12 categorías de solicitantes",
    lead="Tras dos años de residencia temporal — la conversión a la permanente (Residencia Permanente). Desde el 6 de julio de 2026 rige además un sistema de 12 categorías de solicitantes con distintos requisitos de documentos que acreditan ingresos.",
    h2_transition="Conversión general desde la residencia temporal",
    p_transition="La solicitud se presenta dentro de los 90 días previos al vencimiento de la Residencia Temporal, siempre que se hayan cumplido los 2 años completos del estatus. La residencia permanente se otorga por 10 años con posibilidad de renovación, y se pierde si hay ausencia continua del país por más de 3 años.",
    h2_categories="12 categorías de solicitantes — Resolución DNM N.° 407/2026",
    p_categories='La resolución (<a href="{terminologiya}#resolucion-407">Resolución DNM N.° 407/2026</a>) regula precisamente la acreditación de la solvencia económica — no reemplaza el paquete general de documentos para la residencia temporal (ver la página <a href="{dok-temporal}">«Residencia temporal»</a>), sino que añade a este los requisitos de la categoría concreta. Rige para expedientes presentados desde el 6 de julio de 2026.',
    gap_label="Nivel de confianza de la tabla siguiente",
    gap="La estructura de 12 categorías está confirmada por tres fuentes independientes, pero la lista detallada de documentos por categoría proviene de un solo servicio de inmigración comercial, sin verificación línea por línea. Antes de presentar documentos de una categoría concreta, conviene consultarlo directamente con la DNM o con un abogado socio — especialmente en las categorías «autónomo», «accionista» y «dependiente», las más probables para los clientes de la agencia.",
    table_caption="Documentos por categoría de la Resolución DNM N.° 407/2026",
    table_head=["Categoría", "Documentos requeridos", "Comentario"],
    h2_general="Requisitos generales para todas las categorías",
    p_general='Los documentos deben corresponder a la actividad declarada durante la residencia temporal; permitir verificar objetivamente el ingreso real o la fuente de fondos; y estar vigentes. Los documentos extranjeros — con <a href="{terminologiya}#apostil">apostilla</a> y traducción de un traductor público. La resolución no fija un umbral mínimo de ingresos único para todas las categorías — el énfasis está en la suficiencia y verificabilidad de la acreditación, no en una suma fija.',
    p_confidence='Fuentes: Paraguay Sovereign («Resolution 407 Explained»), MERSAN, ADN Digital (25.06.2026). Confianza sobre la existencia de la resolución, su fecha y la estructura de 12 categorías — alta; sobre los documentos dentro de cada categoría — media.',
    p_next='Una vía más rápida a la residencia permanente — sin pasar por la temporal — se describe en la página <a href="{dok-investor}">«Vía de inversor»</a>. La siguiente etapa de legalización después de la residencia permanente es la <a href="{dok-grazhdanstvo}">ciudadanía</a>. Si necesita una evaluación de su categoría — <a href="{kontakty}">solicite una consulta</a>.',
),
"en": dict(
    title="Permanent Residency: Documents & the 12 Categories of Resolución 407/2026 | Grund Paraguay",
    description="Documents for converting to permanent residency in Paraguay: the general conversion procedure from temporary residency and a full table of documents for the 12 applicant categories under Resolución DNM N° 407/2026.",
    h1="Permanent Residency: Documents & the 12 Applicant Categories",
    lead="After two years of temporary residency, the next step is converting to permanent residency (Residencia Permanente). Since July 6, 2026, a system of 12 applicant categories has also been in effect, with different document requirements to prove income.",
    h2_transition="General Conversion from Temporary Residency",
    p_transition="The application is filed within 90 days before Residencia Temporal expires, provided the full 2-year term has been completed. Permanent residency is granted for 10 years with the option to renew, and is forfeited after a continuous absence of more than 3 years.",
    h2_categories="12 Applicant Categories — Resolución DNM N° 407/2026",
    p_categories='The resolution (<a href="{terminologiya}#resolucion-407">Resolución DNM N° 407/2026</a>) specifically governs proof of economic solvency — it doesn\'t replace the general document package for temporary residency (see the <a href="{dok-temporal}">"Temporary Residency"</a> page), but adds category-specific requirements on top of it. It applies to cases filed since July 6, 2026.',
    gap_label="Confidence level for the table below",
    gap='The 12-category structure is confirmed by three independent sources, but the detailed document list for each category comes from a single commercial immigration service, without a line-by-line cross-check. Before filing documents under a specific category, it\'s worth checking directly with DNM or a partner lawyer — especially for the "self-employed", "shareholder", and "dependent" categories, the most likely ones for the agency\'s clients.',
    table_caption="Documents by Category — Resolución DNM N° 407/2026",
    table_head=["Category", "Required Documents", "Comment"],
    h2_general="General Requirements for All Categories",
    p_general='Documents must match the occupation declared during temporary residency; allow objective verification of real income or source of funds; and be current. Foreign documents — <a href="{terminologiya}#apostil">apostilled</a> and translated by a sworn translator. The resolution doesn\'t set a single minimum income threshold for all categories — the emphasis is on the sufficiency and verifiability of the proof, not a fixed amount.',
    p_confidence='Sources: Paraguay Sovereign ("Resolution 407 Explained"), MERSAN, ADN Digital (06/25/2026). Confidence on the resolution\'s existence, date, and 12-category structure — high; on the documents within each category — medium.',
    p_next='A faster route to permanent residency — without going through the temporary stage — is described on the <a href="{dok-investor}">"Investor Route"</a> page. The next legalization stage after permanent residency is <a href="{dok-grazhdanstvo}">citizenship</a>. If you need an assessment of your category — <a href="{kontakty}">request a consultation</a>.',
),
"de": dict(
    title="Daueraufenthalt: Dokumente und die 12 Kategorien der Resolución 407/2026 | Grund Paraguay",
    description="Dokumente für die Umwandlung in den Daueraufenthalt in Paraguay: das allgemeine Verfahren der Umwandlung aus dem befristeten Aufenthalt und die vollständige Dokumententabelle für die 12 Antragstellerkategorien der Resolución DNM N° 407/2026.",
    h1="Daueraufenthalt: Dokumente und die 12 Antragstellerkategorien",
    lead="Nach zwei Jahren befristetem Aufenthalt folgt die Umwandlung in den Daueraufenthalt (Residencia Permanente). Seit dem 6. Juli 2026 gilt zusätzlich ein System aus 12 Antragstellerkategorien mit unterschiedlichen Anforderungen an Einkommensnachweise.",
    h2_transition="Allgemeiner Übergang vom befristeten Aufenthalt",
    p_transition="Der Antrag wird innerhalb von 90 Tagen vor Ablauf der Residencia Temporal gestellt, vorausgesetzt der Status bestand volle 2 Jahre. Der Daueraufenthalt wird für 10 Jahre mit Verlängerungsoption erteilt und erlischt bei ununterbrochener Abwesenheit von mehr als 3 Jahren.",
    h2_categories="12 Antragstellerkategorien — Resolución DNM N° 407/2026",
    p_categories='Die Resolution (<a href="{terminologiya}#resolucion-407">Resolución DNM N° 407/2026</a>) regelt speziell den Nachweis der wirtschaftlichen Leistungsfähigkeit — sie ersetzt nicht das allgemeine Dokumentenpaket für den befristeten Aufenthalt (siehe Seite <a href="{dok-temporal}">„Befristeter Aufenthalt"</a>), sondern ergänzt es um kategorie-spezifische Anforderungen. Sie gilt für Verfahren, die seit dem 6. Juli 2026 eingereicht wurden.',
    gap_label="Vertrauensniveau zur folgenden Tabelle",
    gap='Die Struktur aus 12 Kategorien wird von drei unabhängigen Quellen bestätigt, die detaillierte Dokumentenliste je Kategorie stammt jedoch nur von einem kommerziellen Einwanderungsdienstleister, ohne zeilenweise Gegenprüfung. Vor Einreichung von Dokumenten für eine konkrete Kategorie lohnt sich eine Rücksprache direkt mit der DNM oder einem Partneranwalt — besonders bei den Kategorien „Selbstständiger", „Aktionär" und „Angehöriger", die für Kunden der Agentur am wahrscheinlichsten sind.',
    table_caption="Dokumente nach Kategorie — Resolución DNM N° 407/2026",
    table_head=["Kategorie", "Erforderliche Dokumente", "Kommentar"],
    h2_general="Allgemeine Anforderungen für alle Kategorien",
    p_general='Die Dokumente müssen der während des befristeten Aufenthalts angegebenen Tätigkeit entsprechen; eine objektive Prüfung des tatsächlichen Einkommens oder der Mittelherkunft ermöglichen; und aktuell sein. Ausländische Dokumente — mit <a href="{terminologiya}#apostil">Apostille</a> und Übersetzung durch einen vereidigten Übersetzer. Die Resolution legt keine einheitliche Mindesteinkommensschwelle für alle Kategorien fest — der Schwerpunkt liegt auf der Ausreichung und Nachprüfbarkeit des Nachweises, nicht auf einem festen Betrag.',
    p_confidence='Quellen: Paraguay Sovereign („Resolution 407 Explained"), MERSAN, ADN Digital (25.06.2026). Vertrauen bezüglich der Existenz der Resolution, ihres Datums und der 12-Kategorien-Struktur — hoch; bezüglich der Dokumente innerhalb jeder Kategorie — mittel.',
    p_next='Ein schnellerer Weg zum Daueraufenthalt — ohne die befristete Phase zu durchlaufen — wird auf der Seite <a href="{dok-investor}">„Investorenweg"</a> beschrieben. Die nächste Legalisierungsetappe nach dem Daueraufenthalt ist die <a href="{dok-grazhdanstvo}">Staatsbürgerschaft</a>. Wenn Sie eine Einschätzung Ihrer Kategorie benötigen — <a href="{kontakty}">fordern Sie eine Beratung an</a>.',
),
}


def build_permanente():
    for lang in LANGS:
        l = L(lang)
        t = PERMANENTE[lang]
        rows_html = "\n        ".join(
            f"<tr><td><strong>{num}. {name}</strong></td><td>{docs}</td><td>{comment}</td></tr>"
            for num, name, docs, comment in CATEGORIES_407[lang]
        )
        body = f'''
{breadcrumbs([(NAV_LABELS[lang]["home"], l['home']), (NAV_LABELS[lang]["dokumenty"], l['dokumenty']), (NAV_LABELS[lang]["dok-permanente"], None)])}
<section class="hero" style="padding-top:24px;">
  <div class="wrap">
    <h1>{t["h1"]}</h1>
    <p class="lead">{t["lead"]}</p>
  </div>
</section>
{step_indicator(lang, l, "dok-permanente")}
<section style="padding-top:0;">
  <div class="prose">
    <h2>{t["h2_transition"]}</h2>
    <p>{t["p_transition"]}</p>
    <h2>{t["h2_categories"]}</h2>
    <p>{t["p_categories"].format(**l)}</p>
    <div class="callout"><span class="callout-label">{t["gap_label"]}</span>{t["gap"]}</div>
  </div>
</section>
<section style="padding-top:0;">
  <div class="wrap">
    <table>
      <caption>{t["table_caption"]}</caption>
      <thead><tr><th>{t["table_head"][0]}</th><th>{t["table_head"][1]}</th><th>{t["table_head"][2]}</th></tr></thead>
      <tbody>
        {rows_html}
      </tbody>
    </table>
  </div>
</section>
<section style="padding-top:0;">
  <div class="prose">
    <h2>{t["h2_general"]}</h2>
    <p>{t["p_general"].format(**l)}</p>
    <p class="confidence-note">{t["p_confidence"]}</p>
    <p>{t["p_next"].format(**l)}</p>
  </div>
</section>
'''
        page("dok-permanente", lang, t["title"], t["description"], body,
             extra_schema=schema_breadcrumb([
                 (NAV_LABELS[lang]["home"], f"/{lang}/"),
                 (NAV_LABELS[lang]["dokumenty"], f"/{lang}/{href_to('dokumenty', lang)}"),
                 (NAV_LABELS[lang]["dok-permanente"], f"/{lang}/{href_to('dok-permanente', lang)}"),
             ]))


build_permanente()


# ========================================================= ИНВЕСТОРСКИЙ ПУТЬ

INVESTOR = {
"ru": dict(
    title="Инвесторский путь: документы для сертификата инвестора CIE | Grund Paraguay",
    description="Официальный перечень документов SUACE для сертификата инвестора (CIE) — прямой доступ к постоянной резиденции Парагвая от 70 000 USD инвестиций, без временной резиденции.",
    h1="Инвесторский путь: документы для сертификата инвестора",
    lead="Прямой доступ к постоянной резиденции без прохождения временной — от 70 000 USD инвестиций. Список документов на сертификат инвестора (CIE) ниже — с официального PDF портала SUACE, а не пересказ вторичных источников.",
    source_label="Первоисточник",
    source='Список ниже — с официального PDF suace.gov.py «Requisitos para solicitar la Constancia de Inversionista Extranjero». Уверенность: высокая.',
    h2_docs='Документы для сертификата инвестора (<a href="{terminologiya}#cie">CIE</a>)',
    items=[
        "Заверенная нотариусом копия документа, удостоверяющего личность, — Cédula страны происхождения или загранпаспорт.",
        "Справка о несудимости из страны происхождения — с апостилем или легализацией.",
        "Подтверждение въезда или законного пребывания в Парагвае.",
        "Справка Interpol Paraguay.",
        "Заполненная и подписанная анкета на сертификат иностранного инвестора.",
        'Присяжное заявление об обязательстве открыть бизнес через <a href="{terminologiya}#suace">SUACE</a> и инвестировать в Парагвае — заверяется нотариально.',
        "Профиль инвестиционного проекта, подписанный заявителем.",
    ],
    h2_thresholds="Минимальная сумма инвестиций по веткам",
    p_thresholds='От 70 000 USD — производственная ветка (при бизнес-плане и создании 5 официальных рабочих мест); от 200 000 USD — недвижимость или финансовые инструменты; от 150 000 USD — туризм (при бизнес-плане и полугодовой отчётности). Официальный документ с перечнем документов на CIE не делит список по веткам — судя по всему, тот же комплект подаётся независимо от выбранного режима, а более высокие пороги регулируются самим текстом <a href="{terminologiya}#investor-pass">Resolución MIC N° 0283/2026</a>, а не списком документов на сертификат.',
    gap_label="Что не уточнено",
    gap="Документ SUACE не уточняет, требуются ли для веток «недвижимость» и «финансовые инструменты» дополнительные документы (например, договор купли-продажи или подтверждение депозита) сверх базового списка выше — уточняем это индивидуально на консультации.",
    p_timing="Сертификат CIE оформляется официально за 5 рабочих дней с момента подачи полного пакета документов. Сама постоянная резиденция, по оценке отраслевых изданий, занимает ещё около 3–6 месяцев сверху — это не официальный норматив, а оценка.",
    p_confidence='Источники: официальный PDF suace.gov.py (документы на CIE, первоисточник); IMI Daily, Fragomen (пороги по веткам и сроки резиденции). Уверенность по списку документов — высокая; по срокам получения самой резиденции — средняя (оценка отраслевых изданий, не официальный норматив).',
    p_next='Общий переход к постоянной резиденции без инвестиций описан на странице <a href="{dok-permanente}">«Постоянная резидентура»</a>. Если рассматриваете инвесторский путь — <a href="{kontakty}">оставьте заявку на консультацию</a>, разберём, какая ветка подходит именно вам.',
),
"es": dict(
    title="Vía de inversor: documentos para el certificado de inversor CIE | Grund Paraguay",
    description="Lista oficial de documentos de SUACE para el certificado de inversor (CIE) — acceso directo a la residencia permanente en Paraguay desde 70.000 USD de inversión, sin pasar por la residencia temporal.",
    h1="Vía de inversor: documentos para el certificado de inversor",
    lead="Acceso directo a la residencia permanente sin pasar por la temporal — desde 70.000 USD de inversión. La lista de documentos para el certificado de inversor (CIE) a continuación proviene del PDF oficial del portal de SUACE, no es un resumen de fuentes secundarias.",
    source_label="Fuente primaria",
    source='La lista siguiente proviene del PDF oficial de suace.gov.py «Requisitos para solicitar la Constancia de Inversionista Extranjero». Confianza: alta.',
    h2_docs='Documentos para el certificado de inversor (<a href="{terminologiya}#cie">CIE</a>)',
    items=[
        "Copia certificada por escribano del documento de identidad — Cédula del país de origen o pasaporte.",
        "Certificado de antecedentes penales del país de origen — apostillado o legalizado.",
        "Confirmación de ingreso o estadía legal en Paraguay.",
        "Certificado de Interpol Paraguay.",
        "Formulario de solicitud del certificado de inversor extranjero, completo y firmado.",
        'Declaración jurada del compromiso de abrir una empresa a través de <a href="{terminologiya}#suace">SUACE</a> e invertir en Paraguay — certificada ante escribano.',
        "Perfil del proyecto de inversión, firmado por el solicitante.",
    ],
    h2_thresholds="Monto mínimo de inversión por rama",
    p_thresholds='Desde 70.000 USD — rama productiva (con plan de negocios y creación de 5 puestos de trabajo formales); desde 200.000 USD — inmuebles o instrumentos financieros; desde 150.000 USD — turismo (con plan de negocios e informes semestrales). El documento oficial con la lista de documentos para el CIE no divide la lista por ramas — al parecer, se presenta el mismo paquete independientemente del régimen elegido, y los umbrales más altos están regulados por el propio texto de la <a href="{terminologiya}#investor-pass">Resolución MIC N.° 0283/2026</a>, no por la lista de documentos del certificado.',
    gap_label="Qué no está aclarado",
    gap="El documento de SUACE no aclara si para las ramas «inmuebles» e «instrumentos financieros» se requieren documentos adicionales (por ejemplo, contrato de compraventa o confirmación de depósito) además de la lista básica anterior — lo aclaramos de forma individual en la consulta.",
    p_timing="El certificado CIE se tramita oficialmente en 5 días hábiles desde la presentación del paquete completo de documentos. La residencia permanente en sí, según estimaciones de medios especializados, demora otros 3 a 6 meses adicionales — no es una norma oficial, sino una estimación.",
    p_confidence='Fuentes: PDF oficial de suace.gov.py (documentos para el CIE, fuente primaria); IMI Daily, Fragomen (umbrales por rama y plazos de residencia). Confianza sobre la lista de documentos — alta; sobre los plazos para obtener la residencia en sí — media (estimación de medios especializados, no norma oficial).',
    p_next='La conversión general a la residencia permanente sin inversión se describe en la página <a href="{dok-permanente}">«Residencia permanente»</a>. Si está considerando la vía de inversor — <a href="{kontakty}">solicite una consulta</a>, analizamos qué rama le conviene.',
),
"en": dict(
    title="Investor Route: Documents for the CIE Investor Certificate | Grund Paraguay",
    description="The official SUACE document list for the investor certificate (CIE) — direct access to permanent residency in Paraguay from 70,000 USD in investment, without going through temporary residency.",
    h1="Investor Route: Documents for the Investor Certificate",
    lead="Direct access to permanent residency without going through the temporary stage — from 70,000 USD in investment. The document list for the investor certificate (CIE) below comes from the official SUACE portal PDF, not a summary of secondary sources.",
    source_label="Primary source",
    source='The list below comes from the official suace.gov.py PDF "Requisitos para solicitar la Constancia de Inversionista Extranjero". Confidence: high.',
    h2_docs='Documents for the investor certificate (<a href="{terminologiya}#cie">CIE</a>)',
    items=[
        "A notary-certified copy of your ID document — Cédula from your home country or passport.",
        "A criminal record certificate from your home country — apostilled or legalized.",
        "Confirmation of entry or legal stay in Paraguay.",
        "An Interpol Paraguay certificate.",
        "A completed and signed foreign investor certificate application form.",
        'A sworn statement of your commitment to open a business through <a href="{terminologiya}#suace">SUACE</a> and invest in Paraguay — notarized.',
        "An investment project profile, signed by the applicant.",
    ],
    h2_thresholds="Minimum investment amounts by track",
    p_thresholds='From 70,000 USD — the production track (with a business plan and 5 formal jobs created); from 200,000 USD — real estate or financial instruments; from 150,000 USD — tourism (with a business plan and semi-annual reporting). The official document listing the CIE documents doesn\'t split the list by track — it appears the same package is filed regardless of the chosen regime, and the higher thresholds are governed by the text of <a href="{terminologiya}#investor-pass">Resolución MIC N° 0283/2026</a> itself, not by the certificate\'s document list.',
    gap_label="What isn't specified",
    gap='The SUACE document doesn\'t specify whether the "real estate" and "financial instruments" tracks require additional documents (e.g., a purchase agreement or deposit confirmation) beyond the basic list above — we clarify this individually during a consultation.',
    p_timing="The CIE certificate is officially processed within 5 business days of submitting the complete document package. Permanent residency itself, per industry estimates, takes another roughly 3–6 months on top — this isn't an official rule, just an estimate.",
    p_confidence='Sources: the official suace.gov.py PDF (documents for the CIE, primary source); IMI Daily, Fragomen (thresholds by track and residency timelines). Confidence on the document list — high; on the timeline for obtaining residency itself — medium (an industry estimate, not an official rule).',
    p_next='The general conversion to permanent residency without investment is described on the <a href="{dok-permanente}">"Permanent Residency"</a> page. If you\'re considering the investor route — <a href="{kontakty}">request a consultation</a> and we\'ll work out which track fits you.',
),
"de": dict(
    title="Investorenweg: Dokumente für das Investorenzertifikat CIE | Grund Paraguay",
    description="Die offizielle SUACE-Dokumentenliste für das Investorenzertifikat (CIE) — direkter Zugang zum Daueraufenthalt in Paraguay ab 70.000 USD Investition, ohne befristeten Aufenthalt.",
    h1="Investorenweg: Dokumente für das Investorenzertifikat",
    lead="Direkter Zugang zum Daueraufenthalt ohne befristete Phase — ab 70.000 USD Investition. Die folgende Dokumentenliste für das Investorenzertifikat (CIE) stammt aus dem offiziellen PDF des SUACE-Portals, nicht aus einer Zusammenfassung von Sekundärquellen.",
    source_label="Primärquelle",
    source='Die folgende Liste stammt aus dem offiziellen PDF von suace.gov.py „Requisitos para solicitar la Constancia de Inversionista Extranjero". Vertrauen: hoch.',
    h2_docs='Dokumente für das Investorenzertifikat (<a href="{terminologiya}#cie">CIE</a>)',
    items=[
        "Notariell beglaubigte Kopie des Ausweisdokuments — Cédula des Herkunftslands oder Reisepass.",
        "Führungszeugnis aus dem Herkunftsland — apostilliert oder legalisiert.",
        "Nachweis der Einreise oder des rechtmäßigen Aufenthalts in Paraguay.",
        "Interpol-Paraguay-Bescheinigung.",
        "Ausgefülltes und unterschriebenes Antragsformular für das Zertifikat für ausländische Investoren.",
        'Eidesstattliche Erklärung der Verpflichtung, über <a href="{terminologiya}#suace">SUACE</a> ein Unternehmen zu eröffnen und in Paraguay zu investieren — notariell beglaubigt.',
        "Vom Antragsteller unterschriebenes Investitionsprojektprofil.",
    ],
    h2_thresholds="Mindestinvestitionssummen nach Zweig",
    p_thresholds='Ab 70.000 USD — Produktionszweig (mit Geschäftsplan und Schaffung von 5 offiziellen Arbeitsplätzen); ab 200.000 USD — Immobilien oder Finanzinstrumente; ab 150.000 USD — Tourismus (mit Geschäftsplan und halbjährlicher Berichterstattung). Das offizielle Dokument mit der Liste der CIE-Dokumente unterteilt die Liste nicht nach Zweigen — offenbar wird dasselbe Paket unabhängig vom gewählten Regime eingereicht, und die höheren Schwellenwerte werden durch den Text der <a href="{terminologiya}#investor-pass">Resolución MIC N° 0283/2026</a> selbst geregelt, nicht durch die Dokumentenliste des Zertifikats.',
    gap_label="Was nicht geklärt ist",
    gap='Das SUACE-Dokument gibt nicht an, ob für die Zweige „Immobilien" und „Finanzinstrumente" zusätzliche Dokumente (z. B. Kaufvertrag oder Einlagennachweis) über die obige Basisliste hinaus erforderlich sind — dies klären wir individuell in der Beratung.',
    p_timing="Das CIE-Zertifikat wird offiziell innerhalb von 5 Werktagen ab Einreichung des vollständigen Dokumentenpakets ausgestellt. Der Daueraufenthalt selbst nimmt laut Brancheneinschätzungen weitere etwa 3–6 Monate zusätzlich in Anspruch — das ist keine offizielle Vorschrift, sondern eine Schätzung.",
    p_confidence='Quellen: offizielles PDF von suace.gov.py (Dokumente für das CIE, Primärquelle); IMI Daily, Fragomen (Schwellenwerte nach Zweig und Aufenthaltsfristen). Vertrauen bezüglich der Dokumentenliste — hoch; bezüglich der Fristen für den Daueraufenthalt selbst — mittel (Brancheneinschätzung, keine offizielle Vorschrift).',
    p_next='Die allgemeine Umwandlung in den Daueraufenthalt ohne Investition wird auf der Seite <a href="{dok-permanente}">„Daueraufenthalt"</a> beschrieben. Wenn Sie den Investorenweg in Erwägung ziehen — <a href="{kontakty}">fordern Sie eine Beratung an</a>, wir klären, welcher Zweig zu Ihnen passt.',
),
}


def build_investor():
    for lang in LANGS:
        l = L(lang)
        t = INVESTOR[lang]
        items_html = "\n      ".join(f"<li>{it.format(**l)}</li>" for it in t["items"])
        body = f'''
{breadcrumbs([(NAV_LABELS[lang]["home"], l['home']), (NAV_LABELS[lang]["dokumenty"], l['dokumenty']), (NAV_LABELS[lang]["dok-investor"], None)])}
<section class="hero" style="padding-top:24px;">
  <div class="wrap">
    <h1>{t["h1"]}</h1>
    <p class="lead">{t["lead"]}</p>
  </div>
</section>
{step_indicator(lang, l, "dok-investor")}
<section style="padding-top:0;">
  <div class="prose">
    <div class="callout"><span class="callout-label">{t["source_label"]}</span>{t["source"]}</div>
    <h2>{t["h2_docs"].format(**l)}</h2>
    <ol>
      {items_html}
    </ol>
    <h2>{t["h2_thresholds"]}</h2>
    <p>{t["p_thresholds"].format(**l)}</p>
    <div class="callout"><span class="callout-label">{t["gap_label"]}</span>{t["gap"]}</div>
    <p>{t["p_timing"]}</p>
    <p class="confidence-note">{t["p_confidence"]}</p>
    <p>{t["p_next"].format(**l)}</p>
  </div>
</section>
'''
        page("dok-investor", lang, t["title"], t["description"], body,
             extra_schema=schema_breadcrumb([
                 (NAV_LABELS[lang]["home"], f"/{lang}/"),
                 (NAV_LABELS[lang]["dokumenty"], f"/{lang}/{href_to('dokumenty', lang)}"),
                 (NAV_LABELS[lang]["dok-investor"], f"/{lang}/{href_to('dok-investor', lang)}"),
             ]))


build_investor()


# ================================================================ ГРАЖДАНСТВО

GRAZHDANSTVO = {
"ru": dict(
    title="Гражданство Парагвая: документы для натурализации | Grund Paraguay",
    description="Официальный перечень документов Corte Suprema de Justicia для получения Carta de Naturalización — гражданства Парагвая — не раньше 3 лет после постоянной резиденции.",
    h1="Гражданство: документы для натурализации",
    lead="Натурализация возможна не раньше чем через 3 года после получения постоянной резиденции (ст. 148 Конституции). Дело ведёт не миграционная служба, а Верховный суд (Corte Suprema de Justicia) — список документов ниже получен напрямую с официальной страницы Poder Judicial.",
    source_label="Первоисточник",
    source='Список документов — с официальной страницы Poder Judicial «Carta de Naturalización», не пересказ. Уверенность: высокая.',
    h2_docs='Документы для получения <a href="{terminologiya}#carta-naturalizacion">Carta de Naturalización</a>',
    items=[
        "Фотографии для документов — анфас и профиль, почтовый формат 15×10 см.",
        'Заверенная копия парагвайского удостоверения личности (<a href="{terminologiya}#cedula">Cédula</a>).',
        "Заверенная копия загранпаспорта — все страницы, включая пустые.",
        "Свидетельство о рождении — заверенная копия, с апостилем.",
        "Заверенная копия карты постоянного резидента, выданной DNM.",
        "Справка о резидентском статусе от DNM — 3 года статуса постоянного резидента с даты его получения.",
        "Справка об отсутствии судимости из полицейских органов идентификации Парагвая.",
        "Справка о судимости от судебной власти Парагвая.",
        "Справка о хорошем поведении из страны происхождения — с апостилем.",
        'Документы, подтверждающие род занятий — различаются по категории: наёмные работники — письмо от работодателя с номерами <a href="{terminologiya}#ips">IPS</a> и <a href="{terminologiya}#ruc">RUC</a>; предприниматели — коммерческий патент и данные RUC; студенты — справка об обучении; специалисты — документы о квалификации.',
        "Резюме (curriculum vitae).",
        "Присяжное заявление, подписываемое лично в Верховном суде.",
        "Судебная пошлина — ₲ 43 051.",
        "Письменное ходатайство о натурализации при сопровождении адвоката, с указанием постоянного адреса в Асунсьоне.",
    ],
    p_conditions="Дополнительные условия: заявитель должен быть совершеннолетним; обязательна личная явка для подписания присяжного заявления; все документы — оригиналы или заверенные копии; документы не на испанском переводятся зарегистрированным при Верховном суде переводчиком.",
    gap_label="Открытый вопрос",
    gap="Официальная страница не упоминает экзамен по испанскому/гуарани и истории Парагвая — при этом в 2019 году Сенат одобрил такой законопроект, и его текущий статус (принят/не принят) не выяснен. Уточняем этот вопрос индивидуально, если он окажется актуален к моменту вашей подачи.",
    p_confidence="Источник: официальная страница Poder Judicial «Carta de Naturalización» (первоисточник, государственный домен). Уверенность по списку документов — высокая; по вопросу языкового экзамена — не установлено.",
    p_next='Документы для предыдущего этапа — <a href="{dok-permanente}">постоянной резидентуры</a>. Если вы уже на этом этапе или хотите спланировать путь заранее — <a href="{kontakty}">оставьте заявку на консультацию</a>.',
),
"es": dict(
    title="Ciudadanía paraguaya: documentos para la naturalización | Grund Paraguay",
    description="Lista oficial de documentos de la Corte Suprema de Justicia para obtener la Carta de Naturalización — la ciudadanía paraguaya — no antes de 3 años después de la residencia permanente.",
    h1="Ciudadanía: documentos para la naturalización",
    lead="La naturalización es posible recién 3 años después de obtener la residencia permanente (art. 148 de la Constitución). El trámite no lo lleva el servicio de migraciones, sino la Corte Suprema de Justicia — la lista de documentos a continuación se obtuvo directamente de la página oficial del Poder Judicial.",
    source_label="Fuente primaria",
    source='La lista de documentos proviene de la página oficial del Poder Judicial «Carta de Naturalización», no es un resumen. Confianza: alta.',
    h2_docs='Documentos para obtener la <a href="{terminologiya}#carta-naturalizacion">Carta de Naturalización</a>',
    items=[
        "Fotografías tipo documento — de frente y de perfil, formato carné 15×10 cm.",
        'Copia certificada de la cédula de identidad paraguaya (<a href="{terminologiya}#cedula">Cédula</a>).',
        "Copia certificada del pasaporte — todas las páginas, incluidas las en blanco.",
        "Partida de nacimiento — copia certificada, apostillada.",
        "Copia certificada del carné de residente permanente emitido por la DNM.",
        "Certificado de estatus de residente de la DNM — 3 años de estatus de residente permanente desde la fecha de obtención.",
        "Certificado de antecedentes de los organismos de identificación policial de Paraguay.",
        "Certificado de antecedentes del poder judicial de Paraguay.",
        "Certificado de buena conducta del país de origen — apostillado.",
        'Documentos que acrediten la ocupación — varían según la categoría: trabajadores en relación de dependencia — carta del empleador con los números de <a href="{terminologiya}#ips">IPS</a> y <a href="{terminologiya}#ruc">RUC</a>; empresarios — patente comercial y datos del RUC; estudiantes — certificado de estudios; profesionales — documentos de cualificación.',
        "Currículum vitae.",
        "Declaración jurada, firmada personalmente ante la Corte Suprema.",
        "Tasa judicial — ₲ 43.051.",
        "Solicitud escrita de naturalización con el acompañamiento de un abogado, indicando el domicilio permanente en Asunción.",
    ],
    p_conditions="Condiciones adicionales: el solicitante debe ser mayor de edad; es obligatoria la comparecencia personal para firmar la declaración jurada; todos los documentos deben ser originales o copias certificadas; los documentos que no estén en español deben traducirse por un traductor registrado ante la Corte Suprema.",
    gap_label="Cuestión abierta",
    gap="La página oficial no menciona un examen de español/guaraní ni de historia de Paraguay — aunque en 2019 el Senado aprobó un proyecto de ley en ese sentido, y su estado actual (aprobado o no) no se ha podido determinar. Aclaramos esta cuestión de forma individual si resulta relevante al momento de su presentación.",
    p_confidence="Fuente: página oficial del Poder Judicial «Carta de Naturalización» (fuente primaria, dominio estatal). Confianza sobre la lista de documentos — alta; sobre la cuestión del examen de idioma — no determinada.",
    p_next='Documentos de la etapa anterior — <a href="{dok-permanente}">residencia permanente</a>. Si ya está en esta etapa o quiere planificar el camino con anticipación — <a href="{kontakty}">solicite una consulta</a>.',
),
"en": dict(
    title="Paraguayan Citizenship: Documents for Naturalization | Grund Paraguay",
    description="The official Corte Suprema de Justicia document list for obtaining the Carta de Naturalización — Paraguayan citizenship — not sooner than 3 years after permanent residency.",
    h1="Citizenship: Documents for Naturalization",
    lead="Naturalization is possible only 3 years after obtaining permanent residency (Art. 148 of the Constitution). The case is handled not by the migration service but by the Supreme Court (Corte Suprema de Justicia) — the document list below was taken directly from the official Poder Judicial page.",
    source_label="Primary source",
    source='The document list comes from the official Poder Judicial page "Carta de Naturalización", not a summary. Confidence: high.',
    h2_docs='Documents for obtaining the <a href="{terminologiya}#carta-naturalizacion">Carta de Naturalización</a>',
    items=[
        "Passport-style photos — front and profile, 15×10 cm format.",
        'A certified copy of your Paraguayan ID card (<a href="{terminologiya}#cedula">Cédula</a>).',
        "A certified copy of your passport — all pages, including blank ones.",
        "Birth certificate — certified copy, apostilled.",
        "A certified copy of the permanent resident card issued by DNM.",
        "A residency-status certificate from DNM — 3 years of permanent-resident status from the date it was obtained.",
        "A criminal record certificate from Paraguay's police identification authorities.",
        "A criminal record certificate from Paraguay's judicial branch.",
        "A good-conduct certificate from your home country — apostilled.",
        'Documents proving your occupation — these vary by category: employees — a letter from the employer with <a href="{terminologiya}#ips">IPS</a> and <a href="{terminologiya}#ruc">RUC</a> numbers; entrepreneurs — a commercial license and RUC details; students — an enrollment certificate; professionals — qualification documents.',
        "A résumé (curriculum vitae).",
        "A sworn statement, signed in person at the Supreme Court.",
        "A court fee — ₲43,051.",
        "A written naturalization petition, filed with a lawyer's support, stating your permanent address in Asunción.",
    ],
    p_conditions="Additional conditions: the applicant must be of legal age; appearing in person to sign the sworn statement is mandatory; all documents must be originals or certified copies; documents not in Spanish must be translated by a translator registered with the Supreme Court.",
    gap_label="Open question",
    gap='The official page doesn\'t mention a Spanish/Guaraní language exam or a Paraguayan history exam — though in 2019 the Senate approved a bill along these lines, and its current status (passed or not) hasn\'t been established. We look into this individually if it turns out to be relevant by the time you apply.',
    p_confidence='Source: the official Poder Judicial page "Carta de Naturalización" (primary source, government domain). Confidence on the document list — high; on the language exam question — unresolved.',
    p_next='Documents for the previous stage — <a href="{dok-permanente}">permanent residency</a>. If you\'re already at this stage or want to plan the path ahead of time — <a href="{kontakty}">request a consultation</a>.',
),
"de": dict(
    title="Paraguayische Staatsbürgerschaft: Dokumente für die Einbürgerung | Grund Paraguay",
    description="Die offizielle Dokumentenliste der Corte Suprema de Justicia für die Carta de Naturalización — die paraguayische Staatsbürgerschaft — frühestens 3 Jahre nach dem Daueraufenthalt.",
    h1="Staatsbürgerschaft: Dokumente für die Einbürgerung",
    lead="Die Einbürgerung ist frühestens 3 Jahre nach Erhalt des Daueraufenthalts möglich (Art. 148 der Verfassung). Das Verfahren führt nicht die Migrationsbehörde, sondern der Oberste Gerichtshof (Corte Suprema de Justicia) — die folgende Dokumentenliste stammt direkt von der offiziellen Seite des Poder Judicial.",
    source_label="Primärquelle",
    source='Die Dokumentenliste stammt von der offiziellen Poder-Judicial-Seite „Carta de Naturalización", keine Zusammenfassung. Vertrauen: hoch.',
    h2_docs='Dokumente für den Erhalt der <a href="{terminologiya}#carta-naturalizacion">Carta de Naturalización</a>',
    items=[
        "Passfotos — von vorne und im Profil, Format 15×10 cm.",
        'Beglaubigte Kopie des paraguayischen Personalausweises (<a href="{terminologiya}#cedula">Cédula</a>).',
        "Beglaubigte Kopie des Reisepasses — alle Seiten, einschließlich der leeren.",
        "Geburtsurkunde — beglaubigte Kopie, apostilliert.",
        "Beglaubigte Kopie der von der DNM ausgestellten Daueraufenthaltskarte.",
        "Aufenthaltsstatusbescheinigung der DNM — 3 Jahre Daueraufenthaltsstatus ab dem Datum seines Erhalts.",
        "Führungszeugnis der paraguayischen Polizeiidentifikationsbehörden.",
        "Strafregisterauszug der paraguayischen Justizbehörde.",
        "Führungszeugnis aus dem Herkunftsland — apostilliert.",
        'Dokumente zum Nachweis der Tätigkeit — unterscheiden sich nach Kategorie: Angestellte — Schreiben des Arbeitgebers mit <a href="{terminologiya}#ips">IPS</a>- und <a href="{terminologiya}#ruc">RUC</a>-Nummern; Unternehmer — Gewerbepatent und RUC-Angaben; Studierende — Studienbescheinigung; Fachkräfte — Qualifikationsnachweise.',
        "Lebenslauf (curriculum vitae).",
        "Eidesstattliche Erklärung, persönlich vor dem Obersten Gerichtshof unterschrieben.",
        "Gerichtsgebühr — ₲43.051.",
        "Schriftlicher Einbürgerungsantrag mit anwaltlicher Begleitung, unter Angabe der ständigen Adresse in Asunción.",
    ],
    p_conditions="Zusätzliche Bedingungen: Der Antragsteller muss volljährig sein; das persönliche Erscheinen zur Unterzeichnung der eidesstattlichen Erklärung ist Pflicht; alle Dokumente müssen Originale oder beglaubigte Kopien sein; nicht-spanischsprachige Dokumente werden von einem beim Obersten Gerichtshof registrierten Übersetzer übersetzt.",
    gap_label="Offene Frage",
    gap='Die offizielle Seite erwähnt keine Prüfung in Spanisch/Guaraní oder paraguayischer Geschichte — obwohl der Senat 2019 einen entsprechenden Gesetzentwurf gebilligt hat und dessen aktueller Status (verabschiedet/nicht verabschiedet) nicht geklärt werden konnte. Wir klären diese Frage individuell, falls sie zum Zeitpunkt Ihrer Antragstellung relevant sein sollte.',
    p_confidence='Quelle: offizielle Poder-Judicial-Seite „Carta de Naturalización" (Primärquelle, staatliche Domain). Vertrauen bezüglich der Dokumentenliste — hoch; bezüglich der Sprachprüfungsfrage — nicht geklärt.',
    p_next='Dokumente für die vorherige Etappe — <a href="{dok-permanente}">Daueraufenthalt</a>. Falls Sie sich bereits in dieser Etappe befinden oder den Weg im Voraus planen möchten — <a href="{kontakty}">fordern Sie eine Beratung an</a>.',
),
}


def build_grazhdanstvo():
    for lang in LANGS:
        l = L(lang)
        t = GRAZHDANSTVO[lang]
        items_html = "\n      ".join(f"<li>{it.format(**l)}</li>" for it in t["items"])
        body = f'''
{breadcrumbs([(NAV_LABELS[lang]["home"], l['home']), (NAV_LABELS[lang]["dokumenty"], l['dokumenty']), (NAV_LABELS[lang]["dok-grazhdanstvo"], None)])}
<section class="hero" style="padding-top:24px;">
  <div class="wrap">
    <h1>{t["h1"]}</h1>
    <p class="lead">{t["lead"]}</p>
  </div>
</section>
{step_indicator(lang, l, "dok-grazhdanstvo")}
<section style="padding-top:0;">
  <div class="prose">
    <div class="callout"><span class="callout-label">{t["source_label"]}</span>{t["source"]}</div>
    <h2>{t["h2_docs"].format(**l)}</h2>
    <ol>
      {items_html}
    </ol>
    <p>{t["p_conditions"]}</p>
    <div class="callout"><span class="callout-label">{t["gap_label"]}</span>{t["gap"]}</div>
    <p class="confidence-note">{t["p_confidence"]}</p>
    <p>{t["p_next"].format(**l)}</p>
  </div>
</section>
'''
        page("dok-grazhdanstvo", lang, t["title"], t["description"], body,
             extra_schema=schema_breadcrumb([
                 (NAV_LABELS[lang]["home"], f"/{lang}/"),
                 (NAV_LABELS[lang]["dokumenty"], f"/{lang}/{href_to('dokumenty', lang)}"),
                 (NAV_LABELS[lang]["dok-grazhdanstvo"], f"/{lang}/{href_to('dok-grazhdanstvo', lang)}"),
             ]))


build_grazhdanstvo()
