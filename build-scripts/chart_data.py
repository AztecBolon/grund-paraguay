#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Данные для слайдера с инфографикой (12.08.2026, вторая версия — настоящие графики
динамики за много лет, не карточки с одним числом, см. правку по итогам «Мы не поняли
друг друга» в переписке с заказчиком). Числовые ряды (годы/значения) — на языке
геометрии не зависят, поэтому вынесены один раз; отображаемые строки, подписи и
источники — по языкам отдельно.

Источники и уверенность по каждой цифре — design/fakty-dlya-kontenta.md, раздел 17.
"""
from charts import line_chart, bar_chart, dumbbell_chart

# ---- числовые ряды (общие для всех языков) ----------------------------------------
GDP_YEARS = [2022, 2023, 2024, 2025]
GDP_VALS = [-0.03, 5.29, 4.67, 6.64]

FDI_YEARS = [2022, 2023, 2024, 2025]
FDI_VALS = [855, 1108, 1100, 1180]

LIFE_YEARS = [1980, 1990, 2000, 2010, 2025]
LIFE_VALS = [64.6, 67.3, 70.0, 72.6, 74.1]

GPI_YEARS = [2008, 2010, 2013, 2015, 2019, 2020, 2022, 2023, 2024, 2025]
GPI_VALS = [64, 97, 105, 106, 102, 91, 89, 70, 73, 75]

PASSPORT_YEARS = [2006, 2010, 2019, 2020, 2024, 2026]
PASSPORT_VALS = [39, 46, 31, 33, 31, 28]

DNM_VALS = [26850, 28464, 40600]  # 2023 (оценка) / 2024 / 2025

TAX_VALS = [0, 22, 45, 37]  # Парагвай / Россия / Германия / США

# Новые темы (19.08.2026, доработка карточки налогов по запросу заказчика) — все
# страны в том же порядке Парагвай/Россия/Германия/США. Источники и уверенность —
# design/sravnenie-nalogov-rf-de-avg2026.md.
IRE_VALS = [10, 25, 30, 21]      # налог на прибыль бизнеса
IVA_VALS = [10, 22, 19, 7.53]    # НДС; США — не НДС, налог с продаж (dashed_idx)
IDU_VALS = [8, 15, 26.4, 20]     # налог на дивиденды (резиденты)
IRP_VALS = [10, 22, 45, 37]      # налог на доход физлиц от личных услуг


def _pts(years, vals, disps):
    return list(zip(years, vals, disps))


# ---- по-языковой контент -----------------------------------------------------------
# href — только для RU (хаб); на Главной (все 4 языка) слайдер без ссылок — см. пояснения
# редактора: хаб RU-only, ссылка с ES/EN/DE вела бы в никуда.

def build_topics(lang, href=None):
    """href: dict topic_key -> url (или None). Возвращает список из 8 словарей
    {type, title, caption, summary, chart_kwargs, href}."""
    href = href or {}
    T = TEXT[lang]

    topics = []

    topics.append(dict(
        key="gdp", type="line",
        title=T["gdp_title"], caption=T["gdp_cap"], summary=T["gdp_sum"],
        kwargs=dict(points=_pts(GDP_YEARS, GDP_VALS, T["gdp_disp"]),
                    y_fmt=lambda v: f'{v:.0f}%'),
        href=href.get("gdp"),
    ))
    topics.append(dict(
        key="fdi", type="line",
        title=T["fdi_title"], caption=T["fdi_cap"], summary=T["fdi_sum"],
        kwargs=dict(points=_pts(FDI_YEARS, FDI_VALS, T["fdi_disp"]),
                    y_fmt=lambda v: f'{v:.0f}'),
        href=href.get("fdi"),
    ))
    topics.append(dict(
        key="life", type="line",
        title=T["life_title"], caption=T["life_cap"], summary=T["life_sum"],
        kwargs=dict(points=_pts(LIFE_YEARS, LIFE_VALS, T["life_disp"]),
                    y_fmt=lambda v: f'{v:.0f}'),
        href=href.get("life"),
    ))
    topics.append(dict(
        key="gpi", type="line",
        title=T["gpi_title"], caption=T["gpi_cap"], summary=T["gpi_sum"],
        kwargs=dict(points=_pts(GPI_YEARS, GPI_VALS, T["gpi_disp"]),
                    invert=True, y_fmt=lambda v: f'{v:.0f}'),
        href=href.get("gpi"),
    ))
    topics.append(dict(
        key="passport", type="line",
        title=T["passport_title"], caption=T["passport_cap"], summary=T["passport_sum"],
        kwargs=dict(points=_pts(PASSPORT_YEARS, PASSPORT_VALS, T["passport_disp"]),
                    invert=True, y_fmt=lambda v: f'{v:.0f}'),
        href=href.get("passport"),
    ))
    topics.append(dict(
        key="dnm", type="bar",
        title=T["dnm_title"], caption=T["dnm_cap"], summary=T["dnm_sum"],
        kwargs=dict(cats=T["dnm_cats"], values=DNM_VALS, disps=T["dnm_disp"],
                    y_fmt=lambda v: f'{v:,.0f}'.replace(",", " "), dashed_idx=0),
        href=href.get("dnm"),
    ))
    topics.append(dict(
        key="argentina", type="dumbbell",
        title=T["arg_title"], caption=T["arg_cap"], summary=T["arg_sum"],
        kwargs=dict(rows=T["arg_rows"]),
        href=href.get("argentina"),
    ))
    topics.append(dict(
        key="tax", type="bar",
        title=T["tax_title"], caption=T["tax_cap"], summary=T["tax_sum"],
        kwargs=dict(cats=T["tax_cats"], values=TAX_VALS, disps=T["tax_disp"],
                    y_fmt=lambda v: f'{v:.0f}%'),
        href=href.get("tax"),
    ))
    topics.append(dict(
        key="ire", type="bar",
        title=T["ire_title"], caption=T["ire_cap"], summary=T["ire_sum"],
        kwargs=dict(cats=T["ire_cats"], values=IRE_VALS, disps=T["ire_disp"],
                    y_fmt=lambda v: f'{v:.0f}%'),
        href=href.get("ire"),
    ))
    topics.append(dict(
        key="iva", type="bar",
        title=T["iva_title"], caption=T["iva_cap"], summary=T["iva_sum"],
        kwargs=dict(cats=T["iva_cats"], values=IVA_VALS, disps=T["iva_disp"],
                    y_fmt=lambda v: f'{v:.0f}%', dashed_idx=3),
        href=href.get("iva"),
    ))
    topics.append(dict(
        key="idu", type="bar",
        title=T["idu_title"], caption=T["idu_cap"], summary=T["idu_sum"],
        kwargs=dict(cats=T["idu_cats"], values=IDU_VALS, disps=T["idu_disp"],
                    y_fmt=lambda v: f'{v:.0f}%'),
        href=href.get("idu"),
    ))
    topics.append(dict(
        key="irp", type="bar",
        title=T["irp_title"], caption=T["irp_cap"], summary=T["irp_sum"],
        kwargs=dict(cats=T["irp_cats"], values=IRP_VALS, disps=T["irp_disp"],
                    y_fmt=lambda v: f'{v:.0f}%'),
        href=href.get("irp"),
    ))
    return topics


def render_topic(t):
    if t["type"] == "line":
        svg = line_chart(**t["kwargs"])
    elif t["type"] == "bar":
        svg = bar_chart(**t["kwargs"])
    elif t["type"] == "dumbbell":
        svg = dumbbell_chart(**t["kwargs"])
    else:
        raise ValueError(t["type"])
    # aria-label живёт на корневом <svg ...> — вставляем текстовую сводку вместо пустого атрибута
    svg = svg.replace('aria-label=""', f'aria-label="{t["summary"]}"', 1)
    return svg


UI_LABELS = {
    "ru": dict(region="Парагвай в цифрах — слайдер с графиками", prev="Предыдущий график",
               next="Следующий график", pause="Остановить автопрокрутку", play="Включить автопрокрутку",
               slide_n=lambda i, n, title: f"Слайд {i} из {n}: {title}"),
    "es": dict(region="Paraguay en cifras — carrusel de gráficos", prev="Gráfico anterior",
               next="Gráfico siguiente", pause="Pausar el avance automático", play="Reanudar el avance automático",
               slide_n=lambda i, n, title: f"Diapositiva {i} de {n}: {title}"),
    "en": dict(region="Paraguay in numbers — chart slider", prev="Previous chart",
               next="Next chart", pause="Pause autoplay", play="Resume autoplay",
               slide_n=lambda i, n, title: f"Slide {i} of {n}: {title}"),
    "de": dict(region="Paraguay in Zahlen — Diagramm-Slider", prev="Vorheriges Diagramm",
               next="Nächstes Diagramm", pause="Automatischen Wechsel anhalten", play="Automatischen Wechsel fortsetzen",
               slide_n=lambda i, n, title: f"Folie {i} von {n}: {title}"),
}

TEXT = {
"ru": dict(
    gdp_title="Рост ВВП", gdp_cap="Рекорд за последние 12 лет — Bloomberg, Macrotrends.",
    gdp_sum="График роста ВВП Парагвая по годам: 2022 год −0,03%, 2023 год +5,29%, 2024 год +4,67%, 2025 год +6,64% — рекорд за 12 лет.",
    gdp_disp=["−0,03%", "+5,29%", "+4,67%", "+6,64%"],

    fdi_title="Приток инвестиций (ПИИ)", fdi_cap="Третий год подряд выше $1 млрд — ECLAC.",
    fdi_sum="График притока прямых иностранных инвестиций по годам: 2022 год $855 млн, 2023 год $1,11 млрд, 2024 год $1,10 млрд, 2025 год $1,18 млрд.",
    fdi_disp=["$855 млн", "$1,11 млрд", "$1,10 млрд", "$1,18 млрд"],

    life_title="Продолжительность жизни", life_cap="Уже выше среднемировой (73,7 года) — World Economics.",
    life_sum="График продолжительности жизни в Парагвае: 1980 год 64,6, 1990 год 67,3, 2000 год 70,0, 2010 год 72,6, 2025 год 74,1 года.",
    life_disp=["64,6", "67,3", "70,0", "72,6", "74,1 года"],

    gpi_title="Индекс миролюбия в мире",
    gpi_cap="С 106-го места в 2015 году до 75-го в 2025-м — Vision of Humanity. Пик был в 2023-м (70-е место), после — небольшое снижение.",
    gpi_sum="График места Парагвая в мировом индексе миролюбия: 2008 год 64-е место, ухудшение до 106-го в 2015-м, улучшение до 70-го в 2023-м, 75-е место в 2025-м.",
    gpi_disp=["64-е", "97-е", "105-е", "106-е", "102-е", "91-е", "89-е", "70-е", "73-е", "75-е место"],

    passport_title="Паспорт Парагвая в мире", passport_cap="≈145 стран без визы — Henley Passport Index.",
    passport_sum="График места паспорта Парагвая в мировом рейтинге: с 39-го места в 2006 году до 28-го в 2026-м.",
    passport_disp=["39-е", "46-е", "31-е", "33-е", "31-е", "28-е место"],

    dnm_title="Резиденций выдано DNM", dnm_cap="40 600 против 28 464 годом ранее.",
    dnm_sum="Столбчатая диаграмма резиденций, выданных DNM: 2023 год примерно 26 850 (оценка), 2024 год 28 464, 2025 год 40 600.",
    dnm_cats=["2023 (оценка)", "2024", "2025"], dnm_disp=["≈26 850", "28 464", "40 600"],

    arg_title="Разворот с Аргентиной", arg_cap="65 035 аргентинцев уже переехали в Парагвай.",
    arg_sum="Парагвайцев в Аргентине стало меньше: 550 713 в 2010 году, 522 598 в 2022-м. Заявок от аргентинцев на резиденцию в Парагвае стало больше: около 12 600 в 2015 году, около 38 000 в 2025-м.",
    arg_rows=[
        dict(label="Парагвайцев в Аргентине (2010→2022)", before_disp="550 713", after_disp="522 598", before_frac=0.75, after_frac=0.55),
        dict(label="Заявок от аргентинцев в Парагвае (2015→2025)", before_disp="≈12 600", after_disp="≈38 000", before_frac=0.15, after_frac=0.85),
    ],

    tax_title="Налог на доход из-за рубежа", tax_cap="Территориальный принцип — в отличие от РФ, Германии, США.",
    tax_sum="Столбчатая диаграмма сравнения налога на доход из-за рубежа: Парагвай 0%, Россия до 22%, Германия до 45%, США до 37%.",
    tax_cats=["Парагвай", "Россия", "Германия", "США"], tax_disp=["0%", "до 22%", "до 45%", "до 37%"],

    ire_title="Налог на прибыль бизнеса", ire_cap="IRE — налог на прибыль компании от её деятельности в Парагвае. У Парагвая — самая низкая ставка в сравнении: 10% против 21–30% у остальных.",
    ire_sum="IRE — налог на прибыль компании в Парагвае. Столбчатая диаграмма сравнения ставки: Парагвай 10%, Россия 25%, Германия около 30%, США 21%.",
    ire_cats=["Парагвай", "Россия", "Германия", "США"], ire_disp=["10%", "25%", "≈30%", "21%"],

    iva_title="НДС на товары и услуги", iva_cap="НДС (IVA) — косвенный налог, включённый в цену большинства товаров и услуг. Парагвай — среди самых низких ставок НДС в регионе. В США федерального НДС нет — показан налог с продаж (в среднем по штатам).",
    iva_sum="НДС (IVA) — косвенный налог на товары и услуги. Столбчатая диаграмма сравнения ставки: Парагвай 10%, Россия 22%, Германия 19%, США — федерального НДС нет, налог с продаж в среднем ≈7,5% (пунктиром, не прямой аналог).",
    iva_cats=["Парагвай", "Россия", "Германия", "США*"], iva_disp=["10%", "22%", "19%", "≈7,5%*"],

    idu_title="Налог на дивиденды", idu_cap="IDU — налог, которым облагаются дивиденды, выплачиваемые акционерам компании. 8% для резидентов Парагвая — заметно ниже, чем в России, Германии и США.",
    idu_sum="IDU — налог на дивиденды, выплачиваемые акционерам. Столбчатая диаграмма сравнения: Парагвай 8% (резиденты), Россия до 15%, Германия 26,4%, США до 20% (для резидентов, без учёта дополнительного налога NIIT для высоких доходов).",
    idu_cats=["Парагвай", "Россия", "Германия", "США"], idu_disp=["8%", "до 15%", "26,4%", "до 20%"],

    irp_title="Налог на доход от личных услуг", irp_cap="IRP — налог на доход физлиц от личных услуг (например, работа по найму или как фрилансер). 8–10% в Парагвае против прогрессивных шкал с более высоким верхним порогом в остальных странах.",
    irp_sum="IRP — налог на доход физлиц от личных услуг. Столбчатая диаграмма сравнения: Парагвай до 10%, Россия до 22%, Германия до 45%, США до 37%.",
    irp_cats=["Парагвай", "Россия", "Германия", "США"], irp_disp=["до 10%", "до 22%", "до 45%", "до 37%"],
),
"es": dict(
    gdp_title="Crecimiento del PIB", gdp_cap="Récord de los últimos 12 años — Bloomberg, Macrotrends.",
    gdp_sum="Gráfico del crecimiento del PIB de Paraguay por año: 2022 −0,03%, 2023 +5,29%, 2024 +4,67%, 2025 +6,64% — récord de 12 años.",
    gdp_disp=["−0,03%", "+5,29%", "+4,67%", "+6,64%"],

    fdi_title="Inversión extranjera directa (IED)", fdi_cap="Tercer año consecutivo por encima de US$1.000 M — CEPAL.",
    fdi_sum="Gráfico de la inversión extranjera directa por año: 2022 US$855 M, 2023 US$1.110 M, 2024 US$1.100 M, 2025 US$1.180 M.",
    fdi_disp=["US$855 M", "US$1.110 M", "US$1.100 M", "US$1.180 M"],

    life_title="Esperanza de vida", life_cap="Ya por encima del promedio mundial (73,7 años) — World Economics.",
    life_sum="Gráfico de la esperanza de vida en Paraguay: 1980: 64,6; 1990: 67,3; 2000: 70,0; 2010: 72,6; 2025: 74,1 años.",
    life_disp=["64,6", "67,3", "70,0", "72,6", "74,1 años"],

    gpi_title="Índice de Paz Global",
    gpi_cap="Del puesto 106 en 2015 al 75 en 2025 — Vision of Humanity. El mejor puesto fue en 2023 (70), luego una leve baja.",
    gpi_sum="Gráfico del puesto de Paraguay en el Índice de Paz Global: puesto 64 en 2008, retrocedió al 106 en 2015, mejoró al 70 en 2023, puesto 75 en 2025.",
    gpi_disp=["64.º", "97.º", "105.º", "106.º", "102.º", "91.º", "89.º", "70.º", "73.º", "puesto 75"],

    passport_title="Pasaporte paraguayo en el mundo", passport_cap="≈145 países sin visa — Henley Passport Index.",
    passport_sum="Gráfico del puesto del pasaporte paraguayo: del 39.º lugar en 2006 al 28.º en 2026.",
    passport_disp=["39.º", "46.º", "31.º", "33.º", "31.º", "puesto 28"],

    dnm_title="Residencias otorgadas por la DNM", dnm_cap="40.600 frente a 28.464 el año anterior.",
    dnm_sum="Gráfico de barras de residencias otorgadas por la DNM: 2023 aprox. 26.850 (estimado), 2024: 28.464, 2025: 40.600.",
    dnm_cats=["2023 (estimado)", "2024", "2025"], dnm_disp=["≈26.850", "28.464", "40.600"],

    arg_title="El giro con Argentina", arg_cap="65.035 argentinos ya se mudaron a Paraguay.",
    arg_sum="Los paraguayos en Argentina disminuyeron: 550.713 en 2010, 522.598 en 2022. Las solicitudes de argentinos por residencia en Paraguay aumentaron: unas 12.600 en 2015, unas 38.000 en 2025.",
    arg_rows=[
        dict(label="Paraguayos en Argentina (2010→2022)", before_disp="550.713", after_disp="522.598", before_frac=0.75, after_frac=0.55),
        dict(label="Solicitudes argentinas en Paraguay (2015→2025)", before_disp="≈12.600", after_disp="≈38.000", before_frac=0.15, after_frac=0.85),
    ],

    tax_title="Impuesto sobre ingresos del exterior", tax_cap="Principio territorial — a diferencia de Rusia, Alemania y EE. UU.",
    tax_sum="Gráfico de barras comparando el impuesto sobre ingresos del exterior: Paraguay 0%, Rusia hasta 22%, Alemania hasta 45%, EE. UU. hasta 37%.",
    tax_cats=["Paraguay", "Rusia", "Alemania", "EE. UU."], tax_disp=["0%", "hasta 22%", "hasta 45%", "hasta 37%"],

    ire_title="Impuesto a la renta empresarial", ire_cap="El IRE es el impuesto sobre las ganancias de una empresa por su actividad en Paraguay. Paraguay tiene la tasa más baja de la comparación: 10% frente a 21–30% en el resto.",
    ire_sum="El IRE es el impuesto sobre la ganancia de una empresa en Paraguay. Gráfico de barras comparando la tasa: Paraguay 10%, Rusia 25%, Alemania cerca de 30%, EE. UU. 21%.",
    ire_cats=["Paraguay", "Rusia", "Alemania", "EE. UU."], ire_disp=["10%", "25%", "≈30%", "21%"],

    iva_title="IVA sobre bienes y servicios", iva_cap="El IVA es un impuesto indirecto incluido en el precio de la mayoría de bienes y servicios. Paraguay tiene una de las tasas de IVA más bajas de la región. EE. UU. no tiene IVA federal — se muestra el impuesto a las ventas (promedio estatal).",
    iva_sum="El IVA es un impuesto indirecto sobre bienes y servicios. Gráfico de barras comparando la tasa: Paraguay 10%, Rusia 22%, Alemania 19%, EE. UU. — no hay IVA federal, impuesto a las ventas promedio ≈7,5% (línea punteada, no es un equivalente directo).",
    iva_cats=["Paraguay", "Rusia", "Alemania", "EE. UU.*"], iva_disp=["10%", "22%", "19%", "≈7,5%*"],

    idu_title="Impuesto sobre dividendos", idu_cap="El IDU es el impuesto sobre los dividendos que se pagan a los accionistas de una empresa. 8% para residentes en Paraguay — notablemente más bajo que en Rusia, Alemania y EE. UU.",
    idu_sum="El IDU es el impuesto sobre los dividendos pagados a los accionistas. Gráfico de barras comparando la tasa: Paraguay 8% (residentes), Rusia hasta 15%, Alemania 26,4%, EE. UU. hasta 20% (residentes, sin contar el impuesto adicional NIIT para ingresos altos).",
    idu_cats=["Paraguay", "Rusia", "Alemania", "EE. UU."], idu_disp=["8%", "hasta 15%", "26,4%", "hasta 20%"],

    irp_title="Impuesto sobre ingresos por servicios personales", irp_cap="El IRP es el impuesto sobre los ingresos personales por servicios (por ejemplo, trabajo por cuenta propia o freelance). 8–10% en Paraguay frente a escalas progresivas con topes más altos en el resto de los países.",
    irp_sum="El IRP es el impuesto sobre los ingresos personales por servicios. Gráfico de barras comparando la tasa: Paraguay hasta 10%, Rusia hasta 22%, Alemania hasta 45%, EE. UU. hasta 37%.",
    irp_cats=["Paraguay", "Rusia", "Alemania", "EE. UU."], irp_disp=["hasta 10%", "hasta 22%", "hasta 45%", "hasta 37%"],
),
"en": dict(
    gdp_title="GDP growth", gdp_cap="A 12-year record — Bloomberg, Macrotrends.",
    gdp_sum="Chart of Paraguay's GDP growth by year: 2022 −0.03%, 2023 +5.29%, 2024 +4.67%, 2025 +6.64% — a 12-year record.",
    gdp_disp=["−0.03%", "+5.29%", "+4.67%", "+6.64%"],

    fdi_title="Foreign direct investment (FDI)", fdi_cap="Third year in a row above $1B — ECLAC.",
    fdi_sum="Chart of foreign direct investment by year: 2022 $855M, 2023 $1.11B, 2024 $1.10B, 2025 $1.18B.",
    fdi_disp=["$855M", "$1.11B", "$1.10B", "$1.18B"],

    life_title="Life expectancy", life_cap="Already above the world average (73.7) — World Economics.",
    life_sum="Chart of life expectancy in Paraguay: 1980: 64.6; 1990: 67.3; 2000: 70.0; 2010: 72.6; 2025: 74.1 years.",
    life_disp=["64.6", "67.3", "70.0", "72.6", "74.1 years"],

    gpi_title="Global Peace Index",
    gpi_cap="Up from 106th place in 2015 to 75th in 2025 — Vision of Humanity. The best rank was 2023 (70th), then a slight dip.",
    gpi_sum="Chart of Paraguay's Global Peace Index rank: 64th in 2008, dropped to 106th by 2015, improved to 70th by 2023, 75th in 2025.",
    gpi_disp=["64th", "97th", "105th", "106th", "102nd", "91st", "89th", "70th", "73rd", "75th place"],

    passport_title="Paraguay's passport, worldwide", passport_cap="≈145 visa-free countries — Henley Passport Index.",
    passport_sum="Chart of Paraguay's passport rank: from 39th place in 2006 to 28th in 2026.",
    passport_disp=["39th", "46th", "31st", "33rd", "31st", "28th place"],

    dnm_title="Residencies granted by DNM", dnm_cap="40,600 vs. 28,464 the year before.",
    dnm_sum="Bar chart of residencies granted by DNM: 2023 approx. 26,850 (estimate), 2024: 28,464, 2025: 40,600.",
    dnm_cats=["2023 (est.)", "2024", "2025"], dnm_disp=["≈26,850", "28,464", "40,600"],

    arg_title="The Argentina reversal", arg_cap="65,035 Argentines have already moved to Paraguay.",
    arg_sum="Paraguayans in Argentina declined: 550,713 in 2010, 522,598 in 2022. Applications from Argentines for residency in Paraguay rose: about 12,600 in 2015, about 38,000 in 2025.",
    arg_rows=[
        dict(label="Paraguayans in Argentina (2010→2022)", before_disp="550,713", after_disp="522,598", before_frac=0.75, after_frac=0.55),
        dict(label="Argentine applications in Paraguay (2015→2025)", before_disp="≈12,600", after_disp="≈38,000", before_frac=0.15, after_frac=0.85),
    ],

    tax_title="Tax on foreign-sourced income", tax_cap="Territorial system — unlike Russia, Germany or the US.",
    tax_sum="Bar chart comparing tax on foreign-sourced income: Paraguay 0%, Russia up to 22%, Germany up to 45%, US up to 37%.",
    tax_cats=["Paraguay", "Russia", "Germany", "US"], tax_disp=["0%", "up to 22%", "up to 45%", "up to 37%"],

    ire_title="Corporate income tax", ire_cap="IRE is the tax on a company's profit from its activity in Paraguay. Paraguay has the lowest rate in the comparison: 10% vs. 21–30% elsewhere.",
    ire_sum="IRE is the tax on a company's profit in Paraguay. Bar chart comparing the rate: Paraguay 10%, Russia 25%, Germany about 30%, US 21%.",
    ire_cats=["Paraguay", "Russia", "Germany", "US"], ire_disp=["10%", "25%", "≈30%", "21%"],

    iva_title="VAT on goods and services", iva_cap="VAT (IVA) is an indirect tax built into the price of most goods and services. Paraguay has one of the lowest VAT rates in the region. The US has no federal VAT — shown here is the average state sales tax.",
    iva_sum="VAT is an indirect tax on goods and services. Bar chart comparing the rate: Paraguay 10%, Russia 22%, Germany 19%, US — no federal VAT, average sales tax ≈7.5% (dashed, not a direct equivalent).",
    iva_cats=["Paraguay", "Russia", "Germany", "US*"], iva_disp=["10%", "22%", "19%", "≈7.5%*"],

    idu_title="Dividend tax", idu_cap="IDU is the tax on dividends paid out to a company's shareholders. 8% for Paraguayan residents — notably lower than Russia, Germany or the US.",
    idu_sum="IDU is the tax on dividends paid to shareholders. Bar chart comparing the rate: Paraguay 8% (residents), Russia up to 15%, Germany 26.4%, US up to 20% (residents, excluding the additional NIIT for high earners).",
    idu_cats=["Paraguay", "Russia", "Germany", "US"], idu_disp=["8%", "up to 15%", "26.4%", "up to 20%"],

    irp_title="Tax on personal-services income", irp_cap="IRP is the tax on personal income from services (e.g., employment or freelance work). 8–10% in Paraguay vs. progressive scales with higher top brackets elsewhere.",
    irp_sum="IRP is the tax on personal income from services. Bar chart comparing the rate: Paraguay up to 10%, Russia up to 22%, Germany up to 45%, US up to 37%.",
    irp_cats=["Paraguay", "Russia", "Germany", "US"], irp_disp=["up to 10%", "up to 22%", "up to 45%", "up to 37%"],
),
"de": dict(
    gdp_title="BIP-Wachstum", gdp_cap="Rekord der letzten 12 Jahre — Bloomberg, Macrotrends.",
    gdp_sum="Diagramm des BIP-Wachstums Paraguays nach Jahr: 2022 −0,03%, 2023 +5,29%, 2024 +4,67%, 2025 +6,64% — Rekord der letzten 12 Jahre.",
    gdp_disp=["−0,03%", "+5,29%", "+4,67%", "+6,64%"],

    fdi_title="Ausländische Direktinvestitionen (ADI)", fdi_cap="Drittes Jahr in Folge über 1 Mrd. $ — ECLAC.",
    fdi_sum="Diagramm der ausländischen Direktinvestitionen nach Jahr: 2022 855 Mio. $, 2023 1,11 Mrd. $, 2024 1,10 Mrd. $, 2025 1,18 Mrd. $.",
    fdi_disp=["855 Mio. $", "1,11 Mrd. $", "1,10 Mrd. $", "1,18 Mrd. $"],

    life_title="Lebenserwartung", life_cap="Bereits über dem weltweiten Durchschnitt (73,7) — World Economics.",
    life_sum="Diagramm der Lebenserwartung in Paraguay: 1980: 64,6; 1990: 67,3; 2000: 70,0; 2010: 72,6; 2025: 74,1 Jahre.",
    life_disp=["64,6", "67,3", "70,0", "72,6", "74,1 Jahre"],

    gpi_title="Global Peace Index",
    gpi_cap="2015 noch Platz 106, 2025 Platz 75 — Vision of Humanity. Bester Platz war 2023 (70), danach ein leichter Rückgang.",
    gpi_sum="Diagramm von Paraguays Platzierung im Global Peace Index: Platz 64 im Jahr 2008, Rückgang auf Platz 106 bis 2015, Verbesserung auf Platz 70 bis 2023, Platz 75 im Jahr 2025.",
    gpi_disp=["Platz 64", "Platz 97", "Platz 105", "Platz 106", "Platz 102", "Platz 91", "Platz 89", "Platz 70", "Platz 73", "Platz 75"],

    passport_title="Paraguayischer Pass weltweit", passport_cap="≈145 visumfreie Länder — Henley Passport Index.",
    passport_sum="Diagramm der Platzierung des paraguayischen Passes: von Platz 39 im Jahr 2006 auf Platz 28 im Jahr 2026.",
    passport_disp=["Platz 39", "Platz 46", "Platz 31", "Platz 33", "Platz 31", "Platz 28"],

    dnm_title="2025 erteilte Aufenthaltstitel (DNM)", dnm_cap="40.600 gegenüber 28.464 im Vorjahr.",
    dnm_sum="Balkendiagramm der von der DNM erteilten Aufenthaltstitel: 2023 ca. 26.850 (Schätzung), 2024: 28.464, 2025: 40.600.",
    dnm_cats=["2023 (Schätzung)", "2024", "2025"], dnm_disp=["≈26.850", "28.464", "40.600"],

    arg_title="Die Wende mit Argentinien", arg_cap="65.035 Argentinier sind bereits nach Paraguay gezogen.",
    arg_sum="Die Zahl der Paraguayer in Argentinien sank: 550.713 im Jahr 2010, 522.598 im Jahr 2022. Die Anträge von Argentiniern auf Aufenthalt in Paraguay stiegen: rund 12.600 im Jahr 2015, rund 38.000 im Jahr 2025.",
    arg_rows=[
        dict(label="Paraguayer in Argentinien (2010→2022)", before_disp="550.713", after_disp="522.598", before_frac=0.75, after_frac=0.55),
        dict(label="Argentinische Anträge in Paraguay (2015→2025)", before_disp="≈12.600", after_disp="≈38.000", before_frac=0.15, after_frac=0.85),
    ],

    tax_title="Steuer auf Auslandseinkommen", tax_cap="Territorialprinzip — anders als in Russland, Deutschland oder den USA.",
    tax_sum="Balkendiagramm zum Vergleich der Steuer auf Auslandseinkommen: Paraguay 0%, Russland bis 22%, Deutschland bis 45%, USA bis 37%.",
    tax_cats=["Paraguay", "Russland", "Deutschland", "USA"], tax_disp=["0%", "bis 22%", "bis 45%", "bis 37%"],

    ire_title="Unternehmenssteuer", ire_cap="Die IRE ist die Steuer auf den Gewinn eines Unternehmens aus seiner Tätigkeit in Paraguay. Paraguay hat den niedrigsten Satz im Vergleich: 10% gegenüber 21–30% in den übrigen Ländern.",
    ire_sum="Die IRE ist die Steuer auf den Gewinn eines Unternehmens in Paraguay. Balkendiagramm zum Vergleich: Paraguay 10%, Russland 25%, Deutschland etwa 30%, USA 21%.",
    ire_cats=["Paraguay", "Russland", "Deutschland", "USA"], ire_disp=["10%", "25%", "≈30%", "21%"],

    iva_title="Mehrwertsteuer auf Waren und Dienstleistungen", iva_cap="Die Mehrwertsteuer (IVA) ist eine indirekte Steuer, die im Preis der meisten Waren und Dienstleistungen enthalten ist. Paraguay hat einen der niedrigsten Mehrwertsteuersätze der Region. In den USA gibt es keine bundesweite Mehrwertsteuer — gezeigt wird die durchschnittliche Sales Tax der Bundesstaaten.",
    iva_sum="Die Mehrwertsteuer ist eine indirekte Steuer auf Waren und Dienstleistungen. Balkendiagramm zum Vergleich: Paraguay 10%, Russland 22%, Deutschland 19%, USA — keine bundesweite Mehrwertsteuer, durchschnittliche Sales Tax ≈7,5% (gestrichelt, kein direktes Äquivalent).",
    iva_cats=["Paraguay", "Russland", "Deutschland", "USA*"], iva_disp=["10%", "22%", "19%", "≈7,5%*"],

    idu_title="Steuer auf Dividenden", idu_cap="Die IDU ist die Steuer auf Dividenden, die an die Aktionäre eines Unternehmens ausgeschüttet werden. 8% für Ansässige in Paraguay — deutlich niedriger als in Russland, Deutschland oder den USA.",
    idu_sum="Die IDU ist die Steuer auf Dividenden, die an Aktionäre ausgeschüttet werden. Balkendiagramm zum Vergleich: Paraguay 8% (ansässige Personen), Russland bis 15%, Deutschland 26,4%, USA bis 20% (ansässige Personen, ohne zusätzliche NIIT-Steuer für hohe Einkommen).",
    idu_cats=["Paraguay", "Russland", "Deutschland", "USA"], idu_disp=["8%", "bis 15%", "26,4%", "bis 20%"],

    irp_title="Steuer auf Einkommen aus persönlichen Dienstleistungen", irp_cap="Die IRP ist die Steuer auf persönliches Einkommen aus Dienstleistungen (z. B. Anstellung oder freiberufliche Tätigkeit). 8–10% in Paraguay gegenüber progressiven Skalen mit höheren Spitzensätzen in den übrigen Ländern.",
    irp_sum="Die IRP ist die Steuer auf persönliches Einkommen aus Dienstleistungen. Balkendiagramm zum Vergleich: Paraguay bis 10%, Russland bis 22%, Deutschland bis 45%, USA bis 37%.",
    irp_cats=["Paraguay", "Russland", "Deutschland", "USA"], irp_disp=["bis 10%", "bis 22%", "bis 45%", "bis 37%"],
),
}
