# Grund Paraguay — сайт

Статический многоязычный сайт (RU/ES/EN/DE) агентства по иммиграции в Парагвай.

## Структура

- `ru/`, `es/`, `en/`, `de/` — собранные HTML-страницы сайта (выходные файлы сборки, не редактируются вручную).
- `assets/` — CSS, изображения, favicon.
- `build-scripts/` — генератор сайта на Python. Каждый `pages_*.py` собирает свою группу
  страниц самостоятельно (`python3 pages_X.py`) — общего build-раннера пока нет.
- `index.html`, `robots.txt`, `sitemap.xml` — корневые файлы.

## Как пересобрать сайт

Из `build-scripts/`:

```
python3 pages_root.py
python3 pages_home_uslugi.py
python3 pages_uslugi_stranitsy.py
python3 pages_kak_my_rabotaem.py
python3 pages_process_risks.py
python3 pages_cost_company_privacy.py
python3 pages_cases_contacts.py
python3 pages_paragvay_hub.py
python3 pages_turizm.py
python3 pages_dokumenty.py
python3 pages_terminology.py
python3 pages_sitemap.py
python3 pages_legal_seo.py
```

Порядок важен только для `pages_terminology.py` (сканирует остальные `pages_*.py` на предмет
бэклинков — запускать после всех остальных) и `pages_legal_seo.py`/`pages_sitemap.py`
(перечисляют финальный список страниц — запускать последними).

## Проверка

```
python3 check_links.py
```

Проверяет все href/src во всех собранных HTML-файлах на битые ссылки и якоря.
