#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Карта сайта — служебная страница со списком всех разделов и страниц со ссылками
(13.08.2026). Ссылка на неё — в дропдауне "Документы ▾" служебной строки (header-utility)
и в колонке "Документы" футера, см. FOOTER_LEGAL_ORDER в build.py.

Группы и заголовки берутся из NAV_LABELS/DOCS_LABEL, а не дублируются здесь строками —
если слаг или подпись пункта меню поменяются в build.py, карта сайта обновится сама при
пересборке, без риска разъехаться с реальной структурой."""
from build import page, breadcrumbs, schema_breadcrumb, NAV_LABELS, DOCS_LABEL, href_to

# Подписи 7 подстраниц хаба «Парагвай для переезда» — сознательное дублирование значений
# CARD_TITLE из pages_paragvay_hub.py (не импортируем сам модуль: его код собирает страницы
# уже на уровне модуля, без "if __name__", импорт заново перезаписал бы весь хаб как побочный
# эффект). Если подписи карточек хаба поменяются — поправить синхронно и здесь.
HUB_SUBPAGE_LABELS = {
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

# «Релокация организаций» и «Туризм» (21.08.2026, обе переведены на ES/EN/DE) — подписи для
# карты сайта; USLUGA_LABEL/TURIZM_LABEL не импортируются из pages_uslugi_stranitsy.py/
# pages_turizm.py по той же причине, что и HUB_SUBPAGE_LABELS выше (импорт модуля целиком
# пересобрал бы его страницы как побочный эффект) — подписи продублированы здесь вручную.
EXTRA_LABELS = {
    "usluga-relocation": {"ru": "Релокация организаций", "es": "Relocalización de empresas",
                           "en": "Business Relocation", "de": "Unternehmensrelokation"},
    "turizm": {"ru": "Туризм", "es": "Turismo", "en": "Tourism", "de": "Tourismus"},
    "usluga-medicina": {"ru": "Медицинское сопровождение", "es": "Asistencia médica",
                         "en": "Medical Support", "de": "Medizinische Begleitung"},
    "meditsina-v-paragvae": {"ru": "Медицина в Парагвае", "es": "Medicina en Paraguay",
                              "en": "Healthcare in Paraguay", "de": "Medizin in Paraguay"},
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
    "rabota-v-paragvae": {"ru": "Работа в Парагвае", "es": "Trabajo en Paraguay",
                           "en": "Working in Paraguay", "de": "Arbeiten in Paraguay"},
}

LABELS = {lang: {**NAV_LABELS[lang], **HUB_SUBPAGE_LABELS[lang],
                  **{k: v[lang] for k, v in EXTRA_LABELS.items()}} for lang in NAV_LABELS}

ALL_IDS = [
    "home", "uslugi", "usluga-relocation", "usluga-medicina",
    "usluga-compliance", "usluga-citizenship", "usluga-realestate", "usluga-company", "usluga-business",
    "kak-my-rabotaem", "protsess", "riski", "stoimost",
    "paragvay-hub", "pochemu-paragvay", "zhizn-v-paragvae", "stoimost-zhizni",
    "nalogi-inostrantsev", "banki-perevody", "viza-vyezd", "mify-voprosy", "turizm", "meditsina-v-paragvae",
    "rabota-v-paragvae",
    "o-kompanii", "keisy", "kontakty",
    "konfidentsialnost", "dokumenty", "dok-temporal", "dok-permanente", "dok-investor", "dok-grazhdanstvo",
    "terminologiya", "oferta", "politika", "sitemap",
]

def L(lang):
    return {pid: href_to(pid, lang) for pid in ALL_IDS}

# Группы страницы: id=None — группа без собственной страницы (используется её ярлык
# DOCS_LABEL, как в дропдауне шапки). children — плоский список id, элемент-строка "dokumenty"
# внутри последней группы дополнительно разворачивается через DOCS_SUBCHILDREN.
SECTIONS = [
    dict(id="home", children=[]),
    dict(id="uslugi", children=["usluga-relocation", "usluga-medicina",
                                 "usluga-compliance", "usluga-citizenship", "usluga-realestate",
                                 "usluga-company", "usluga-business"]),
    dict(id="kak-my-rabotaem", children=["protsess", "riski"]),
    dict(id="stoimost", children=[]),
    dict(id="paragvay-hub", children=["pochemu-paragvay", "zhizn-v-paragvae", "stoimost-zhizni",
                                       "nalogi-inostrantsev", "banki-perevody", "viza-vyezd", "mify-voprosy",
                                       "turizm", "meditsina-v-paragvae", "rabota-v-paragvae"]),
    dict(id="o-kompanii", children=[]),
    dict(id="keisy", children=[]),
    dict(id="kontakty", children=[]),
    dict(id=None, children=["konfidentsialnost", "dokumenty", "terminologiya", "oferta", "politika", "sitemap"]),
]
DOCS_SUBCHILDREN = {"dokumenty": ["dok-temporal", "dok-permanente", "dok-investor", "dok-grazhdanstvo"]}

SITEMAP = {
"ru": dict(
    title="Карта сайта — все страницы Grund Paraguay",
    description="Полный список разделов и страниц сайта Grund Paraguay со ссылками — быстрый способ найти нужный раздел.",
    h1="Карта сайта",
    lead="Полный список разделов и страниц сайта — если не получилось найти нужное через меню.",
),
"es": dict(
    title="Mapa del sitio — todas las páginas de Grund Paraguay",
    description="Lista completa de las secciones y páginas del sitio de Grund Paraguay con enlaces — una forma rápida de encontrar lo que busca.",
    h1="Mapa del sitio",
    lead="Lista completa de las secciones y páginas del sitio — por si no encontró lo que buscaba a través del menú.",
),
"en": dict(
    title="Sitemap — all Grund Paraguay pages",
    description="A complete list of Grund Paraguay's sections and pages with links — a quick way to find what you're looking for.",
    h1="Sitemap",
    lead="A complete list of the site's sections and pages — in case the menu didn't get you where you needed.",
),
"de": dict(
    title="Seitenübersicht — alle Seiten von Grund Paraguay",
    description="Vollständige Liste der Bereiche und Seiten von Grund Paraguay mit Links — ein schneller Weg, um das Gesuchte zu finden.",
    h1="Seitenübersicht",
    lead="Vollständige Liste der Bereiche und Seiten der Website — falls Sie über das Menü nicht gefunden haben, was Sie suchten.",
),
}

def render_children(ids, lang, l):
    items = []
    for cid in ids:
        sub = DOCS_SUBCHILDREN.get(cid)
        if sub:
            sub_html = "".join(f'<li><a href="{l[sid]}">{LABELS[lang][sid]}</a></li>' for sid in sub)
            items.append(f'<li><a href="{l[cid]}">{LABELS[lang][cid]}</a><ul>{sub_html}</ul></li>')
        else:
            items.append(f'<li><a href="{l[cid]}">{LABELS[lang][cid]}</a></li>')
    return "".join(items)

for lang, t in SITEMAP.items():
    l = L(lang)
    groups_html = []
    for sec in SECTIONS:
        if sec["id"]:
            heading = f'<h2><a href="{l[sec["id"]]}">{LABELS[lang][sec["id"]]}</a></h2>'
        else:
            heading = f'<h2>{DOCS_LABEL[lang]}</h2>'
        children_html = f'<ul>{render_children(sec["children"], lang, l)}</ul>' if sec["children"] else ""
        groups_html.append(f'<div class="prose sitemap-group" style="padding:0;max-width:100%;">{heading}{children_html}</div>')
    sitemap_body = f'''
{breadcrumbs([(LABELS[lang]["home"], l["home"]), (t["h1"], None)])}
<section class="hero" style="padding-top:24px;">
  <div class="wrap">
    <h1>{t["h1"]}</h1>
    <p class="lead">{t["lead"]}</p>
  </div>
</section>
<section style="padding-top:0;">
  <div class="wrap">
    <div class="grid grid-3 sitemap-groups">
      {"".join(groups_html)}
    </div>
  </div>
</section>
'''
    page("sitemap", lang, t["title"], t["description"], sitemap_body,
         extra_schema=schema_breadcrumb([(LABELS[lang]["home"], f"/{lang}/"), (t["h1"], f"/{lang}/{href_to('sitemap', lang)}")]),
         robots="noindex,follow")
