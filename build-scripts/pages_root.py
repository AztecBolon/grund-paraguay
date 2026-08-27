#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Корневая страница-редирект (языковой пикер) — /index.html.
Не использует page() из build.py, так как лежит на уровень выше /ru //es //en/
(другие относительные пути к assets), и не должна попадать в hreflang как
отдельная языковая версия — это языково-нейтральный вход на сайт."""
from build import ROOT, DOMAIN, SITE_NAME, LANGS, DEFAULT_LANG, slug
import os

LABELS = {
    "ru": {"native": "Русский", "tagline": "Переезд, резидентура и бизнес в Парагвае", "enter": "Открыть сайт на русском"},
    "es": {"native": "Español", "tagline": "Mudanza, residencia y negocios en Paraguay", "enter": "Abrir el sitio en español"},
    "en": {"native": "English", "tagline": "Relocation, residency and business in Paraguay", "enter": "Open the site in English"},
    "de": {"native": "Deutsch", "tagline": "Umzug, Aufenthalt und Geschäft in Paraguay", "enter": "Website auf Deutsch öffnen"},
}
REDIRECTING = {"ru": "Определяем язык…", "es": "Detectando idioma…", "en": "Detecting language…", "de": "Sprache wird erkannt…"}
CHOOSE = {"ru": "Или выберите язык вручную:", "es": "O elija el idioma manualmente:", "en": "Or choose a language manually:", "de": "Oder Sprache manuell wählen:"}

lang_cards = "\n".join(
    f'''      <a class="lang-card" href="{l}/{slug("home", l)}" data-lang="{l}">
        <span class="lang-native">{LABELS[l]["native"]}</span>
        <span class="lang-tagline">{LABELS[l]["tagline"]}</span>
      </a>''' for l in LANGS
)

default_url = f"{DEFAULT_LANG}/{slug('home', DEFAULT_LANG)}"

# JS: сопоставляем navigator.language с поддерживаемыми языками, иначе — DEFAULT_LANG
detect_js = f'''
(function () {{
  var supported = {LANGS!r};
  var def = {DEFAULT_LANG!r};
  var langs = (navigator.languages && navigator.languages.length) ? navigator.languages : [navigator.language || navigator.userLanguage || def];
  var target = def;
  for (var i = 0; i < langs.length; i++) {{
    var code = (langs[i] || '').slice(0, 2).toLowerCase();
    if (supported.indexOf(code) !== -1) {{ target = code; break; }}
  }}
  var dest = {{{", ".join(f'{l!r}: "{l}/{slug("home", l)}"' for l in LANGS)}}}[target];
  if (dest) {{ window.location.replace(dest); }}
}})();
'''

html = f'''<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{SITE_NAME}</title>
<meta name="robots" content="noindex,follow">
<link rel="canonical" href="{DOMAIN}/">
<meta http-equiv="refresh" content="3;url={default_url}">
<link rel="icon" href="assets/img/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="assets/img/favicon-180.png">
<link rel="stylesheet" href="assets/css/style.css">
<style>
  body{{display:flex;align-items:center;justify-content:center;min-height:100vh;background:var(--paper);}}
  .picker{{max-width:520px;width:100%;padding:32px 24px;text-align:center;}}
  .picker img{{width:56px;height:56px;margin-bottom:16px;}}
  .picker .redirect-note{{font-size:13px;color:var(--ink-muted);margin-bottom:24px;}}
  .picker .choose-label{{font-size:13px;color:var(--ink-muted);margin:20px 0 10px;}}
  .lang-cards{{display:flex;flex-direction:column;gap:10px;}}
  .lang-card{{display:flex;flex-direction:column;gap:2px;padding:14px 18px;border:1px solid rgba(20,33,59,.15);border-radius:8px;text-decoration:none;text-align:left;transition:border-color .15s,background .15s;}}
  .lang-card:hover{{border-color:var(--blue);background:var(--paper-alt);}}
  .lang-native{{font-weight:700;color:var(--ink);font-size:16px;}}
  .lang-tagline{{font-size:13px;color:var(--ink-muted);}}
</style>
<script>{detect_js}</script>
</head>
<body>
  <div class="picker">
    <img src="assets/img/mark.png" alt="{SITE_NAME}" width="56" height="56">
    <div class="redirect-note">{REDIRECTING["ru"]} / {REDIRECTING["es"]} / {REDIRECTING["en"]} / {REDIRECTING["de"]}</div>
    <div class="choose-label">{CHOOSE["ru"]} / {CHOOSE["es"]} / {CHOOSE["en"]} / {CHOOSE["de"]}</div>
    <div class="lang-cards">
{lang_cards}
    </div>
  </div>
</body>
</html>'''

out_path = os.path.join(ROOT, "index.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html)
print("wrote index.html (root language picker)")
