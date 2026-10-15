#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Стоимость, О компании, Конфиденциальность — ru/es/en"""
from build import page, breadcrumbs, schema_breadcrumb, DOMAIN, href_to, NAV_LABELS, ICONS, seal_svg

def L(lang):
    return {pid: href_to(pid, lang) for pid in
            ["home","uslugi","protsess","riski","stoimost","o-kompanii","konfidentsialnost","keisy","kontakty","terminologiya","politika","kak-my-rabotaem"]}

# Печать «Пошлина отдельно» на «Стоимости» (12.08.2026) — новая, пятая печать (остальные
# четыре — на Главной, pages_home_uslugi.py). Не новый факт: дословно то же утверждение,
# что было в обычной плашке badge-price на этой же странице («Пошлина — отдельной строкой
# в договоре») и повторено в p_final «О компании» этого же файла — просто в формате печати
# вместо плашки. Иконка/цвет — те же, что были у прежней плашки (stamp, red).
FEE_SEPARATE_SEAL = {
    "ru": ("stamp", "red", "Пошлина — отдельно", "Отдельной строкой",
           "Пошлина — отдельной строкой в письменной договорённости: государственная пошлина не смешивается с гонораром агентства"),
    "es": ("stamp", "red", "Arancel aparte", "Línea separada",
           "El arancel estatal, como línea aparte en el acuerdo por escrito: nunca se mezcla con los honorarios de la agencia"),
    "en": ("stamp", "red", "Fee kept separate", "A separate line",
           "The government fee as a separate line in the written agreement: never blended with the agency's fee"),
    "de": ("stamp", "red", "Gebühr getrennt", "Eigene Zeile",
           "Die staatliche Gebühr als separate Zeile in der schriftlichen Vereinbarung: wird nie mit dem Honorar der Agentur vermischt"),
}

# Печати «Фиксированная цена» и «Конфиденциальность» на «О компании» (12.08.2026) — те же
# две печати (иконки stamp/shield, красная/синяя), что и в SEALS["ru"][0] и [1] на Главной —
# заменяют собой прежнюю пару обычных плашек badge-price/badge-confidential в разделе
# «Договор и гарантии». Формулировки ring-текста и aria — дословно оттуда же.
COMPANY_SEALS = {
    "ru": [("stamp", "red", "Фиксированная цена", "Сумма не меняется",
            "Фиксированная цена: сумма не меняется в процессе работы"),
           ("shield", "blue", "Конфиденциальность", "Соглашение с каждым клиентом",
            "Конфиденциальность: отдельное соглашение с каждым клиентом")],
    "es": [("stamp", "red", "Precio fijo", "El monto no cambia",
            "Precio fijo: el monto no cambia durante el proceso"),
           ("shield", "blue", "Confidencialidad", "Acuerdo con cada cliente",
            "Confidencialidad: un acuerdo aparte con cada cliente")],
    "en": [("stamp", "red", "Fixed price", "The amount doesn't change",
            "Fixed price: the amount doesn't change during the process"),
           ("shield", "blue", "Confidentiality", "A separate agreement",
            "Confidentiality: a separate agreement with every client")],
    "de": [("stamp", "red", "Festpreis", "Der Betrag ändert sich nicht",
            "Festpreis: der Betrag ändert sich während des Prozesses nicht"),
           ("shield", "blue", "Vertraulichkeit", "Vereinbarung pro Mandant",
            "Vertraulichkeit: eine gesonderte Vereinbarung mit jedem Mandanten")],
}

def fee_scheme_svg(cap):
    # cap: [title, desc, box1_title, box1_l1, box1_l2, box2_title, box2_l1, box2_l2, footer]
    return f'''
<svg viewBox="0 0 640 220" width="100%" height="auto" role="img" aria-labelledby="feeTitle feeDesc">
  <title id="feeTitle">{cap[0]}</title>
  <desc id="feeDesc">{cap[1]}</desc>
  <rect x="20" y="40" width="230" height="110" rx="8" fill="none" stroke="#E8F1FB" stroke-width="1.6"/>
  <text x="135" y="80" text-anchor="middle" font-size="15" font-weight="600">{cap[2]}</text>
  <text x="135" y="102" text-anchor="middle" class="dim" font-size="12">{cap[3]}</text>
  <text x="135" y="118" text-anchor="middle" class="dim" font-size="12">{cap[4]}</text>

  <text x="278" y="102" text-anchor="middle" font-size="22" class="accent">+</text>

  <rect x="310" y="40" width="230" height="110" rx="8" fill="none" stroke="#E96C63" stroke-width="1.6" class="accent"/>
  <text x="425" y="80" text-anchor="middle" font-size="15" font-weight="600">{cap[5]}</text>
  <text x="425" y="102" text-anchor="middle" class="dim" font-size="12">{cap[6]}</text>
  <text x="425" y="118" text-anchor="middle" class="dim" font-size="12">{cap[7]}</text>

  <line x1="270" y1="170" x2="270" y2="190" stroke="#2C5480" class="grid-line"/>
  <line x1="20" y1="190" x2="540" y2="190" stroke="#2C5480" class="grid-line"/>
  <text x="20" y="212" font-size="12" class="dim">{cap[8]}</text>
</svg>
'''

# ============================================================ СТОИМОСТЬ / COST

