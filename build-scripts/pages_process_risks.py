#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Процесс и сроки + Честно о рисках — ru/es/en"""
from build import page, breadcrumbs, schema_breadcrumb, DOMAIN, href_to, NAV_LABELS, seal_svg, icon

def L(lang):
    return {pid: href_to(pid, lang) for pid in
            ["home","uslugi","protsess","riski","stoimost","o-kompanii","konfidentsialnost","keisy","kontakty","terminologiya","kak-my-rabotaem",
             "dok-temporal","dok-permanente","dok-grazhdanstvo"]}

# Штампы-ссылки на таймлайне «Процесс и сроки» (12.08.2026, декор-фаза 1.2 — "флагманская"
# идея плана перелинковки) — у этапов, для которых есть отдельная программная страница в
# разделе «Документы», под текстом появляется маленький штамп-ссылка на неё. Этап 1
# (Temporal) → dok-temporal, этап 3 (Permanente) → dok-permanente, этап 4 (Гражданство) →
# dok-grazhdanstvo. Этап 2 (окно подачи) не ведёт никуда — это не отдельная программа, а
# процедурное окно внутри перехода Temporal → Permanente, под него нет страницы документов.
TIMELINE_DOC_PIDS = ["dok-temporal", None, "dok-permanente", "dok-grazhdanstvo"]
TIMELINE_DOC_LABEL = {
    "ru": "Документы для этого этапа",
    "es": "Documentos para esta etapa",
    "en": "Documents for this stage",
    "de": "Dokumente für diese Etappe",
}

# Печать «Без ложных обещаний» на «Процессе и сроках» (12.08.2026) — та же печать
# (иконка honest, красный цвет), что и в SEALS["ru"][2] на Главной (pages_home_uslugi.py) и
# формулировка её ring-текста дословно взята оттуда же. Эта страница — первоисточник самого
# факта (директор DNM, ABC Color, 04.05.2026), поэтому печать здесь даже уместнее, чем на
# Главной, где это лишь один из четырёх коротких тизеров.
HONEST_SEAL = {
    "ru": ("honest", "red", "Без ложных обещаний", "Срок 7–8 лет, не «за год»",
           "Без ложных обещаний: реальный срок — 7–8 лет, а не «за один год», по словам директора DNM (ABC Color, 04.05.2026)"),
    "es": ("honest", "red", "Sin promesas falsas", "7–8 años, no «un año»",
           "Sin promesas falsas: el plazo real es de 7–8 años, no «en un año», según el director de la DNM (ABC Color, 04.05.2026)"),
    "en": ("honest", "red", "No false promises", "7–8 years, not \"one year\"",
           "No false promises: the real timeline is 7–8 years, not \"one year,\" according to the DNM director (ABC Color, 05/04/2026)"),
    "de": ("honest", "red", "Keine falschen Versprechen", "7–8 Jahre, nicht „ein Jahr\"",
           "Keine falschen Versprechen: die reale Frist beträgt 7–8 Jahre, nicht „ein Jahr\", laut dem Direktor der DNM (ABC Color, 04.05.2026)"),
}

# ==================================================== ПРОЦЕСС И СРОКИ / PROCESS

