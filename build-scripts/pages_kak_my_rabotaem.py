#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""«Как мы работаем» — посадочная страница (11.08.2026, вторая правка дня),
объединяющая в меню два уже существующих раздела: «Процесс и сроки» и «Честно о рисках».
Сами страницы protsess/riski не меняются по содержанию — здесь только связка между ними.

Стиль блоков (11.08.2026, третья правка дня — единый стиль для всех hub-страниц): один
столбец без сетки и без иконок, по образцу блоков услуг на странице «Услуги» (тот же класс
.card, тот же ритм), но короче — 2–3 предложения вместо полного абзаца, с обязательной
ссылкой «Подробнее →» в конце (в отличие от «Услуги», где контент самодостаточен и ссылок
дальше нет). Тот же паттерн используется на странице-хабе «Парагвай для переезда».
"""
from build import page, breadcrumbs, schema_breadcrumb, href_to, NAV_LABELS


def L(lang):
    return {pid: href_to(pid, lang) for pid in ["home", "protsess", "riski", "kak-my-rabotaem"]}


HUB = {
"ru": dict(
    title="Как мы работаем: процесс, сроки и риски | Grund Paraguay",
    description="Как устроена работа с Grund Paraguay: пошаговый процесс от заявки до резидентства и честный разбор рисков и трудностей переезда в Парагвай.",
    h1="Как мы работаем",
    lead="Два раздела, которые вместе отвечают на вопрос «чего реально ждать от работы с нами»: пошаговая дорожная карта с честными сроками и прямой разговор о рисках и трудностях, с которыми сталкиваются переезжающие — без нагнетания, но и без замалчивания.",
    card1_title="Процесс и сроки",
    card1_desc="Пошаговая дорожная карта от подачи документов на временную резиденцию до гражданства: что происходит на каждом этапе, сколько это реально занимает и когда открывается окно для следующего шага. Ключевая цифра — 7–8 лет от переезда до паспорта, по словам директора миграционной службы (DNM), а не «один год», как иногда обещают на рынке.",
    card2_title="Честно о рисках",
    card2_desc="Климат и здоровье, приграничные зоны с повышенной криминогенностью, регуляторное окно и мошеннические схемы на рынке переезда — то, что стоит знать заранее, без прикрас и без нагнетания. Это редкая страница такого рода: большинство агентств про трудности переезда просто молчат.",
    more="Подробнее →",
),
"es": dict(
    title="Cómo trabajamos: proceso, plazos y riesgos | Grund Paraguay",
    description="Cómo es trabajar con Grund Paraguay: hoja de ruta paso a paso hacia la residencia y un análisis honesto de los riesgos de mudarse a Paraguay.",
    h1="Cómo trabajamos",
    lead="Dos secciones que juntas responden a la pregunta «qué esperar realmente de trabajar con nosotros»: una hoja de ruta paso a paso con plazos honestos, y una conversación directa sobre los riesgos y dificultades que enfrentan quienes se mudan — sin alarmismo, pero sin ocultar nada.",
    card1_title="Proceso y plazos",
    card1_desc="Hoja de ruta paso a paso desde la presentación de documentos para la residencia temporal hasta la ciudadanía: qué ocurre en cada etapa, cuánto tiempo lleva en realidad y cuándo se abre la ventana para el siguiente paso. La cifra clave es 7–8 años desde la mudanza hasta el pasaporte, según el director de la agencia de migraciones (DNM), no «un año» como a veces se promete en el mercado.",
    card2_title="Riesgos, con honestidad",
    card2_desc="Clima y salud, zonas fronterizas con mayor criminalidad, la ventana regulatoria actual y esquemas fraudulentos del mercado de mudanzas — lo que conviene saber de antemano, sin adornos y sin alarmismo. Es una página poco frecuente en este mercado: la mayoría de las agencias simplemente no habla de las dificultades de mudarse.",
    more="Más →",
),
"en": dict(
    title="How We Work: Process, Timeline & Risks | Grund Paraguay",
    description="How working with Grund Paraguay actually works: a step-by-step roadmap to residency and an honest look at the risks of relocating to Paraguay.",
    h1="How We Work",
    lead="Two sections that together answer the question «what to actually expect from working with us»: a step-by-step roadmap with honest timelines, and a direct conversation about the risks and difficulties people relocating actually face — without alarmism, but without hiding anything either.",
    card1_title="Process & Timeline",
    card1_desc="A step-by-step roadmap from filing documents for temporary residency to citizenship: what happens at each stage, how long it actually takes, and when the window opens for the next step. The key figure is 7–8 years from moving to getting a passport, according to the director of the migration agency (DNM) — not \"one year,\" as sometimes promised on the market.",
    card2_title="Risks, Honestly",
    card2_desc="Climate and health, border areas with higher crime rates, the current regulatory window, and fraud schemes in the relocation market — what's worth knowing in advance, without sugarcoating and without alarmism. It's a rare page of its kind: most agencies simply stay silent about the difficulties of relocating.",
    more="Learn more →",
),
"de": dict(
    title="Wie wir arbeiten: Prozess, Fristen und Risiken | Grund Paraguay",
    description="Wie die Zusammenarbeit mit Grund Paraguay abläuft: ein Schritt-für-Schritt-Fahrplan bis zur Aufenthaltsgenehmigung und eine ehrliche Betrachtung der Risiken eines Umzugs nach Paraguay.",
    h1="Wie wir arbeiten",
    lead="Zwei Bereiche, die gemeinsam die Frage beantworten, was man von der Zusammenarbeit mit uns wirklich erwarten kann: ein Schritt-für-Schritt-Fahrplan mit ehrlichen Fristen und ein direktes Gespräch über die Risiken und Schwierigkeiten, denen Umziehende tatsächlich begegnen — ohne Panikmache, aber auch ohne etwas zu verschweigen.",
    card1_title="Prozess und Fristen",
    card1_desc="Ein Schritt-für-Schritt-Fahrplan von der Antragstellung für die befristete Aufenthaltsgenehmigung bis zur Staatsbürgerschaft: was in jeder Etappe passiert, wie lange es wirklich dauert und wann sich das Zeitfenster für den nächsten Schritt öffnet. Die Schlüsselzahl sind 7–8 Jahre vom Umzug bis zum Reisepass, laut dem Direktor der Migrationsbehörde (DNM) — nicht „ein Jahr\", wie manchmal auf dem Markt versprochen wird.",
    card2_title="Risiken ehrlich betrachtet",
    card2_desc="Klima und Gesundheit, Grenzregionen mit erhöhter Kriminalität, das aktuelle regulatorische Zeitfenster und Betrugsmaschen auf dem Umzugsmarkt — was man vorab wissen sollte, ohne Beschönigung und ohne Panikmache. Das ist eine seltene Seite dieser Art: die meisten Agenturen schweigen einfach über die Schwierigkeiten eines Umzugs.",
    more="Mehr erfahren →",
),
}

for lang, t in HUB.items():
    l = L(lang)
    body = f'''
{breadcrumbs([(NAV_LABELS[lang]["home"], l['home']), (NAV_LABELS[lang]["kak-my-rabotaem"], None)])}
<section class="hero" style="padding-top:24px;">
  <div class="wrap">
    <h1>{t["h1"]}</h1>
    <p class="lead">{t["lead"]}</p>
  </div>
</section>
<section style="padding-top:0;">
  <div class="prose">
    <article class="card" style="margin-bottom:24px;">
      <h3>{t["card1_title"]}</h3>
      <p style="font-size:16px;">{t["card1_desc"]}</p>
      <a class="card-link" href="{l['protsess']}">{t["more"]}</a>
    </article>
    <article class="card" style="margin-bottom:24px;">
      <h3>{t["card2_title"]}</h3>
      <p style="font-size:16px;">{t["card2_desc"]}</p>
      <a class="card-link" href="{l['riski']}">{t["more"]}</a>
    </article>
  </div>
</section>
'''
    page("kak-my-rabotaem", lang, t["title"], t["description"], body,
         extra_schema=schema_breadcrumb([(NAV_LABELS[lang]["home"], f"/{lang}/"), (NAV_LABELS[lang]["kak-my-rabotaem"], f"/{lang}/{href_to('kak-my-rabotaem', lang)}")]))
