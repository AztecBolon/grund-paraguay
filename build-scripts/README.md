# Сборка сайта

Статические HTML-страницы в корне архива собраны этими Python-скриптами из
текстов `design/teksty-sait-seo.md` (проект Cowork). Изменили текст в проекте —
поправьте соответствующий блок в одном из pages_*.py и пересоберите:

    cd build-scripts
    python3 pages_home_uslugi.py
    python3 pages_process_risks.py
    python3 pages_cost_company_privacy.py
    python3 pages_cases_contacts.py
    python3 pages_terminology.py
    python3 pages_legal_seo.py

Каждый скрипт пишет готовые .html-файлы на уровень выше (в корень сайта).
Общий шаблон (шапка/подвал/схема.org) — в build.py.