PROCESS = {
"ru": dict(
    title="Сроки ВНЖ и гражданства Парагвая: честный таймлайн | Grund Paraguay",
    description="Реальный таймлайн переезда в Парагвай: временная и постоянная резиденция, окно подачи документов и честный срок до гражданства — 7–8 лет, а не за один год.",
    h1="Процесс и реальные сроки: от переезда до гражданства Парагвая",
    lead='Реальная последовательность этапов на пути к постоянному статусу в Парагвае, без сокращений и без обещаний «оформим за неделю». Подробно о том, что входит в оформление каждого этапа, — на странице <a href="{uslugi}">«Услуги»</a>.',
    steps=[
      ("Этап 1. Временная резиденция (Residencia Temporal)",
       'Оформляется по Ley N° 6984/22 «De Migraciones» (ст. 46) и действует до 2 лет. При необходимости резиденция может быть продлена ещё на такой же срок. Статус утрачивается при отсутствии в стране свыше 1 года. Уже на этом этапе, после получения резиденции, возникает обязанность зарегистрировать <a href="{terminologiya}#ruc">RUC</a> и вести регулярную налоговую отчётность (как правило — ежемесячно) — это отдельная услуга сопровождения (см. страницу <a href="{uslugi}">«Услуги»</a>), а не формальность, которую можно отложить.'),
      ("Этап 2. Окно подачи на постоянную резиденцию",
       'Заявление на Residencia Permanente обычным путём подаётся в течение 90 дней до истечения срока Residencia Temporal — то есть переход не происходит автоматически и требует отдельного действия в конкретный временной интервал. Исключение — инвесторский путь через <a href="{terminologiya}#suace">SUACE</a> (см. страницу «Услуги»): при инвестициях от 70 000 USD постоянная резиденция доступна напрямую, без прохождения Temporal.'),
      ("Этап 3. Постоянная резиденция (Residencia Permanente)",
       'Выдаётся на 10 лет и также подлежит продлению; утрачивается при отсутствии в стране свыше 3 лет подряд. С 6 июля 2026 года заявки на Permanente рассматриваются по новой резолюции миграционной службы (<a href="{terminologiya}#dnm">DNM</a>) N° 407/2026 — она вводит 12 категорий заявителей (профессионалы, наёмные работники, фрилансеры и цифровые кочевники, коммерсанты, поставщики услуг, собственники недвижимости, акционеры бизнеса, фермеры, священнослужители, пенсионеры, иждивенцы, студенты) с отдельными требованиями по подтверждению платёжеспособности для каждой. Точные пороги по категориям официально пока не опубликованы в открытом доступе — мы уточняем их индивидуально под вашу ситуацию на момент подачи; актуальные тарифы — на странице <a href="{stoimost}">«Стоимость и тарифы»</a>.'),
      ("Этап 4. Гражданство",
       'По Конституции Парагвая (ст. 148) натурализация возможна не ранее чем через 3 года «radicación» (проживания со статусом) — и этот срок отсчитывается именно с даты получения Residencia Permanente, а не с момента въезда в страну. Дело о натурализации ведёт не миграционная служба, а Верховный суд (<a href="{terminologiya}#corte-suprema">Corte Suprema de Justicia</a>); процедура требует личной явки заявителя и сопровождения адвоката.'),
    ],
    fact_num="5 лет", fact_cap="теоретический минимум (2 года Temporal + 3 года ожидания после Permanente) — формальная сумма сроков этапов, без учёта времени на сбор документов и рассмотрение дела.",
    p_after='На практике, с учётом реального времени на сбор документов, рассмотрение дела и его прохождение через Corte Suprema, директор DNM Хорхе Кронаветтер в мае 2026 года публично назвал более честную цифру — <strong>7–8 лет</strong> от переезда до паспорта (ABC Color, 04.05.2026). Это и есть срок, на который стоит рассчитывать при планировании переезда, а не рекламные обещания «гражданства за год» — подробнее о том, откуда берутся такие обещания и почему им не стоит верить, на странице <a href="{riski}">«Риски и трудности»</a>.',
    callout_label="Методологическая оговорка",
    callout='Официально фиксированных нормативов по срокам рассмотрения самой заявки DNM (сколько именно недель или месяцев занимает выдача Temporal или парагвайской <a href="{terminologiya}#cedula">Cédula</a> после подачи полного пакета) в открытых источниках на момент подготовки этого текста нет — это внутренняя административная практика, которая может меняться. Мы отслеживаем статус каждого дела индивидуально и сообщаем клиенту актуальные сроки по мере продвижения, а не даём усреднённую цифру, которую невозможно проверить.',
),
"es": dict(
    title="Plazos de residencia y ciudadanía en Paraguay: cronología honesta | Grund Paraguay",
    description="Cronología real de la mudanza a Paraguay: residencia temporal y permanente, ventana para presentar documentos y el plazo honesto hasta la ciudadanía — 7 a 8 años, no en un año.",
    h1="Proceso y plazos reales: de la mudanza a la ciudadanía paraguaya",
    lead='La secuencia real de etapas hacia el estatus permanente en Paraguay, sin atajos ni promesas de «lo tramitamos en una semana». Los detalles de cada etapa están en la página <a href="{uslugi}">«Servicios»</a>.',
    steps=[
      ("Etapa 1. Residencia temporal (Residencia Temporal)",
       'Se tramita según la Ley N.° 6984/22 «De Migraciones» (art. 46) y es válida hasta por 2 años. Si es necesario, puede renovarse por el mismo plazo. El estatus se pierde si hay ausencia del país por más de 1 año. Ya en esta etapa, tras obtener la residencia, surge la obligación de inscribir el <a href="{terminologiya}#ruc">RUC</a> y presentar declaraciones tributarias de forma periódica (por lo general mensual) — es un servicio de acompañamiento aparte (ver la página <a href="{uslugi}">«Servicios»</a>), no un trámite que se pueda postergar.'),
      ("Etapa 2. Ventana para solicitar la residencia permanente",
       'La solicitud de Residencia Permanente por la vía habitual se presenta dentro de los 90 días previos al vencimiento de la Residencia Temporal — es decir, el paso no es automático y requiere una acción concreta dentro de una ventana específica. La excepción es la vía de inversor a través de <a href="{terminologiya}#suace">SUACE</a> (ver «Servicios»): con inversiones desde 70.000 USD, la residencia permanente está disponible directamente, sin pasar por la Temporal.'),
      ("Etapa 3. Residencia permanente (Residencia Permanente)",
       'Se otorga por 10 años y también es renovable; se pierde con una ausencia del país superior a 3 años consecutivos. Desde el 6 de julio de 2026, las solicitudes de Permanente se evalúan según la nueva resolución de la <a href="{terminologiya}#dnm">DNM</a> N.° 407/2026 — introduce 12 categorías de solicitantes (profesionales, empleados, freelancers y nómadas digitales, comerciantes, prestadores de servicios, propietarios de inmuebles, accionistas de empresas, agricultores, religiosos, jubilados, dependientes, estudiantes) con requisitos propios de solvencia para cada una. Los umbrales exactos por categoría aún no están publicados oficialmente — los confirmamos de forma individual según su situación al momento de la solicitud; tarifas actuales en la página <a href="{stoimost}">«Costos y tarifas»</a>.'),
      ("Etapa 4. Ciudadanía",
       'Según la Constitución de Paraguay (art. 148), la naturalización es posible recién a partir de los 3 años de «radicación» (residencia con estatus) — y este plazo se cuenta desde la fecha de obtención de la Residencia Permanente, no desde el ingreso al país. El trámite de naturalización lo lleva la Corte Suprema (<a href="{terminologiya}#corte-suprema">Corte Suprema de Justicia</a>), no la DNM; el procedimiento requiere comparecencia personal del solicitante y el acompañamiento de un abogado.'),
    ],
    fact_num="5 años", fact_cap="mínimo teórico (2 años de Temporal + 3 años de espera tras la Permanente) — la suma formal de los plazos de cada etapa, sin contar el tiempo real de reunir documentos y tramitar el caso.",
    p_after='En la práctica, considerando el tiempo real para reunir documentos, tramitar el caso y su paso por la Corte Suprema, el director de la DNM, Jorge Cronovetter, dio a conocer en mayo de 2026 una cifra más honesta — <strong>7 a 8 años</strong> desde la mudanza hasta el pasaporte (ABC Color, 04.05.2026). Este es el plazo con el que conviene planificar la mudanza, y no las promesas publicitarias de «ciudadanía en un año» — más sobre de dónde salen esas promesas y por qué no creerles, en la página <a href="{riski}">«Riesgos y dificultades»</a>.',
    callout_label="Nota metodológica",
    callout='No existen normas oficiales fijadas sobre los plazos de tramitación de la solicitud ante la DNM (cuántas semanas o meses exactos toma emitir la Temporal o la Cédula paraguaya (<a href="{terminologiya}#cedula">Cédula</a>) tras presentar el paquete completo) en fuentes abiertas al momento de preparar este texto — es una práctica administrativa interna que puede cambiar. Seguimos el estado de cada caso de forma individual e informamos al cliente los plazos vigentes a medida que avanza, en lugar de dar una cifra promedio imposible de verificar.',
),
"en": dict(
    title="Paraguay residency & citizenship timelines: an honest timeline | Grund Paraguay",
    description="The real timeline for moving to Paraguay: temporary and permanent residency, the filing window, and the honest timeline to citizenship — 7 to 8 years, not one year.",
    h1="Process & real timelines: from moving to Paraguayan citizenship",
    lead='The real sequence of stages toward permanent status in Paraguay, with no shortcuts and no promises of "we\'ll handle it in a week." Details on what each stage involves are on the <a href="{uslugi}">"Services"</a> page.',
    steps=[
      ("Stage 1. Temporary residency (Residencia Temporal)",
       'Processed under Ley N° 6984/22 "De Migraciones" (Art. 46) and valid for up to 2 years. If needed, it can be renewed for the same period. Status is lost after an absence from the country of more than 1 year. Already at this stage, once you get residency, you must register a <a href="{terminologiya}#ruc">RUC</a> and file tax returns regularly (usually monthly) — this is a separate support service (see the <a href="{uslugi}">"Services"</a> page), not a formality you can put off.'),
      ("Stage 2. Window to apply for permanent residency",
       'The standard application for Residencia Permanente is filed within 90 days before Residencia Temporal expires — meaning the transition isn\'t automatic and requires a specific action within a specific window. The exception is the investor route via <a href="{terminologiya}#suace">SUACE</a> (see "Services"): with investments from 70,000 USD, permanent residency is available directly, without going through Temporal.'),
      ("Stage 3. Permanent residency (Residencia Permanente)",
       'Issued for 10 years and also renewable; lost after an absence from the country of more than 3 consecutive years. Since July 6, 2026, Permanente applications are reviewed under the new <a href="{terminologiya}#dnm">DNM</a> resolution N° 407/2026 — it introduces 12 applicant categories (professionals, employees, freelancers and digital nomads, merchants, service providers, property owners, business shareholders, farmers, clergy, retirees, dependents, students) with separate financial-capacity requirements for each. The exact thresholds per category haven\'t been officially published yet — we confirm them individually for your situation at the time of filing; current rates are on the <a href="{stoimost}">"Pricing"</a> page.'),
      ("Stage 4. Citizenship",
       'Under Paraguay\'s Constitution (Art. 148), naturalization is only possible after 3 years of "radicación" (residency with status) — and this period is counted from the date you received Residencia Permanente, not from the date you entered the country. The naturalization case is handled by the Supreme Court (<a href="{terminologiya}#corte-suprema">Corte Suprema de Justicia</a>), not the migration service; the procedure requires the applicant to appear in person with legal representation.'),
    ],
    fact_num="5 years", fact_cap="the theoretical minimum (2 years of Temporal + 3 years of waiting after Permanente) — the formal sum of stage timelines, not counting the real time needed to gather documents and process the case.",
    p_after='In practice, accounting for the real time it takes to gather documents, process the case, and get it through the Supreme Court, DNM director Jorge Cronovetter publicly gave a more honest figure in May 2026 — <strong>7 to 8 years</strong> from moving to holding a passport (ABC Color, 05/04/2026). That\'s the timeline worth planning around — not the marketing promises of "citizenship in a year." More on where those promises come from and why not to trust them is on the <a href="{riski}">"Risks & Difficulties"</a> page.',
    callout_label="Methodological note",
    callout='There are no officially fixed standards for how long the DNM takes to process an application itself (exactly how many weeks or months it takes to issue Temporal status or a Paraguayan <a href="{terminologiya}#cedula">Cédula</a> after filing the full package) in open sources as of this writing — it\'s internal administrative practice that can change. We track each case individually and tell clients the current timeline as it progresses, rather than giving an average figure that can\'t be verified.',
),
"de": dict(
    title="Fristen für Aufenthalt und Staatsbürgerschaft in Paraguay: ehrliche Zeitachse | Grund Paraguay",
    description="Die reale Zeitachse für den Umzug nach Paraguay: befristeter und unbefristeter Aufenthalt, das Antragsfenster und die ehrliche Frist bis zur Staatsbürgerschaft — 7 bis 8 Jahre, nicht ein Jahr.",
    h1="Prozess und reale Fristen: vom Umzug bis zur paraguayischen Staatsbürgerschaft",
    lead='Die reale Abfolge der Etappen auf dem Weg zum unbefristeten Status in Paraguay, ohne Abkürzungen und ohne Versprechen von „wir erledigen das in einer Woche\". Details zu jeder Etappe finden Sie auf der Seite <a href="{uslugi}">„Leistungen"</a>.',
    steps=[
      ("Etappe 1. Befristeter Aufenthalt (Residencia Temporal)",
       'Wird gemäß Ley N° 6984/22 „De Migraciones" (Art. 46) bearbeitet und gilt bis zu 2 Jahre. Bei Bedarf kann der Aufenthalt um denselben Zeitraum verlängert werden. Der Status erlischt bei einer Abwesenheit vom Land von mehr als 1 Jahr. Bereits in dieser Etappe entsteht nach Erhalt des Aufenthaltstitels die Pflicht, eine <a href="{terminologiya}#ruc">RUC</a> zu registrieren und regelmäßig (in der Regel monatlich) Steuererklärungen einzureichen — das ist eine eigenständige Begleitleistung (siehe Seite <a href="{uslugi}">„Leistungen"</a>), keine Formalität, die man aufschieben kann.'),
      ("Etappe 2. Antragsfenster für den unbefristeten Aufenthalt",
       'Der Antrag auf Residencia Permanente wird auf dem Standardweg innerhalb von 90 Tagen vor Ablauf der Residencia Temporal gestellt — das heißt, der Übergang erfolgt nicht automatisch und erfordert eine gesonderte Handlung innerhalb eines konkreten Zeitfensters. Ausnahme ist der Investorenweg über <a href="{terminologiya}#suace">SUACE</a> (siehe „Leistungen"): Bei Investitionen ab 70.000 USD ist der unbefristete Aufenthalt direkt verfügbar, ohne den Weg über Temporal.'),
      ("Etappe 3. Unbefristeter Aufenthalt (Residencia Permanente)",
       'Wird für 10 Jahre erteilt und ist ebenfalls verlängerbar; erlischt bei einer Abwesenheit vom Land von mehr als 3 aufeinanderfolgenden Jahren. Seit dem 6. Juli 2026 werden Permanente-Anträge nach der neuen Resolution der Migrationsbehörde (<a href="{terminologiya}#dnm">DNM</a>) N° 407/2026 geprüft — sie führt 12 Antragstellerkategorien ein (Fachkräfte, Angestellte, Freiberufler und digitale Nomaden, Kaufleute, Dienstleister, Immobilieneigentümer, Unternehmensaktionäre, Landwirte, Geistliche, Rentner, Angehörige, Studenten) mit jeweils eigenen Anforderungen zum Nachweis der Zahlungsfähigkeit. Die genauen Schwellenwerte je Kategorie sind offiziell noch nicht öffentlich veröffentlicht — wir klären sie individuell zum Zeitpunkt der Antragstellung für Ihre Situation; aktuelle Gebühren auf der Seite <a href="{stoimost}">„Preise"</a>.'),
      ("Etappe 4. Staatsbürgerschaft",
       'Gemäß der paraguayischen Verfassung (Art. 148) ist die Einbürgerung frühestens 3 Jahre nach „radicación" (Aufenthalt mit Status) möglich — und diese Frist wird ab dem Datum des Erhalts der Residencia Permanente gezählt, nicht ab der Einreise ins Land. Das Einbürgerungsverfahren führt nicht die Migrationsbehörde, sondern der Oberste Gerichtshof (<a href="{terminologiya}#corte-suprema">Corte Suprema de Justicia</a>); das Verfahren erfordert das persönliche Erscheinen des Antragstellers und anwaltliche Begleitung.'),
    ],
    fact_num="5 Jahre", fact_cap="das theoretische Minimum (2 Jahre Temporal + 3 Jahre Wartezeit nach Permanente) — die formale Summe der Etappenfristen, ohne die reale Zeit für das Sammeln von Dokumenten und die Fallbearbeitung.",
    p_after='In der Praxis, unter Berücksichtigung der realen Zeit für das Sammeln von Dokumenten, die Fallbearbeitung und den Durchlauf durch den Obersten Gerichtshof, nannte DNM-Direktor Jorge Cronovetter im Mai 2026 öffentlich eine ehrlichere Zahl — <strong>7 bis 8 Jahre</strong> vom Umzug bis zum Pass (ABC Color, 04.05.2026). Das ist die Frist, mit der man bei der Umzugsplanung rechnen sollte — nicht die Werbeversprechen von „Staatsbürgerschaft in einem Jahr\". Mehr dazu, woher solche Versprechen kommen und warum man ihnen nicht trauen sollte, auf der Seite <a href="{riski}">„Risiken und Schwierigkeiten"</a>.',
    callout_label="Methodischer Hinweis",
    callout='Es gibt keine offiziell festgelegten Normen für die Bearbeitungsdauer des DNM-Antrags selbst (wie viele Wochen oder Monate genau die Ausstellung der Temporal oder der paraguayischen <a href="{terminologiya}#cedula">Cédula</a> nach Einreichung des vollständigen Pakets dauert) in offenen Quellen zum Zeitpunkt der Erstellung dieses Textes — das ist interne Verwaltungspraxis, die sich ändern kann. Wir verfolgen den Status jedes Falls individuell und teilen dem Mandanten die aktuellen Fristen mit, während sich der Fall entwickelt, statt eine Durchschnittszahl anzugeben, die sich nicht überprüfen lässt.',
),
}

