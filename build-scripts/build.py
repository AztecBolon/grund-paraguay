#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Сборка мультиязычного статического сайта Grund Paraguay (ru/es/en/de).
Структура: /assets (общие), /ru/*.html, /es/*.html, /en/*.html, /de/*.html, / (языковой пикер).
"""
import os, re, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # site root, one level above build-scripts/

SITE_NAME = "Grund Paraguay"
DOMAIN = "https://grundparaguay.com"
LANGS = ["ru", "es", "en", "de"]
DEFAULT_LANG = "ru"  # x-default / корневой редирект — первая целевая аудитория проекта

# ---------------------------------------------------------------- icons ----

ICONS = {
"residencia": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="7" width="26" height="18" rx="3"/><circle cx="10.5" cy="14.5" r="2.6"/><path d="M6.5 21c0-2.4 1.9-4 4-4s4 1.6 4 4"/><line x1="18" y1="12" x2="25.5" y2="12"/><line x1="18" y1="16" x2="25.5" y2="16"/><line x1="18" y1="20" x2="23" y2="20"/></svg>',
"compliance": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="3.5" width="20" height="25" rx="2.5"/><path d="M11 11h10M11 16h10M11 21h6"/><path d="M20.5 24.5l2 2 4-4" stroke-width="1.8"/></svg>',
"citizenship": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M16 3.5l3.3 2.1 3.9-.4 1.2 3.7 3.2 2.3-1.6 3.6 1.6 3.6-3.2 2.3-1.2 3.7-3.9-.4L16 27.5l-3.3-2.1-3.9.4-1.2-3.7-3.2-2.3 1.6-3.6-1.6-3.6 3.2-2.3 1.2-3.7 3.9.4z"/><path d="M12 16.3l2.6 2.6L20.5 13"/></svg>',
"investor": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><line x1="4" y1="27" x2="28" y2="27"/><rect x="7" y="17" width="4.5" height="10"/><rect x="14" y="12" width="4.5" height="15"/><rect x="21" y="7" width="4.5" height="20"/><path d="M22 3.5h4.5V8" /><line x1="26.5" y1="3.5" x2="18" y2="12"/></svg>',
"realestate": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 15.5L15 7l10 8.5"/><path d="M7.5 13.5V26h15V13.5"/><rect x="13" y="18" width="6" height="8"/><circle cx="23.5" cy="21.5" r="4.2"/><line x1="26.6" y1="24.6" x2="29.5" y2="27.5"/></svg>',
"company": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="10.5" width="22" height="17" rx="1.5"/><path d="M11 10.5V6.5a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v4"/><line x1="5" y1="17" x2="27" y2="17"/><line x1="16" y1="17" x2="16" y2="27"/></svg>',
"business": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12l6.5-6.5 4 3 6-6L26 8"/><path d="M4 12v3l6.5 3 4-2.3 6 2.3 5.5-3v-3"/><path d="M4 15v9.5a2 2 0 0 0 2 2h20a2 2 0 0 0 2-2V15"/></svg>',
# --- "relocation" — иконка для новой услуги «Релокация организаций» (21.08.2026): силуэт
# здания (тот же стиль двери/линии, что у "company") + стрелка перемещения вверх-вправо
# (тот же приём "линия + наконечник", что у стрелки роста в иконке "investor").
"relocation": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="13" width="14" height="14" rx="1.5"/><line x1="4" y1="19" x2="18" y2="19"/><line x1="11" y1="19" x2="11" y2="27"/><path d="M21 14.5L28.5 7"/><path d="M28.5 12V7h-5"/></svg>',
# --- "medicina" — иконка для услуги «Медицинское сопровождение» (24.08.2026): та же карточка,
# что у "residencia" (это тоже "документ/карта"), но со знаком креста вместо силуэта человека —
# читается как "медицинская карта/полис".
"medicina": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="7" width="26" height="18" rx="3"/><line x1="16" y1="12" x2="16" y2="20"/><line x1="12" y1="16" x2="20" y2="16"/><line x1="7" y1="22.5" x2="12" y2="22.5"/></svg>',
"stamp": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="9.5" r="6"/><path d="M9 9.7l2 2 4-4.2"/><path d="M8 15.2L6.3 21l5.7-2.4 5.7 2.4-1.7-5.8"/></svg>',
"shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l7 3v5.5c0 4.6-3 8.3-7 9.5-4-1.2-7-4.9-7-9.5V6z"/><path d="M9 12l2 2 4-4.3"/></svg>',
# --- Три иконки для ряда "печатей доверия" на Главной (12.08.2026, четвёртая правка) ---
"honest": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5.5h16a1 1 0 0 1 1 1V15a1 1 0 0 1-1 1H9l-4 3.5V16H4a1 1 0 0 1-1-1V6.5a1 1 0 0 1 1-1z"/><path d="M8.5 11.2l2 2 4-4.3"/></svg>',
"contract": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="3" width="12" height="17" rx="1.5"/><line x1="8" y1="7.5" x2="14" y2="7.5"/><line x1="8" y1="11" x2="14" y2="11"/><line x1="8" y1="14.5" x2="11.5" y2="14.5"/><path d="M14.3 15.8l4.7-4.7 2 2-4.7 4.7-2.4.4z"/></svg>',
"split": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M6 3h6l3 3v14l-1.7-1.1-1.8 1.1-1.5-1.1-1.5 1.1-1.8-1.1L6 20V3z"/><line x1="12" y1="3" x2="12" y2="20"/><line x1="8" y1="8" x2="9.5" y2="8"/><line x1="14.5" y1="8" x2="16" y2="6.5"/></svg>',
# --- Четвёртый набор: 4 маленькие иконки для степ-индикатора раздела «Документы»
# (12.08.2026, декор-фаза 2.1) — по одной на каждую из 4 программ (Temporal/Permanente/
# инвестор/гражданство), используются и в степ-индикаторе на страницах программ, и рядом
# с заголовками карточек на хабе «Документы». Тот же стиль: viewBox 24x24, stroke-width
# 1.7, скруглённые концы/стыки — согласовано с уже существующими иконками выше, а не
# новый визуальный язык.
"step-temporal": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="8" width="16" height="11" rx="1.5"/><path d="M9 8V6a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2"/><line x1="4" y1="13" x2="20" y2="13"/><line x1="11" y1="12.3" x2="13" y2="12.3"/></svg>',
"step-permanente": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M4 11.2L12 4l8 7.2"/><path d="M6 9.7V20h12V9.7"/><rect x="10" y="14" width="4" height="6"/></svg>',
"step-investor": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="8.3"/><path d="M14.4 9.4c-.4-.9-1.4-1.4-2.4-1.4-1.4 0-2.6.9-2.6 2s1.1 1.6 2.6 2 2.6.9 2.6 2-1.2 2-2.6 2c-1 0-1.9-.5-2.4-1.4"/><line x1="12" y1="6.7" x2="12" y2="17.3"/></svg>',
"step-citizenship": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><line x1="6" y1="3" x2="6" y2="21"/><path d="M6 4.5h11.5l-3 4 3 4H6"/></svg>',
}

def icon(name, cls="icon"):
    return f'<span class="{cls}">{ICONS[name]}</span>'

import math

def seal_svg(icon_name, top_text, bottom_text, color_cls, aria_label, uid, size=176):
    """Круглая "печать доверия" (12.08.2026, девятая правка Главной — равномерные
    звёзды). Кольцевая надпись идёт по всему периметру зазора между двумя кольцами:
    заголовок сверху, короткое пояснение снизу, левый/правый "бока" зазора заполнены
    декоративными звёздочками — по образцу настоящих печатей, где надписи/орнамент
    идут по всему кольцу. Слова (верх/низ) больше НЕ несут звёзды внутри своего
    textLength-растяжения — раньше пограничные звёзды "★ текст ★" растягивались вместе
    со словом на своей дуге, а бока — отдельной строкой "★ ★ ★" на своей дуге; это
    были два независимых расчёта длины с общей угловой границей, из-за чего звёзды на
    стыках визуально слипались, а середина бокового зазора выглядела пустой. Теперь
    звёзды на боках — отдельные, НЕ связанные с textPath, глифы <text>, расставленные
    вручную по строго равным угловым интервалам (шаг = ширина_зоны / n, звезда в
    центре каждого интервала) — так расстояния между звёздами и от звёзд до соседних
    слов равны по построению, а не по совпадению двух растяжений. Левая зона раньше
    была вдвое уже правой (180–160° = 20° вместо 40°) и оставляла пустой промежуток
    160→200° без единой звезды — исправлено на симметричные 40°-зоны слева и справа,
    как у правой. SVG textPath рисует буквы от опорной линии в сторону, которая
    зависит от НАПРАВЛЕНИЯ ОБХОДА дуги (флаг sweep): у дуг с sweep=1 (верх — обход по
    часовой стрелке) буквы растут НАРУЖУ (к внешнему кольцу), у дуг с sweep=0 (низ —
    обход против часовой) — ВНУТРЬ (к внутреннему кольцу и иконке), поэтому опорная
    линия слов смещена по-разному для двух групп дуг. Отдельные звёзды-глифы этой
    асимметрии не подвержены (dominant-baseline="central" центрирует их вертикально
    независимо от позиции на круге), поэтому сидят строго на середине зазора между
    кольцами. Иконка — крупная, занимает почти всю внутреннюю площадь. Слова
    растягиваются/сжимаются под фиксированную длину дуги через textLength +
    lengthAdjust="spacingAndGlyphs" — не нужно вручную подбирать размер круга под
    каждый язык. Полный смысл (с источником) — в aria-label."""
    cx = cy = size / 2
    r_outer = size / 2 - 4
    r_inner = size / 2 - 20
    gap = r_outer - r_inner
    r_text_out = r_inner + gap * 0.34  # sweep=1: буквы растут наружу — линия ближе к внутреннему кольцу
    r_text_in = r_outer - gap * 0.34   # sweep=0: буквы растут внутрь — линия ближе к внешнему кольцу
    r_star = (r_inner + r_outer) / 2   # отдельные звёзды центрируются сами — берём середину зазора
    icon_r = r_inner * 0.68
    def pt(angle_deg, radius):
        a = math.radians(angle_deg)
        return cx + radius * math.cos(a), cy + radius * math.sin(a)
    def arc_text(start_a, end_a, content, seg_id, sweep=1):
        r_t = r_text_out if sweep == 1 else r_text_in
        x1, y1 = pt(start_a, r_t)
        x2, y2 = pt(end_a, r_t)
        arc_len = r_t * math.radians(abs(end_a - start_a))
        path_id = f"seal-arc-{uid}-{seg_id}"
        return (
            f'<path id="{path_id}" d="M {x1:.1f} {y1:.1f} A {r_t:.1f} {r_t:.1f} 0 0 {sweep} {x2:.1f} {y2:.1f}" fill="none"/>'
            f'<text class="seal-ring-text"><textPath href="#{path_id}" textLength="{arc_len:.0f}" '
            f'lengthAdjust="spacingAndGlyphs" startOffset="0">{content}</textPath></text>'
        )
    def stars(center_a, zone_w, n):
        # n звёзд строго по центрам n равных угловых долек зоны — расстояния между
        # звёздами и до края зоны равны по построению (край = половина шага).
        seg = zone_w / n
        out = []
        for i in range(n):
            a = center_a - zone_w / 2 + seg * (i + 0.5)
            x, y = pt(a, r_star)
            out.append(f'<text class="seal-ring-star" x="{x:.1f}" y="{y:.1f}" text-anchor="middle" dominant-baseline="central">★</text>')
        return "".join(out)
    # Верх (270°=12 часов, sweep=1) и низ (90°=6 часов, sweep=0) — слова по 140°;
    # правый (0°=3 часа) и левый (180°=9 часов) "бока" — по 40°, симметрично, только
    # равномерно расставленные звёзды, без пустых промежутков и без слипания на стыках.
    top = arc_text(200, 340, top_text, "top")
    bottom = arc_text(160, 20, bottom_text, "bot", sweep=0)
    right_stars = stars(0, 40, 3)
    left_stars = stars(180, 40, 3)
    icon_x, icon_y = cx - icon_r, cy - icon_r
    return (
        f'<svg class="seal-emblem {color_cls}" viewBox="0 0 {size} {size}" role="img" aria-label="{aria_label}">'
        f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r_outer:.1f}" fill="none" stroke="currentColor" stroke-width="1.4"/>'
        f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r_inner:.1f}" fill="none" stroke="currentColor" stroke-width="1"/>'
        f'{top}{right_stars}{bottom}{left_stars}'
        f'<svg x="{icon_x:.1f}" y="{icon_y:.1f}" width="{icon_r*2:.1f}" height="{icon_r*2:.1f}">{ICONS[icon_name]}</svg>'
        f'</svg>'
    )

# --------------------------------------------------------- page registry ---
# page_id -> {lang: slug}. 'home' всегда index.html во всех языках.

SLUGS = {
    "home":               {"ru": "index.html",                    "es": "index.html",                      "en": "index.html",                "de": "index.html"},
    "uslugi":             {"ru": "uslugi.html",                    "es": "servicios.html",                  "en": "services.html",              "de": "dienstleistungen.html"},
    "protsess":           {"ru": "protsess-i-sroki.html",          "es": "proceso-y-plazos.html",            "en": "process-and-timeline.html",  "de": "prozess-und-fristen.html"},
    "riski":              {"ru": "riski.html",                     "es": "riesgos.html",                     "en": "risks.html",                 "de": "risiken.html"},
    "stoimost":           {"ru": "stoimost.html",                  "es": "costos.html",                      "en": "pricing.html",               "de": "preise.html"},
    "o-kompanii":         {"ru": "o-kompanii.html",                "es": "sobre-nosotros.html",               "en": "about-us.html",              "de": "ueber-uns.html"},
    "konfidentsialnost":  {"ru": "konfidentsialnost.html",         "es": "confidencialidad-cliente.html",     "en": "client-confidentiality.html","de": "vertraulichkeit-mandant.html"},
    "keisy":              {"ru": "keisy.html",                     "es": "casos.html",                        "en": "case-studies.html",          "de": "fallstudien.html"},
    "kontakty":           {"ru": "kontakty.html",                  "es": "contacto.html",                     "en": "contact.html",               "de": "kontakt.html"},
    "terminologiya":      {"ru": "terminologiya.html",             "es": "terminologia.html",                 "en": "terminology.html",           "de": "terminologie.html"},
    "oferta":             {"ru": "oferta.html",                    "es": "oferta.html",                       "en": "public-offer.html",          "de": "oeffentliches-angebot.html"},
    "politika":           {"ru": "politika-konfidentsialnosti.html","es": "politica-privacidad-sitio.html",   "en": "site-privacy-policy.html",   "de": "datenschutzerklaerung.html"},

    # --- Хаб «Парагвай для переезда» (11.08.2026, RU-only на старте; 11.08.2026 вечер —
    # переведён на ES/EN/DE по решению заказчика). Слаги на ES/EN/DE подобраны по аналогии с
    # уже переведёнными 12 страницами (короткие, по-язычно осмысленные, без диакритики в URL).
    # helper-функции в этом файле (slug/href_to/header/page) по-прежнему рассчитаны на страницы
    # без части языков — это больше не нужно для хаба, но осталось общим механизмом на будущее.
    "paragvay-hub":       {"ru": "paragvay-dlya-pereezda.html",     "es": "mudarse-a-paraguay.html",         "en": "paraguay-for-relocation.html", "de": "paraguay-fuer-auswanderer.html"},
    "pochemu-paragvay":   {"ru": "pochemu-paragvay.html",           "es": "por-que-paraguay.html",           "en": "why-paraguay.html",            "de": "warum-paraguay.html"},
    "zhizn-v-paragvae":   {"ru": "zhizn-v-paragvae.html",           "es": "vida-en-paraguay.html",           "en": "life-in-paraguay.html",         "de": "leben-in-paraguay.html"},
    "stoimost-zhizni":    {"ru": "stoimost-zhizni.html",            "es": "costo-de-vida.html",              "en": "cost-of-living.html",           "de": "lebenshaltungskosten.html"},
    "nalogi-inostrantsev":{"ru": "nalogi-dlya-inostrantsev.html",   "es": "impuestos-para-extranjeros.html", "en": "taxes-for-foreigners.html",     "de": "steuern-fuer-auslaender.html"},
    "banki-perevody":     {"ru": "banki-i-perevody.html",           "es": "bancos-y-transferencias.html",    "en": "banking-and-money-transfers.html","de": "banken-und-geldtransfers.html"},
    "viza-vyezd":         {"ru": "viza-i-vyezd.html",               "es": "visa-y-entrada.html",             "en": "visa-and-entry.html",           "de": "visum-und-einreise.html"},
    "mify-voprosy":       {"ru": "mify-i-voprosy.html",             "es": "mitos-y-preguntas.html",          "en": "myths-and-questions.html",      "de": "mythen-und-fragen.html"},

    # --- «Как мы работаем» (11.08.2026, вторая правка) — новая посадочная страница, объединяющая
    # в меню два уже существующих раздела (Процесс и сроки + Риски) под одним пунктом; сами
    # страницы "protsess"/"riski" остаются на своих местах, меняется только навигация к ним.
    "kak-my-rabotaem":    {"ru": "kak-my-rabotaem.html", "es": "como-trabajamos.html", "en": "how-we-work.html", "de": "wie-wir-arbeiten.html"},

    # --- Раздел «Документы» (12.08.2026, старт RU-only; 12.08.2026 вечер — переведён на ES/EN/DE
    # по запросу заказчика «делай мультиязычность по документам») — чек-листы документов по каждой
    # программе миграции: посадочная страница-хаб + 4 страницы с деталями по программам. Источник
    # фактуры — design/dokumenty-po-programmam-migratsii.md (проект Cowork). Живёт в выпадающем
    # меню "Документы" (см. FOOTER_LEGAL_ORDER ниже) рядом с уже существующими Конфиденциальностью/
    # Терминологией/Офертой/Политикой; хаб добавлен в FOOTER_LEGAL_ORDER, 4 страницы программ
    # доступны через ссылки с хаба. Слаги на ES/EN/DE подобраны по аналогии с уже переведёнными
    # разделами — короткие, по-язычно осмысленные, без диакритики в URL.
    "dokumenty":          {"ru": "dokumenty-po-programmam.html",         "es": "documentos-por-programa.html",         "en": "documents-by-program.html",           "de": "dokumente-nach-programm.html"},
    "dok-temporal":       {"ru": "dokumenty-vremennaya-rezidentura.html","es": "documentos-residencia-temporal.html",  "en": "documents-temporary-residency.html",  "de": "dokumente-befristeter-aufenthalt.html"},
    "dok-permanente":     {"ru": "dokumenty-postoyannaya-rezidentura.html","es": "documentos-residencia-permanente.html","en": "documents-permanent-residency.html", "de": "dokumente-daueraufenthalt.html"},
    "dok-investor":       {"ru": "dokumenty-investorskiy-put.html",     "es": "documentos-via-inversionista.html",    "en": "documents-investor-path.html",        "de": "dokumente-investorenweg.html"},
    "dok-grazhdanstvo":   {"ru": "dokumenty-grazhdanstvo.html",         "es": "documentos-naturalizacion.html",       "en": "documents-citizenship.html",          "de": "dokumente-einbuergerung.html"},

    # --- Развёрнутые страницы услуг (19.08.2026, старт RU-only, пилот на 2 из 7 услуг —
    # «Резидентура» и «Инвесторский путь») — по запросу заказчика карточки на «Услугах» станут
    # анонсами, а полный текст переезжает на отдельные посадочные страницы, по образцу уже
    # обкатанного паттерна хаба «Парагвай для переезда» (сначала RU, перевод на ES/EN/DE —
    # отдельным шагом, когда подход утверждён на пилоте). ES/EN/DE-слаги сознательно не заведены
    # заранее — до перевода страниц это были бы битые ссылки; href_to()/header() уже умеют
    # пропускать язык, если слага нет (см. slug() выше).
    "usluga-residencia":  {"ru": "rezidentura.html"},
    "usluga-investor":    {"ru": "investorskiy-put.html"},

    # --- Оставшиеся 5 услуг из 9 (27.08.2026, по запросу заказчика «у нас должны быть страницы
    # по всем услугам со страницы /uslugi.html?» → «Все 5 сразу, сразу на 4 языках») — полные
    # страницы + короткие анонсы на «Услугах», сразу мультиязычные (в отличие от пилота
    # «Резидентура»/«Инвесторский путь», которые остались RU-only). Источник фактуры — уже
    # опубликованные карточки «Услуг», design/plan-razvernutye-stranitsy-uslug.md (структура и
    # идеи иллюстраций по каждой) и design/proverka-nalogov-avg2026.md (Impuesto Inmobiliario —
    # для «Недвижимости»).
    "usluga-compliance":  {"ru": "soprovozhdenie-i-komplaens.html", "es": "acompanamiento-y-cumplimiento.html",
                            "en": "ongoing-compliance.html", "de": "begleitung-und-compliance.html"},
    "usluga-citizenship": {"ru": "grazhdanstvo-paragvaya.html", "es": "ciudadania-paraguaya.html",
                            "en": "paraguayan-citizenship.html", "de": "paraguayische-staatsbuergerschaft.html"},
    "usluga-realestate":  {"ru": "nedvizhimost-proverka-i-pokupka.html", "es": "verificacion-y-compra-de-inmuebles.html",
                            "en": "real-estate-verification-purchase.html", "de": "immobilien-pruefung-und-kauf.html"},
    "usluga-company":     {"ru": "otkrytie-kompanii.html", "es": "apertura-de-empresa.html",
                            "en": "company-formation.html", "de": "unternehmensgruendung.html"},
    "usluga-business":    {"ru": "pokupka-i-prodazha-biznesa.html", "es": "compra-y-venta-de-empresas.html",
                            "en": "buying-selling-a-business.html", "de": "kauf-und-verkauf-von-unternehmen.html"},

    # --- «Медицинское сопровождение» — девятая услуга (24.08.2026, старт RU-only; 27.08.2026 —
    # переведена на ES/EN/DE по запросу заказчика «Делай мультиязычность и правь карту сайта»).
    # Источник фактуры — design/meditsina-strakhovanie-issledovanie.md (проект Cowork). Тот же
    # паттерн, что и «Резидентура»/«Инвесторский путь»/«Релокация организаций»: полная страница +
    # короткий анонс на «Услугах».
    "usluga-medicina":    {"ru": "meditsinskoe-soprovozhdenie.html", "es": "asistencia-medica.html",
                            "en": "medical-support.html", "de": "medizinische-begleitung.html"},

    # --- «Медицина в Парагвае» — подстраница хаба «Парагвай для переезда» (24.08.2026, старт
    # RU-only; 27.08.2026 — переведена на ES/EN/DE, тем же запросом, что и usluga-medicina выше).
    # Источник фактуры — тот же design-документ.
    "meditsina-v-paragvae": {"ru": "meditsina-v-paragvae.html", "es": "medicina-en-paraguay.html",
                              "en": "healthcare-in-paraguay.html", "de": "medizin-in-paraguay.html"},

    # --- «Работа в Парагвае» — новая подстраница хаба «Парагвай для переезда» (28.08.2026, по
    # запросу заказчика «Сделай страницу Работа в Парагвае» — сразу мультиязычная, тем же
    # порядком, что и последние добавления в разделе). Источник фактуры — веб-поиск в этой сессии
    # Cowork (резидентура как единственное основание для права на работу, 10 требований для
    # cédula, обязанность RUC уже подтверждена в проекте ранее, IPS 25,5% и Código del Trabajo
    # Ley 213/93) — см. design/rabota-v-paragvae-issledovanie.md (проект Cowork).
    "rabota-v-paragvae":   {"ru": "rabota-v-paragvae.html", "es": "trabajo-en-paraguay.html",
                             "en": "working-in-paraguay.html", "de": "arbeiten-in-paraguay.html"},

    # --- «Карта Парагвая» — новая подстраница хаба «Парагвай для переезда» (15.10.2026, правки
    # партнёра на месте, октябрь 2026; design/promt-vnedrenie-izmeneniy-sayt-okt2026.md, раздел
    # «Новый раздел — Karte von Paraguay»). Содержательная страница со схемой — не то же самое,
    # что связка с map.grundparaguay.com в map_link.py (там MAP_LIVE = False).
    "karta-paragvaya":     {"ru": "karta-paragvaya.html", "es": "mapa-de-paraguay.html",
                             "en": "map-of-paraguay.html", "de": "karte-von-paraguay.html"},

    # --- «Релокация организаций» — восьмая услуга (21.08.2026, старт RU-only; 21.08.2026 —
    # переведена на ES/EN/DE по запросу заказчика «Делай релокацию и достопримечательности
    # мультиязычными»). Источник фактуры — design/relokatsiya-organizatsiy-issledovanie.md
    # (проект Cowork): режим Maquila (Ley N° 1064/97, REDIEX/MIC) как ключевое УТП, уже известные
    # факты о регистрации компании (EAS/S.A./S.R.L.), отсутствие отдельной корпоративной/
    # цифровой-номадской визы (команда переезжает через N параллельных дел по уже существующей
    # услуге «Резидентура»). Пакетная услуга: полная страница + короткий анонс на «Услугах»
    # (8-я карточка), тот же паттерн пилота, что и «Резидентура»/«Инвесторский путь» выше.
    "usluga-relocation":  {"ru": "relokatsiya-organizatsiy.html", "es": "relocalizacion-de-empresas.html",
                            "en": "business-relocation.html", "de": "unternehmensrelokation.html"},

    # --- «Туризм» — новая подстраница хаба «Парагвай для переезда» (21.08.2026, старт RU-only;
    # 21.08.2026 — переведена на ES/EN/DE, тем же запросом, что и «Релокация организаций» выше).
    # 20 отдельных страниц-достопримечательностей + сама страница-анонс "turizm" — источник
    # фактуры design/dostoprimechatelnosti-paragvaya.md. См. pages_turizm.py.
    "turizm":                 {"ru": "turizm.html", "es": "turismo.html", "en": "tourism.html", "de": "tourismus.html"},
    "attr-palacio-lopez":     {"ru": "dvorets-lopesa.html", "es": "palacio-de-lopez.html", "en": "palacio-lopez.html", "de": "palacio-lopez.html"},
    "attr-panteon-geroev":    {"ru": "panteon-geroev.html", "es": "panteon-de-los-heroes.html", "en": "pantheon-of-heroes.html", "de": "heldenpantheon.html"},
    "attr-sobor-asunsiona":   {"ru": "sobor-asunsiona.html", "es": "catedral-de-asuncion.html", "en": "asuncion-cathedral.html", "de": "kathedrale-von-asuncion.html"},
    "attr-kostanera-asunsiona": {"ru": "kostanera-asunsiona.html", "es": "costanera-de-asuncion.html", "en": "asuncion-riverside.html", "de": "costanera-von-asuncion.html"},
    "attr-san-heronimo":      {"ru": "raion-san-heronimo.html", "es": "barrio-san-jeronimo.html", "en": "san-jeronimo-neighborhood.html", "de": "viertel-san-jeronimo.html"},
    "attr-botanicheskiy-sad": {"ru": "botanicheskiy-sad-asunsiona.html", "es": "jardin-botanico-de-asuncion.html", "en": "asuncion-botanical-garden.html", "de": "botanischer-garten-asuncion.html"},
    "attr-dom-nezavisimosti": {"ru": "dom-nezavisimosti.html", "es": "casa-de-la-independencia.html", "en": "independence-house.html", "de": "haus-der-unabhaengigkeit.html"},
    "attr-muzey-del-barro":   {"ru": "muzey-del-barro.html", "es": "museo-del-barro.html", "en": "museo-del-barro.html", "de": "museo-del-barro.html"},
    "attr-merkado-4":         {"ru": "merkado-4.html", "es": "mercado-4.html", "en": "mercado-4.html", "de": "mercado-4.html"},
    "attr-aldea-maka":        {"ru": "derevnya-maka.html", "es": "aldea-maka.html", "en": "maka-village.html", "de": "maka-dorf.html"},
    "attr-iezuitskie-missii": {"ru": "iezuitskie-missii.html", "es": "misiones-jesuiticas.html", "en": "jesuit-missions.html", "de": "jesuitenmissionen.html"},
    "attr-itaipu":            {"ru": "itaipu.html", "es": "represa-de-itaipu.html", "en": "itaipu-dam.html", "de": "itaipu-staudamm.html"},
    "attr-siudad-del-este":   {"ru": "siudad-del-este.html", "es": "ciudad-del-este.html", "en": "ciudad-del-este.html", "de": "ciudad-del-este.html"},
    "attr-saltos-del-monday": {"ru": "saltos-del-monday.html", "es": "saltos-del-monday.html", "en": "saltos-del-monday-falls.html", "de": "saltos-del-monday-wasserfaelle.html"},
    "attr-kostanera-enkarnasiona": {"ru": "kostanera-enkarnasiona.html", "es": "costanera-de-encarnacion.html", "en": "encarnacion-riverside.html", "de": "costanera-von-encarnacion.html"},
    "attr-kaakupe":           {"ru": "bazilika-kaakupe.html", "es": "basilica-de-caacupe.html", "en": "caacupe-basilica.html", "de": "basilika-von-caacupe.html"},
    "attr-cerro-cora":        {"ru": "park-serro-kora.html", "es": "parque-nacional-cerro-cora.html", "en": "cerro-cora-national-park.html", "de": "nationalpark-cerro-cora.html"},
    "attr-ibikui":            {"ru": "park-ibikui.html", "es": "parque-nacional-ybycui.html", "en": "ybycui-national-park.html", "de": "nationalpark-ybycui.html"},
    "attr-san-bernardino":    {"ru": "san-bernardino-i-ozero-ipakarai.html", "es": "san-bernardino-lago-ypacarai.html", "en": "san-bernardino-lake-ypacarai.html", "de": "san-bernardino-see-ypacarai.html"},
    "attr-filadelfia":        {"ru": "filadelfia-i-chako.html", "es": "filadelfia-y-colonias-menonitas.html", "en": "filadelfia-mennonite-colonies.html", "de": "filadelfia-mennonitenkolonien.html"},

    # --- Карта сайта (13.08.2026) — служебная страница со списком всех разделов и ссылками,
    # см. pages_sitemap.py. Добавлена в FOOTER_LEGAL_ORDER ниже — попадает и в дропдаун
    # "Документы ▾" служебной строки (header-utility), и в колонку "Документы" в футере,
    # тем же механизмом, что и остальные пункты этого списка.
    "sitemap":            {"ru": "karta-sayta.html", "es": "mapa-del-sitio.html", "en": "sitemap.html", "de": "seitenuebersicht.html"},
}

# 11.08.2026 (вторая правка): перегруппировка меню по запросу заказчика —
# - "kontakty" убран из главного меню: кнопка «Заявка на консультацию» и контакты в служебной
#   строке хедера уже ведут туда же, отдельный пункт дублировал их (страница и её слаг никуда не
#   делись, просто больше не входят в NAV_ORDER — доступна по прямой ссылке и через CTA/подвал);
# - "protsess" и "riski" как отдельные пункты меню заменены одним пунктом "kak-my-rabotaem"
#   (соответствует смысловой группировке из struktura-saita.md §3.4 «Как мы работаем»);
# - "paragvay-hub" добавлен в меню под своим названием «Парагвай для переезда» (RU-only, см.
#   комментарий выше);
# - "o-kompanii" сознательно оставлен в главном меню, а не перенесён в служебную строку — по
#   struktura-saita.md (§0) доверие/команда/юрлицо — ключевой элемент позиционирования на
#   репутационно токсичном рынке, прятать это в служебную строку заказчик решил не стал.
NAV_ORDER = ["home", "uslugi", "kak-my-rabotaem", "stoimost", "paragvay-hub", "o-kompanii", "keisy"]
# 12.08.2026 — "dokumenty" (хаб раздела «Документы по программам») добавлен вторым пунктом,
# сразу после Конфиденциальности, теперь на всех 4 языках; сами 4 страницы программ в этот список
# не входят — доступны через ссылки с хаба, см. комментарий у SLUGS выше.
FOOTER_LEGAL_ORDER = ["konfidentsialnost", "dokumenty", "terminologiya", "oferta", "politika", "sitemap"]

NAV_LABELS = {
    "ru": {"home": "Главная", "uslugi": "Услуги", "protsess": "Процесс и сроки", "riski": "Риски",
           "stoimost": "Стоимость", "o-kompanii": "О компании", "keisy": "Кейсы", "kontakty": "Контакты",
           "konfidentsialnost": "Конфиденциальность (соглашение с клиентом)", "terminologiya": "Терминология и курс валюты",
           "oferta": "Публичная оферта", "politika": "Политика конфиденциальности сайта",
           "kak-my-rabotaem": "Как мы работаем", "paragvay-hub": "Парагвай для переезда",
           "dokumenty": "Документы по программам", "dok-temporal": "Временная резидентура — документы",
           "dok-permanente": "Постоянная резидентура — документы", "dok-investor": "Инвесторский путь — документы",
           "dok-grazhdanstvo": "Гражданство — документы", "sitemap": "Карта сайта"},
    "es": {"home": "Inicio", "uslugi": "Servicios", "protsess": "Proceso y plazos", "riski": "Riesgos",
           "stoimost": "Costos", "o-kompanii": "Sobre nosotros", "keisy": "Casos", "kontakty": "Contacto",
           "konfidentsialnost": "Confidencialidad (acuerdo con el cliente)", "terminologiya": "Terminología y tipo de cambio",
           "oferta": "Oferta pública", "politika": "Política de privacidad del sitio",
           "kak-my-rabotaem": "Cómo trabajamos", "paragvay-hub": "Paraguay para mudarse",
           "dokumenty": "Documentos por programa", "dok-temporal": "Residencia temporal — documentos",
           "dok-permanente": "Residencia permanente — documentos", "dok-investor": "Vía de inversor — documentos",
           "dok-grazhdanstvo": "Ciudadanía — documentos", "sitemap": "Mapa del sitio"},
    "en": {"home": "Home", "uslugi": "Services", "protsess": "Process & Timeline", "riski": "Risks",
           "stoimost": "Pricing", "o-kompanii": "About Us", "keisy": "Case Studies", "kontakty": "Contact",
           "konfidentsialnost": "Confidentiality (client agreement)", "terminologiya": "Terminology & exchange rate",
           "oferta": "Public offer", "politika": "Site privacy policy",
           "kak-my-rabotaem": "How We Work", "paragvay-hub": "Paraguay for Relocation",
           "dokumenty": "Documents by Program", "dok-temporal": "Temporary Residency — Documents",
           "dok-permanente": "Permanent Residency — Documents", "dok-investor": "Investor Path — Documents",
           "dok-grazhdanstvo": "Citizenship — Documents", "sitemap": "Sitemap"},
    "de": {"home": "Startseite", "uslugi": "Leistungen", "protsess": "Prozess und Fristen", "riski": "Risiken",
           "stoimost": "Preise", "o-kompanii": "Über uns", "keisy": "Fallstudien", "kontakty": "Kontakt",
           "konfidentsialnost": "Vertraulichkeit (Mandantenvereinbarung)", "terminologiya": "Terminologie & Wechselkurs",
           "oferta": "Öffentliches Angebot", "politika": "Datenschutzerklärung der Website",
           "kak-my-rabotaem": "Wie wir arbeiten", "paragvay-hub": "Paraguay für Auswanderer",
           "dokumenty": "Dokumente nach Programm", "dok-temporal": "Befristeter Aufenthalt — Dokumente",
           "dok-permanente": "Daueraufenthalt — Dokumente", "dok-investor": "Investorenweg — Dokumente",
           "dok-grazhdanstvo": "Staatsbürgerschaft — Dokumente", "sitemap": "Seitenübersicht"},
}

LANG_LABEL = {"ru": "RU", "es": "ES", "en": "EN", "de": "DE"}
CTA_LABEL = {"ru": "Заявка на консультацию", "es": "Solicitar consulta", "en": "Request a consultation", "de": "Beratung anfragen"}
SKIP_LABEL = {"ru": "Перейти к содержанию", "es": "Ir al contenido", "en": "Skip to content", "de": "Zum Inhalt springen"}
MENU_LABEL = {"ru": "Меню", "es": "Menú", "en": "Menu", "de": "Menü"}
DOCS_LABEL = {"ru": "Документы", "es": "Documentos", "en": "Documents", "de": "Dokumente"}

# контактные данные — язык-независимые, используются и в служебной строке хедера, и в подвале
# (12.08.2026 — реальные реквизиты от заказчика: название, адрес, телефон, email. Telegram
# заказчик не присылал — @grundparaguay остаётся тем же плейсхолдером, что был; см. пометку
# ниже в FOOTER_DRAFT_NOTE, которая теперь сужена именно до этого пункта, а не до всех контактов).
CONTACT_PHONE = "+595 98 39 555 04"
CONTACT_TELEGRAM_HANDLE = "@grundparaguay"
CONTACT_TELEGRAM_URL = "https://t.me/grundparaguay"
CONTACT_EMAIL = "office@fortuna-vida.com.py"
CONTACT_LEGAL_NAME = "Fortuna Vida E.A.S."
CONTACT_ADDRESS = "ETAPA 9009 San Isidro, 6000 Encarnación, Paraguay"

FOOTER_DISCLAIMER = {
    "ru": 'Сопровождаем переезд, резидентуру и бизнес в Парагвае по письменной договорённости с фиксированной ценой. Мы не обещаем гражданство «за год» — срок по нашему опыту и то, откуда он берётся, — на странице <a href="{protsess}">«Процесс и сроки»</a>.',
    "es": 'Acompañamos la mudanza, la residencia y los negocios en Paraguay con un acuerdo por escrito de precio fijo. No prometemos la ciudadanía «en un año» — el plazo según nuestra experiencia y de dónde sale, en la página <a href="{protsess}">«Proceso y plazos»</a>.',
    "en": 'We support relocation, residency and business in Paraguay under a written fixed-price agreement. We don\'t promise citizenship "in a year" — the timeline from our experience, and where it comes from, is on the <a href="{protsess}">"Process & Timeline"</a> page.',
    "de": 'Wir begleiten den Umzug, die Aufenthaltsgenehmigung und das Geschäft in Paraguay auf Basis einer schriftlichen Vereinbarung mit Festpreis. Wir versprechen keine Staatsbürgerschaft „in einem Jahr" — die Frist nach unserer Erfahrung und woher sie stammt, steht auf der Seite <a href="{protsess}">„Prozess und Fristen"</a>.',
}
FOOTER_SECTIONS_LABEL = {"ru": "Разделы", "es": "Secciones", "en": "Sections", "de": "Bereiche"}
FOOTER_DOCS_LABEL = {"ru": "Документы", "es": "Documentos", "en": "Documents", "de": "Dokumente"}
FOOTER_CONTACT_LABEL = {"ru": "Связь", "es": "Contacto", "en": "Get in touch", "de": "Kontakt"}
FOOTER_HOURS = {"ru": "Будни, 9:00–18:00 (PYT)", "es": "Días hábiles, 9:00–18:00 (PYT)", "en": "Weekdays, 9:00 AM–6:00 PM (PYT)", "de": "Werktags, 9:00–18:00 Uhr (PYT)"}
FOOTER_COPY = {"ru": f"© 2026 {CONTACT_LEGAL_NAME}", "es": f"© 2026 {CONTACT_LEGAL_NAME}", "en": f"© 2026 {CONTACT_LEGAL_NAME}", "de": f"© 2026 {CONTACT_LEGAL_NAME}"}
# 12.08.2026 — было общей пометкой «юр. название и контакты пока заглушка»; название, адрес,
# телефон и email теперь реальные (реквизиты от заказчика), сужено до Telegram и рег. номера —
# единственных двух пунктов, которые пока не подтверждены.
FOOTER_DRAFT_NOTE = {
    "ru": "Тестовая (черновая) версия сайта — Telegram и регистрационный номер компании пока не подтверждены, см. внутренний чек-лист",
    "es": "Versión de prueba (borrador) del sitio — el Telegram y el número de registro de la empresa aún no están confirmados, ver la lista de verificación interna",
    "en": "Draft/test version of the site — the Telegram handle and the company's registration number aren't confirmed yet, see internal checklist",
    "de": "Test-/Entwurfsversion der Website — Telegram-Handle und Handelsregisternummer sind noch nicht bestätigt, siehe interne Checkliste",
}

def slug(page_id, lang):
    """Возвращает slug страницы на языке lang, либо None, если страница на этом языке не
    существует (используется для RU-only разделов вроде хаба «Парагвай для переезда»)."""
    return SLUGS[page_id].get(lang)

def href_to(page_id, lang, from_lang=None):
    """Ссылка на page_id на языке lang. Если from_lang задан и отличается — относительный путь через уровень выше.
    Возвращает None, если у page_id нет версии на языке lang (RU-only страницы) — вызывающий код
    должен это учитывать (см. header()/page() ниже)."""
    s = slug(page_id, lang)
    if s is None:
        return None
    if from_lang is None or from_lang == lang:
        return s
    return f"../{lang}/{s}"

def header(lang, active_id):
    links = []
    for pid in NAV_ORDER:
        target = href_to(pid, lang)
        if target is None:
            continue  # у пункта меню нет версии на этом языке (RU-only раздел) — не показываем битую ссылку
        cur = ' aria-current="page"' if pid == active_id else ''
        links.append(f'<a href="{target}"{cur}>{NAV_LABELS[lang][pid]}</a>')
    nav_html = "\n      ".join(links)
    lang_links = []
    for l in LANGS:
        target = href_to(active_id, l, from_lang=lang)
        if target is None:
            continue  # у страницы нет версии на этом языке (RU-only раздел) — не показываем битую ссылку
        cur_cls = ' class="lang-current"' if l == lang else ''
        lang_links.append(f'<a href="{target}"{cur_cls}>{LANG_LABEL[l]}</a>')
    lang_switch = "".join(lang_links)
    docs_links_list = []
    for pid in FOOTER_LEGAL_ORDER:
        target = href_to(pid, lang)
        if target is None:
            continue  # у пункта нет версии на этом языке (RU-only раздел «Документы») — не показываем битую ссылку
        docs_links_list.append(f'<a href="{target}">{NAV_LABELS[lang][pid]}</a>')
    docs_links = "\n          ".join(docs_links_list)
    return f'''<a class="skip-link" href="#main">{SKIP_LABEL[lang]}</a>
<div class="header-utility">
  <div class="wrap">
    <div class="utility-contact">
      <a href="tel:{CONTACT_PHONE.replace(" ", "")}">{CONTACT_PHONE}</a>
      <a href="{CONTACT_TELEGRAM_URL}">{CONTACT_TELEGRAM_HANDLE}</a>
      <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>
    </div>
    <div class="utility-right">
      <details class="docs-dropdown">
        <summary>{DOCS_LABEL[lang]}</summary>
        <div class="docs-menu">
          {docs_links}
        </div>
      </details>
      <div class="lang-switch lang-switch--dark" aria-label="Language">{lang_switch}</div>
      <a class="btn btn-utility" href="{href_to('kontakty', lang)}">{CTA_LABEL[lang]}</a>
    </div>
  </div>
</div>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{href_to('home', lang)}">
      <img src="../assets/img/mark.png" alt="Grund Paraguay" width="80" height="80">
      <span class="brand-word"><b>GRUND</b><span>PARAGUAY</span></span>
    </a>
    <button class="nav-toggle" aria-label="{MENU_LABEL[lang]}" aria-expanded="false" onclick="var n=document.getElementById('mainnav');var open=n.classList.toggle('open');this.setAttribute('aria-expanded',open);">☰</button>
    <nav class="main-nav" id="mainnav">
      {nav_html}
    </nav>
  </div>
</header>'''

def footer(lang):
    main_items = "\n        ".join(
        f'<li><a href="{href_to(pid, lang)}">{NAV_LABELS[lang][pid]}</a></li>'
        for pid in NAV_ORDER if href_to(pid, lang) is not None
    )
    legal_items_list = []
    for pid in FOOTER_LEGAL_ORDER:
        target = href_to(pid, lang)
        if target is None:
            continue  # у пункта нет версии на этом языке (RU-only раздел «Документы») — не показываем битую ссылку
        legal_items_list.append(f'<li><a href="{target}">{NAV_LABELS[lang][pid]}</a></li>')
    legal_items = "\n        ".join(legal_items_list)
    disclaimer = FOOTER_DISCLAIMER[lang].format(protsess=href_to("protsess", lang))
    return f'''<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <span class="brand-word"><b>GRUND</b><span>PARAGUAY</span></span>
        <p class="disclaimer">{disclaimer}</p>
      </div>
      <div>
        <h4>{FOOTER_SECTIONS_LABEL[lang]}</h4>
        <ul>
        {main_items}
        </ul>
      </div>
      <div>
        <h4>{FOOTER_DOCS_LABEL[lang]}</h4>
        <ul>
        {legal_items}
        </ul>
      </div>
      <div>
        <h4>{FOOTER_CONTACT_LABEL[lang]}</h4>
        <ul>
          <li><a href="{CONTACT_TELEGRAM_URL}">Telegram: {CONTACT_TELEGRAM_HANDLE}</a></li>
          <li><a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></li>
          <li>{CONTACT_PHONE}</li>
          <li>{FOOTER_HOURS[lang]}</li>
          <li>{CONTACT_ADDRESS}</li>
        </ul>
      </div>
    </div>
    <div class="foot-bottom">
      <span>{FOOTER_COPY[lang]}</span>
      <span>{FOOTER_DRAFT_NOTE[lang]}</span>
    </div>
  </div>
</footer>
<script>
document.addEventListener('DOMContentLoaded', function () {{
  document.querySelectorAll('nav.main-nav a').forEach(function(a){{
    a.addEventListener('click', function(){{ document.getElementById('mainnav').classList.remove('open'); }});
  }});
}});
</script>'''

def breadcrumbs(path_pairs):
    parts = []
    for label, href in path_pairs:
        if href:
            parts.append(f'<a href="{href}">{label}</a>')
        else:
            parts.append(f'<span aria-current="page">{label}</span>')
    return f'<div class="breadcrumbs wrap">{" &rsaquo; ".join(parts)}</div>'

def chart_slider(slides, ui, slider_id="chart-slider", more_label="Подробнее →"):
    """Слайдер с инфографикой (12.08.2026, вторая версия — заменяет прежний CSS-only
    stat_slider() по прямой просьбе заказчика: «инфографика по каждой теме, график
    изменений в динамике за много лет, слайды листаются и обновляются сами»).

    slides: список dict {svg, title, caption, href (опц.), summary} — по одному
    графику (уже отрендеренный <svg>, см. chart_data.render_topic()) на слайд.
    ui: словарь локализованных подписей управления — chart_data.UI_LABELS[lang].
    slider_id: должен быть уникален в пределах страницы (на каждой из двух страниц,
    где используется компонент, сейчас только один экземпляр — коллизий нет).

    Автопрокрутка — JS (первая содержательная JS-логика на сайте не считая уже
    существующего переключателя мобильного меню в footer()): пауза при наведении/
    фокусе, явная кнопка паузы, отключение автостарта при prefers-reduced-motion —
    WCAG 2.2.2 (Pause, Stop, Hide) для авто-обновляющегося контента длительностью
    больше 5 секунд."""
    n = len(slides)
    track_items = []
    dot_items = []
    for i, s in enumerate(slides):
        link_html = f'\n        <a class="card-link" href="{s["href"]}">{more_label}</a>' if s.get("href") else ""
        track_items.append(f'''<div class="chart-slide" role="group" aria-roledescription="slide"
         aria-label="{ui["slide_n"](i+1, n, s["title"])}">
      <h3>{s["title"]}</h3>
      <div class="diagram">
        {s["svg"]}
        <p class="diagram-caption">{s["caption"]}</p>
      </div>{link_html}
    </div>''')
        dot_items.append(
            f'<button type="button" class="chart-slider-dot" aria-current="{"true" if i==0 else "false"}" '
            f'aria-label="{s["title"]}" data-i="{i}"></button>'
        )
    track_html = "\n    ".join(track_items)
    dots_html = "".join(dot_items)
    return f'''<div class="chart-slider" id="{slider_id}" role="region" aria-roledescription="carousel" aria-label="{ui["region"]}">
  <div class="chart-slider-viewport">
    <div class="chart-slider-track">
    {track_html}
    </div>
    <button type="button" class="chart-slider-arrow chart-slider-arrow--overlay chart-slider-prev" aria-label="{ui["prev"]}">‹</button>
    <button type="button" class="chart-slider-arrow chart-slider-arrow--overlay chart-slider-next" aria-label="{ui["next"]}">›</button>
    <div class="chart-slider-controls chart-slider-controls--overlay">
      <div class="chart-slider-dots">{dots_html}</div>
      <button type="button" class="chart-slider-play" aria-pressed="false" aria-label="{ui["pause"]}">⏸</button>
    </div>
  </div>
</div>
<script>
(function(){{
  var root = document.getElementById("{slider_id}");
  if(!root) return;
  var viewport = root.querySelector(".chart-slider-viewport");
  var track = root.querySelector(".chart-slider-track");
  var slides = root.querySelectorAll(".chart-slide");
  var dots = root.querySelectorAll(".chart-slider-dot");
  var prevBtn = root.querySelector(".chart-slider-prev");
  var nextBtn = root.querySelector(".chart-slider-next");
  var controlsPill = root.querySelector(".chart-slider-controls--overlay");
  var playBtn = root.querySelector(".chart-slider-play");
  var n = slides.length, i = 0, timer = null, playing = true;
  var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var PAUSE_LABEL = {json.dumps(ui["pause"], ensure_ascii=False)};
  var PLAY_LABEL = {json.dumps(ui["play"], ensure_ascii=False)};
  // 13.08.2026, третий заход: стрелки и панель точек/паузы стали overlay поверх самой
  // карточки графика (по эскизу заказчика — убрать нижнюю полосу совсем, слайдер = высота
  // одной карточки). Два замера на каждый слайд: (1) высота вьюпорта — под контент
  // ТЕКУЩЕГО слайда, а не под самый высокий из восьми (flex-ряд по умолчанию растягивает
  // все .chart-slide по высоте самого высокого); (2) позиция стрелок/пилюли — привязана
  // к самой .diagram (тёмной карточке с графиком), а не к вьюпорту целиком — на слайдах
  // хаба «Парагвай для переезда» после диаграммы ещё идёт ссылка «Подробнее», и без этой
  // привязки пилюля с точками легла бы поверх нее вместо нижнего края графика.
  function syncLayout(){{
    var s = slides[i];
    var diagramEl = s.querySelector(".diagram");
    var last = s.querySelector(".card-link") || diagramEl;
    if(!last) return;
    var vpRect = viewport.getBoundingClientRect();
    var lastRect = last.getBoundingClientRect();
    viewport.style.height = Math.ceil(lastRect.bottom - s.getBoundingClientRect().top) + "px";
    if(diagramEl){{
      var dRect = diagramEl.getBoundingClientRect();
      // Стрелки центрируем по самому SVG-графику, а не по всей карточке — иначе на
      // невысоких графиках (узкий экран, широкий viewBox) центр съезжает на подпись,
      // которая идёт под графиком внутри той же .diagram.
      var svgEl = diagramEl.querySelector("svg");
      var cRect = svgEl ? svgEl.getBoundingClientRect() : dRect;
      var centerY = Math.round((cRect.top + cRect.bottom)/2 - vpRect.top);
      // 19.08.2026: точки/пауза перенесены к верхнему краю карточки графика (раньше были
      // внизу — при более длинной подписи высота .diagram не всегда успевала «угнаться» за
      // пилюлей, и та вылезала на светлый фон под карточкой). Верх — фиксированный отступ
      // от диаграммы, гарантированно внутри тёмного фона за счёт padding-top в CSS.
      var topGap = Math.round(dRect.top - vpRect.top) + 8;
      prevBtn.style.top = centerY + "px";
      nextBtn.style.top = centerY + "px";
      if(controlsPill) controlsPill.style.top = topGap + "px";
    }}
  }}
  function go(idx){{
    i = (idx % n + n) % n;
    track.style.transform = "translateX(-" + (i*100) + "%)";
    dots.forEach(function(d, di){{ d.setAttribute("aria-current", di===i ? "true" : "false"); }});
    syncLayout();
  }}
  function tick(){{ go(i+1); }}
  function clear(){{ if(timer){{ clearInterval(timer); timer = null; }} }}
  function schedule(){{ clear(); if(playing && !reduceMotion) timer = setInterval(tick, 6500); }}
  function setPlaying(p){{
    playing = p;
    playBtn.setAttribute("aria-pressed", p ? "false" : "true");
    playBtn.textContent = p ? "⏸" : "▶";
    playBtn.setAttribute("aria-label", p ? PAUSE_LABEL : PLAY_LABEL);
    schedule();
  }}
  prevBtn.addEventListener("click", function(){{ go(i-1); schedule(); }});
  nextBtn.addEventListener("click", function(){{ go(i+1); schedule(); }});
  dots.forEach(function(d){{ d.addEventListener("click", function(){{ go(parseInt(d.getAttribute("data-i"),10)); schedule(); }}); }});
  playBtn.addEventListener("click", function(){{ setPlaying(!playing); }});
  root.addEventListener("mouseenter", clear);
  root.addEventListener("mouseleave", function(){{ if(playing) schedule(); }});
  root.addEventListener("focusin", clear);
  root.addEventListener("focusout", function(){{ if(playing) schedule(); }});
  window.addEventListener("resize", syncLayout);
  go(0);
  setPlaying(!reduceMotion);
  // Досчёт после загрузки веб-шрифта — до этого момента подпись графика может
  // рендериться запасным шрифтом с другими метриками, из-за чего первый замер
  // (в go(0) выше) слегка неточен, а resize по факту подгрузки шрифта не срабатывает.
  if(document.fonts && document.fonts.ready){{ document.fonts.ready.then(syncLayout); }}
}})();
</script>'''

def hero_photo_slider(photos, ui, slider_id="hero-photo"):
    """Фоновый фотослайдер hero на Главной (13.08.2026, заготовка — решение заказчика:
    «H1 надо вынести из слайдера», локация части фото (снимки со скайлайном через реку)
    не подтверждена — используем без привязки к конкретному городу, долг проверки
    зафиксирован в design/plan-foto-kontenta.md).

    photos: список dict {src, alt, lead} — src относительный путь от lang-папки
    (assets/img/hero/...), alt — текст для атрибута alt, lead — вариант текста-подписи
    под H1 для этого фото. H1 и кнопки статичны и в слайдере не участвуют — крутится
    только фон и текст .lead. Первое фото — eager/fetchpriority (LCP этого, самого
    посещаемого экрана сайта), остальные — lazy.

    Кроссфейд по opacity, а не translateX, как в chart_slider — здесь не нужно
    синхронизировать высоту вьюпорта под контент слайда: высота блока фиксирована
    (полноэкранное фото, см. .hero--photo в CSS), а не подстраивается под содержимое.

    Возвращает dict с готовыми фрагментами разметки — собираются в pages_home_uslugi.py
    вперемешку со статичным текстом (kicker/H1/кнопки из переводов HOME[lang])."""
    n = len(photos)
    slide_items, dot_items, lead_items = [], [], []
    for i, p in enumerate(photos):
        loading = "eager" if i == 0 else "lazy"
        fetchpriority = ' fetchpriority="high"' if i == 0 else ""
        slide_items.append(
            f'<img class="hero-photo-slide{" is-active" if i==0 else ""}" src="{p["src"]}" alt="{p["alt"]}" '
            f'loading="{loading}"{fetchpriority} aria-hidden="{"false" if i==0 else "true"}" data-i="{i}">'
        )
        dot_items.append(
            f'<button type="button" class="hero-photo-dot" aria-current="{"true" if i==0 else "false"}" '
            f'aria-label="{ui["slide_n"](i+1, n, p["alt"])}" data-i="{i}"></button>'
        )
        lead_items.append(f'<li data-i="{i}">{p["lead"]}</li>')
    slides_html = "\n    ".join(slide_items)
    dots_html = "".join(dot_items)
    leads_html = "\n    ".join(lead_items)
    photos_html = f'''<div class="hero-photo-viewport" id="{slider_id}" role="region" aria-roledescription="carousel" aria-label="{ui["region"]}">
    {slides_html}
    <div class="hero-photo-scrim" aria-hidden="true"></div>
    <button type="button" class="hero-photo-arrow hero-photo-prev" aria-label="{ui["prev"]}">‹</button>
    <button type="button" class="hero-photo-arrow hero-photo-next" aria-label="{ui["next"]}">›</button>
  </div>'''
    controls_html = f'''<div class="hero-photo-controls">
      <div class="hero-photo-dots">{dots_html}</div>
      <button type="button" class="hero-photo-play" aria-pressed="false" aria-label="{ui["pause"]}">⏸</button>
    </div>'''
    lead_variants_html = f'<ul class="hero-lead-variants" hidden>\n    {leads_html}\n  </ul>'
    script_html = f'''<script>
(function(){{
  var viewport = document.getElementById("{slider_id}");
  if(!viewport) return;
  var root = viewport.closest(".hero--photo");
  var slides = viewport.querySelectorAll(".hero-photo-slide");
  var dots = root.querySelectorAll(".hero-photo-dot");
  var prevBtn = viewport.querySelector(".hero-photo-prev");
  var nextBtn = viewport.querySelector(".hero-photo-next");
  var playBtn = root.querySelector(".hero-photo-play");
  var leadEl = root.querySelector(".lead");
  var leadVariants = root.querySelectorAll(".hero-lead-variants li");
  var n = slides.length, i = 0, timer = null, playing = true;
  var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var PAUSE_LABEL = {json.dumps(ui["pause"], ensure_ascii=False)};
  var PLAY_LABEL = {json.dumps(ui["play"], ensure_ascii=False)};
  function go(idx){{
    i = (idx % n + n) % n;
    slides.forEach(function(s, si){{
      s.setAttribute("aria-hidden", si===i ? "false" : "true");
      s.classList.toggle("is-active", si===i);
    }});
    dots.forEach(function(d, di){{ d.setAttribute("aria-current", di===i ? "true" : "false"); }});
    if(leadEl && leadVariants[i]) leadEl.textContent = leadVariants[i].textContent;
  }}
  function tick(){{ go(i+1); }}
  function clear(){{ if(timer){{ clearInterval(timer); timer = null; }} }}
  function schedule(){{ clear(); if(playing && !reduceMotion) timer = setInterval(tick, 6500); }}
  function setPlaying(p){{
    playing = p;
    playBtn.setAttribute("aria-pressed", p ? "false" : "true");
    playBtn.textContent = p ? "⏸" : "▶";
    playBtn.setAttribute("aria-label", p ? PAUSE_LABEL : PLAY_LABEL);
    schedule();
  }}
  prevBtn.addEventListener("click", function(){{ go(i-1); schedule(); }});
  nextBtn.addEventListener("click", function(){{ go(i+1); schedule(); }});
  dots.forEach(function(d){{ d.addEventListener("click", function(){{ go(parseInt(d.getAttribute("data-i"),10)); schedule(); }}); }});
  playBtn.addEventListener("click", function(){{ setPlaying(!playing); }});
  root.addEventListener("mouseenter", clear);
  root.addEventListener("mouseleave", function(){{ if(playing) schedule(); }});
  root.addEventListener("focusin", clear);
  root.addEventListener("focusout", function(){{ if(playing) schedule(); }});
  go(0);
  setPlaying(!reduceMotion);
}})();
</script>'''
    return dict(photos=photos_html, controls=controls_html, lead_variants=lead_variants_html, script=script_html)

# Локали для группировки разрядов в Intl.NumberFormat — подобраны так, чтобы live-курс на
# виджете визуально совпадал с уже принятым на сайте форматом сумм в гуарани на каждом языке
# (12.08.2026: RU — пробел "₲ 2 787 550", ES/DE — точка "₲ 2.787.550"/"₲2.787.550",
# EN — запятая "₲2,787,550"; см. суммы пошлин в pages_dokumenty.py/pages_cost_company_privacy.py).
# es-PY (не es-ES) — намеренно: у es-ES в современных ICU/CLDR minimumGroupingDigits=2,
# из-за чего 4-значные числа вроде 5925 остаются БЕЗ разделителя разрядов ("5925" вместо
# "5.925") — проверено вручную (node -e "Intl.NumberFormat('es-ES')..."), баг именно
# локали, не наш. es-PY групирует с той же цифры, что и остальной сайт (см. суммы пошлин
# в ES-текстах — "₲ 2.787.550"), и семантически точнее — валюта самого Парагвая.
RATE_WIDGET_LOCALE = {"ru": "ru-RU", "es": "es-PY", "en": "en-US", "de": "de-DE"}

RATE_WIDGET_TEXT = {
    "ru": dict(
        loading="Курс подключается…",
        updated="Обновлено", source="Источник",
        error='Не удалось загрузить текущий курс — возможно, браузер блокирует запрос к внешнему API. '
              'Актуальный курс — на официальной странице <a href="https://www.bcp.gov.py/es/cotizaciones">'
              'Banco Central del Paraguay (BCP)</a>.',
        noscript='Курс валют на этой странице обновляется скриптом в браузере — с отключённым JavaScript '
                 'показать его нельзя. Актуальный курс — на официальной странице '
                 '<a href="https://www.bcp.gov.py/es/cotizaciones">Banco Central del Paraguay (BCP)</a>.',
        disclaimer='Курс — рыночный, от агрегатора <a href="https://www.exchangerate-api.com" rel="nofollow noopener">'
                    'ExchangeRate-API</a>, обновляется у них раз в сутки. Он близок к официальной котировке BCP, '
                    'но не тождественен ей — для государственных пошлин и налогов ориентируйтесь на суммы в '
                    'гуарани, указанные на сайте, а не на пересчёт по этому курсу.',
    ),
    "es": dict(
        loading="Conectando con el tipo de cambio…",
        updated="Actualizado", source="Fuente",
        error='No se pudo cargar el tipo de cambio actual — puede que el navegador esté bloqueando la solicitud '
              'a la API externa. El tipo de cambio vigente está en la página oficial del '
              '<a href="https://www.bcp.gov.py/es/cotizaciones">Banco Central del Paraguay (BCP)</a>.',
        noscript='El tipo de cambio de esta página se actualiza mediante un script en el navegador — con '
                 'JavaScript desactivado no se puede mostrar. El tipo de cambio vigente está en la página '
                 'oficial del <a href="https://www.bcp.gov.py/es/cotizaciones">Banco Central del Paraguay (BCP)</a>.',
        disclaimer='Es un tipo de cambio de mercado, del agregador <a href="https://www.exchangerate-api.com" '
                    'rel="nofollow noopener">ExchangeRate-API</a>, que ellos actualizan una vez al día. Es '
                    'cercano a la cotización oficial del BCP, pero no idéntico — para aranceles e impuestos '
                    'estatales, guíese por los montos en guaraníes indicados en el sitio, no por esta conversión.',
    ),
    "en": dict(
        loading="Connecting to the exchange rate…",
        updated="Updated", source="Source",
        error='Couldn\'t load the current exchange rate — the browser may be blocking the request to the '
              'external API. The current rate is on the official <a href="https://www.bcp.gov.py/en/cotizaciones">'
              'Banco Central del Paraguay (BCP)</a> page.',
        noscript='The exchange rate on this page updates via a browser script — it can\'t be shown with '
                 'JavaScript disabled. The current rate is on the official '
                 '<a href="https://www.bcp.gov.py/en/cotizaciones">Banco Central del Paraguay (BCP)</a> page.',
        disclaimer='This is a market rate from the <a href="https://www.exchangerate-api.com" rel="nofollow '
                    'noopener">ExchangeRate-API</a> aggregator, updated by them once a day. It\'s close to '
                    'the official BCP quote but not identical — for government fees and taxes, go by the '
                    'guaraní amounts stated on the site, not by converting through this rate.',
    ),
    "de": dict(
        loading="Wechselkurs wird geladen…",
        updated="Aktualisiert", source="Quelle",
        error='Der aktuelle Wechselkurs konnte nicht geladen werden — möglicherweise blockiert der Browser die '
              'Anfrage an die externe API. Der aktuelle Kurs steht auf der offiziellen Seite der '
              '<a href="https://www.bcp.gov.py/en/cotizaciones">Banco Central del Paraguay (BCP)</a>.',
        noscript='Der Wechselkurs auf dieser Seite wird per Skript im Browser aktualisiert — bei '
                 'deaktiviertem JavaScript kann er nicht angezeigt werden. Der aktuelle Kurs steht auf der '
                 'offiziellen Seite der <a href="https://www.bcp.gov.py/en/cotizaciones">Banco Central del '
                 'Paraguay (BCP)</a>.',
        disclaimer='Das ist ein Marktkurs des Aggregators <a href="https://www.exchangerate-api.com" '
                    'rel="nofollow noopener">ExchangeRate-API</a>, von diesem einmal täglich aktualisiert. Er '
                    'liegt nah am offiziellen BCP-Kurs, ist ihm aber nicht gleichzusetzen — bei staatlichen '
                    'Gebühren und Steuern richten Sie sich nach den auf der Website genannten '
                    'Guaraní-Beträgen, nicht nach dieser Umrechnung.',
    ),
}

def rate_widget(lang, widget_id="rate-widget"):
    """Живой виджет курса ₲/USD, ₲/EUR, ₲/RUB (12.08.2026) — заменяет прежнюю текстовую
    заглушку .rate-widget-placeholder на «Терминологии». Источник — открытый (без ключа и
    регистрации) endpoint open.er-api.com (проект ExchangeRate-API, см. RATE_WIDGET_TEXT
    выше) — у самого BCP нет публичного API/виджета (проверено 12.08.2026: их страница
    котировок отдаёт только HTML-таблицу и PDF, см. design/plan-dekora-i-perelinkovki.md
    не про это, а design-проект отдельно зафиксировал этот факт в переписке с заказчиком).
    Один запрос с base=USD — из него же считаются EUR и RUB через кросс-курс
    (rates.PYG/rates.EUR и rates.PYG/rates.RUB), см. JS ниже. Запрос идёт из браузера
    посетителя сайта, а не с сервера — открытый endpoint именно для этого и предназначен,
    ключ не нужен. При сбое (сеть, блокировщик, отключённый JS) — не подставляем никакую
    цифру от себя, а показываем ссылку на официальную страницу BCP (правило проекта
    «не изобретай факты» применимо и к рантайм-данным, не только к тексту)."""
    t = RATE_WIDGET_TEXT[lang]
    locale = RATE_WIDGET_LOCALE[lang]
    rows_html = "\n    ".join(
        f'<div class="rate-row"><span class="rate-code">{code}</span>'
        f'<span class="rate-value num" data-cur="{code}">…</span></div>'
        for code in ("USD", "EUR", "RUB")
    )
    return f'''<div class="rate-widget" id="{widget_id}">
  <div class="rate-widget-rows">
    {rows_html}
  </div>
  <p class="rate-widget-status">{t["loading"]}</p>
  <p class="rate-widget-meta" hidden>{t["updated"]}: <span class="rate-updated"></span> ·
    {t["source"]}: <a href="https://www.exchangerate-api.com" rel="nofollow noopener">ExchangeRate-API</a></p>
  <p class="rate-widget-disclaimer" hidden>{t["disclaimer"]}</p>
</div>
<noscript><style>#{widget_id}{{display:none}}</style><p class="rate-widget-error">{t["noscript"]}</p></noscript>
<script>
(function(){{
  var root = document.getElementById("{widget_id}");
  if(!root) return;
  var rowsBox = root.querySelector(".rate-widget-rows");
  var statusEl = root.querySelector(".rate-widget-status");
  var metaEl = root.querySelector(".rate-widget-meta");
  var updatedEl = root.querySelector(".rate-updated");
  var discEl = root.querySelector(".rate-widget-disclaimer");
  var ERROR_HTML = {json.dumps(t["error"], ensure_ascii=False)};
  var fmt = (window.Intl && Intl.NumberFormat)
    ? new Intl.NumberFormat({json.dumps(locale, ensure_ascii=False)}, {{maximumFractionDigits: 0}})
    : null;
  fetch("https://open.er-api.com/v6/latest/USD")
    .then(function(r){{ if(!r.ok) throw new Error("bad status"); return r.json(); }})
    .then(function(data){{
      if(data.result !== "success" || !data.rates || !data.rates.PYG || !data.rates.EUR || !data.rates.RUB){{
        throw new Error("bad payload");
      }}
      var pyg = {{
        USD: data.rates.PYG,
        EUR: data.rates.PYG / data.rates.EUR,
        RUB: data.rates.PYG / data.rates.RUB
      }};
      rowsBox.querySelectorAll(".rate-value").forEach(function(el){{
        var v = pyg[el.getAttribute("data-cur")];
        var formatted = fmt ? fmt.format(v) : String(Math.round(v));
        el.textContent = "₲ " + formatted.replace(/ /g, " ");
      }});
      if(data.time_last_update_utc){{
        var d = new Date(data.time_last_update_utc);
        var pad = function(n){{ return (n < 10 ? "0" : "") + n; }};
        updatedEl.textContent = isNaN(d.getTime())
          ? data.time_last_update_utc
          : pad(d.getUTCDate()) + "." + pad(d.getUTCMonth()+1) + "." + d.getUTCFullYear()
            + ", " + pad(d.getUTCHours()) + ":" + pad(d.getUTCMinutes()) + " UTC";
      }}
      statusEl.hidden = true;
      metaEl.hidden = false;
      discEl.hidden = false;
    }})
    .catch(function(){{
      statusEl.innerHTML = ERROR_HTML;
      rowsBox.hidden = true;
    }});
}})();
</script>'''

def schema_breadcrumb(items):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i+1, "name": name, "item": DOMAIN + url}
            for i, (name, url) in enumerate(items)
        ]
    }

def page(page_id, lang, title, description, body_html, extra_schema=None, robots="index,follow"):
    fname = f"{lang}/{slug(page_id, lang)}"
    canonical = f"/{lang}/{slug(page_id, lang)}"
    schemas = []
    if extra_schema:
        schemas.extend(extra_schema if isinstance(extra_schema, list) else [extra_schema])
    schema_tags = "\n".join(
        f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>'
        for s in schemas
    )
    hreflang_tags = "\n".join(
        f'<link rel="alternate" hreflang="{l}" href="{DOMAIN}/{l}/{slug(page_id, l)}">' for l in LANGS if slug(page_id, l)
    )
    if slug(page_id, DEFAULT_LANG):
        hreflang_tags += f'\n<link rel="alternate" hreflang="x-default" href="{DOMAIN}/{DEFAULT_LANG}/{slug(page_id, DEFAULT_LANG)}">'
    html_lang = {"ru": "ru", "es": "es", "en": "en", "de": "de"}[lang]
    html = f'''<!doctype html>
<html lang="{html_lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{DOMAIN}{canonical}">
{hreflang_tags}
<link rel="icon" href="../assets/img/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="../assets/img/favicon-180.png">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:locale" content="{html_lang}">
<meta property="og:image" content="{DOMAIN}/assets/img/favicon-512.png">
<link rel="stylesheet" href="../assets/css/style.css">
{schema_tags}
</head>
<body>
{header(lang, page_id)}
<main id="main">
{body_html}
</main>
{footer(lang)}
</body>
</html>'''
    out_path = os.path.join(ROOT, fname)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", fname)

ORG_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": CONTACT_LEGAL_NAME,
    "url": DOMAIN,
    "logo": DOMAIN + "/assets/img/favicon-512.png",
    "email": CONTACT_EMAIL,
    "telephone": CONTACT_PHONE,
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "ETAPA 9009 San Isidro",
        "postalCode": "6000",
        "addressLocality": "Encarnación",
        "addressCountry": "PY",
    },
    "sameAs": ["https://t.me/grundparaguay"],
    "description": "Юридическое сопровождение переезда, резидентуры и бизнеса в Парагвае для русскоязычных клиентов."
}

print("helpers loaded (multilingual)")