COST = {
"ru": dict(
    title="Стоимость ВНЖ и услуг в Парагвае: пошлины и тарифы | Grund Paraguay",
    description="Государственные пошлины и налоги Парагвая — отдельно от гонорара агентства: таблица актуальных тарифов на резидентуру, комплаенс, компанию и недвижимость.",
    h1="Стоимость и тарифы: пошлина отдельно от гонорара агентства",
    lead='Два отдельных блока: государственные пошлины и налоги, которые вы платите органам Парагвая напрямую (и которые от нас не зависят), и стоимость наших услуг (полный перечень — на странице <a href="{uslugi}">«Услуги»</a>). Мы принципиально не смешиваем эти суммы в одной цифре — в отличие от части рекламы на рынке, где государственная пошлина и гонорар агентства подаются как единая «цена под ключ».',
    fee_cap=["Пошлина отдельно от гонорара",
             "Схема: государственная пошлина уходит в бюджет Парагвая, гонорар агентства — отдельная сумма за услуги.",
             "Госпошлина DNM", "оплачивается напрямую", "государству Парагвая",
             "Гонорар агентства", "проверка документов,", "сопровождение, комплаенс",
             "Две отдельные суммы — не единая «цена под ключ»"],
    h2_duties="Государственные пошлины и налоги (актуальность подтверждается на момент оплаты)",
    callout1_label="Важная оговорка",
    callout1='Часть сумм пошлин указана по данным на 1 июля 2025 года. С 1 июля 2026 года пошлины миграционной службы (<a href="{terminologiya}#dnm">DNM</a>) были повышены заново (Decreto N° 6225/2026 и Resolución DNM N° 478/2026; новая база расчёта — минимальный размер оплаты труда ₲ 3 044 000, выросший к июлю 2026 на 5%), но точные новые суммы в гуарани по состоянию на 19.08.2026 в открытых источниках всё ещё не опубликованы — официальная таблица тарифов, судя по новостным публикациям DNM, существует на сайте миграционной службы, но не была нам доступна напрямую на момент проверки. Пошлины пересматриваются ежегодно к 1 июля вместе с МРОТ — поэтому точную актуальную сумму на дату вашей оплаты мы уточняем индивидуально, а не публикуем цифру, которая может устареть за несколько недель. Актуальный курс гуарани к доллару и рублю — на странице <a href="{terminologiya}#kurs-valyuty">«Терминология»</a>.',
    table1_caption="Данные на 01.07.2025, требуют подтверждения на текущую дату",
    table1_head=["Статья","Сумма","Комментарий"],
    table1_rows=[
        ["Пошлина за Residencia Temporal","25 дн. ставок = ₲ 2 787 550","Повышена с 01.07.2026, новая сумма уточняется"],
        ["Пошлина за Residencia Permanente","25 дн. ставок = ₲ 2 787 550","Повышена с 01.07.2026, новая сумма уточняется"],
        ["Продление Residencia Temporal","11 дн. ставок = ₲ 1 226 522","Повышена с 01.07.2026, новая сумма уточняется"],
        ["Смена категории резидента","10 дн. ставок = ₲ 1 115 020","Повышена с 01.07.2026, новая сумма уточняется"],
        ["Штраф за просрочку продления","6 дн. ставок = ₲ 669 012","Повышена с 01.07.2026, новая сумма уточняется"],
        ["Сертификат инвестора (CIE), путь SUACE / Investor Pass","₲ 2 783 457","Официальный источник — PDF SUACE"],
        ["Пошлина за натурализацию (гражданство)","₲ 43 051","Официальный источник — Poder Judicial"],
    ],
    p_taxes='Налоги после получения резиденции и регистрации <a href="{terminologiya}#ruc">RUC</a>: <a href="{terminologiya}#iva">IVA</a> — 10% по общей ставке, 5% по льготной, декларация подаётся через <a href="{terminologiya}#formulario-120">Formulario 120</a> (периодичность подачи по общему режиму уточняется индивидуально — источники расходятся, точная норма требует сверки с текстом Ley 6380/19 перед публикацией клиенту); упрощённый режим для микробизнеса <a href="{terminologiya}#ire">IRE RESIMPLE</a> — при годовом обороте до ₲ 80 млн фиксированные квартальные платежи от ₲ 60 000 до ₲ 240 000, с автоматическим формированием нулевой декларации системой <a href="{terminologiya}#marangatu">Marangatú</a>, если отчёт не подан в срок; <a href="{terminologiya}#irp">IRP</a> от личных услуг — от 8 до 10% при доходе от ₲ 80 млн в год; пеня за просрочку уплаты — от 4% (до 1 месяца просрочки) до 14% (свыше 5 месяцев).',
    callout2_label="Пробел в источниках",
    callout2='Точные актуальные штрафы за непредставление отчётности по общему режиму IVA/IRP (не RESIMPLE) в открытых источниках не найдены — уточняются индивидуально в рамках абонемента сопровождения (см. страницу <a href="{uslugi}">«Услуги»</a>).',
    p_realestate='<strong>Пример структуры расходов при сделке с недвижимостью</strong> (не тариф на конкретный объект): гонорар нотариуса (<a href="{terminologiya}#escribano">escribano</a>) — ориентировочно 0,75% от суммы сделки для объектов дороже ₲ 200 млн (1–2% для более дешёвых) плюс НДС 10% на сам гонорар; регистрационный сбор — около 0,8%; муниципальный налог на передачу — около 0,3%; НДС на саму передачу недвижимости, если продавец — плательщик НДС, — 5% от презюмируемой налоговой базы (30% цены продажи), то есть примерно 1,5% от полной цены объекта. Суммарно транзакционные издержки по примеру такой сделки — около 2,3% без учёта НДС на передачу.',
    p_company='<strong>Расходы на регистрацию компании:</strong> упрощённое акционерное общество (<a href="{terminologiya}#eas">EAS</a>) — по оценке отраслевых деловых изданий, около 800 USD без учёта госпошлин (оценка для полностью онлайн-регистрации; у нас регистрация проходит только при личном присутствии); <a href="{terminologiya}#sa">S.A.</a> и <a href="{terminologiya}#srl">S.R.L.</a> — ориентировочно 2000–2500 USD, включая нотариальный акт (для S.A. — также обязательную публикацию в СМИ). Официальная государственная тарифная сетка по статьям в открытом доступе не найдена — приведённые суммы это независимые оценки деловых медиа, не официальный прайс регулятора.',
    p_confidence='Пороги и суммы, которые фактура прямо помечает как неподтверждённые официально (в частности, конкретные денежные требования по 12 категориям резолюции DNM N° 407/2026 к платёжеспособности заявителей — см. также <a href="{protsess}">«Процесс и сроки»</a>), мы не публикуем как цифры — они рассчитываются и подтверждаются индивидуально по действующим тарифам и требованиям DNM на момент вашей заявки.',
    h2_services="Наши услуги",
    table2_head=["Услуга","Стоимость","Комментарий"],
    table2_rows=[
        ["Резидентура (ВНЖ) — пакет Temporal → Permanente","2000–4000 USD","В пакет входит проверка документов и юридическое сопровождение; сумма зависит от категории заявителя по Resolución 407/2026"],
        ["Сопровождение и комплаенс","25–50 USD / мес.","Ведение RUC, ежемесячная отчётность (включая нулевую), контроль статуса дела"],
        ["Открытие компании (EAS/SRL)","500–1500 USD","Регистрация через партнёра на месте, только при личном присутствии; существенно ниже части предложений на рынке (там же встречаются цены 5000–13000 USD за ту же услугу)"],
        ["Проверка и покупка недвижимости (due diligence)","по запросу","Фиксированная цена за отчёт, не зависит от того, состоится сделка или нет"],
        ["Гражданство Парагвая — полное сопровождение с адвокатом","ориентировочно от 5000 USD","Адвокат, сборы и т. д.; госпошлина ₲ 43 051 оплачивается отдельно (см. таблицу выше); точная сумма уточняется индивидуально"],
        ["Инвесторский путь (SUACE / Investor Pass)","по запросу","Зависит от выбранной инвестиционной ветки"],
        ["Покупка и продажа бизнеса","по запросу","Индивидуальная оценка ввиду отсутствия стандартизированного рынка сделок"],
        ["Релокация организаций","индивидуально","По часовой ставке — в зависимости от числа сотрудников, необходимости режима Maquila и т. д."],
    ],
    badge="Пошлина — отдельной строкой в договорённости",
    p_terms='<strong>Условия оплаты и что не входит в цену.</strong> Цены не включают услуги сторонних партнёров (например, юристов и нотариусов на месте) — они оплачиваются отдельно. Полная сумма за нашу услугу вносится к моменту подачи на Cédula (CI). Спецпожелания (например, поиск жилья или аренда авто) возможны всегда, но фиксированного прайс-листа на них нет: трудозатраты заранее точно не оценить, поэтому такие задачи оплачиваются по часовой ставке или пакетом.',
    p_final='Государственная пошлина в каждом случае оплачивается отдельно от гонорара агентства — это указано в письменной договорённости отдельной строкой (подробнее — на странице <a href="{o-kompanii}">«О компании»</a>). Если готовы обсудить свою ситуацию — <a href="{kontakty}">оставьте заявку на консультацию</a>.',
),
"es": dict(
    title="Costo de la residencia y servicios en Paraguay: aranceles y tarifas | Grund Paraguay",
    description="Aranceles estatales e impuestos de Paraguay — aparte de los honorarios de la agencia: tabla de tarifas vigentes para residencia, cumplimiento, empresa y bienes raíces.",
    h1="Costos y tarifas: el arancel aparte de los honorarios de la agencia",
    lead='Dos bloques separados: los aranceles e impuestos estatales que usted paga directamente a las autoridades de Paraguay (y que no dependen de nosotros), y el costo de nuestros servicios (lista completa en la página <a href="{uslugi}">«Servicios»</a>). Por principio no mezclamos estas sumas en una sola cifra — a diferencia de parte de la publicidad del mercado, donde el arancel estatal y los honorarios de la agencia se presentan como un único «precio llave en mano».',
    fee_cap=["El arancel, aparte de los honorarios",
             "Esquema: el arancel estatal va al presupuesto de Paraguay; los honorarios de la agencia son una suma aparte por los servicios.",
             "Arancel estatal DNM", "se paga directamente", "al Estado paraguayo",
             "Honorarios de la agencia", "revisión de documentos,", "acompañamiento, cumplimiento",
             "Dos sumas separadas — no un «precio llave en mano» único"],
    h2_duties="Aranceles e impuestos estatales (la vigencia se confirma al momento del pago)",
    callout1_label="Aclaración importante",
    callout1='Parte de los montos de aranceles corresponde a datos del 1 de julio de 2025. Desde el 1 de julio de 2026 los aranceles del servicio de migraciones (<a href="{terminologiya}#dnm">DNM</a>) fueron actualizados nuevamente (Decreto N.° 6225/2026 y Resolución DNM N.° 478/2026; la nueva base de cálculo es el salario mínimo de ₲ 3.044.000, que subió un 5% hacia julio de 2026), pero los montos exactos en guaraníes, al 19.08.2026, siguen sin publicarse en fuentes abiertas — según las noticias de la DNM existe una tabla oficial de aranceles en el sitio de migraciones, pero no pudimos acceder a ella directamente al momento de la verificación. Los aranceles se revisan cada año el 1 de julio junto con el salario mínimo — por eso confirmamos el monto exacto vigente en la fecha de su pago de forma individual, en lugar de publicar una cifra que puede quedar desactualizada en pocas semanas. El tipo de cambio actual del guaraní frente al dólar y al rublo está en la página <a href="{terminologiya}#kurs-valyuty">«Terminología»</a>.',
    table1_caption="Datos al 01.07.2025, requieren confirmación a la fecha actual",
    table1_head=["Concepto","Monto","Comentario"],
    table1_rows=[
        ["Arancel por Residencia Temporal","25 jornales = ₲ 2.787.550","Actualizado desde el 01.07.2026, nuevo monto en confirmación"],
        ["Arancel por Residencia Permanente","25 jornales = ₲ 2.787.550","Actualizado desde el 01.07.2026, nuevo monto en confirmación"],
        ["Renovación de Residencia Temporal","11 jornales = ₲ 1.226.522","Actualizado desde el 01.07.2026, nuevo monto en confirmación"],
        ["Cambio de categoría de residente","10 jornales = ₲ 1.115.020","Actualizado desde el 01.07.2026, nuevo monto en confirmación"],
        ["Multa por renovación fuera de plazo","6 jornales = ₲ 669.012","Actualizado desde el 01.07.2026, nuevo monto en confirmación"],
        ["Certificado de inversor (CIE), vía SUACE / Investor Pass","₲ 2.783.457","Fuente oficial: PDF de SUACE"],
        ["Arancel de naturalización (ciudadanía)","₲ 43.051","Fuente oficial: Poder Judicial"],
    ],
    p_taxes='Impuestos tras obtener la residencia e inscribir el <a href="{terminologiya}#ruc">RUC</a>: <a href="{terminologiya}#iva">IVA</a> — 10% en la tasa general, 5% en la reducida, declaración mediante el <a href="{terminologiya}#formulario-120">Formulario 120</a> (la periodicidad en el régimen general se confirma de forma individual — las fuentes difieren y la norma exacta requiere cotejo con el texto de la Ley 6380/19 antes de comunicarla al cliente); régimen simplificado para microempresas <a href="{terminologiya}#ire">IRE RESIMPLE</a> — con facturación anual de hasta ₲ 80 millones, pagos trimestrales fijos de ₲ 60.000 a ₲ 240.000, con generación automática de declaración en cero por el sistema <a href="{terminologiya}#marangatu">Marangatú</a> si no se presenta a tiempo; <a href="{terminologiya}#irp">IRP</a> por servicios personales — del 8 al 10% con ingresos desde ₲ 80 millones anuales; recargo por mora — del 4% (hasta 1 mes de atraso) al 14% (más de 5 meses).',
    callout2_label="Vacío en las fuentes",
    callout2='No se encontraron en fuentes abiertas las multas exactas vigentes por no presentar declaraciones en el régimen general de IVA/IRP (no RESIMPLE) — se confirman de forma individual dentro del servicio de acompañamiento (ver la página <a href="{uslugi}">«Servicios»</a>).',
    p_realestate='<strong>Ejemplo de estructura de gastos en una operación inmobiliaria</strong> (no es una tarifa para un inmueble concreto): honorarios del escribano — aproximadamente 0,75% del valor de la operación para inmuebles de más de ₲ 200 millones (1–2% para los más económicos) más el IVA del 10% sobre esos honorarios; tasa de registro — alrededor de 0,8%; impuesto municipal a la transferencia — alrededor de 0,3%; IVA sobre la propia transferencia del inmueble, si el vendedor es contribuyente de IVA — 5% sobre la base imponible presunta (30% del precio de venta), es decir, aproximadamente 1,5% del precio total del inmueble. En total, los costos de transacción en este ejemplo rondan el 2,3%, sin contar el IVA sobre la transferencia.',
    p_company='<strong>Gastos de constitución de una empresa:</strong> sociedad por acciones simplificada (<a href="{terminologiya}#eas">EAS</a>) — según estimaciones de medios de negocios del sector, alrededor de 800 USD sin contar los aranceles estatales (estimación para un registro totalmente en línea; con nosotros la inscripción se hace solo de forma presencial); <a href="{terminologiya}#sa">S.A.</a> y <a href="{terminologiya}#srl">S.R.L.</a> — aproximadamente 2000–2500 USD, incluyendo el acto notarial (para la S.A., también la publicación obligatoria en medios). No se encontró una tabla arancelaria estatal oficial y detallada en acceso abierto — los montos indicados son estimaciones independientes de medios de negocios, no un precio oficial del regulador.',
    p_confidence='Los umbrales y montos que la factura señala explícitamente como no confirmados oficialmente (en particular, las exigencias monetarias concretas para las 12 categorías de la Resolución DNM N.° 407/2026 sobre solvencia de los solicitantes — ver también <a href="{protsess}">«Proceso y plazos»</a>) no los publicamos como cifras: se calculan y confirman de forma individual según las tarifas y requisitos vigentes de la DNM al momento de su solicitud.',
    h2_services="Nuestros servicios",
    table2_head=["Servicio","Costo","Comentario"],
    table2_rows=[
        ["Residencia — paquete Temporal → Permanente","2000–4000 USD","Incluye revisión de documentos y acompañamiento legal; el monto depende de la categoría del solicitante según la Resolución 407/2026"],
        ["Acompañamiento y cumplimiento","25–50 USD / mes","Gestión del RUC, declaraciones mensuales (incluidas las de cero), seguimiento del estado del trámite"],
        ["Constitución de empresa (EAS/SRL)","500–1500 USD","Inscripción a través de un socio en el lugar, solo de forma presencial; sustancialmente por debajo de parte de las ofertas del mercado (donde se ven precios de 5000–13000 USD por el mismo servicio)"],
        ["Verificación y compra de inmuebles (due diligence)","a pedido","Precio fijo por el informe, independiente de si la operación se concreta o no"],
        ["Ciudadanía paraguaya — acompañamiento completo con abogado","aprox. desde 5000 USD","Abogado, tasas, etc.; el arancel de ₲ 43.051 se paga aparte (ver la tabla de arriba); el monto exacto se confirma de forma individual"],
        ["Vía de inversor (SUACE / Investor Pass)","a pedido","Depende de la rama de inversión elegida"],
        ["Compra y venta de negocios","a pedido","Evaluación individual, dado que no existe un mercado estandarizado de operaciones"],
        ["Relocalización de empresas","individual","Por tarifa horaria — según el número de empleados, la necesidad del régimen Maquila, etc."],
    ],
    badge="El arancel, como línea aparte en el acuerdo",
    p_terms='<strong>Condiciones de pago y qué no incluye el precio.</strong> Los precios no incluyen los servicios de socios externos (por ejemplo, abogados y escribanos en el lugar), que se pagan aparte. El monto completo de nuestro servicio se abona hasta el momento de solicitar la Cédula (CI). Los pedidos especiales (por ejemplo, buscar vivienda o alquilar un auto) siempre son posibles, pero no tienen una lista de precios fija: el trabajo no se puede estimar con exactitud de antemano, por eso se cobran por tarifa horaria o como paquete.',
    p_final='El arancel estatal siempre se paga aparte de los honorarios de la agencia — así consta como línea separada en el acuerdo por escrito (más sobre el acuerdo en la página <a href="{o-kompanii}">«Sobre nosotros»</a>). Si está listo para conversar sobre su situación — <a href="{kontakty}">deje una solicitud de consulta</a>.',
),
"en": dict(
    title="Cost of residency and services in Paraguay: fees and rates | Grund Paraguay",
    description="Paraguay's government fees and taxes — separate from the agency's fee: a table of current rates for residency, compliance, company formation and real estate.",
    h1="Costs and rates: the government fee, separate from the agency's fee",
    lead='Two separate blocks: the government fees and taxes you pay directly to Paraguay\'s authorities (which don\'t depend on us), and the cost of our services (full list on the <a href="{uslugi}">"Services"</a> page). We deliberately never blend these into one number — unlike some advertising on this market, where the government fee and the agency\'s fee are presented as a single "turnkey price."',
    fee_cap=["The fee, separate from our services",
             "Diagram: the government fee goes to Paraguay's budget; the agency's fee is a separate amount for services.",
             "Government DNM fee", "paid directly", "to the State of Paraguay",
             "Agency fee", "document review,", "support, compliance",
             "Two separate amounts — not a single \"turnkey price\""],
    h2_duties="Government fees and taxes (current as of the payment date)",
    callout1_label="Important caveat",
    callout1="Some fee amounts reflect data as of July 1, 2025. As of July 1, 2026, migration service (<a href=\"{terminologiya}#dnm\">DNM</a>) fees were revised again (Decreto N° 6225/2026 and Resolución DNM N° 478/2026; the new calculation base is the minimum wage of ₲3,044,000, which rose 5% by July 2026), but as of August 19, 2026, the exact new amounts in guaraníes still weren't published in open sources — per DNM's own news releases, an official fee table exists on the migration service's website, but we couldn't access it directly at the time of checking. Fees are revised annually on July 1 along with the minimum wage — so we confirm the exact current amount for your payment date individually, rather than publish a figure that could be outdated within weeks. The current guaraní exchange rate against the dollar and the ruble is on the <a href=\"{terminologiya}#kurs-valyuty\">\"Terminology\"</a> page.",
    table1_caption="Data as of 07/01/2025, requires confirmation as of the current date",
    table1_head=["Item","Amount","Comment"],
    table1_rows=[
        ["Residencia Temporal fee","25 daily wage units = ₲2,787,550","Raised as of 07/01/2026, new amount pending confirmation"],
        ["Residencia Permanente fee","25 daily wage units = ₲2,787,550","Raised as of 07/01/2026, new amount pending confirmation"],
        ["Residencia Temporal renewal","11 daily wage units = ₲1,226,522","Raised as of 07/01/2026, new amount pending confirmation"],
        ["Change of resident category","10 daily wage units = ₲1,115,020","Raised as of 07/01/2026, new amount pending confirmation"],
        ["Late renewal penalty","6 daily wage units = ₲669,012","Raised as of 07/01/2026, new amount pending confirmation"],
        ["Investor certificate (CIE), SUACE / Investor Pass route","₲2,783,457","Official source — SUACE PDF"],
        ["Naturalization (citizenship) fee","₲43,051","Official source — Poder Judicial"],
    ],
    p_taxes='Taxes after obtaining residency and registering an <a href="{terminologiya}#ruc">RUC</a>: <a href="{terminologiya}#iva">IVA</a> (VAT) — 10% general rate, 5% reduced rate, filed via <a href="{terminologiya}#formulario-120">Formulario 120</a> (filing frequency under the general regime is confirmed individually — sources vary, and the exact rule requires checking against the text of Ley 6380/19 before it\'s shared with a client); the simplified microbusiness regime <a href="{terminologiya}#ire">IRE RESIMPLE</a> — for annual turnover up to ₲80 million, fixed quarterly payments from ₲60,000 to ₲240,000, with the <a href="{terminologiya}#marangatu">Marangatú</a> system auto-generating a zero return if none is filed on time; <a href="{terminologiya}#irp">IRP</a> on personal-services income — 8–10% for income from ₲80 million a year; late-payment penalty — from 4% (up to 1 month late) to 14% (over 5 months late).',
    callout2_label="Gap in sources",
    callout2='The exact current penalties for failing to file under the general IVA/IRP regime (not RESIMPLE) were not found in open sources — these are confirmed individually as part of the ongoing support subscription (see the <a href="{uslugi}">"Services"</a> page).',
    p_realestate='<strong>Example cost structure for a real-estate transaction</strong> (not a rate for a specific property): notary (<a href="{terminologiya}#escribano">escribano</a>) fee — roughly 0.75% of the transaction amount for properties over ₲200 million (1–2% for cheaper ones), plus 10% VAT on that fee; registration fee — around 0.8%; municipal transfer tax — around 0.3%; VAT on the transfer itself, if the seller is a VAT payer — 5% of the presumed tax base (30% of the sale price), i.e., roughly 1.5% of the full property price. Total transaction costs in this example — around 2.3%, excluding VAT on the transfer.',
    p_company='<strong>Company formation costs:</strong> a simplified joint-stock company (<a href="{terminologiya}#eas">EAS</a>) — per estimates from industry business media, around 800 USD excluding government fees (an estimate for a fully online registration; with us, registration is done in person only); <a href="{terminologiya}#sa">S.A.</a> and <a href="{terminologiya}#srl">S.R.L.</a> — roughly 2,000–2,500 USD, including the notarial deed (for an S.A., also the mandatory press publication). No official state fee schedule by line item was found in open access — the amounts given are independent estimates from business media, not an official regulator price list.',
    p_confidence='Thresholds and amounts that our source material explicitly flags as officially unconfirmed (in particular, the specific financial requirements for the 12 applicant categories under DNM Resolution N° 407/2026 — see also <a href="{protsess}">"Process & Timeline"</a>) we do not publish as figures — they are calculated and confirmed individually against DNM\'s current rates and requirements at the time of your application.',
    h2_services="Our services",
    table2_head=["Service","Cost","Comment"],
    table2_rows=[
        ["Residency — Temporal → Permanente package","2,000–4,000 USD","Includes document review and legal support; the amount depends on the applicant category under Resolución 407/2026"],
        ["Ongoing support and compliance","25–50 USD / month","RUC management, monthly filings (including zero returns), case status tracking"],
        ["Company formation (EAS/SRL)","500–1,500 USD","Registration through a local partner, in person only; substantially below some market offers (where prices of 5,000–13,000 USD for the same service also appear)"],
        ["Real-estate due diligence and purchase support","on request","Fixed price for the report, regardless of whether the deal closes"],
        ["Paraguayan citizenship — full support with a lawyer","roughly from 5,000 USD","Lawyer, charges, etc.; the ₲43,051 government fee is paid separately (see the table above); the exact amount is confirmed individually"],
        ["Investor route (SUACE / Investor Pass)","on request","Depends on the chosen investment track"],
        ["Buying and selling a business","on request","Individual assessment, given the absence of a standardized deal market"],
        ["Business relocation","individual","At an hourly rate — depending on the number of employees, whether the Maquila regime is needed, etc."],
    ],
    badge="The fee — a separate line in the agreement",
    p_terms="<strong>Payment terms and what the price doesn't include.</strong> Prices don't include the services of third-party partners (for example, local lawyers and notaries), which are paid separately. The full amount for our service is due by the time the Cédula (CI) application is filed. Special requests (for example, finding housing or renting a car) are always possible, but there's no fixed price list for them: the effort can't be estimated precisely in advance, so they're billed at an hourly rate or as a package.",
    p_final='The government fee is always paid separately from the agency\'s fee — this is stated as a separate line in the written agreement (more on the agreement on the <a href="{o-kompanii}">"About Us"</a> page). Ready to discuss your situation? <a href="{kontakty}">Request a consultation</a>.',
),
"de": dict(
    title="Kosten für Aufenthalt und Leistungen in Paraguay: Gebühren und Preise | Grund Paraguay",
    description="Staatliche Gebühren und Steuern in Paraguay — getrennt vom Honorar der Agentur: Tabelle der aktuellen Preise für Aufenthalt, Compliance, Unternehmen und Immobilien.",
    h1="Preise und Tarife: die Gebühr getrennt vom Honorar der Agentur",
    lead='Zwei getrennte Blöcke: die staatlichen Gebühren und Steuern, die Sie direkt an die Behörden Paraguays zahlen (und die nicht von uns abhängen), und die Kosten unserer Leistungen (vollständige Liste auf der Seite <a href="{uslugi}">„Leistungen"</a>). Wir vermischen diese Beträge grundsätzlich nicht in einer Zahl — anders als ein Teil der Werbung auf dem Markt, wo die staatliche Gebühr und das Honorar der Agentur als ein einziger „Festpreis" dargestellt werden.',
    fee_cap=["Die Gebühr, getrennt vom Honorar",
             "Schema: Die staatliche Gebühr fließt in den Haushalt Paraguays, das Honorar der Agentur ist ein separater Betrag für Leistungen.",
             "Staatliche DNM-Gebühr", "wird direkt gezahlt", "an den Staat Paraguay",
             "Honorar der Agentur", "Dokumentenprüfung,", "Begleitung, Compliance",
             "Zwei getrennte Beträge — kein einheitlicher „Festpreis\""],
    h2_duties="Staatliche Gebühren und Steuern (Aktualität wird zum Zahlungszeitpunkt bestätigt)",
    callout1_label="Wichtiger Hinweis",
    callout1='Ein Teil der Gebührenbeträge basiert auf Daten vom 1. Juli 2025. Seit dem 1. Juli 2026 wurden die Gebühren der Migrationsbehörde (<a href="{terminologiya}#dnm">DNM</a>) erneut angehoben (Decreto Nr. 6225/2026 und Resolución DNM Nr. 478/2026; neue Berechnungsgrundlage ist der Mindestlohn von ₲ 3.044.000, der bis Juli 2026 um 5% gestiegen ist), aber die genauen neuen Beträge in Guaraní waren zum Stand 19.08.2026 weiterhin nicht in offenen Quellen veröffentlicht — laut den Meldungen der DNM existiert eine offizielle Gebührentabelle auf der Website der Migrationsbehörde, auf die wir zum Zeitpunkt der Prüfung jedoch nicht direkt zugreifen konnten. Die Gebühren werden jährlich zum 1. Juli zusammen mit dem Mindestlohn überprüft — daher klären wir den genauen aktuellen Betrag für Ihr Zahlungsdatum individuell, statt eine Zahl zu veröffentlichen, die innerhalb weniger Wochen veraltet sein könnte. Der aktuelle Wechselkurs des Guaraní zu Dollar und Rubel steht auf der Seite <a href="{terminologiya}#kurs-valyuty">„Terminologie"</a>.',
    table1_caption="Daten Stand 01.07.2025, erfordern Bestätigung zum aktuellen Datum",
    table1_head=["Posten","Betrag","Kommentar"],
    table1_rows=[
        ["Gebühr für Residencia Temporal","25 Tagessätze = ₲ 2.787.550","Angehoben seit 01.07.2026, neuer Betrag wird geklärt"],
        ["Gebühr für Residencia Permanente","25 Tagessätze = ₲ 2.787.550","Angehoben seit 01.07.2026, neuer Betrag wird geklärt"],
        ["Verlängerung der Residencia Temporal","11 Tagessätze = ₲ 1.226.522","Angehoben seit 01.07.2026, neuer Betrag wird geklärt"],
        ["Wechsel der Residentenkategorie","10 Tagessätze = ₲ 1.115.020","Angehoben seit 01.07.2026, neuer Betrag wird geklärt"],
        ["Strafe für verspätete Verlängerung","6 Tagessätze = ₲ 669.012","Angehoben seit 01.07.2026, neuer Betrag wird geklärt"],
        ["Investorenzertifikat (CIE), SUACE / Investor-Pass-Weg","₲ 2.783.457","Offizielle Quelle — SUACE-PDF"],
        ["Gebühr für Einbürgerung (Staatsbürgerschaft)","₲ 43.051","Offizielle Quelle — Poder Judicial"],
    ],
    p_taxes='Steuern nach Erhalt des Aufenthaltstitels und Registrierung einer <a href="{terminologiya}#ruc">RUC</a>: <a href="{terminologiya}#iva">IVA</a> — 10% zum allgemeinen Satz, 5% zum ermäßigten Satz, Meldung über das <a href="{terminologiya}#formulario-120">Formulario 120</a> (die Meldehäufigkeit im allgemeinen Regime wird individuell geklärt — die Quellen weichen voneinander ab, die genaue Regel erfordert einen Abgleich mit dem Text des Ley 6380/19 vor der Kommunikation an den Mandanten); vereinfachtes Regime für Kleinunternehmen <a href="{terminologiya}#ire">IRE RESIMPLE</a> — bei einem Jahresumsatz bis ₲ 80 Mio. feste Quartalszahlungen von ₲ 60.000 bis ₲ 240.000, mit automatischer Erstellung einer Nullmeldung durch das System <a href="{terminologiya}#marangatu">Marangatú</a>, falls keine Meldung fristgerecht eingereicht wird; <a href="{terminologiya}#irp">IRP</a> auf persönliche Dienstleistungen — 8 bis 10% bei einem Einkommen ab ₲ 80 Mio. jährlich; Verzugszinsen — von 4% (bis 1 Monat Verzug) bis 14% (über 5 Monate).',
    callout2_label="Lücke in den Quellen",
    callout2='Die genauen aktuellen Strafen für die Nichtabgabe von Meldungen im allgemeinen IVA/IRP-Regime (nicht RESIMPLE) wurden in offenen Quellen nicht gefunden — sie werden individuell im Rahmen des Begleitabonnements geklärt (siehe Seite <a href="{uslugi}">„Leistungen"</a>).',
    p_realestate='<strong>Beispiel für die Kostenstruktur bei einer Immobilientransaktion</strong> (kein Tarif für ein konkretes Objekt): Notarhonorar (<a href="{terminologiya}#escribano">escribano</a>) — ca. 0,75% des Transaktionsbetrags für Objekte über ₲ 200 Mio. (1–2% für günstigere) zuzüglich 10% MwSt. auf das Honorar selbst; Registrierungsgebühr — etwa 0,8%; kommunale Übertragungssteuer — etwa 0,3%; MwSt. auf die Übertragung der Immobilie selbst, sofern der Verkäufer MwSt.-pflichtig ist — 5% der vermuteten Steuerbemessungsgrundlage (30% des Verkaufspreises), also etwa 1,5% des vollen Objektpreises. Insgesamt betragen die Transaktionskosten in diesem Beispiel etwa 2,3%, ohne die MwSt. auf die Übertragung.',
    p_company='<strong>Kosten für die Unternehmensgründung:</strong> vereinfachte Aktiengesellschaft (<a href="{terminologiya}#eas">EAS</a>) — nach Einschätzung von Branchenmedien etwa 800 USD ohne staatliche Gebühren (Schätzung für eine vollständig online durchgeführte Registrierung; bei uns erfolgt die Registrierung nur mit persönlicher Anwesenheit); <a href="{terminologiya}#sa">S.A.</a> und <a href="{terminologiya}#srl">S.R.L.</a> — etwa 2000–2500 USD, einschließlich notarieller Urkunde (bei der S.A. auch die obligatorische Presseveröffentlichung). Eine offizielle staatliche Gebührentabelle nach Posten wurde im offenen Zugang nicht gefunden — die angegebenen Beträge sind unabhängige Schätzungen von Wirtschaftsmedien, kein offizieller Preis der Aufsichtsbehörde.',
    p_confidence='Schwellenwerte und Beträge, die unser Quellenmaterial ausdrücklich als offiziell unbestätigt kennzeichnet (insbesondere die konkreten finanziellen Anforderungen für die 12 Antragstellerkategorien der DNM-Resolution N° 407/2026 — siehe auch <a href="{protsess}">„Prozess und Fristen"</a>), veröffentlichen wir nicht als Zahlen — sie werden individuell anhand der aktuellen Tarife und Anforderungen der DNM zum Zeitpunkt Ihres Antrags berechnet und bestätigt.',
    h2_services="Unsere Leistungen",
    table2_head=["Leistung","Kosten","Kommentar"],
    table2_rows=[
        ["Aufenthaltstitel — Paket Temporal → Permanente","2000–4000 USD","Enthält Dokumentenprüfung und rechtliche Begleitung; der Betrag hängt von der Antragstellerkategorie gemäß Resolución 407/2026 ab"],
        ["Laufende Begleitung und Compliance","25–50 USD / Monat","RUC-Verwaltung, monatliche Meldungen (einschließlich Nullmeldungen), Statuskontrolle des Verfahrens"],
        ["Unternehmensgründung (EAS/SRL)","500–1500 USD","Registrierung über einen Partner vor Ort, nur mit persönlicher Anwesenheit; deutlich unter einem Teil der Marktangebote (dort finden sich auch Preise von 5000–13000 USD für dieselbe Leistung)"],
        ["Prüfung und Kauf von Immobilien (Due Diligence)","auf Anfrage","Festpreis pro Bericht, unabhängig davon, ob das Geschäft zustande kommt"],
        ["Paraguayische Staatsbürgerschaft — vollständige Begleitung mit Anwalt","ab etwa 5000 USD","Anwalt, Gebühren usw.; die staatliche Gebühr von ₲ 43.051 wird separat gezahlt (siehe Tabelle oben); der genaue Betrag wird individuell geklärt"],
        ["Investorenweg (SUACE / Investor Pass)","auf Anfrage","Abhängig vom gewählten Investitionszweig"],
        ["Kauf und Verkauf von Unternehmen","auf Anfrage","Individuelle Bewertung mangels standardisiertem Transaktionsmarkt"],
        ["Unternehmensrelokation","individuell","Nach Stundensatz — abhängig von der Anzahl der Mitarbeiter, ob das Maquila-Regime benötigt wird usw."],
    ],
    badge="Die Gebühr — als separate Zeile in der Vereinbarung",
    p_terms='<strong>Zahlungsbedingungen und was nicht im Preis enthalten ist.</strong> Die Preise enthalten keine Leistungen externer Partner (z. B. Anwälte und Notare vor Ort) — diese werden gesondert bezahlt. Der volle Betrag für unsere Leistung ist bis zur Einreichung des Antrags auf die Cédula (CI) zu zahlen. Sonderwünsche (etwa Wohnungssuche oder Mietwagen) sind jederzeit möglich, aber dafür gibt es keine feste Preisliste: Der Aufwand lässt sich vorab nicht genau abschätzen, daher werden sie nach Stundensatz oder als Paket abgerechnet.',
    p_final='Die staatliche Gebühr wird in jedem Fall getrennt vom Honorar der Agentur gezahlt — dies ist in der schriftlichen Vereinbarung als separate Zeile ausgewiesen (mehr zur Vereinbarung auf der Seite <a href="{o-kompanii}">„Über uns"</a>). Bereit, über Ihre Situation zu sprechen? <a href="{kontakty}">Fordern Sie eine Beratung an</a>.',
),
}