for lang, t in PROCESS.items():
    l = L(lang)
    honest_icon, honest_color, honest_top, honest_bottom, honest_aria = HONEST_SEAL[lang]
    steps_html = ""
    for i, (title, text) in enumerate(t["steps"]):
        doc_pid = TIMELINE_DOC_PIDS[i] if i < len(TIMELINE_DOC_PIDS) else None
        doc_link = (f'<a class="timeline-doc-link" href="{l[doc_pid]}">{icon("stamp","timeline-doc-link-icon")}{TIMELINE_DOC_LABEL[lang]}</a>'
                    if doc_pid else "")
        steps_html += f'<li><h3>{title}</h3><p>{text.format(**l)}</p>{doc_link}</li>\n'
    process_body = f'''
{breadcrumbs([(NAV_LABELS[lang]["home"], l['home']), (NAV_LABELS[lang]["kak-my-rabotaem"], l['kak-my-rabotaem']), (NAV_LABELS[lang]["protsess"], None)])}
<section class="hero" style="padding-top:24px;">
  <div class="wrap">
    <h1>{t["h1"]}</h1>
    <p class="lead">{t["lead"].format(**l)}</p>
  </div>
</section>
<section style="padding-top:0;">
  <div class="prose">
    <ol class="timeline">
      {steps_html}
    </ol>

    <div class="key-fact">
      <span class="num">{t["fact_num"]}</span>
      <span class="cap">{t["fact_cap"]}</span>
    </div>

    <div class="seal seal-float">{seal_svg(honest_icon, honest_top, honest_bottom, "seal-"+honest_color, honest_aria, uid=f"protsess-{lang}")}</div>
    <p>{t["p_after"].format(**l)}</p>

    <div class="callout">
      <span class="callout-label">{t["callout_label"]}</span>
      {t["callout"].format(**l)}
    </div>
  </div>
</section>
'''
    page("protsess", lang, t["title"], t["description"], process_body,
         extra_schema=schema_breadcrumb([(NAV_LABELS[lang]["home"], f"/{lang}/"), (NAV_LABELS[lang]["kak-my-rabotaem"], f"/{lang}/{href_to('kak-my-rabotaem', lang)}"), (NAV_LABELS[lang]["protsess"], f"/{lang}/{href_to('protsess', lang)}")]))

# =========================================================== РИСКИ / RISKS

border_map_svg = lambda cap_lines: f'''
<svg viewBox="0 0 640 360" width="100%" height="auto" role="img" aria-labelledby="mapTitle mapDesc">
  <title id="mapTitle">{cap_lines[0]}</title>
  <desc id="mapDesc">{cap_lines[1]}</desc>
  <rect x="40" y="30" width="560" height="300" rx="18" fill="none" stroke="#2C5480" stroke-width="1.5" class="grid-line" stroke-dasharray="3 5"/>
  <path d="M90,300 C80,220 110,140 170,90 C220,55 300,45 360,55 C430,65 480,60 520,90 C555,115 560,170 545,220 C520,270 460,300 400,305 C320,312 180,310 90,300 Z"
        fill="none" stroke="#E8F1FB" stroke-width="2"/>
  <text x="320" y="345" text-anchor="middle" class="dim" font-size="12">{cap_lines[2]}</text>

  <circle cx="470" cy="95" r="6" class="accent"/><text x="484" y="99" font-size="13">Amambay</text>
  <circle cx="505" cy="140" r="6" class="accent"/><text x="519" y="144" font-size="13">Canindeyú</text>
  <circle cx="440" cy="70" r="6" class="accent"/><text x="454" y="55" font-size="13">Concepción</text>
  <circle cx="470" cy="180" r="6" class="accent"/><text x="484" y="184" font-size="13">Alto Paraná</text>
  <circle cx="390" cy="120" r="6" class="accent"/><text x="404" y="124" font-size="13">San Pedro</text>

  <text x="120" y="270" font-size="12" class="dim">{cap_lines[3]}</text>
  <text x="120" y="286" font-size="12" class="dim">{cap_lines[4]}</text>
</svg>
'''