for lang in ["ru","es","en","de"]:
    t = COST[lang]
    l = L(lang)
    fee_icon, fee_color, fee_top, fee_bottom, fee_aria = FEE_SEPARATE_SEAL[lang]
    table1_rows_html = "\n".join(
        f'<tr><td>{r[0]}</td><td class="num">{r[1]}</td><td>{r[2]}</td></tr>' for r in t["table1_rows"]
    )
    table2_rows_html = "\n".join(
        f'<tr><td>{r[0]}</td><td class="num">{r[1]}</td><td>{r[2]}</td></tr>' for r in t["table2_rows"]
    )
    cost_body = f'''
{breadcrumbs([(NAV_LABELS[lang]["home"], l["home"]), (NAV_LABELS[lang]["stoimost"], None)])}
<section class="hero" style="padding-top:24px;">
  <div class="wrap">
    <h1>{t["h1"]}</h1>
    <p class="lead">{t["lead"].format(**l)}</p>
  </div>
</section>
<section style="padding-top:0;">
  <div class="wrap">
    <div class="diagram">{fee_scheme_svg(t["fee_cap"])}</div>

    <div class="prose" style="max-width:100%;padding:0;">
    <h2>{t["h2_duties"]}</h2>
    <div class="callout"><span class="callout-label">{t["callout1_label"]}</span>{t["callout1"].format(**l)}</div>
    </div>

    <table>
      <caption>{t["table1_caption"]}</caption>
      <thead><tr><th>{t["table1_head"][0]}</th><th class="num">{t["table1_head"][1]}</th><th>{t["table1_head"][2]}</th></tr></thead>
      <tbody>
        {table1_rows_html}
      </tbody>
    </table>

    <div class="prose" style="max-width:100%;padding:0;">
    <p>{t["p_taxes"].format(**l)}</p>
    <div class="callout"><span class="callout-label">{t["callout2_label"]}</span>{t["callout2"].format(**l)}</div>

    <p>{t["p_realestate"].format(**l)}</p>

    <p>{t["p_company"].format(**l)}</p>

    <p class="confidence-note">{t["p_confidence"].format(**l)}</p>

    <h2>{t["h2_services"]}</h2>
    </div>

    <table>
      <thead><tr><th>{t["table2_head"][0]}</th><th class="num">{t["table2_head"][1]}</th><th>{t["table2_head"][2]}</th></tr></thead>
      <tbody>
        {table2_rows_html}
      </tbody>
    </table>

    <div class="prose" style="max-width:640px;margin:0;padding:0;">
    <p>{t["p_terms"]}</p>
    <div class="seal seal-float">{seal_svg(fee_icon, fee_top, fee_bottom, "seal-"+fee_color, fee_aria, uid=f"stoimost-{lang}")}</div>
    <p>{t["p_final"].format(**l)}</p>
    </div>
  </div>
</section>
'''
    page("stoimost", lang, t["title"], t["description"], cost_body,
         extra_schema=schema_breadcrumb([(NAV_LABELS[lang]["home"], f"/{lang}/"), (NAV_LABELS[lang]["stoimost"], f"/{lang}/{href_to('stoimost', lang)}")]))