RISKS = {
"ru": dict(
    title="Риски и трудности переезда в Парагвай: честный разбор | Grund Paraguay",
    description="Мошенничество, денге, безопасность и регуляторные изменения 2026 года в Парагвае — честно, без запугивания и без замалчивания трудностей первого года.",
    h1="Честно о рисках и трудностях переезда в Парагвай",
    lead='Эта страница — не запугивание, а управление ожиданиями: то, что должно быть частью услуги с самого начала, а не выясняться постфактум. Если вы уже читали страницу <a href="{protsess}">«Процесс и сроки»</a> — здесь то же отношение к честности, только применительно к рискам, а не срокам.',
    h2_fraud="Мошенничество на рынке релокации",
    p_fraud1='Рынок посреднических услуг по переезду в Латинскую Америку в целом репутационно токсичен, и Парагвай не исключение. При этом нам не удалось найти опубликованное официальное предупреждение миграционной службы Парагвая (<a href="{terminologiya}#dnm">DNM</a>), прямо адресованное мошенническим агентам-посредникам, — по образцу похожих публичных предупреждений миграционных служб некоторых других стран региона. Это не значит, что такого предупреждения не существует: часть официальных ресурсов DNM была недоступна на момент сбора информации, и мы не смогли подтвердить его текст и дату напрямую.',
    callout1_label="Единичный случай, не статистика",
    callout1="Отдельно зафиксирован случай, когда DNM обнаружила поддельные документы у заявителя и приняла решение о его выдворении, — но это пример мошенничества со стороны самого заявителя, а не агентства-посредника против клиента; подробности этого случая тоже не подтверждены первичным источником, поэтому мы упоминаем его как единичный прецедент, а не статистику.",
    p_fraud2='Практический вывод для вас: любое предложение «ускорить» или «обойти» процесс нестандартным способом стоит проверять отдельно, а не принимать на веру только потому, что о нём рассказали в чате — наши договор и фиксированные условия описаны на странице <a href="{o-kompanii}">«О компании»</a>.',
    h2_health="Здоровье и климат",
    p_health1='Денге — реальный сезонный риск, а не редкость. За весь 2025 год в Парагвае зафиксировано 31 656 случаев с подозрением на денге, из них 1374 подтверждённых лабораторно и 1 летальный исход (451 случай на 100 000 населения); в первых четырёх неделях 2026 года — уже 2412 случаев с восходящим трендом (источник: <a href="{terminologiya}#paho">PAHO</a>, отчёт от 18.02.2026). При этом более свежий отчёт Минздрава Парагвая на 9 января 2026 года описывал картину как «стабильную при низкой вирусной циркуляции» — всего 3 подтверждённых случая за 3 недели при около 465 подозрительных обращениях в неделю по стране. Оба отчёта не противоречат друг другу: они относятся к разным периодам и разным уровням подтверждения диагноза, и оба говорят об одном — риск сезонный и требует стандартных мер профилактики, а не паники.',
    p_health2='Официальный портал Великобритании для путешественников (GOV.UK) прямо называет денге и чикунгунью актуальными рисками для въезжающих в Парагвай и отдельно отмечает: качественная частная медицинская помощь доступна в основном в крупных городах, частные клиники обычно требуют немедленной оплаты на месте, и настоятельно рекомендуется медицинская страховка с покрытием экстренной эвакуации. Это стоит учитывать при планировании бюджета на первый год — подробный разбор расходов на странице <a href="{stoimost}">«Стоимость и тарифы»</a>.',
    callout2_label="Требует проверки",
    callout2='По отдельным данным (актуальность которых на 2026 год не переподтверждена в этом заходе — цифры относятся к 2022 году), при въезде в Парагвай из Боливии, Бразилии, Перу или Венесуэлы может требоваться сертификат о вакцинации от жёлтой лихорадки для лиц от 1 до 59 лет — этот пункт стоит уточнять отдельно перед поездкой, если маршрут проходит через одну из этих стран.',
    p_health3='Отдельный практический момент: доступ к государственному медицинскому страхованию (<a href="{terminologiya}#ips">IPS</a>) в Парагвае связан с формальной занятостью и статусом постоянного резидента; у временных резидентов автоматического доступа к нему нет — то есть частная страховка на первые годы почти всегда нужна независимо от статуса резиденции.',
    h2_safety="Безопасность",
    p_safety1='По официальной статистике, 2025 год закрылся с показателем 391 убийство по стране (6,1 на 100 000 населения) — снижение на 18,6% к 2024 году (477 случаев, 7,5 на 100 000); это третий по величине показатель безопасности в Латинской Америке после Аргентины и Чили (источники: InSight Crime, La Nación, июнь 2026). Структура Госдепартамента США по безопасности зарубежных представительств (<a href="{terminologiya}#osac">OSAC</a>) в отчёте от 27.05.2025 оценивала уровень угрозы для Асунсьона как высокий по общеуголовной преступности, средний — по политическому насилию и низкий — по терроризму; заказные убийства снизились со 110 случаев в 2019 году до 18 в 2024-м, а похищения иностранцев крайне редки (по данным этого источника, ни одного случая с гражданами США с 2011 года), хотя растёт число «виртуальных похищений» — телефонного мошенничества с имитацией похищения.',
    p_safety2_before="Официальный уровень предупреждений о поездках Госдепартамента США по Парагваю в целом — базовый («обычные меры предосторожности»), но для пяти северо-восточных департаментов на границе с Бразилией действует повышенный уровень осторожности из-за контрабанды и ограниченного присутствия полиции:",
    map_caption="Схема условная (не картографическая точность) — по данным Госдепартамента США, страница с этой оценкой датирована 30.04.2025, то есть на момент подготовки текста ей больше года; стоит перепроверить на актуальность перед публикацией.",
    map_svg_title="Схема: департаменты у границы с Бразилией",
    map_svg_desc="Не географическая карта — условная схема расположения пяти департаментов, для которых источники отмечают повышенный уровень осторожности.",
    map_svg_note="Условная схема территории Парагвая — не топографическая карта",
    map_svg_center1="Асунсьон и центр страны —", map_svg_center2="базовый уровень осторожности",
    callout3_label="Требует проверки",
    callout3="В приграничном регионе Сьюдад-дель-Эсте / Альто-Парана отмечается присутствие бразильских преступных группировок и местных кланов, а в департаменте Амамбай уровень убийств оценивается как заметно выше среднего по стране — точные актуальные цифры по этим двум пунктам в источниках устарели (данные частично относятся к 2019 и 2022 годам) и требуют отдельной проверки перед использованием в конкретных консультациях.",
    p_safety3="По международному индексу организованной преступности (Organized Crime Index), Парагвай — крупный транзитный узел кокаина и крупнейший производитель каннабиса в Южной Америке, с индексом криминальности 7,48 из 10 (4-е место в мире) при низкой устойчивости системы к преступности. По индексу восприятия коррупции Transparency International за 2025 год у Парагвая 24 балла из 100 (150-е место в мире) — ниже среднего по Америке (42/100), без изменений к 2024 году.",
    p_safety4="Ни один из этих показателей не означает, что переезд в Парагвай рискованнее, чем в среднем по региону, — большинство статистики указывает на обратное. Но приграничные департаменты и общая осторожность с личными данными в поездках — реальные, а не гипотетические факторы, которые стоит знать заранее.",
    h2_reg="Регуляторное окно",
    p_reg='С 6 июля 2026 года вступила в силу резолюция <a href="{terminologiya}#dnm">DNM</a> N° 407/2026 — более строгая проверка платёжеспособности по 12 категориям заявителей на Residencia Permanente. С 1 июля 2026 года также действуют новые государственные пошлины DNM (Decreto 6225/2026 и Resolución DNM N° 478/2026); эти пошлины ежегодно индексируются вместе с минимальным размером оплаты труда — то есть это не разовое повышение, а регулярно обновляемая величина, которую нужно проверять заново каждый год к 1 июля (актуальные суммы — на странице <a href="{stoimost}">«Стоимость и тарифы»</a>). Как индикатор общего направления политики: с 10 января 2026 года ужесточён въезд для граждан Венесуэлы (Decreto N° 5278/2026) — прямого отношения к гражданам России это решение не имеет, но показывает, что миграционная политика Парагвая в течение 2026 года в целом двигается в сторону более строгого контроля, а не либерализации. Это не повод для паники, но обоснованная причина не откладывать решение на неопределённый срок, если переезд уже рассматривается всерьёз — примеры того, как это выглядело для конкретных клиентов, в разделе <a href="{keisy}">«Кейсы и отзывы»</a>.',
),
"es": dict(
    title="Riesgos y dificultades de mudarse a Paraguay: un análisis honesto | Grund Paraguay",
    description="Fraude, dengue, seguridad y cambios regulatorios de 2026 en Paraguay — con honestidad, sin alarmismo y sin ocultar las dificultades del primer año.",
    h1="Honestamente sobre los riesgos y dificultades de mudarse a Paraguay",
    lead='Esta página no busca alarmar, sino gestionar expectativas: algo que debería ser parte del servicio desde el principio, no descubrirse después. Si ya leyó la página <a href="{protsess}">«Proceso y plazos»</a>, aquí aplicamos la misma honestidad, pero a los riesgos en lugar de los plazos.',
    h2_fraud="Fraude en el mercado de reubicación",
    p_fraud1='El mercado de servicios de intermediación para mudarse a América Latina tiene, en general, mala reputación, y Paraguay no es la excepción. No obstante, no logramos encontrar una advertencia oficial publicada por la Dirección Nacional de Migraciones (<a href="{terminologiya}#dnm">DNM</a>) dirigida directamente a agentes intermediarios fraudulentos, del tipo de advertencias públicas similares de otros servicios migratorios de la región. Esto no significa que no exista: parte de los recursos oficiales de la DNM no estaban disponibles al momento de recopilar esta información, y no pudimos confirmar directamente su texto ni su fecha.',
    callout1_label="Caso aislado, no estadística",
    callout1="Se registró por separado un caso en el que la DNM detectó documentos falsos de un solicitante y decidió su expulsión — pero es un ejemplo de fraude por parte del propio solicitante, no de una agencia intermediaria contra un cliente; los detalles de este caso tampoco están confirmados por una fuente primaria, por lo que lo mencionamos como un precedente aislado, no como estadística.",
    p_fraud2='Conclusión práctica: cualquier oferta de «acelerar» o «saltarse» el proceso por vías no estándar conviene verificarla por separado, no aceptarla solo porque se la contaron en un chat — nuestro contrato y condiciones fijas están descritos en la página <a href="{o-kompanii}">«Sobre nosotros»</a>.',
    h2_health="Salud y clima",
    p_health1='El dengue es un riesgo estacional real, no una rareza. En todo 2025 se registraron en Paraguay 31.656 casos sospechosos de dengue, de los cuales 1.374 fueron confirmados por laboratorio y hubo 1 fallecimiento (451 casos por cada 100.000 habitantes); en las primeras cuatro semanas de 2026 ya había 2.412 casos con tendencia al alza (fuente: <a href="{terminologiya}#paho">PAHO</a>, informe del 18.02.2026). Al mismo tiempo, un informe más reciente del Ministerio de Salud de Paraguay del 9 de enero de 2026 describía la situación como «estable, con baja circulación viral» — solo 3 casos confirmados en 3 semanas, con unas 465 consultas sospechosas semanales en todo el país. Ambos informes no se contradicen: corresponden a periodos distintos y a distintos niveles de confirmación diagnóstica, y ambos dicen lo mismo: el riesgo es estacional y requiere medidas de prevención estándar, no pánico.',
    p_health2='El portal oficial de Reino Unido para viajeros (GOV.UK) señala directamente el dengue y el chikungunya como riesgos vigentes al ingresar a Paraguay, y aclara además: la atención médica privada de calidad está disponible sobre todo en las grandes ciudades, las clínicas privadas suelen exigir el pago inmediato en el lugar, y se recomienda encarecidamente un seguro médico con cobertura de evacuación de emergencia. Vale la pena tenerlo en cuenta al planificar el presupuesto del primer año — un desglose detallado de gastos está en la página <a href="{stoimost}">«Costos y tarifas»</a>.',
    callout2_label="Requiere verificación",
    callout2='Según algunos datos (cuya vigencia en 2026 no fue reconfirmada en esta revisión — las cifras corresponden a 2022), al ingresar a Paraguay desde Bolivia, Brasil, Perú o Venezuela puede exigirse un certificado de vacunación contra la fiebre amarilla para personas de 1 a 59 años — conviene confirmar este punto por separado antes del viaje si la ruta pasa por alguno de esos países.',
    p_health3='Un aspecto práctico aparte: el acceso al seguro médico estatal (<a href="{terminologiya}#ips">IPS</a>) en Paraguay está vinculado al empleo formal y al estatus de residente permanente; los residentes temporales no tienen acceso automático — es decir, casi siempre hace falta un seguro privado durante los primeros años, sin importar el estatus de residencia.',
    h2_safety="Seguridad",
    p_safety1='Según estadísticas oficiales, el año 2025 cerró con 391 homicidios en todo el país (6,1 por cada 100.000 habitantes) — una baja del 18,6% respecto de 2024 (477 casos, 7,5 por cada 100.000); es el tercer indicador de seguridad más alto de América Latina, después de Argentina y Chile (fuentes: InSight Crime, La Nación, junio de 2026). El Consejo Asesor de Seguridad en el Extranjero del Departamento de Estado de EE. UU. (<a href="{terminologiya}#osac">OSAC</a>), en un informe del 27.05.2025, calificó el nivel de amenaza para Asunción como alto en delincuencia común, medio en violencia política y bajo en terrorismo; los asesinatos por encargo bajaron de 110 casos en 2019 a 18 en 2024, y los secuestros de extranjeros son muy poco frecuentes (según esta fuente, ningún caso con ciudadanos de EE. UU. desde 2011), aunque crecen los «secuestros virtuales» — estafas telefónicas que simulan un secuestro.',
    p_safety2_before="El nivel oficial de advertencias de viaje del Departamento de Estado de EE. UU. para Paraguay en general es básico («precauciones normales»), pero para cinco departamentos del noreste en la frontera con Brasil rige un nivel de precaución más alto por contrabando y presencia policial limitada:",
    map_caption="Esquema orientativo (sin precisión cartográfica) — según el Departamento de Estado de EE. UU.; la página con esta evaluación está fechada el 30.04.2025, es decir, tiene más de un año al momento de preparar este texto y conviene reverificar su vigencia antes de publicar.",
    map_svg_title="Esquema: departamentos junto a la frontera con Brasil",
    map_svg_desc="No es un mapa geográfico — es un esquema orientativo de la ubicación de cinco departamentos para los que las fuentes señalan un nivel de precaución más alto.",
    map_svg_note="Esquema orientativo del territorio de Paraguay — no es un mapa topográfico",
    map_svg_center1="Asunción y el centro del país —", map_svg_center2="nivel de precaución básico",
    callout3_label="Requiere verificación",
    callout3="En la región fronteriza de Ciudad del Este / Alto Paraná se señala la presencia de bandas criminales brasileñas y clanes locales, y en el departamento de Amambay la tasa de homicidios se estima notablemente superior al promedio nacional — las cifras exactas y actuales de estos dos puntos están desactualizadas en las fuentes (los datos corresponden en parte a 2019 y 2022) y requieren verificación aparte antes de usarlas en consultas concretas.",
    p_safety3="Según el Índice Global de Crimen Organizado, Paraguay es un gran nodo de tránsito de cocaína y el mayor productor de cannabis de Sudamérica, con un índice de criminalidad de 7,48 sobre 10 (4.º lugar en el mundo) y baja resiliencia del sistema frente al crimen. Según el Índice de Percepción de la Corrupción de Transparency International de 2025, Paraguay tiene 24 puntos sobre 100 (puesto 150 en el mundo) — por debajo del promedio de América (42/100), sin cambios respecto de 2024.",
    p_safety4="Ninguno de estos indicadores significa que mudarse a Paraguay sea más riesgoso que el promedio regional — la mayoría de las estadísticas apunta a lo contrario. Pero los departamentos fronterizos y el cuidado general con los datos personales al viajar son factores reales, no hipotéticos, que conviene conocer de antemano.",
    h2_reg="Ventana regulatoria",
    p_reg='El 6 de julio de 2026 entró en vigencia la resolución de la <a href="{terminologiya}#dnm">DNM</a> N.° 407/2026 — un control más estricto de solvencia para las 12 categorías de solicitantes de Residencia Permanente. Desde el 1 de julio de 2026 también rigen nuevas tasas estatales de la DNM (Decreto 6225/2026 y Resolución DNM N.° 478/2026); estas tasas se actualizan anualmente junto con el salario mínimo — es decir, no es un aumento puntual, sino un valor que se actualiza cada año y debe verificarse de nuevo cada 1 de julio (montos actuales en la página <a href="{stoimost}">«Costos y tarifas»</a>). Como indicador de la dirección general de la política: desde el 10 de enero de 2026 se endureció el ingreso para ciudadanos venezolanos (Decreto N.° 5278/2026) — esta decisión no tiene relación directa con los ciudadanos rusos, pero muestra que la política migratoria de Paraguay durante 2026 se mueve en general hacia un control más estricto, no hacia la liberalización. No es motivo de pánico, pero sí una razón fundada para no postergar la decisión indefinidamente si la mudanza ya se está considerando en serio — ejemplos de cómo fue esto para clientes concretos, en la sección <a href="{keisy}">«Casos y testimonios»</a>.',
),
"en": dict(
    title="Risks and difficulties of moving to Paraguay: an honest look | Grund Paraguay",
    description="Fraud, dengue, safety, and 2026 regulatory changes in Paraguay — honestly, without scaremongering and without hiding first-year difficulties.",
    h1="Honestly: risks and difficulties of moving to Paraguay",
    lead='This page isn\'t meant to scare you — it\'s meant to manage expectations: something that should be part of the service from the start, not something you find out later. If you\'ve already read the <a href="{protsess}">"Process & Timeline"</a> page, this is the same commitment to honesty, applied to risks instead of timelines.',
    h2_fraud="Fraud in the relocation market",
    p_fraud1='The market for relocation intermediary services to Latin America has a generally toxic reputation, and Paraguay is no exception. That said, we couldn\'t find a published official warning from the migration service (<a href="{terminologiya}#dnm">DNM</a>) specifically addressing fraudulent intermediary agents, of the kind other migration services in the region have issued. That doesn\'t mean one doesn\'t exist: part of the DNM\'s official resources were unavailable when we gathered this information, and we couldn\'t confirm its text or date directly.',
    callout1_label="An isolated case, not a statistic",
    callout1="Separately, there's a documented case where the DNM found forged documents from an applicant and decided to deport them — but that's an example of fraud by the applicant themselves, not an agency defrauding a client; the details of this case also aren't confirmed by a primary source, so we mention it as an isolated precedent, not a statistic.",
    p_fraud2='The practical takeaway: any offer to "speed up" or "get around" the process through non-standard means is worth checking independently, not taking on faith just because someone mentioned it in a chat — our contract and fixed terms are described on the <a href="{o-kompanii}">"About Us"</a> page.',
    h2_health="Health and climate",
    p_health1='Dengue is a real seasonal risk, not a rarity. Throughout 2025, Paraguay recorded 31,656 suspected dengue cases, of which 1,374 were lab-confirmed and 1 was fatal (451 cases per 100,000 population); in the first four weeks of 2026 alone, there were already 2,412 cases with an upward trend (source: <a href="{terminologiya}#paho">PAHO</a>, report dated 02/18/2026). Meanwhile, a more recent Paraguayan Ministry of Health report from January 9, 2026 described the picture as "stable, with low viral circulation" — just 3 confirmed cases over 3 weeks, with about 465 suspected cases reported per week nationwide. The two reports don\'t contradict each other: they cover different periods and different levels of diagnostic confirmation, and both say the same thing — the risk is seasonal and calls for standard prevention, not panic.',
    p_health2="The UK's official travel portal (GOV.UK) directly names dengue and chikungunya as current risks for those entering Paraguay, and separately notes: good-quality private medical care is mainly available in major cities, private clinics usually require immediate payment on the spot, and medical insurance with emergency evacuation coverage is strongly recommended. Worth factoring into your first-year budget planning — a detailed cost breakdown is on the <a href=\"{stoimost}\">\"Pricing\"</a> page.",
    callout2_label="Needs verification",
    callout2='According to some data (whose currency for 2026 wasn\'t re-confirmed in this pass — the figures date to 2022), entering Paraguay from Bolivia, Brazil, Peru, or Venezuela may require a yellow fever vaccination certificate for people aged 1–59 — worth confirming separately before travel if your route passes through one of those countries.',
    p_health3='One practical point: access to state health insurance (<a href="{terminologiya}#ips">IPS</a>) in Paraguay is tied to formal employment and permanent-resident status; temporary residents don\'t get automatic access — meaning private insurance is almost always needed for the first years, regardless of residency status.',
    h2_safety="Safety",
    p_safety1='Per official statistics, 2025 closed with 391 homicides nationwide (6.1 per 100,000 population) — down 18.6% from 2024 (477 cases, 7.5 per 100,000); the third-best safety figure in Latin America after Argentina and Chile (sources: InSight Crime, La Nación, June 2026). The US State Department\'s Overseas Security Advisory Council (<a href="{terminologiya}#osac">OSAC</a>), in a report dated 05/27/2025, rated the threat level for Asunción as high for street crime, medium for political violence, and low for terrorism; contract killings dropped from 110 cases in 2019 to 18 in 2024, and kidnappings of foreigners are quite rare (per this source, no cases involving US citizens since 2011), though "virtual kidnapping" phone scams are on the rise.',
    p_safety2_before="The US State Department's overall travel advisory level for Paraguay is the baseline level (\"exercise normal precautions\"), but five northeastern departments on the Brazilian border are flagged for heightened caution due to smuggling and limited police presence:",
    map_caption="This is an orientation diagram, not cartographically precise — per the US State Department; the page with this assessment is dated 04/30/2025, meaning it's over a year old as of this writing and worth re-checking for currency before publishing.",
    map_svg_title="Diagram: departments along the Brazilian border",
    map_svg_desc="Not a geographic map — an orientation diagram of the five departments sources flag for heightened caution.",
    map_svg_note="Orientation diagram of Paraguay's territory — not a topographic map",
    map_svg_center1="Asunción and the country's center —", map_svg_center2="baseline caution level",
    callout3_label="Needs verification",
    callout3="In the Ciudad del Este / Alto Paraná border region, sources note the presence of Brazilian criminal groups and local clans, and Amambay department's homicide rate is estimated to be notably above the national average — the exact current figures for these two points are outdated in the sources (data partly from 2019 and 2022) and need separate verification before use in specific consultations.",
    p_safety3="Per the Global Organized Crime Index, Paraguay is a major cocaine transit hub and South America's largest cannabis producer, with a criminality score of 7.48 out of 10 (4th highest worldwide) and low system resilience against crime. Per Transparency International's 2025 Corruption Perceptions Index, Paraguay scores 24 out of 100 (150th worldwide) — below the Americas average of 42/100, unchanged from 2024.",
    p_safety4="None of these figures mean moving to Paraguay is riskier than the regional average — most statistics point the other way. But the border departments and general caution with personal data while traveling are real, not hypothetical, factors worth knowing in advance.",
    h2_reg="Regulatory window",
    p_reg='On July 6, 2026, <a href="{terminologiya}#dnm">DNM</a> resolution N° 407/2026 took effect — stricter financial-capacity checks across 12 applicant categories for Residencia Permanente. Since July 1, 2026, new DNM government fees have also applied (Decreto 6225/2026 and Resolución DNM N° 478/2026); these fees are indexed annually alongside the minimum wage — meaning this isn\'t a one-time hike but a regularly updated figure that needs re-checking every year around July 1 (current amounts are on the <a href="{stoimost}">"Pricing"</a> page). As an indicator of the broader policy direction: since January 10, 2026, entry has been tightened for Venezuelan citizens (Decreto N° 5278/2026) — this decision has no direct bearing on Russian citizens, but it shows that Paraguay\'s immigration policy in 2026 is generally moving toward tighter control, not liberalization. That\'s not a reason to panic, but it is a reasonable argument against putting off the decision indefinitely if a move is already being seriously considered — examples of how this played out for specific clients are in the <a href="{keisy}">"Case Studies"</a> section.',
),
"de": dict(
    title="Risiken und Schwierigkeiten beim Umzug nach Paraguay: ehrliche Betrachtung | Grund Paraguay",
    description="Betrug, Dengue, Sicherheit und regulatorische Änderungen 2026 in Paraguay — ehrlich, ohne Panikmache und ohne die Schwierigkeiten des ersten Jahres zu verschweigen.",
    h1="Ehrlich über Risiken und Schwierigkeiten beim Umzug nach Paraguay",
    lead='Diese Seite soll nicht abschrecken, sondern Erwartungen steuern: etwas, das von Anfang an Teil der Leistung sein sollte, nicht erst im Nachhinein auffallen. Wenn Sie bereits die Seite <a href="{protsess}">„Prozess und Fristen"</a> gelesen haben — hier gilt dieselbe Ehrlichkeit, nur bezogen auf Risiken statt auf Fristen.',
    h2_fraud="Betrug auf dem Umzugsmarkt",
    p_fraud1='Der Markt für Vermittlungsleistungen beim Umzug nach Lateinamerika hat insgesamt einen zweifelhaften Ruf, und Paraguay bildet keine Ausnahme. Dennoch konnten wir keine veröffentlichte offizielle Warnung der Migrationsbehörde (<a href="{terminologiya}#dnm">DNM</a>) finden, die sich direkt an betrügerische Vermittleragenten richtet — nach dem Vorbild ähnlicher öffentlicher Warnungen von Migrationsbehörden anderer Länder der Region. Das bedeutet nicht, dass es eine solche Warnung nicht gibt: Ein Teil der offiziellen DNM-Ressourcen war zum Zeitpunkt der Informationssammlung nicht zugänglich, und wir konnten Text und Datum nicht direkt bestätigen.',
    callout1_label="Einzelfall, keine Statistik",
    callout1="Gesondert dokumentiert ist ein Fall, in dem die DNM gefälschte Dokumente eines Antragstellers entdeckte und dessen Ausweisung beschloss — das ist jedoch ein Beispiel für Betrug seitens des Antragstellers selbst, nicht einer Vermittlungsagentur gegenüber einem Mandanten; auch die Details dieses Falls sind nicht durch eine Primärquelle bestätigt, daher erwähnen wir ihn als Einzelfall, nicht als Statistik.",
    p_fraud2='Praktische Schlussfolgerung: Jedes Angebot, den Prozess auf nicht standardmäßige Weise zu „beschleunigen\" oder zu „umgehen\", sollte separat geprüft werden, statt es nur deshalb zu glauben, weil davon in einem Chat die Rede war — unser Vertrag und unsere Festkonditionen sind auf der Seite <a href="{o-kompanii}">„Über uns"</a> beschrieben.',
    h2_health="Gesundheit und Klima",
    p_health1='Dengue ist ein reales saisonales Risiko, keine Seltenheit. Im gesamten Jahr 2025 wurden in Paraguay 31.656 Verdachtsfälle auf Dengue registriert, davon 1.374 laborbestätigt und 1 Todesfall (451 Fälle pro 100.000 Einwohner); in den ersten vier Wochen 2026 waren es bereits 2.412 Fälle mit steigender Tendenz (Quelle: <a href="{terminologiya}#paho">PAHO</a>, Bericht vom 18.02.2026). Gleichzeitig beschrieb ein aktuellerer Bericht des paraguayischen Gesundheitsministeriums vom 9. Januar 2026 die Lage als „stabil bei geringer Viruszirkulation\" — nur 3 bestätigte Fälle in 3 Wochen bei etwa 465 landesweit gemeldeten Verdachtsfällen pro Woche. Beide Berichte widersprechen sich nicht: Sie beziehen sich auf unterschiedliche Zeiträume und unterschiedliche Bestätigungsgrade der Diagnose, und beide sagen dasselbe — das Risiko ist saisonal und erfordert Standardvorbeugung, keine Panik.',
    p_health2='Das offizielle Reiseportal Großbritanniens (GOV.UK) nennt Dengue und Chikungunya direkt als aktuelle Risiken für die Einreise nach Paraguay und weist gesondert darauf hin: qualitativ hochwertige private medizinische Versorgung ist vor allem in Großstädten verfügbar, private Kliniken verlangen in der Regel sofortige Zahlung vor Ort, und eine Krankenversicherung mit Deckung für Notfallevakuierung wird dringend empfohlen. Das lohnt sich bei der Budgetplanung für das erste Jahr zu berücksichtigen — eine detaillierte Kostenaufstellung finden Sie auf der Seite <a href="{stoimost}">„Preise"</a>.',
    callout2_label="Erfordert Überprüfung",
    callout2='Nach einzelnen Angaben (deren Aktualität für 2026 in diesem Durchgang nicht erneut bestätigt wurde — die Zahlen stammen aus dem Jahr 2022) kann bei der Einreise nach Paraguay aus Bolivien, Brasilien, Peru oder Venezuela ein Gelbfieber-Impfzertifikat für Personen im Alter von 1 bis 59 Jahren erforderlich sein — dieser Punkt sollte vor der Reise gesondert geklärt werden, falls die Route durch eines dieser Länder führt.',
    p_health3='Ein weiterer praktischer Punkt: Der Zugang zur staatlichen Krankenversicherung (<a href="{terminologiya}#ips">IPS</a>) in Paraguay ist an formale Beschäftigung und den Status als unbefristeter Resident gebunden; befristete Residenten haben keinen automatischen Zugang dazu — das heißt, eine private Versicherung ist für die ersten Jahre fast immer erforderlich, unabhängig vom Aufenthaltsstatus.',
    h2_safety="Sicherheit",
    p_safety1='Laut offizieller Statistik schloss das Jahr 2025 mit 391 Tötungsdelikten landesweit (6,1 pro 100.000 Einwohner) — ein Rückgang um 18,6% gegenüber 2024 (477 Fälle, 7,5 pro 100.000); der drittbeste Sicherheitswert in Lateinamerika nach Argentinien und Chile (Quellen: InSight Crime, La Nación, Juni 2026). Der Beirat für Sicherheit im Ausland des US-Außenministeriums (<a href="{terminologiya}#osac">OSAC</a>) bewertete in einem Bericht vom 27.05.2025 die Bedrohungslage für Asunción als hoch bei allgemeiner Kriminalität, mittel bei politischer Gewalt und niedrig bei Terrorismus; Auftragsmorde sanken von 110 Fällen 2019 auf 18 im Jahr 2024, und Entführungen von Ausländern sind äußerst selten (laut dieser Quelle kein Fall mit US-Bürgern seit 2011), wobei „virtuelle Entführungen\" — telefonischer Betrug mit vorgetäuschter Entführung — zunehmen.',
    p_safety2_before="Die offizielle Reisewarnstufe des US-Außenministeriums für Paraguay insgesamt ist die Basisstufe („normale Vorsichtsmaßnahmen\"), aber für fünf nordöstliche Departamentos an der Grenze zu Brasilien gilt aufgrund von Schmuggel und begrenzter Polizeipräsenz eine erhöhte Vorsichtsstufe:",
    map_caption="Schematische Darstellung (keine kartografische Genauigkeit) — laut US-Außenministerium; die Seite mit dieser Einschätzung ist auf den 30.04.2025 datiert, ist zum Zeitpunkt der Texterstellung also über ein Jahr alt und sollte vor der Veröffentlichung auf Aktualität überprüft werden.",
    map_svg_title="Schema: Departamentos an der Grenze zu Brasilien",
    map_svg_desc="Keine geografische Karte — eine schematische Darstellung der Lage der fünf Departamentos, für die Quellen eine erhöhte Vorsichtsstufe angeben.",
    map_svg_note="Schematische Darstellung des Staatsgebiets von Paraguay — keine topografische Karte",
    map_svg_center1="Asunción und das Landeszentrum —", map_svg_center2="Basis-Vorsichtsstufe",
    callout3_label="Erfordert Überprüfung",
    callout3="In der Grenzregion Ciudad del Este / Alto Paraná wird die Präsenz brasilianischer krimineller Gruppen und lokaler Clans festgestellt, und im Departamento Amambay wird die Tötungsrate als deutlich über dem Landesdurchschnitt liegend eingeschätzt — die genauen aktuellen Zahlen zu diesen beiden Punkten sind in den Quellen veraltet (die Daten stammen teilweise aus den Jahren 2019 und 2022) und erfordern eine gesonderte Überprüfung vor der Verwendung in konkreten Beratungen.",
    p_safety3="Laut dem globalen Index für organisierte Kriminalität (Organized Crime Index) ist Paraguay ein bedeutender Transitknoten für Kokain und der größte Cannabisproduzent Südamerikas, mit einem Kriminalitätsindex von 7,48 von 10 (weltweit 4. Platz) bei geringer Widerstandsfähigkeit des Systems gegenüber Kriminalität. Laut dem Korruptionswahrnehmungsindex 2025 von Transparency International erreicht Paraguay 24 von 100 Punkten (weltweit Platz 150) — unter dem amerikanischen Durchschnitt (42/100), unverändert gegenüber 2024.",
    p_safety4="Keiner dieser Werte bedeutet, dass ein Umzug nach Paraguay riskanter ist als der regionale Durchschnitt — die meisten Statistiken zeigen das Gegenteil. Aber die Grenz-Departamentos und die allgemeine Vorsicht mit persönlichen Daten auf Reisen sind reale, keine hypothetischen Faktoren, die man vorab kennen sollte.",
    h2_reg="Regulatorisches Zeitfenster",
    p_reg='Am 6. Juli 2026 trat die Resolution der <a href="{terminologiya}#dnm">DNM</a> N° 407/2026 in Kraft — eine strengere Prüfung der Zahlungsfähigkeit für 12 Antragstellerkategorien bei der Residencia Permanente. Seit dem 1. Juli 2026 gelten außerdem neue staatliche DNM-Gebühren (Decreto 6225/2026 und Resolución DNM N° 478/2026); diese Gebühren werden jährlich zusammen mit dem Mindestlohn indexiert — das heißt, es handelt sich nicht um eine einmalige Erhöhung, sondern um einen regelmäßig aktualisierten Wert, der jedes Jahr zum 1. Juli neu geprüft werden muss (aktuelle Beträge auf der Seite <a href="{stoimost}">„Preise"</a>). Als Indikator für die allgemeine politische Richtung: Seit dem 10. Januar 2026 wurde die Einreise für venezolanische Staatsbürger verschärft (Decreto N° 5278/2026) — diese Entscheidung betrifft russische Staatsbürger nicht direkt, zeigt aber, dass sich Paraguays Einwanderungspolitik im Jahr 2026 insgesamt in Richtung strengerer Kontrolle bewegt, nicht in Richtung Liberalisierung. Das ist kein Grund zur Panik, aber ein begründeter Anlass, die Entscheidung nicht unbegrenzt aufzuschieben, wenn ein Umzug bereits ernsthaft erwogen wird — Beispiele, wie das für konkrete Mandanten aussah, im Abschnitt <a href="{keisy}">„Fallstudien"</a>.',
),
}

for lang, t in RISKS.items():
    l = L(lang)
    map_svg = border_map_svg([t["map_svg_title"], t["map_svg_desc"], t["map_svg_note"], t["map_svg_center1"], t["map_svg_center2"]])
    risks_body = f'''
{breadcrumbs([(NAV_LABELS[lang]["home"], l['home']), (NAV_LABELS[lang]["kak-my-rabotaem"], l['kak-my-rabotaem']), (NAV_LABELS[lang]["riski"], None)])}
<section class="hero" style="padding-top:24px;">
  <div class="wrap">
    <h1>{t["h1"]}</h1>
    <p class="lead">{t["lead"].format(**l)}</p>
  </div>
</section>
<section style="padding-top:0;">
  <div class="prose">
    <h2>{t["h2_fraud"]}</h2>
    <p>{t["p_fraud1"].format(**l)}</p>
    <div class="callout"><span class="callout-label">{t["callout1_label"]}</span>{t["callout1"]}</div>
    <p>{t["p_fraud2"].format(**l)}</p>

    <h2>{t["h2_health"]}</h2>
    <p>{t["p_health1"].format(**l)}</p>
    <p>{t["p_health2"].format(**l)}</p>
    <div class="callout"><span class="callout-label">{t["callout2_label"]}</span>{t["callout2"]}</div>
    <p>{t["p_health3"].format(**l)}</p>

    <h2>{t["h2_safety"]}</h2>
    <p>{t["p_safety1"].format(**l)}</p>
    <p>{t["p_safety2_before"]}</p>

    <div class="diagram">
      {map_svg}
      <p class="diagram-caption">{t["map_caption"]}</p>
    </div>

    <div class="callout"><span class="callout-label">{t["callout3_label"]}</span>{t["callout3"]}</div>
    <p>{t["p_safety3"]}</p>
    <p>{t["p_safety4"]}</p>

    <h2>{t["h2_reg"]}</h2>
    <p>{t["p_reg"].format(**l)}</p>
  </div>
</section>
'''
    page("riski", lang, t["title"], t["description"], risks_body,
         extra_schema=schema_breadcrumb([(NAV_LABELS[lang]["home"], f"/{lang}/"), (NAV_LABELS[lang]["kak-my-rabotaem"], f"/{lang}/{href_to('kak-my-rabotaem', lang)}"), (NAV_LABELS[lang]["riski"], f"/{lang}/{href_to('riski', lang)}")]))