# =========================================================== О КОМПАНИИ / COMPANY

COMPANY = {
"ru": dict(
    title="О компании: команда, договорённость и условия работы в Парагвае | Grund Paraguay",
    description="Агентство сопровождения переезда в Парагвай: письменная договорённость с фиксированной ценой на каждом этапе, реальная команда, партнёры на месте — без анонимности и доплат.",
    h1="О компании: договорённость, фиксированные цены, реальная команда",
    lead="Мы решаем один узкий вопрос: как переехать в Парагвай так, чтобы через два года не разбираться, почему резиденция не продлилась, почему налоговая насчитала штраф за неподанную нулевую декларацию или почему купленный участок земли оказался неотчуждаемым. Это не вопрос удачи или знакомств — это вопрос дисциплины в работе с документами и чёткой договорённости, которая фиксирует объём и стоимость работ для обеих сторон.",
    p_intro_link='Как именно мы оцениваем риски и говорим о них прямо — на странице <a href="{riski}">«Риски и трудности»</a>.',
    h2_team="Команда и полномочия",
    p_team='Работаем как <strong>Fortuna Vida E.A.S.</strong> и с локальными партнёрами на месте — юристами и нотариусами (escribanos), которые ведут сделки по парагвайскому праву, а не дистанционно из России. Это отдельно важно для due diligence по недвижимости и для регистрации компаний, где законный представитель по закону обязан иметь парагвайское гражданство или <a href="{terminologiya}#cedula">Cédula</a>. Состав команды публикуем по мере готовности материалов — открытость по этому пункту для нас так же важна, как фиксированная цена и честный срок (о том, почему мы, наоборот, не называем имена клиентов, — на странице <a href="{konfidentsialnost}">«Конфиденциальность»</a>).',
    h2_contract="Договорённость и условия",
    p_contract='Мы работаем по письменной договорённости, которая фиксирует объём услуг и стоимость до начала работы — без плавающей цены «по факту сложности», которая на этом рынке нередко означает доплаты после того, как клиент уже вовлечён в процесс. Конкретный результат или сроки мы не обещаем: решения принимают государственные органы, а сроки на сайте основаны на нашем опыте и в конкретном случае могут отличаться — это предпринимательский риск, который честно не может взять на себя ни одно агентство. Полная стоимость по каждой услуге — на странице <a href="{stoimost}">«Стоимость и тарифы»</a>. Условия договорённости обсуждаем и показываем на консультации до подписания.',
    badge1="Фиксированная цена в договорённости",
    badge2="Соглашение о конфиденциальности",
    p_crosslink='Как это выглядит на практике — в разделе <a href="{keisy}">«Кейсы и отзывы»</a>: иллюстративные сценарии (не реальные случаи клиентов), включая честный разговор о трудностях первого года. Пошаговый процесс и открытый разговор о рисках — на странице <a href="{kak-my-rabotaem}">«Как мы работаем»</a>.',
    p_final='Мы не обещаем гражданство «за год» и не смешиваем государственную пошлину с нашим гонораром в одной цифре в рекламе — оба этих пункта отражены в письменной договорённости отдельными строками, а не только в тексте на сайте. Готовы обсудить вашу ситуацию — <a href="{kontakty}">оставьте заявку</a>.',
),
"es": dict(
    title="Sobre nosotros: equipo, acuerdo y forma de trabajo en Paraguay | Grund Paraguay",
    description="Agencia de acompañamiento para mudarse a Paraguay: acuerdo por escrito de precio fijo en cada etapa, equipo real, socios en el lugar — sin anonimato ni sobrecostos.",
    h1="Sobre nosotros: acuerdo, precios fijos, un equipo real",
    lead="Resolvemos una sola cuestión concreta: cómo mudarse a Paraguay de forma que, dos años después, no tenga que averiguar por qué no se renovó la residencia, por qué el fisco le aplicó una multa por no presentar una declaración en cero, o por qué el terreno que compró resultó ser inenajenable. No es una cuestión de suerte o de contactos: es una cuestión de disciplina en el manejo de documentos y de un acuerdo claro que fija el alcance y el costo para ambas partes.",
    p_intro_link='Cómo evaluamos exactamente los riesgos y hablamos de ellos sin rodeos, en la página <a href="{riski}">«Riesgos y dificultades»</a>.',
    h2_team="Equipo y facultades",
    p_team='Trabajamos como <strong>Fortuna Vida E.A.S.</strong> y con socios locales en el lugar — abogados y escribanos que gestionan las operaciones conforme al derecho paraguayo, no a distancia desde Rusia. Esto es particularmente importante para el due diligence inmobiliario y para la constitución de empresas, donde el representante legal debe tener por ley ciudadanía paraguaya o <a href="{terminologiya}#cedula">Cédula</a>. Publicamos la composición del equipo a medida que los materiales estén listos — la transparencia en este punto es para nosotros tan importante como el precio fijo y el plazo honesto (sobre por qué, en cambio, no damos los nombres de los clientes, en la página <a href="{konfidentsialnost}">«Confidencialidad»</a>).',
    h2_contract="Acuerdo y condiciones",
    p_contract='Trabajamos con un acuerdo por escrito que fija el alcance de los servicios y el costo antes de comenzar — sin un precio flotante «según la complejidad», que en este mercado suele significar cargos adicionales una vez que el cliente ya está involucrado en el proceso. No prometemos un resultado ni plazos concretos: las decisiones las toman las autoridades, y los plazos del sitio se basan en nuestra experiencia y en cada caso pueden variar — es un riesgo empresarial que ninguna agencia puede asumir con honestidad. El costo completo de cada servicio está en la página <a href="{stoimost}">«Costos y tarifas»</a>. Las condiciones del acuerdo se conversan y se muestran en la consulta previa a la firma.',
    badge1="Precio fijo en el acuerdo",
    badge2="Acuerdo de confidencialidad",
    p_crosslink='Cómo se ve esto en la práctica — en la sección <a href="{keisy}">«Casos y testimonios»</a>: escenarios ilustrativos (no casos reales de clientes), incluida una conversación honesta sobre las dificultades del primer año. El proceso paso a paso y una conversación abierta sobre los riesgos están en la página <a href="{kak-my-rabotaem}">«Cómo trabajamos»</a>.',
    p_final='No prometemos la ciudadanía «en un año» ni mezclamos el arancel estatal con nuestros honorarios en una sola cifra en la publicidad — ambos puntos constan como líneas separadas en el acuerdo por escrito, no solo en el texto del sitio. Si está listo para conversar sobre su situación — <a href="{kontakty}">deje una solicitud</a>.',
),
"en": dict(
    title="About Us: team, agreement and how we work in Paraguay | Grund Paraguay",
    description="A relocation-support agency for Paraguay: a written fixed-price agreement at every stage, a real team, on-the-ground partners — no anonymity, no add-on charges.",
    h1="About Us: a clear agreement, fixed prices, a real team",
    lead="We solve one narrow problem: how to move to Paraguay in a way that means, two years from now, you're not left wondering why your residency wasn't renewed, why the tax office charged a penalty for a zero return you never filed, or why the land you bought turned out to be non-transferable. That's not a matter of luck or connections — it's a matter of discipline in handling documents, and a clear agreement that sets out scope and price for both sides.",
    p_intro_link='How exactly we assess risks and talk about them plainly is on the <a href="{riski}">"Risks & Difficulties"</a> page.',
    h2_team="Team and authority",
    p_team='We operate as <strong>Fortuna Vida E.A.S.</strong> and work with local partners on the ground — lawyers and notaries (escribanos) who handle transactions under Paraguayan law, not remotely from Russia. This matters in particular for real-estate due diligence and for company registration, where the legal representative is required by law to hold Paraguayan citizenship or a <a href="{terminologiya}#cedula">Cédula</a>. We publish our team roster as materials become ready — openness on this point matters to us as much as a fixed price and an honest timeline (on why, conversely, we don\'t publish client names, see the <a href="{konfidentsialnost}">"Confidentiality"</a> page).',
    h2_contract="Agreement and terms",
    p_contract='We work under a written agreement that fixes the scope of services and the price before work begins — no floating "depends on complexity" pricing, which on this market often means add-on charges once the client is already committed to the process. We do not promise a specific result or timeline: decisions are made by the authorities, and the timelines on this site are based on our experience and may vary in an individual case — that is a business risk no agency can honestly take on. The full price of each service is on the <a href="{stoimost}">"Costs and Rates"</a> page. We discuss and show the terms of the agreement at the consultation, before it\'s signed.',
    badge1="Fixed price in the agreement",
    badge2="Confidentiality agreement",
    p_crosslink='What this looks like in practice — in the <a href="{keisy}">"Case Studies"</a> section: illustrative scenarios (not real client cases), including an honest conversation about the difficulties of the first year. The step-by-step process and an open conversation about risks are on the <a href="{kak-my-rabotaem}">"How We Work"</a> page.',
    p_final='We don\'t promise citizenship "in a year," and we don\'t blend the government fee with our own fee into a single advertised number — both points appear as separate lines in the written agreement, not just in text on the site. Ready to discuss your situation? <a href="{kontakty}">Leave a request</a>.',
),
"de": dict(
    title="Über uns: Team, Vereinbarung und Arbeitsweise in Paraguay | Grund Paraguay",
    description="Eine Agentur für die Begleitung des Umzugs nach Paraguay: schriftliche Vereinbarung mit Festpreis für jede Etappe, echtes Team, Partner vor Ort — ohne Anonymität und Zusatzkosten.",
    h1="Über uns: Vereinbarung, Festpreise, ein echtes Team",
    lead="Wir lösen eine eng umrissene Frage: Wie zieht man so nach Paraguay um, dass man zwei Jahre später nicht herausfinden muss, warum der Aufenthaltstitel nicht verlängert wurde, warum das Finanzamt eine Strafe für eine nicht eingereichte Nullmeldung berechnet hat oder warum das gekaufte Grundstück sich als unveräußerlich herausstellte. Das ist keine Frage von Glück oder Beziehungen — es ist eine Frage der Disziplin im Umgang mit Dokumenten und einer klaren Vereinbarung, die Umfang und Kosten für beide Seiten festhält.",
    p_intro_link='Wie genau wir Risiken einschätzen und offen darüber sprechen, auf der Seite <a href="{riski}">„Risiken und Schwierigkeiten"</a>.',
    h2_team="Team und Vollmachten",
    p_team='Wir arbeiten als <strong>Fortuna Vida E.A.S.</strong> und mit lokalen Partnern vor Ort — Anwälten und Notaren (escribanos), die Geschäfte nach paraguayischem Recht abwickeln, nicht aus der Ferne aus Russland. Das ist besonders wichtig für die Immobilien-Due-Diligence und die Unternehmensregistrierung, wo der gesetzliche Vertreter laut Gesetz zwingend die paraguayische Staatsbürgerschaft oder eine paraguayische <a href="{terminologiya}#cedula">Cédula</a> besitzen muss. Die Zusammensetzung des Teams veröffentlichen wir, sobald die Materialien fertig sind — Offenheit ist uns bei diesem Punkt genauso wichtig wie ein Festpreis und eine ehrliche Frist (warum wir umgekehrt keine Namen von Mandanten nennen, auf der Seite <a href="{konfidentsialnost}">„Vertraulichkeit"</a>).',
    h2_contract="Vereinbarung und Bedingungen",
    p_contract='Wir arbeiten mit einer schriftlichen Vereinbarung, die den Leistungsumfang und die Kosten vor Arbeitsbeginn festlegt — ohne einen „je nach Komplexität\" schwankenden Preis, der auf diesem Markt häufig Nachzahlungen bedeutet, nachdem der Mandant bereits in den Prozess eingebunden ist. Ein bestimmtes Ergebnis oder feste Fristen sagen wir nicht zu: Die Entscheidungen treffen die Behörden, und die Fristen auf dieser Website beruhen auf unserer Erfahrung — im Einzelfall können sie abweichen. Das ist ein unternehmerisches Risiko, das keine Agentur ehrlich übernehmen kann. Die vollständigen Kosten jeder Leistung finden Sie auf der Seite <a href="{stoimost}">„Preise"</a>. Die Bedingungen der Vereinbarung besprechen und zeigen wir bei der Beratung vor der Unterzeichnung.',
    badge1="Festpreis in der Vereinbarung",
    badge2="Vertraulichkeitsvereinbarung",
    p_crosslink='Wie sich das in der Praxis zeigt — im Abschnitt <a href="{keisy}">„Fallstudien"</a>: Beispielszenarien (keine realen Mandantenfälle), einschließlich eines ehrlichen Gesprächs über die Schwierigkeiten des ersten Jahres. Den Schritt-für-Schritt-Prozess und ein offenes Gespräch über Risiken finden Sie auf der Seite <a href="{kak-my-rabotaem}">„Wie wir arbeiten"</a>.',
    p_final='Wir versprechen keine Staatsbürgerschaft „in einem Jahr\" und vermischen in der Werbung nicht die staatliche Gebühr mit unserem Honorar in einer Zahl — beide Punkte sind in der schriftlichen Vereinbarung als separate Zeilen ausgewiesen, nicht nur im Text der Website. Bereit, über Ihre Situation zu sprechen? <a href="{kontakty}">Fordern Sie eine Beratung an</a>.',
),
}

for lang in ["ru","es","en","de"]:
    t = COMPANY[lang]
    l = L(lang)
    company_seal_row = "\n      ".join(
        f'<div class="seal">{seal_svg(icon, top, bottom, "seal-"+color, aria, uid=f"okompanii-{lang}-{i}")}</div>'
        for i, (icon, color, top, bottom, aria) in enumerate(COMPANY_SEALS[lang])
    )
    company_body = f'''
{breadcrumbs([(NAV_LABELS[lang]["home"], l["home"]), (NAV_LABELS[lang]["o-kompanii"], None)])}
<section class="hero" style="padding-top:24px;">
  <div class="wrap">
    <h1>{t["h1"]}</h1>
    <p class="lead">{t["lead"]}</p>
    <p>{t["p_intro_link"].format(**l)}</p>
  </div>
</section>
<section style="padding-top:0;">
  <div class="prose">
    <h2>{t["h2_team"]}</h2>
    <p>{t["p_team"].format(**l)}</p>

    <h2>{t["h2_contract"]}</h2>
    <p>{t["p_contract"].format(**l)}</p>

    <div class="seal-row" style="justify-content:flex-start;">
      {company_seal_row}
    </div>

    <p>{t["p_crosslink"].format(**l)}</p>

    <p>{t["p_final"].format(**l)}</p>
  </div>
</section>
'''
    page("o-kompanii", lang, t["title"], t["description"], company_body,
         extra_schema=schema_breadcrumb([(NAV_LABELS[lang]["home"], f"/{lang}/"), (NAV_LABELS[lang]["o-kompanii"], f"/{lang}/{href_to('o-kompanii', lang)}")]))

# ================================================= КОНФИДЕНЦИАЛЬНОСТЬ / PRIVACY

PRIVACY = {
"ru": dict(
    title="Конфиденциальность данных клиентов при переезде в Парагвай | Grund Paraguay",
    description="Как агентство защищает личные, финансовые и иммиграционные данные клиентов при переезде в Парагвай — соглашение о конфиденциальности как часть соглашения с клиентом.",
    h1="Соглашение о конфиденциальности данных клиента",
    lead='Мы работаем с людьми, для которых переезд — чувствительная тема: часть клиентов принимает решение о переезде по политическим или финансовым причинам и не заинтересована в том, чтобы детали её дела где-либо всплывали. Отдельно рынок посреднических услуг по переезду в целом репутационно токсичен из-за случаев мошенничества — поэтому для нас важно показать, что мы относимся к данным клиента так же серьёзно, как к деньгам и документам (подробнее о том, как мы работаем по письменной договорённости в целом, — на странице <a href="{o-kompanii}">«О компании»</a>).',
    callout_mix_label="Важно не путать",
    callout_mix='Это соглашение о конфиденциальности — не футерная «политика обработки данных сайта» (та регулирует куки, формы и аналитику и находится в подвале сайта отдельно — см. <a href="{politika}">«Политика конфиденциальности сайта»</a>), а часть основного соглашения, которое мы подписываем с каждым клиентом.',
    h2_scope="Что относится к защищаемой информации",
    p_scope='Личные и паспортные данные; статус и детали иммиграционного дела на всех этапах — от подачи на временную резиденцию (<a href="{terminologiya}#residencia-temporal">Residencia Temporal</a>) до рассмотрения дела о гражданстве в Верховном суде (<a href="{terminologiya}#corte-suprema">Corte Suprema de Justicia</a>); финансовые данные по сделкам с недвижимостью и бизнесом; вся переписка и документы, переданные нам в рамках нашей совместной работы.',
    h2_wont="Что мы обязуемся не делать",
    p_wont="Мы не публикуем и не передаём эту информацию третьим лицам без письменного согласия клиента. Это правило распространяется и на наших партнёров по сделке — юристов, нотариусов (escribanos), банки, — для которых действует тот же режим конфиденциальности в рамках совместной работы над вашим делом.",
    h2_cases="Как используются типичные истории клиентов",
    p_cases='В разделе <a href="{keisy}">«Кейсы и отзывы»</a> мы публикуем только иллюстративные сценарии — обезличенные и типичные, а не реальные случаи клиентов: без имён, фотографий и деталей, по которым дело можно было бы узнать. Сроки и условия в этих историях реалистичны и опираются на нашу практику, но сама история и профиль клиента — обобщённые, а не пересказ конкретного дела без разрешения.',
    h2_storage="Хранение и удаление данных",
    p_storage="Данные клиента хранятся на срок, необходимый для ведения дела и исполнения соглашения, и могут быть удалены по запросу клиента после завершения работы — за исключением документов, которые мы обязаны хранить по требованиям законодательства.",
    h2_contact="Куда обращаться",
    p_contact='По любым вопросам, связанным с этим соглашением или обработкой ваших данных, можно обратиться напрямую через страницу <a href="{kontakty}">«Контакты»</a>.',
    p_confidence='Образец соглашения о конфиденциальности пока готовится — актуальный статус см. на странице «Контакты» или уточните напрямую; оно автоматически прикладывается к основному соглашению при оформлении заявки на услугу.',
),
"es": dict(
    title="Confidencialidad de los datos de clientes al mudarse a Paraguay | Grund Paraguay",
    description="Cómo protege la agencia los datos personales, financieros y migratorios de sus clientes al mudarse a Paraguay — el acuerdo de confidencialidad como parte del acuerdo con el cliente.",
    h1="Acuerdo de confidencialidad de los datos del cliente",
    lead='Trabajamos con personas para quienes la mudanza es un tema sensible: parte de los clientes toma la decisión de mudarse por razones políticas o financieras y no le interesa que los detalles de su caso salgan a la luz. Además, el mercado de servicios de intermediación para la mudanza es, en general, reputacionalmente tóxico por casos de fraude — por eso es importante para nosotros demostrar que tratamos los datos del cliente con la misma seriedad que el dinero y los documentos (más sobre cómo trabajamos con el acuerdo por escrito en general, en la página <a href="{o-kompanii}">«Sobre nosotros»</a>).',
    callout_mix_label="Importante no confundir",
    callout_mix='Este acuerdo de confidencialidad no es la «política de tratamiento de datos del sitio» del pie de página (esa regula cookies, formularios y analítica, y está en el pie del sitio por separado — ver <a href="{politika}">«Política de privacidad del sitio»</a>), sino parte del acuerdo principal que firmamos con cada cliente.',
    h2_scope="Qué se considera información protegida",
    p_scope='Datos personales y de pasaporte; el estado y los detalles del trámite migratorio en todas sus etapas — desde la solicitud de residencia temporal (<a href="{terminologiya}#residencia-temporal">Residencia Temporal</a>) hasta el análisis del expediente de ciudadanía en la Corte Suprema de Justicia (<a href="{terminologiya}#corte-suprema">Corte Suprema de Justicia</a>); datos financieros de operaciones inmobiliarias y de negocios; toda la correspondencia y los documentos que nos entregue en el marco de nuestro trabajo conjunto.',
    h2_wont="Qué nos comprometemos a no hacer",
    p_wont="No publicamos ni transferimos esta información a terceros sin el consentimiento por escrito del cliente. Esta regla también se aplica a nuestros socios en la operación — abogados, escribanos, bancos —, para quienes rige el mismo régimen de confidencialidad en el trabajo conjunto sobre su caso.",
    h2_cases="Cómo se usan las historias típicas de clientes",
    p_cases='En la sección <a href="{keisy}">«Casos y testimonios»</a> publicamos únicamente escenarios ilustrativos — típicos y anonimizados, no casos reales de clientes: sin nombres, fotos ni detalles por los que se pueda identificar el caso. Los plazos y condiciones de estas historias son realistas y se basan en nuestra práctica, pero la historia y el perfil del cliente están generalizados, no son el relato de un caso concreto sin autorización.',
    h2_storage="Conservación y eliminación de datos",
    p_storage="Los datos del cliente se conservan durante el plazo necesario para gestionar el caso y cumplir el acuerdo, y pueden eliminarse a pedido del cliente una vez finalizado el trabajo — salvo los documentos que estamos obligados a conservar por requisitos legales.",
    h2_contact="Dónde consultar",
    p_contact='Para cualquier consulta relacionada con este acuerdo o con el tratamiento de sus datos, puede escribirnos directamente a través de la página <a href="{kontakty}">«Contacto»</a>.',
    p_confidence='El modelo del acuerdo de confidencialidad está en preparación — consulte el estado actual en la página «Contacto» o pregúntenos directamente; se adjunta automáticamente al acuerdo principal al formalizar una solicitud de servicio.',
),
"en": dict(
    title="Confidentiality of client data when relocating to Paraguay | Grund Paraguay",
    description="How the agency protects clients' personal, financial, and immigration data when relocating to Paraguay — a confidentiality agreement as part of the client agreement.",
    h1="Client data confidentiality agreement",
    lead='We work with people for whom relocation is a sensitive matter: some clients decide to relocate for political or financial reasons and have no interest in the details of their case surfacing anywhere. Separately, the relocation-intermediary market as a whole carries a reputational stigma due to cases of fraud — which is why it matters to us to show that we treat client data with the same seriousness as money and documents (more on how we work under a written agreement generally is on the <a href="{o-kompanii}">"About Us"</a> page).',
    callout_mix_label="Important — don't confuse the two",
    callout_mix='This confidentiality agreement is not the site\'s footer "data processing policy" (that one governs cookies, forms, and analytics, and lives in the site footer separately — see the <a href="{politika}">"Site Privacy Policy"</a>); it is part of the main agreement we sign with every client.',
    h2_scope="What counts as protected information",
    p_scope='Personal and passport data; the status and details of the immigration case at every stage — from the Residencia Temporal application (<a href="{terminologiya}#residencia-temporal">Residencia Temporal</a>) to the review of a citizenship case at the Supreme Court (<a href="{terminologiya}#corte-suprema">Corte Suprema de Justicia</a>); financial data related to real-estate and business deals; all correspondence and documents provided to us in the course of our work.',
    h2_wont="What we commit not to do",
    p_wont="We do not publish or share this information with third parties without the client's written consent. This rule also extends to our deal partners — lawyers, notaries (escribanos), banks — who are bound by the same confidentiality regime while working jointly on your case.",
    h2_cases="How typical client stories are used",
    p_cases='On the <a href="{keisy}">"Case Studies"</a> page we publish only illustrative scenarios — anonymized and typical, not real client cases: no names, photos, or details that would allow a case to be identified. The timelines and terms in these stories are realistic and grounded in our practice, but the story and client profile themselves are composites — not a retelling of a specific case without permission.',
    h2_storage="Data retention and deletion",
    p_storage="Client data is retained for as long as needed to handle the case and fulfill the agreement, and can be deleted at the client's request once the work is complete — except for documents we are legally required to retain.",
    h2_contact="Where to reach us",
    p_contact='For any questions related to this agreement or to how your data is handled, you can reach us directly via the <a href="{kontakty}">"Contact"</a> page.',
    p_confidence='A sample confidentiality agreement is still being prepared — see the current status on the Contact page or ask us directly; it is automatically attached to the main agreement when a service request is finalized.',
),
"de": dict(
    title="Vertraulichkeit von Mandantendaten beim Umzug nach Paraguay | Grund Paraguay",
    description="Wie die Agentur persönliche, finanzielle und einwanderungsrechtliche Daten von Mandanten beim Umzug nach Paraguay schützt — die Vertraulichkeitsvereinbarung als Teil der Mandantenvereinbarung.",
    h1="Vertraulichkeitsvereinbarung für Mandantendaten",
    lead='Wir arbeiten mit Menschen, für die der Umzug ein sensibles Thema ist: Ein Teil der Mandanten trifft die Umzugsentscheidung aus politischen oder finanziellen Gründen und hat kein Interesse daran, dass Details ihres Falls irgendwo auftauchen. Zudem ist der Markt für Vermittlungsleistungen beim Umzug insgesamt reputativ belastet durch Betrugsfälle — deshalb ist es uns wichtig zu zeigen, dass wir mit Mandantendaten genauso sorgfältig umgehen wie mit Geld und Dokumenten (mehr dazu, wie wir generell mit der schriftlichen Vereinbarung arbeiten, auf der Seite <a href="{o-kompanii}">„Über uns"</a>).',
    callout_mix_label="Wichtig, nicht zu verwechseln",
    callout_mix='Diese Vertraulichkeitsvereinbarung ist nicht die „Datenverarbeitungsrichtlinie der Website\" im Footer (diese regelt Cookies, Formulare und Analytics und befindet sich gesondert im Footer der Website — siehe <a href="{politika}">„Datenschutzerklärung der Website"</a>), sondern Teil der Hauptvereinbarung, die wir mit jedem Mandanten unterzeichnen.',
    h2_scope="Was als zu schützende Information gilt",
    p_scope='Persönliche Daten und Passdaten; Status und Details des Einwanderungsfalls in allen Etappen — von der Beantragung des befristeten Aufenthalts (<a href="{terminologiya}#residencia-temporal">Residencia Temporal</a>) bis zur Prüfung eines Staatsbürgerschaftsfalls beim Obersten Gerichtshof (<a href="{terminologiya}#corte-suprema">Corte Suprema de Justicia</a>); Finanzdaten zu Immobilien- und Geschäftstransaktionen; die gesamte Korrespondenz und Dokumente, die uns im Rahmen der Zusammenarbeit übergeben werden.',
    h2_wont="Was wir uns verpflichten, nicht zu tun",
    p_wont="Wir veröffentlichen oder übermitteln diese Informationen nicht an Dritte ohne die schriftliche Zustimmung des Mandanten. Diese Regel gilt auch für unsere Geschäftspartner — Anwälte, Notare (escribanos), Banken —, für die im Rahmen der gemeinsamen Arbeit an Ihrem Fall dieselbe Vertraulichkeitsregelung gilt.",
    h2_cases="Wie typische Mandantengeschichten verwendet werden",
    p_cases='Im Abschnitt <a href="{keisy}">„Fallstudien"</a> veröffentlichen wir nur Beispielszenarien — anonymisiert und typisch, keine realen Mandantenfälle: ohne Namen, Fotos und Details, an denen der Fall erkennbar wäre. Die Fristen und Bedingungen in diesen Geschichten sind realistisch und basieren auf unserer Praxis, aber die Geschichte und das Mandantenprofil selbst sind verallgemeinert — keine Nacherzählung eines konkreten Falls ohne Erlaubnis.',
    h2_storage="Speicherung und Löschung von Daten",
    p_storage="Mandantendaten werden für den zur Bearbeitung des Falls und zur Erfüllung der Vereinbarung erforderlichen Zeitraum gespeichert und können nach Abschluss der Arbeit auf Antrag des Mandanten gelöscht werden — mit Ausnahme von Dokumenten, die wir gesetzlich aufbewahren müssen.",
    h2_contact="Wohin man sich wenden kann",
    p_contact='Bei allen Fragen zu dieser Vereinbarung oder zur Verarbeitung Ihrer Daten können Sie sich direkt über die Seite <a href="{kontakty}">„Kontakt"</a> an uns wenden.',
    p_confidence='Ein Muster der Vertraulichkeitsvereinbarung wird noch vorbereitet — den aktuellen Status finden Sie auf der Kontaktseite oder fragen Sie direkt nach; sie wird der Hauptvereinbarung bei der Erstellung einer Serviceanfrage automatisch beigefügt.',
),
}

for lang in ["ru","es","en","de"]:
    t = PRIVACY[lang]
    l = L(lang)
    privacy_body = f'''
{breadcrumbs([(NAV_LABELS[lang]["home"], l["home"]), (NAV_LABELS[lang]["konfidentsialnost"], None)])}
<section class="hero" style="padding-top:24px;">
  <div class="wrap">
    <h1>{t["h1"]}</h1>
    <p class="lead">{t["lead"].format(**l)}</p>
  </div>
</section>
<section style="padding-top:0;">
  <div class="prose">
    <div class="callout"><span class="callout-label">{t["callout_mix_label"]}</span>{t["callout_mix"].format(**l)}</div>

    <h2>{t["h2_scope"]}</h2>
    <p>{t["p_scope"].format(**l)}</p>

    <h2>{t["h2_wont"]}</h2>
    <p>{t["p_wont"]}</p>

    <h2>{t["h2_cases"]}</h2>
    <p>{t["p_cases"].format(**l)}</p>

    <h2>{t["h2_storage"]}</h2>
    <p>{t["p_storage"]}</p>

    <h2>{t["h2_contact"]}</h2>
    <p>{t["p_contact"].format(**l)}</p>

    <p class="confidence-note">{t["p_confidence"]}</p>
  </div>
</section>
'''
    page("konfidentsialnost", lang, t["title"], t["description"], privacy_body,
         extra_schema=schema_breadcrumb([(NAV_LABELS[lang]["home"], f"/{lang}/"), (NAV_LABELS[lang]["konfidentsialnost"], f"/{lang}/{href_to('konfidentsialnost', lang)}")]))
