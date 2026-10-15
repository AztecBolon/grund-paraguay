#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Главная и Услуги — ru/es/en"""
from build import page, breadcrumbs, schema_breadcrumb, ORG_SCHEMA, ICONS, DOMAIN, href_to, NAV_LABELS, chart_slider, seal_svg, hero_photo_slider
from chart_data import build_topics, render_topic, UI_LABELS

def L(lang):
    return {pid: href_to(pid, lang) for pid in
            ["home","uslugi","protsess","riski","stoimost","o-kompanii","konfidentsialnost","keisy","kontakty","terminologiya","kak-my-rabotaem",
             "dok-temporal","dok-permanente","dok-investor","dok-grazhdanstvo","usluga-residencia","usluga-investor","usluga-relocation",
             "usluga-medicina","usluga-compliance","usluga-citizenship","usluga-realestate","usluga-company","usluga-business"]}

# =========================================================== ГЛАВНАЯ / HOME

HOME = {
"ru": dict(
    title="Переезд в Парагвай без сюрпризов — юридическое сопровождение | Grund Paraguay",
    description="Переезд в Парагвай с чёткой договорённостью и фиксированными ценами: сроки ВНЖ и гражданства по опыту, разбор рисков, реальная команда — без обещаний «за один год».",
    kicker="Grund Paraguay — юридическое сопровождение переезда",
    h1="Переезд в Парагвай без сюрпризов",
    lead="Мы сопровождаем переезд в Парагвай так, как это делает дотошный юрист, а не агентство, которое обещает результат к пятнице. Письменная договорённость фиксирует объём работ и стоимость до того, как вы платите первый доллар; сроки на сайте — по нашему опыту, а не рекламные, и в конкретном случае могут отличаться.",
    cta1="Оставить заявку на консультацию", cta2="Смотреть услуги",
    services_h2="Услуги",
    svc_residencia_title="Резидентура (ВНЖ)", svc_residencia_desc="Temporal → Permanente, проверка документов до подачи.",
    svc_realestate_title="Недвижимость", svc_realestate_desc="Due diligence по конкретному объекту, а не каталог.",
    svc_compliance_title="Сопровождение и комплаенс", svc_compliance_desc="RUC, ежемесячная отчётность, контроль статуса дела.",
    more="Подробнее →",
    final_h2="Готовы обсудить свою ситуацию?",
    final_p="Если вы только начинаете разбираться в теме — скачайте бесплатный гайд «С чего начать переезд в Парагвай». Если готовы — оставьте заявку на консультацию.",
    final_cta="Оставить заявку",
),
"es": dict(
    title="Mudarse a Paraguay sin sorpresas — asesoría legal | Grund Paraguay",
    description="Mudanza a Paraguay con un acuerdo claro y precios fijos: plazos de residencia y ciudadanía según nuestra experiencia, análisis de riesgos, equipo real — sin promesas de «un año».",
    kicker="Grund Paraguay — asesoría legal para la mudanza",
    h1="Mudarse a Paraguay sin sorpresas",
    lead="Acompañamos la mudanza a Paraguay como lo haría un abogado meticuloso, no una agencia que promete resultados para el viernes. Un acuerdo por escrito fija el alcance del trabajo y el precio antes de que pague el primer dólar; los plazos en el sitio se basan en nuestra experiencia, no en la publicidad, y en cada caso pueden variar.",
    cta1="Solicitar una consulta", cta2="Ver servicios",
    services_h2="Servicios",
    svc_residencia_title="Residencia", svc_residencia_desc="Temporal → Permanente, verificación de documentos antes de presentar.",
    svc_realestate_title="Inmuebles", svc_realestate_desc="Due diligence sobre un inmueble concreto, no un catálogo.",
    svc_compliance_title="Acompañamiento y cumplimiento", svc_compliance_desc="RUC, declaraciones mensuales, control del estado del trámite.",
    more="Más información →",
    final_h2="¿Listo para hablar de su situación?",
    final_p="Si recién empieza a informarse — descargue la guía gratuita «Por dónde empezar a mudarse a Paraguay». Si ya está listo — solicite una consulta.",
    final_cta="Solicitar consulta",
),
"en": dict(
    title="Move to Paraguay without surprises — legal support | Grund Paraguay",
    description="Move to Paraguay with a clear fixed-price agreement: timelines for residency and citizenship based on experience, an honest look at risks, a real team — no promises of \"one year.\"",
    kicker="Grund Paraguay — legal support for your move",
    h1="Move to Paraguay without surprises",
    lead="We support your move to Paraguay the way a meticulous lawyer would, not an agency promising results by Friday. A written agreement fixes the scope of work and the price before you pay a single dollar; the timelines on this site are based on our experience, not marketing copy, and may vary in an individual case.",
    cta1="Request a consultation", cta2="See our services",
    services_h2="Services",
    svc_residencia_title="Residency", svc_residencia_desc="Temporal → Permanente, documents checked before filing.",
    svc_realestate_title="Real estate", svc_realestate_desc="Due diligence on a specific property, not a catalog.",
    svc_compliance_title="Ongoing compliance", svc_compliance_desc="RUC, monthly filings, case status tracking.",
    more="Learn more →",
    final_h2="Ready to discuss your situation?",
    final_p="Just getting started? Download the free guide \"Where to start moving to Paraguay.\" Ready now? Request a consultation.",
    final_cta="Request a consultation",
),
"de": dict(
    title="Ohne Überraschungen nach Paraguay auswandern — Rechtsbegleitung | Grund Paraguay",
    description="Umzug nach Paraguay mit klarer Vereinbarung und Festpreisen: Fristen nach Erfahrung für Aufenthaltstitel und Staatsbürgerschaft, Risikoanalyse, echtes Team — ohne Versprechen „in einem Jahr\".",
    kicker="Grund Paraguay — Rechtsbegleitung für Ihren Umzug",
    h1="Ohne Überraschungen nach Paraguay auswandern",
    lead="Wir begleiten Ihren Umzug nach Paraguay so, wie es ein gründlicher Anwalt tun würde — nicht wie eine Agentur, die Ergebnisse bis Freitag verspricht. Eine schriftliche Vereinbarung legt Umfang und Preis fest, bevor Sie den ersten Dollar zahlen; die Fristen auf dieser Website beruhen auf unserer Erfahrung, nicht auf Werbung — im Einzelfall können sie abweichen.",
    cta1="Beratung anfragen", cta2="Leistungen ansehen",
    services_h2="Leistungen",
    svc_residencia_title="Aufenthaltstitel", svc_residencia_desc="Temporal → Permanente, Dokumentenprüfung vor der Einreichung.",
    svc_realestate_title="Immobilien", svc_realestate_desc="Due Diligence für ein konkretes Objekt, kein Katalog.",
    svc_compliance_title="Begleitung und Compliance", svc_compliance_desc="RUC, monatliche Meldungen, Statuskontrolle des Verfahrens.",
    more="Mehr erfahren →",
    final_h2="Bereit, über Ihre Situation zu sprechen?",
    final_p="Fangen Sie gerade erst an? Laden Sie den kostenlosen Leitfaden „Womit beginnt der Umzug nach Paraguay\" herunter. Schon bereit? Fordern Sie eine Beratung an.",
    final_cta="Anfrage stellen",
),
}

# Фоновый фотослайдер hero (13.08.2026, заготовка — по решению заказчика: «H1 надо вынести
# из слайдера», текст первого фото при загрузке = неизменный HOME[lang]["lead"], для
# остальных 5 фото — новые короткие подписи, привязанные к настроению кадра, а не к фактам
# о переезде (числа/сроки — только в основном lead и в разделах ниже, не здесь).
#
# ДОЛГ: локация снимков со скайлайном на другом берегу реки (skyline-sunset и, отчасти,
# beach-day-city) не подтверждена — это Энкарнасьон или Посадас (Аргентина), photographer
# не уточнил. Подписи ниже намеренно НЕ называют конкретный город на этих двух фото —
# см. design/plan-foto-kontenta.md, раздел «долги». Остальные 4 фото (сельский пейзаж,
# два пляжных дневных/закатных кадра, пустой берег) локацию не называют вовсе — риска нет.
HERO_PHOTOS = {
"ru": [
    dict(src="../assets/img/hero/countryside.webp",
         alt="Сельский пейзаж на юге Парагвая — поля и пастбища у реки",
         lead=HOME["ru"]["lead"]),
    dict(src="../assets/img/hero/riverbeach-day.webp",
         alt="Пляжный клуб на реке в Парагвае днём",
         lead="Пляж на реке в получасе от центра — часть обычной недели, а не курортная открытка."),
    dict(src="../assets/img/hero/beach-sunset-people.webp",
         alt="Закат на пляже у реки в Парагвае",
         lead="Закат у воды — не повод для отпуска, а часть будничного вечера."),
    dict(src="../assets/img/hero/skyline-sunset.webp",
         alt="Закат над рекой на юге Парагвая",
         lead="На юге Парагвая вечера не хочется торопить."),
    dict(src="../assets/img/hero/beach-empty-sunset.webp",
         alt="Пустой берег реки на закате",
         lead="Пустой берег и час без спешки — ровно то, ради чего многие сюда переезжают."),
    dict(src="../assets/img/hero/beach-day-city.webp",
         alt="Городской пляж на юге Парагвая днём",
         lead="Город и река — в одной прогулке, а не в разных концах жизни."),
],
"es": [
    dict(src="../assets/img/hero/countryside.webp",
         alt="Paisaje rural en el sur de Paraguay — campos y pasturas junto al río",
         lead=HOME["es"]["lead"]),
    dict(src="../assets/img/hero/riverbeach-day.webp",
         alt="Un club de playa junto al río en Paraguay, de día",
         lead="Una playa de río a media hora del centro — parte de una semana común, no una postal de vacaciones."),
    dict(src="../assets/img/hero/beach-sunset-people.webp",
         alt="Atardecer en una playa junto al río en Paraguay",
         lead="Un atardecer junto al agua no es motivo de vacaciones, sino parte de una tarde cualquiera."),
    dict(src="../assets/img/hero/skyline-sunset.webp",
         alt="Atardecer sobre el río en el sur de Paraguay",
         lead="En el sur de Paraguay no dan ganas de apurar los atardeceres."),
    dict(src="../assets/img/hero/beach-empty-sunset.webp",
         alt="Orilla vacía del río al atardecer",
         lead="Una orilla vacía y una hora sin apuro — justamente lo que muchos buscan al mudarse aquí."),
    dict(src="../assets/img/hero/beach-day-city.webp",
         alt="Playa urbana en el sur de Paraguay durante el día",
         lead="La ciudad y el río, a un paseo de distancia — no en extremos distintos de la vida."),
],
"en": [
    dict(src="../assets/img/hero/countryside.webp",
         alt="Rural landscape in southern Paraguay — fields and pastures by the river",
         lead=HOME["en"]["lead"]),
    dict(src="../assets/img/hero/riverbeach-day.webp",
         alt="A river beach club in Paraguay during the day",
         lead="A river beach half an hour from downtown — part of an ordinary week, not a postcard."),
    dict(src="../assets/img/hero/beach-sunset-people.webp",
         alt="Sunset at a riverside beach in Paraguay",
         lead="A sunset by the water isn't a vacation moment here — it's part of an ordinary evening."),
    dict(src="../assets/img/hero/skyline-sunset.webp",
         alt="Sunset over the river in southern Paraguay",
         lead="In southern Paraguay, evenings aren't something you want to rush."),
    dict(src="../assets/img/hero/beach-empty-sunset.webp",
         alt="Empty riverbank at sunset",
         lead="An empty shore and an unhurried hour — exactly what many people move here for."),
    dict(src="../assets/img/hero/beach-day-city.webp",
         alt="An urban beach in southern Paraguay during the day",
         lead="The city and the river, one walk apart — not opposite ends of daily life."),
],
"de": [
    dict(src="../assets/img/hero/countryside.webp",
         alt="Ländliche Landschaft im Süden Paraguays — Felder und Weiden am Fluss",
         lead=HOME["de"]["lead"]),
    dict(src="../assets/img/hero/riverbeach-day.webp",
         alt="Ein Flussstrand-Club in Paraguay am Tag",
         lead="Ein Flussstrand eine halbe Stunde vom Zentrum — Teil einer gewöhnlichen Woche, keine Urlaubspostkarte."),
    dict(src="../assets/img/hero/beach-sunset-people.webp",
         alt="Sonnenuntergang an einem Flussstrand in Paraguay",
         lead="Ein Sonnenuntergang am Wasser ist hier kein Urlaubsmoment, sondern Teil eines gewöhnlichen Abends."),
    dict(src="../assets/img/hero/skyline-sunset.webp",
         alt="Sonnenuntergang über dem Fluss im Süden Paraguays",
         lead="Im Süden Paraguays möchte man die Abende nicht hetzen."),
    dict(src="../assets/img/hero/beach-empty-sunset.webp",
         alt="Leeres Flussufer bei Sonnenuntergang",
         lead="Ein leeres Ufer und eine Stunde ohne Eile — genau das, weswegen viele hierher ziehen."),
    dict(src="../assets/img/hero/beach-day-city.webp",
         alt="Ein Stadtstrand im Süden Paraguays am Tag",
         lead="Stadt und Fluss, einen Spaziergang voneinander entfernt — keine gegensätzlichen Enden des Alltags."),
],
}

HERO_UI = {
    "ru": dict(region="Фото Парагвая — слайдер", prev="Предыдущее фото", next="Следующее фото",
               pause="Остановить автопрокрутку", play="Включить автопрокрутку",
               slide_n=lambda i, n, alt: f"Фото {i} из {n}: {alt}"),
    "es": dict(region="Fotos de Paraguay — carrusel", prev="Foto anterior", next="Foto siguiente",
               pause="Pausar el avance automático", play="Reanudar el avance automático",
               slide_n=lambda i, n, alt: f"Foto {i} de {n}: {alt}"),
    "en": dict(region="Photos of Paraguay — slider", prev="Previous photo", next="Next photo",
               pause="Pause autoplay", play="Resume autoplay",
               slide_n=lambda i, n, alt: f"Photo {i} of {n}: {alt}"),
    "de": dict(region="Fotos aus Paraguay — Slider", prev="Vorheriges Foto", next="Nächstes Foto",
               pause="Automatischen Wechsel anhalten", play="Automatischen Wechsel fortsetzen",
               slide_n=lambda i, n, alt: f"Foto {i} von {n}: {alt}"),
}

# Слайдер с инфографикой на Главной (12.08.2026, вторая версия) — те же 8 тем и настоящих
# графика динамики, что и на хабе «Парагвай для переезда» (pages_paragvay_hub.py), переведены
# на все 4 языка, т.к. Главная, в отличие от хаба, полностью многоязычна. Без ссылок
# «Подробнее»: хаб (куда логично вели бы 6 из 8 слайдов) — RU-only раздел, ссылка на него с
# ES/EN/DE-версий Главной вела бы в никуда. Данные и переводы — chart_data.py.
STATS_H2 = {"ru": "Парагвай в цифрах", "es": "Paraguay en cifras", "en": "Paraguay in numbers", "de": "Paraguay in Zahlen"}

# Полоса доверия «печатями» (12.08.2026, седьмая правка) — по замечанию заказчика:
# кольцевая надпись была смещена к внешнему кольцу (не по центру зазора — поправлено
# в геометрии seal_svg()), внизу печати пустовало место. Решение — вернуть вторую,
# поясняющую надпись, но не под печатью (как было в пятой правке), а ВТОРОЙ дугой
# внизу самой печати; левый/правый бока зазора между кольцами заполнены звёздами,
# чтобы по всему кольцу не оставалось пустых промежутков. Каждый кортеж: (иконка из
# ICONS, цвет, top — короткий заголовок сверху, bottom — короткое пояснение снизу
# (те же формулировки, что были в пятой правке до того, как их временно объединили
# с заголовком), aria — полный смысл с источником для читалок экрана).
# Печати кликабельны (12.08.2026, декор-фаза 1.1) — каждая ведёт на страницу-первоисточник
# того же утверждения, где оно повторено отдельной "эхо"-печатью: stamp/red → «Стоимость»,
# shield/blue → «О компании» (там же конфиденциальность), honest/red → «Процесс и сроки»
# (там же первоисточник цитаты DNM), contract/blue → «О компании» (тот же договор). 6-й элемент
# кортежа — pid страницы-цели для L(lang).
SEALS = {
"ru": [
    ("stamp", "red", "Фиксированная цена", "Сумма не меняется",
     "Фиксированная цена: сумма не меняется в процессе работы", "stoimost"),
    ("shield", "blue", "Конфиденциальность", "Соглашение с каждым клиентом",
     "Конфиденциальность: отдельное соглашение с каждым клиентом", "o-kompanii"),
    ("honest", "red", "Без ложных обещаний", "Срок 7–8 лет, не «за год»",
     "Без ложных обещаний: реальный срок — 7–8 лет, а не «за один год», по словам директора DNM (ABC Color, 04.05.2026)", "protsess"),
    ("contract", "blue", "Договорённость до оплаты", "Условия — письменно",
     "Договорённость до оплаты: условия зафиксированы письменно, а не на словах", "o-kompanii"),
],
"es": [
    ("stamp", "red", "Precio fijo", "El monto no cambia",
     "Precio fijo: el monto no cambia durante el proceso", "stoimost"),
    ("shield", "blue", "Confidencialidad", "Acuerdo con cada cliente",
     "Confidencialidad: un acuerdo aparte con cada cliente", "o-kompanii"),
    ("honest", "red", "Sin promesas falsas", "7–8 años, no «un año»",
     "Sin promesas falsas: el plazo real es de 7–8 años, no «en un año», según el director de la DNM (ABC Color, 04.05.2026)", "protsess"),
    ("contract", "blue", "Acuerdo antes del pago", "Condiciones por escrito",
     "Acuerdo antes del pago: las condiciones constan por escrito, no de palabra", "o-kompanii"),
],
"en": [
    ("stamp", "red", "Fixed price", "The amount doesn't change",
     "Fixed price: the amount doesn't change during the process", "stoimost"),
    ("shield", "blue", "Confidentiality", "A separate agreement",
     "Confidentiality: a separate agreement with every client", "o-kompanii"),
    ("honest", "red", "No false promises", "7–8 years, not \"one year\"",
     "No false promises: the real timeline is 7–8 years, not \"one year,\" according to the DNM director (ABC Color, 05/04/2026)", "protsess"),
    ("contract", "blue", "Agreement before payment", "Terms in writing",
     "Agreement before payment: the terms are set out in writing, not just spoken", "o-kompanii"),
],
"de": [
    ("stamp", "red", "Festpreis", "Der Betrag ändert sich nicht",
     "Festpreis: der Betrag ändert sich während des Prozesses nicht", "stoimost"),
    ("shield", "blue", "Vertraulichkeit", "Vereinbarung pro Mandant",
     "Vertraulichkeit: eine gesonderte Vereinbarung mit jedem Mandanten", "o-kompanii"),
    ("honest", "red", "Keine falschen Versprechen", "7–8 Jahre, nicht „ein Jahr\"",
     "Keine falschen Versprechen: die reale Frist beträgt 7–8 Jahre, nicht „ein Jahr\", laut dem Direktor der DNM (ABC Color, 04.05.2026)", "protsess"),
    ("contract", "blue", "Vereinbarung vor Zahlung", "Bedingungen schriftlich",
     "Vereinbarung vor Zahlung: die Bedingungen stehen schriftlich fest, nicht nur mündlich", "o-kompanii"),
],
}

# Пересборка Главной (12.08.2026, третья правка) — по прямому замечанию заказчика: «оформление
# текста не нравится, суть не соответствует Главной, начинается со второстепенных вещей».
# Пять сплошных абзацев (p1–p5) заменены на 3 тизера по образцу уже одобренного hub-паттерна
# (заголовок + 2–3 предложения + «Подробнее →») — тот же `.card`, без нового визуального языка.
# Текст тизеров — не новый контент, а сжатые версии уже утверждённых `lead` с целевых страниц
# («Как мы работаем», «О компании», «Кейсы и отзывы»), как и в своё время для hub-лендинга.
# Инвестиционный акцент на Главной (18.08.2026) — по отзыву партнёра: инвестиционные
# тизеры были не видны на Главной (карточка «Инвесторский путь» есть только на «Услугах»).
# Цифры/сроки/номер резолюции — дословное сжатие уже проверенного текста карточки
# "investor" из USLUGI_PAGE (см. design/plan-otzyv-partnera-avg2026.md) — новых фактов
# не добавлено. Блок стоит сразу после «Парагвай в цифрах» (BIP-график), как предложил
# партнёр (investment chancen рядом с BIP grafik).
INVEST = {
"ru": dict(
    h2="Инвесторский путь — быстрее, чем через резидентуру",
    p="При инвестициях от 70 000 до 200 000 USD (недвижимость, финансовые инструменты или "
      "производственный проект с созданием 5 официальных рабочих мест) можно получить "
      "постоянную резиденцию напрямую, минуя Residencia Temporal. Режим действует по "
      "резолюции MIC № 0283/2026 и администрируется через SUACE.",
    cta="Подробнее об инвесторском пути →",
    fact_num="5 дней", fact_cap="Официальный срок выдачи сертификата инвестора (CIE) после подачи полного пакета документов.",
),
"es": dict(
    h2="Vía de inversor — más rápida que la residencia habitual",
    p="Con inversiones desde 70.000 hasta 200.000 USD (inmuebles, instrumentos financieros o "
      "un proyecto productivo con 5 puestos de trabajo formales) es posible obtener la "
      "residencia permanente directamente, sin pasar por la Residencia Temporal. El régimen "
      "funciona según la resolución del MIC N.° 0283/2026 y se administra a través de SUACE.",
    cta="Más sobre la vía de inversor →",
    fact_num="5 días", fact_cap="Plazo oficial de emisión del certificado de inversor (CIE) tras presentar el paquete completo de documentos.",
),
"en": dict(
    h2="Investor route — faster than standard residency",
    p="With investments from $70,000 to $200,000 USD (real estate, financial instruments, or "
      "a production project creating 5 formal jobs), you can get permanent residency directly, "
      "without going through Residencia Temporal. The scheme runs under MIC resolution "
      "N° 0283/2026 and is administered through SUACE.",
    cta="More on the investor route →",
    fact_num="5 business days", fact_cap="Official issuance time for the investor certificate (CIE) after filing the complete document package.",
),
"de": dict(
    h2="Investorenweg — schneller als der reguläre Aufenthaltstitel",
    p="Bei Investitionen ab 70.000 bis 200.000 USD (Immobilien, Finanzinstrumente oder ein "
      "Produktionsprojekt mit 5 geschaffenen offiziellen Arbeitsplätzen) ist der direkte Zugang "
      "zum unbefristeten Aufenthaltstitel möglich — ohne den Weg über die Residencia Temporal. "
      "Die Regelung gilt gemäß der MIC-Resolution N° 0283/2026 und wird über SUACE verwaltet.",
    cta="Mehr zum Investorenweg →",
    fact_num="5 Werktage", fact_cap="Offizielle Ausstellungsfrist für das Investorenzertifikat (CIE) nach Einreichung des vollständigen Dokumentenpakets.",
),
}

TEASERS_H2 = {"ru": "Узнать больше", "es": "Más información", "en": "Learn more", "de": "Mehr erfahren"}

TEASERS = {
"ru": [
    ("kak-my-rabotaem", "Как мы работаем",
     "Пошаговая дорожная карта с честными сроками — и прямой разговор о рисках и трудностях "
     "переезда, без нагнетания, но и без замалчивания."),
    ("o-kompanii", "О компании",
     "Мы решаем один узкий вопрос: как переехать так, чтобы через два года не разбираться с "
     "последствиями упущенной детали в документах. Чёткая договорённость об объёме и стоимости "
     "работ, реальная команда — без анонимности."),
    ("keisy", "Кейсы и отзывы",
     "Иллюстративные сценарии, а не реальные случаи клиентов: типичные обобщённые истории — резидентура, инвестиции, бизнес и честный разговор "
     "о трудностях первого года. Имена и фото не публикуем — по условиям соглашения о "
     "конфиденциальности."),
],
"es": [
    ("kak-my-rabotaem", "Cómo trabajamos",
     "Una hoja de ruta paso a paso con plazos honestos — y una conversación directa sobre los "
     "riesgos y dificultades de la mudanza, sin alarmismo, pero sin ocultar nada."),
    ("o-kompanii", "Sobre nosotros",
     "Resolvemos una sola cuestión: cómo mudarse de forma que, dos años después, no tenga que "
     "lidiar con las consecuencias de un detalle pasado por alto en los documentos. Un acuerdo "
     "claro sobre el alcance y el costo, un equipo real — sin anonimato."),
    ("keisy", "Casos y testimonios",
     "Escenarios ilustrativos, no casos reales de clientes: historias típicas y generalizadas — residencia, inversiones, negocios y una "
     "conversación honesta sobre las dificultades del primer año. No publicamos nombres ni fotos, "
     "según nuestro acuerdo de confidencialidad."),
],
"en": [
    ("kak-my-rabotaem", "How We Work",
     "A step-by-step roadmap with honest timelines — and a direct conversation about the risks "
     "and difficulties of relocating, without alarmism, but without hiding anything either."),
    ("o-kompanii", "About Us",
     "We solve one narrow problem: how to move in a way that means, two years later, you're not "
     "dealing with the consequences of one overlooked detail in your paperwork. A clear agreement "
     "on scope and price, a real team — no anonymity."),
    ("keisy", "Case Studies",
     "Illustrative scenarios, not real client cases: typical, generalized stories — residency, investment, business, and an honest look "
     "at the difficulties of the first year. We don't publish names or photos, under our "
     "confidentiality agreement."),
],
"de": [
    ("kak-my-rabotaem", "Wie wir arbeiten",
     "Ein Schritt-für-Schritt-Fahrplan mit ehrlichen Fristen — und ein direktes Gespräch über die "
     "Risiken und Schwierigkeiten des Umzugs, ohne Panikmache, aber auch ohne etwas zu verschweigen."),
    ("o-kompanii", "Über uns",
     "Wir lösen eine eng umrissene Frage: Wie zieht man so um, dass man zwei Jahre später nicht "
     "mit den Folgen eines übersehenen Details in den Unterlagen dasteht. Eine klare Vereinbarung "
     "über Umfang und Kosten, ein echtes Team — ohne Anonymität."),
    ("keisy", "Fallstudien",
     "Beispielszenarien, keine realen Mandantenfälle: typische, verallgemeinerte Geschichten — Aufenthaltstitel, Investitionen, Geschäft "
     "und ein ehrlicher Blick auf die Schwierigkeiten des ersten Jahres. Wir veröffentlichen keine "
     "Namen oder Fotos — gemäß unserer Vertraulichkeitsvereinbarung."),
],
}

for lang, t in HOME.items():
    l = L(lang)
    teaser_cards = "\n      ".join(
        f'<div class="card"><h3>{title}</h3><p>{desc}</p><a class="card-link" href="{l[page_id]}">{t["more"]}</a></div>'
        for page_id, title, desc in TEASERS[lang]
    )
    seal_row = "\n      ".join(
        f'<div class="seal"><a href="{l[link_pid]}" aria-label="{aria}">{seal_svg(icon, top, bottom, "seal-"+color, aria, uid=f"{lang}-{i}")}</a></div>'
        for i, (icon, color, top, bottom, aria, link_pid) in enumerate(SEALS[lang])
    )
    hero = hero_photo_slider(HERO_PHOTOS[lang], HERO_UI[lang], slider_id=f"{lang}-home-hero-photo")
    home_body = f'''
<section class="hero hero--photo">
  {hero["photos"]}
  <div class="wrap hero-photo-content">
    <p class="kicker">{t["kicker"]}</p>
    <h1>{t["h1"]}</h1>
    <p class="lead">{t["lead"]}</p>
    <div class="hero-actions">
      <a class="btn" href="{l['kontakty']}">{t["cta1"]}</a>
      <a class="btn btn-outline" href="{l['uslugi']}">{t["cta2"]}</a>
    </div>
    {hero["controls"]}
  </div>
  {hero["lead_variants"]}
</section>
{hero["script"]}

<section style="padding-top:0;">
  <div class="wrap">
    <div class="seal-row">
      {seal_row}
    </div>
  </div>
</section>

<section class="section-alt" style="padding-top:0;">
  <div class="wrap">
    <h2 style="margin-top:0">{t["services_h2"]}</h2>
    <div class="grid grid-3">
      <div class="card"><div class="icon">{ICONS['residencia']}</div><h3>{t["svc_residencia_title"]}</h3><p>{t["svc_residencia_desc"]}</p><a class="card-link" href="{l['usluga-residencia'] or l['uslugi']+'#residencia'}">{t["more"]}</a></div>
      <div class="card"><div class="icon">{ICONS['realestate']}</div><h3>{t["svc_realestate_title"]}</h3><p>{t["svc_realestate_desc"]}</p><a class="card-link" href="{l['uslugi']}#realestate">{t["more"]}</a></div>
      <div class="card"><div class="icon">{ICONS['compliance']}</div><h3>{t["svc_compliance_title"]}</h3><p>{t["svc_compliance_desc"]}</p><a class="card-link" href="{l['uslugi']}#compliance">{t["more"]}</a></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2 style="margin-top:0">{STATS_H2[lang]}</h2>
    {chart_slider(
        [dict(svg=render_topic(ct), title=ct["title"], caption=ct["caption"], href=ct["href"])
         for ct in build_topics(lang) if ct["key"] != "life"],
        UI_LABELS[lang], slider_id="home-stats-slider",
    )}
  </div>
</section>

<section style="padding-top:0;">
  <div class="wrap">
    <div class="grid grid-2 invest-teaser">
      <div class="prose" style="padding:0;margin:0;max-width:100%;">
        <div class="invest-icon">{ICONS['investor']}</div>
        <h2 style="margin-top:8px">{INVEST[lang]["h2"]}</h2>
        <p>{INVEST[lang]["p"]}</p>
        <a class="btn" href="{l['usluga-investor'] or l['uslugi']+'#investor'}">{INVEST[lang]["cta"]}</a>
      </div>
      <div class="key-fact" style="align-self:center;">
        <span class="num">{INVEST[lang]["fact_num"]}</span>
        <span class="cap">{INVEST[lang]["fact_cap"]}</span>
      </div>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="wrap">
    <h2 style="margin-top:0">{TEASERS_H2[lang]}</h2>
    <div class="grid grid-3">
      {teaser_cards}
    </div>
  </div>
</section>

<div class="prose">
  <div class="final-cta">
    <h2>{t["final_h2"]}</h2>
    <p>{t["final_p"]}</p>
    <a class="btn" href="{l['kontakty']}">{t["final_cta"]}</a>
  </div>
</div>
'''
    page("home", lang, t["title"], t["description"], home_body,
         extra_schema=[ORG_SCHEMA, schema_breadcrumb([(NAV_LABELS[lang]["home"], f"/{lang}/")])])

# =========================================================== УСЛУГИ / SERVICES

SERVICE_KEYS = ["residencia", "compliance", "citizenship", "investor", "realestate", "company", "business"]

USLUGI_PAGE = {
"ru": dict(
    title="Услуги по переезду в Парагвай: ВНЖ, бизнес, недвижимость | Grund Paraguay",
    description="Резидентура, гражданство, инвесторский путь, сопровождение бизнеса, недвижимость и компании в Парагвае — честные сроки и фиксированные цены на каждую услугу.",
    h1="Услуги по переезду и легализации в Парагвае",
    lead="Семь услуг, с которыми мы работаем. Резидентура (ВНЖ) здесь не конечная цель, а входной этап: рынок оформления временной и постоянной резиденции в Парагвае уже заполнен посредниками, и конкурировать на нём одной лишь ценой бессмысленно. Настоящая работа начинается после получения резиденции — в сопровождении и комплаенсе, которые превращают разовую сделку в устойчивое легальное присутствие в стране.",
    footer_p='Полную стоимость каждой позиции смотрите на странице <a href="{stoimost}">«Стоимость и тарифы»</a>; типичные примеры того, как это выглядит на практике, — в разделе <a href="{keisy}">«Кейсы и отзывы»</a>.',
    cards={
      "residencia": ("Резидентура (ВНЖ)", 'Резидентура — вид на жительство в Парагвае, дающий право законно жить и работать в стране. Оформляется в два этапа: сначала временная (<a href="{terminologiya}#residencia-temporal">Residencia Temporal</a>, до 2 лет с продлением), затем — обычно через 2–5 лет — постоянная (<a href="{terminologiya}#residencia-permanente">Residencia Permanente</a>, на 10 лет с продлением); это не разовая услуга, а первый этап более длительного процесса (полный таймлайн — на странице <a href="{protsess}">«Процесс и сроки»</a>). Мы проверяем комплект документов — загранпаспорт, консульская виза, свидетельство о рождении, справка о семейном положении, международная справка о несудимости и другие документы по ст. 50 Ley N° 6984/22 «De Migraciones» — до подачи, а не после отказа. С 6 июля 2026 года действует новая резолюция миграционной службы (<a href="{terminologiya}#dnm">DNM</a>) N° 407/2026 с 12 категориями заявителей и отдельными требованиями по каждой; точные пороги по категориям на момент публикации официально не раскрыты, поэтому стоимость и условия по вашей категории мы уточняем индивидуально. Сама по себе резидентура не решает вопрос легальной жизни в стране без дальнейшего сопровождения (см. следующий раздел). Полный чек-лист документов — на страницах <a href="{dok-temporal}">«Временная резидентура»</a> и <a href="{dok-permanente}">«Постоянная резидентура»</a> в разделе «Документы».'),
      "compliance": ("Сопровождение и комплаенс (абонемент)", 'Сопровождение и комплаенс — абонентская услуга, которая поддерживает статус резидента в силе на всём пути от временной резиденции к постоянной, чтобы он не был потерян из-за пропущенной отчётности. После получения Residencia Temporal у иностранца возникает обязанность зарегистрировать <a href="{terminologiya}#ruc">RUC</a> (единый номер налогоплательщика, привязанный к <a href="{terminologiya}#cedula">Cédula</a>) и регулярно (как правило — ежемесячно, точная периодичность по общему режиму уточняется индивидуально) подавать налоговую отчётность, включая нулевую, если деятельности не было. Абонемент закрывает именно это: ведение отчётности, контроль сроков и статуса дела на всём пути от Temporal к Permanente, который обычно занимает от 2 до 5 лет. Это отдельная услуга, а не бонус к резидентуре — без действующего комплаенса перевод в постоянную резиденцию рискует растянуться или сорваться.'),
      "citizenship": ("Гражданство Парагвая", 'Гражданство Парагвая — статус, который даёт паспорт с безвизовым доступом примерно в 145 стран (Henley Passport Index) и более устойчивое правовое положение, чем резиденция. Натурализация возможна не раньше чем через 3 года после получения Residencia Permanente (ст. 148 Конституции Парагвая) — то есть реалистичный полный срок от переезда до паспорта складывается в 7–8 лет, а не «год», как иногда обещают на рынке (подробнее — на Главной и на странице <a href="{riski}">«Риски и трудности»</a>). Дело о натурализации ведёт не миграционная служба, а Верховный суд (<a href="{terminologiya}#corte-suprema">Corte Suprema de Justicia</a>); процедура требует личной явки и сопровождения адвоката. Мы ведём этот этап так же, как резидентуру, — с проверкой документов и честной оценкой сроков конкретно по вашей ситуации. Полный список документов на натурализацию — на странице <a href="{dok-grazhdanstvo}">«Гражданство: документы»</a>.'),
      "investor": ("Инвесторский путь (SUACE / Investor Pass)", 'Инвесторский путь — способ получить постоянную резиденцию напрямую, минуя временную, за счёт инвестиций в страну. Для инвестиций от 70 000 USD (производственная ветка, при бизнес-плане и создании 5 официальных рабочих мест) до 200 000 USD (недвижимость или финансовые инструменты) возможен прямой доступ к постоянной резиденции без прохождения Residencia Temporal. Режим действует по резолюции Министерства промышленности и торговли (<a href="{terminologiya}#mic">MIC</a>) N° 0283/2026 (с 21 апреля 2026 года) и администрируется через <a href="{terminologiya}#suace">SUACE</a>. Сертификат инвестора (<a href="{terminologiya}#cie">CIE</a>) оформляется официально за 5 рабочих дней после подачи полного пакета документов; сама постоянная резиденция, по оценке отраслевых изданий, занимает ещё около 3–6 месяцев сверху. Это отдельный путь для более состоятельного сегмента — мы не смешиваем его с массовой резидентурой. Официальный перечень документов на сертификат инвестора — на странице <a href="{dok-investor}">«Инвесторский путь: документы»</a>.'),
      "realestate": ("Проверка и покупка недвижимости", 'Проверка и покупка недвижимости — услуга due diligence по конкретному объекту, которая защищает от переплаты и от скрытых рисков сделки. Мы не ведём каталог объектов — вместо этого проверяем конкретную сделку: цепочку правоустанавливающих документов, статус земли (в частности, риск отнесения к категории «lote agrario» — неотчуждаемых земель аграрной реформы <a href="{terminologiya}#indert">INDERT</a>), работу через независимого нотариуса (<a href="{terminologiya}#escribano">escribano</a>), а при необходимости — оформление сделки по удалённой доверенности для тех, кто ещё не переехал. Цена проверки фиксированная за отчёт — независимо от того, состоится сделка или нет.'),
      "company": ("Открытие компании (EAS/SRL)", 'Открытие компании — регистрация юридического лица в Парагвае, которое даёт возможность вести бизнес легально: выставлять счета, нанимать сотрудников и открывать банковский счёт на компанию. Регистрация упрощённого акционерного общества (<a href="{terminologiya}#eas">EAS</a>) через SUACE официально занимает до 72 рабочих часов по типовому уставу (для <a href="{terminologiya}#sa">S.A.</a> — 8–30 рабочих дней, для <a href="{terminologiya}#srl">S.R.L.</a> — 15–30 рабочих дней). Для EAS законный представитель обязательно должен иметь парагвайское гражданство или парагвайскую Cédula «без исключений» — это прямое требование официального портала EAS того же MIC; если резидентства пока нет, эту роль берёт на себя представитель по доверенности. Регистрацию мы передаём проверенному партнёру; она проходит только при личном присутствии.'),
      "business": ("Покупка и продажа бизнеса", 'Покупка и продажа бизнеса — сопровождение сделки для тех, кто хочет войти в дело через готовую компанию или выйти из своей, а не запускать регистрацию с нуля. Рынок сделок купли-продажи бизнеса в Парагвае небольшой и непрозрачный: крупные международные трекеры сделок (например, TTR Data) вообще не включают Парагвай в число охваченных стран — в отличие от соседних Аргентины и Уругвая. Это означает, что стандартной статистики по мультипликаторам оценки и объёму сделок просто не существует, а проверенных предложений на открытом рынке немного. Мы сопровождаем такие сделки индивидуально: независимая оценка, проверка предложения и сопровождение передачи бизнеса.'),
    },
),
"es": dict(
    title="Servicios para mudarse a Paraguay: residencia, negocios, inmuebles | Grund Paraguay",
    description="Residencia, ciudadanía, vía de inversor, acompañamiento de negocios, inmuebles y empresas en Paraguay — plazos honestos y precios fijos para cada servicio.",
    h1="Servicios de mudanza y legalización en Paraguay",
    lead="Siete servicios en los que trabajamos. La residencia aquí no es el objetivo final, sino la etapa de entrada: el mercado de trámites de residencia temporal y permanente en Paraguay ya está saturado de intermediarios, y competir solo por precio no tiene sentido. El trabajo real empieza después de obtener la residencia — en el acompañamiento y el cumplimiento, que convierten una operación puntual en una presencia legal estable en el país.",
    footer_p='El costo completo de cada servicio está en la página <a href="{stoimost}">«Costos y tarifas»</a>; ejemplos típicos de cómo funciona en la práctica, en la sección <a href="{keisy}">«Casos y testimonios»</a>.',
    cards={
      "residencia": ("Residencia", 'La residencia es un permiso que da derecho a vivir y trabajar legalmente en Paraguay. Se tramita en dos etapas: primero la temporal (<a href="{terminologiya}#residencia-temporal">Residencia Temporal</a>, hasta 2 años con renovación), luego — normalmente a los 2–5 años — la permanente (<a href="{terminologiya}#residencia-permanente">Residencia Permanente</a>, por 10 años con renovación); no es un servicio puntual, sino la primera etapa de un proceso más largo (cronología completa en la página <a href="{protsess}">«Proceso y plazos»</a>). Verificamos el paquete de documentos — pasaporte, visa consular, partida de nacimiento, certificado de estado civil, certificado de antecedentes internacional y otros documentos según el art. 50 de la Ley N.° 6984/22 «De Migraciones» — antes de presentarlos, no después de un rechazo. Tras recibir la Cédula (CI), el <a href="{terminologiya}#ruc">RUC</a> se obtiene, por lo general, en un promedio de 3 a 6 días. Desde el 6 de julio de 2026 rige la nueva resolución de la Dirección Nacional de Migraciones (<a href="{terminologiya}#dnm">DNM</a>) N.° 407/2026, con 12 categorías de solicitantes y requisitos propios para cada una; los umbrales exactos por categoría no se han publicado oficialmente al momento de esta publicación, por lo que confirmamos el costo y las condiciones de su categoría de forma individual. Por sí sola, la residencia no resuelve la cuestión de la vida legal en el país sin un acompañamiento posterior (ver la siguiente sección). La lista completa de documentos está en las páginas <a href="{dok-temporal}">«Residencia temporal»</a> y <a href="{dok-permanente}">«Residencia permanente»</a> de la sección «Documentos».'),
      "compliance": ("Acompañamiento y cumplimiento (suscripción)", 'El acompañamiento y cumplimiento es un servicio por suscripción que mantiene vigente el estatus de residente durante todo el camino de la temporal a la permanente, para que no se pierda por una declaración omitida. Tras obtener la Residencia Temporal, el extranjero debe inscribir el <a href="{terminologiya}#ruc">RUC</a> (número único de contribuyente, vinculado a la <a href="{terminologiya}#cedula">Cédula</a>) y presentar declaraciones tributarias de forma periódica (por lo general mensual; la periodicidad exacta bajo el régimen general se confirma de forma individual), incluidas declaraciones en cero si no hubo actividad. La suscripción cubre justamente esto: llevar la contabilidad, controlar los plazos y el estado del trámite en todo el camino de Temporal a Permanente, que suele durar de 2 a 5 años. Es un servicio aparte, no un bono de la residencia — sin un cumplimiento activo, la conversión a residencia permanente corre el riesgo de demorarse o fracasar.'),
      "citizenship": ("Ciudadanía paraguaya", 'La ciudadanía paraguaya otorga un pasaporte con acceso sin visa a unos 145 países (Henley Passport Index) y un estatus jurídico más estable que la residencia. La naturalización es posible recién 3 años después de obtener la Residencia Permanente (art. 148 de la Constitución de Paraguay) — es decir, el plazo real completo desde la mudanza hasta el pasaporte es de 7 a 8 años, no «un año» como a veces se promete en el mercado (más detalles en la página de Inicio y en <a href="{riski}">«Riesgos y dificultades»</a>). El trámite de naturalización lo lleva la Corte Suprema (<a href="{terminologiya}#corte-suprema">Corte Suprema de Justicia</a>), no la DNM; el procedimiento requiere comparecencia personal y el acompañamiento de un abogado. Llevamos esta etapa igual que la residencia — con verificación de documentos y una evaluación honesta de los plazos según su situación concreta. La lista completa de documentos para la naturalización está en la página <a href="{dok-grazhdanstvo}">«Ciudadanía: documentos»</a>.'),
      "investor": ("Vía de inversor (SUACE / Investor Pass)", 'La vía de inversor es una forma de obtener la residencia permanente directamente, sin pasar por la temporal, mediante una inversión en el país. Con inversiones desde 70.000 USD (rama productiva, con plan de negocios y creación de 5 puestos de trabajo formales) hasta 200.000 USD (inmuebles o instrumentos financieros) es posible acceder directamente a la residencia permanente sin pasar por la Residencia Temporal. El régimen funciona según la resolución del Ministerio de Industria y Comercio (<a href="{terminologiya}#mic">MIC</a>) N.° 0283/2026 (desde el 21 de abril de 2026) y se administra a través de <a href="{terminologiya}#suace">SUACE</a>. El certificado de inversor (<a href="{terminologiya}#cie">CIE</a>) se emite oficialmente en 5 días hábiles tras presentar el paquete completo; la residencia permanente en sí, según estimaciones de medios especializados, toma unos 3 a 6 meses adicionales. Es una vía aparte para un segmento con mayor capacidad — no la mezclamos con la residencia masiva. La lista oficial de documentos para el certificado de inversor está en la página <a href="{dok-investor}">«Vía de inversor: documentos»</a>.'),
      "realestate": ("Verificación y compra de inmuebles", 'La verificación y compra de inmuebles es un servicio de due diligence sobre una propiedad concreta, que protege de sobrepagar o de riesgos ocultos en la operación. No manejamos un catálogo de propiedades — en cambio, verificamos la operación concreta: la cadena de títulos de propiedad, el estatus de la tierra (en particular, el riesgo de que se trate de un «lote agrario» — tierras inalienables de la reforma agraria del <a href="{terminologiya}#indert">INDERT</a>), el trabajo a través de un escribano independiente (<a href="{terminologiya}#escribano">escribano</a>) y, si hace falta, la operación mediante poder a distancia para quienes aún no se han mudado. El costo de la verificación es fijo por informe, sin importar si la operación se concreta o no.'),
      "company": ("Apertura de empresa (EAS/SRL)", 'La apertura de empresa es la inscripción de una persona jurídica en Paraguay, que permite operar legalmente: facturar, contratar personal y abrir una cuenta bancaria a nombre de la empresa. La inscripción de una Empresa por Acciones Simplificada (<a href="{terminologiya}#eas">EAS</a>) a través de SUACE demora oficialmente hasta 72 horas hábiles con estatuto tipo (para <a href="{terminologiya}#sa">S.A.</a>, de 8 a 30 días hábiles; para <a href="{terminologiya}#srl">S.R.L.</a>, de 15 a 30 días hábiles). Para la EAS, el representante legal debe tener obligatoriamente ciudadanía paraguaya o Cédula paraguaya «sin excepciones» — es un requisito directo del portal oficial de EAS del mismo MIC; si aún no hay residencia, esta función la asume un apoderado. La inscripción la derivamos a un socio verificado; se hace solo de forma presencial.'),
      "business": ("Compra y venta de empresas", 'La compra y venta de empresas es el acompañamiento de una operación para quienes prefieren entrar a un negocio ya en marcha o salir del propio, en lugar de registrar uno desde cero. El mercado de compraventa de empresas en Paraguay es pequeño y poco transparente: los grandes rastreadores internacionales de operaciones (por ejemplo, TTR Data) directamente no incluyen a Paraguay entre los países cubiertos, a diferencia de la vecina Argentina y Uruguay. Esto significa que no existe estadística estándar sobre múltiplos de valuación ni volumen de operaciones, y hay pocas ofertas verificadas en el mercado abierto. Acompañamos estas operaciones de forma individual: valuación independiente, verificación de la oferta y acompañamiento en la transferencia del negocio.'),
    },
),
"en": dict(
    title="Services for moving to Paraguay: residency, business, real estate | Grund Paraguay",
    description="Residency, citizenship, the investor route, business support, real estate and companies in Paraguay — honest timelines and fixed prices for every service.",
    h1="Relocation & legalization services in Paraguay",
    lead="Seven services we handle. Residency here isn't the end goal but the entry stage: the market for temporary and permanent residency processing in Paraguay is already crowded with intermediaries, and competing on price alone doesn't make sense. The real work starts after you get residency — in the ongoing support and compliance that turn a one-off transaction into a stable legal presence in the country.",
    footer_p='Full pricing for each service is on the <a href="{stoimost}">"Pricing"</a> page; typical real-world examples are in the <a href="{keisy}">"Case Studies"</a> section.',
    cards={
      "residencia": ("Residency", 'Residency is a legal status that gives you the right to live and work in Paraguay. It comes in two stages: first temporary (<a href="{terminologiya}#residencia-temporal">Residencia Temporal</a>, up to 2 years with renewal), then — usually after 2–5 years — permanent (<a href="{terminologiya}#residencia-permanente">Residencia Permanente</a>, for 10 years with renewal); it isn\'t a one-off service — it\'s the first stage of a longer process (full timeline on the <a href="{protsess}">"Process & Timeline"</a> page). We check your document package — passport, consular visa, birth certificate, marital status certificate, international criminal record certificate, and other documents under Art. 50 of Ley N° 6984/22 "De Migraciones" — before filing, not after a rejection. After you receive the Cédula (CI), the <a href="{terminologiya}#ruc">RUC</a> is usually issued within 3–6 days on average. Since July 6, 2026, a new migration service (<a href="{terminologiya}#dnm">DNM</a>) resolution N° 407/2026 has been in effect, with 12 applicant categories and separate requirements for each; the exact thresholds per category haven\'t been officially published as of this writing, so we confirm the cost and conditions for your category individually. On its own, residency doesn\'t settle the question of living legally in the country without ongoing support (see the next section). The full document checklist is on the <a href="{dok-temporal}">"Temporary Residency"</a> and <a href="{dok-permanente}">"Permanent Residency"</a> pages in the "Documents" section.'),
      "compliance": ("Ongoing compliance (subscription)", 'Ongoing compliance is a subscription service that keeps your resident status valid all the way from temporary to permanent, so it isn\'t lost over a missed filing. After getting Residencia Temporal, a foreigner must register a <a href="{terminologiya}#ruc">RUC</a> (a unique taxpayer number tied to the <a href="{terminologiya}#cedula">Cédula</a>) and file tax returns regularly (usually monthly; the exact frequency under the general regime is confirmed individually), including zero filings when there was no activity. The subscription covers exactly this: bookkeeping, tracking deadlines, and monitoring case status all the way from Temporal to Permanente, which usually takes 2 to 5 years. This is a separate service, not a bonus to residency — without active compliance, converting to permanent residency risks dragging on or falling through.'),
      "citizenship": ("Paraguayan citizenship", 'Paraguayan citizenship grants a passport with visa-free access to roughly 145 countries (Henley Passport Index) and a more stable legal status than residency. Naturalization is only possible 3 years after getting Residencia Permanente (Art. 148 of Paraguay\'s Constitution) — meaning the realistic full timeline from moving to holding a passport works out to 7–8 years, not "a year" as some agencies promise (more on the Home page and on the <a href="{riski}">"Risks & Difficulties"</a> page). The naturalization case is handled by the Supreme Court (<a href="{terminologiya}#corte-suprema">Corte Suprema de Justicia</a>), not the migration service; the procedure requires appearing in person and legal representation. We run this stage the same way as residency — checking documents and giving an honest timeline estimate for your specific situation. The full document list for naturalization is on the <a href="{dok-grazhdanstvo}">"Citizenship: Documents"</a> page.'),
      "investor": ("Investor route (SUACE / Investor Pass)", 'The investor route is a way to get permanent residency directly, skipping the temporary stage, by investing in the country. With investments from 70,000 USD (production track, with a business plan and 5 formal jobs created) up to 200,000 USD (real estate or financial instruments), direct access to permanent residency is possible without going through Residencia Temporal. The scheme runs under Ministry of Industry and Commerce (<a href="{terminologiya}#mic">MIC</a>) resolution N° 0283/2026 (as of April 21, 2026) and is administered through <a href="{terminologiya}#suace">SUACE</a>. The investor certificate (<a href="{terminologiya}#cie">CIE</a>) is officially issued within 5 business days after the full package is filed; the permanent residency itself, per industry estimates, takes another 3–6 months on top of that. This is a separate track for a wealthier segment — we don\'t mix it with mass-market residency. The official document list for the investor certificate is on the <a href="{dok-investor}">"Investor Route: Documents"</a> page.'),
      "realestate": ("Real estate verification & purchase", "Real estate verification & purchase is a due-diligence service on a specific property, protecting you from overpaying or from hidden risks in the deal. We don't run a listings catalog — instead we verify the specific deal: the chain of title documents, the land's status (in particular, the risk of it being classed as \"lote agrario\" — inalienable land reform land under <a href=\"{terminologiya}#indert\">INDERT</a>), working through an independent notary (<a href=\"{terminologiya}#escribano\">escribano</a>), and, if needed, structuring the deal via a remote power of attorney for those who haven't moved yet. The verification is a fixed price per report — regardless of whether the deal goes through."),
      "company": ("Company formation (EAS/SRL)", 'Company formation is registering a legal entity in Paraguay, which lets you do business legally: issue invoices, hire staff, and open a bank account in the company\'s name. Registering a simplified joint-stock company (<a href="{terminologiya}#eas">EAS</a>) through SUACE officially takes up to 72 business hours with a standard charter (for <a href="{terminologiya}#sa">S.A.</a> — 8–30 business days; for <a href="{terminologiya}#srl">S.R.L.</a> — 15–30 business days). For an EAS, the legal representative must hold Paraguayan citizenship or a Paraguayan Cédula "with no exceptions" — a direct requirement of the MIC official EAS portal; if you don\'t have residency yet, a proxy representative takes on this role. We hand registration over to a vetted partner; it is done in person only.'),
      "business": ("Buying & selling a business", "Buying & selling a business is deal support for those who'd rather step into a running company or exit their own, instead of registering one from scratch. The market for buying and selling businesses in Paraguay is small and opaque: major international deal trackers (e.g., TTR Data) don't cover Paraguay at all, unlike neighboring Argentina and Uruguay. That means there's no standard statistics on valuation multiples or deal volume, and few verified offers on the open market. We support these deals individually: independent valuation, offer verification, and support through the handover."),
    },
),
"de": dict(
    title="Dienstleistungen für den Umzug nach Paraguay: Aufenthalt, Geschäft, Immobilien | Grund Paraguay",
    description="Aufenthaltstitel, Staatsbürgerschaft, Investorenweg, Geschäftsbegleitung, Immobilien und Unternehmen in Paraguay — ehrliche Fristen und Festpreise für jede Leistung.",
    h1="Umzugs- und Legalisierungsleistungen in Paraguay",
    lead="Sieben Leistungen, mit denen wir arbeiten. Der Aufenthaltstitel ist hier nicht das Endziel, sondern die Einstiegsetappe: Der Markt für die Bearbeitung befristeter und unbefristeter Aufenthaltstitel in Paraguay ist bereits voller Vermittler, und allein über den Preis zu konkurrieren, ergibt keinen Sinn. Die eigentliche Arbeit beginnt nach Erhalt des Aufenthaltstitels — in der laufenden Begleitung und Compliance, die aus einer einmaligen Transaktion eine stabile legale Präsenz im Land machen.",
    footer_p='Die vollständigen Kosten jeder Leistung finden Sie auf der Seite <a href="{stoimost}">„Preise"</a>; typische Beispiele aus der Praxis im Abschnitt <a href="{keisy}">„Fallstudien"</a>.',
    cards={
      "residencia": ("Aufenthaltstitel", 'Der Aufenthaltstitel ist ein Rechtsstatus, der das Recht gibt, legal in Paraguay zu leben und zu arbeiten. Er wird in zwei Etappen erworben: zunächst der befristete (<a href="{terminologiya}#residencia-temporal">Residencia Temporal</a>, bis zu 2 Jahre mit Verlängerung), dann — meist nach 2–5 Jahren — der unbefristete (<a href="{terminologiya}#residencia-permanente">Residencia Permanente</a>, für 10 Jahre mit Verlängerung); das ist keine einmalige Leistung, sondern die erste Etappe eines längeren Prozesses (vollständige Zeitachse auf der Seite <a href="{protsess}">„Prozess und Fristen"</a>). Wir prüfen das Dokumentenpaket — Reisepass, konsularisches Visum, Geburtsurkunde, Familienstandsbescheinigung, internationales Führungszeugnis und weitere Dokumente gemäß Art. 50 des Ley N° 6984/22 „De Migraciones" — vor der Einreichung, nicht nach einer Ablehnung. Nach Erhalt der Cédula (CI) wird die <a href="{terminologiya}#ruc">RUC</a> in der Regel durchschnittlich innerhalb von 3–6 Tagen erteilt. Seit dem 6. Juli 2026 gilt die neue Resolution der Migrationsbehörde (<a href="{terminologiya}#dnm">DNM</a>) N° 407/2026 mit 12 Antragstellerkategorien und jeweils eigenen Anforderungen; die genauen Schwellenwerte je Kategorie sind zum Zeitpunkt der Veröffentlichung offiziell nicht bekannt gegeben worden, daher klären wir Kosten und Bedingungen für Ihre Kategorie individuell. Der Aufenthaltstitel allein löst ohne weitere Begleitung nicht die Frage des legalen Lebens im Land (siehe nächster Abschnitt). Die vollständige Dokumenten-Checkliste steht auf den Seiten <a href="{dok-temporal}">„Befristeter Aufenthalt"</a> und <a href="{dok-permanente}">„Daueraufenthalt"</a> im Bereich „Dokumente".'),
      "compliance": ("Begleitung und Compliance (Abonnement)", 'Begleitung und Compliance ist eine Abonnement-Leistung, die den Aufenthaltsstatus auf dem gesamten Weg von befristet zu unbefristet aufrechterhält, damit er nicht wegen einer versäumten Meldung verloren geht. Nach Erhalt der Residencia Temporal entsteht für Ausländer die Pflicht, eine <a href="{terminologiya}#ruc">RUC</a> (einheitliche Steuernummer, gekoppelt an die <a href="{terminologiya}#cedula">Cédula</a>) zu registrieren und regelmäßig (in der Regel monatlich; die genaue Häufigkeit im allgemeinen Regime wird individuell geklärt) Steuererklärungen einzureichen, einschließlich Nullmeldungen bei fehlender Tätigkeit. Das Abonnement deckt genau das ab: Buchführung, Fristenkontrolle und Statusüberwachung des Verfahrens auf dem gesamten Weg von Temporal zu Permanente, der in der Regel 2 bis 5 Jahre dauert. Das ist eine eigenständige Leistung, kein Bonus zum Aufenthaltstitel — ohne laufende Compliance riskiert die Umwandlung in den unbefristeten Aufenthaltstitel, sich zu verzögern oder zu scheitern.'),
      "citizenship": ("Paraguayische Staatsbürgerschaft", 'Die paraguayische Staatsbürgerschaft verleiht einen Reisepass mit visumfreiem Zugang zu rund 145 Ländern (Henley Passport Index) und einen stabileren Rechtsstatus als der Aufenthaltstitel. Die Einbürgerung ist erst 3 Jahre nach Erhalt der Residencia Permanente möglich (Art. 148 der paraguayischen Verfassung) — das heißt, die realistische Gesamtfrist vom Umzug bis zum Pass beträgt 7–8 Jahre, nicht „ein Jahr", wie manchmal auf dem Markt versprochen wird (mehr auf der Startseite und auf der Seite <a href="{riski}">„Risiken und Schwierigkeiten"</a>). Das Einbürgerungsverfahren führt nicht die Migrationsbehörde, sondern der Oberste Gerichtshof (<a href="{terminologiya}#corte-suprema">Corte Suprema de Justicia</a>); das Verfahren erfordert persönliches Erscheinen und anwaltliche Begleitung. Wir führen diese Etappe genauso wie den Aufenthaltstitel — mit Dokumentenprüfung und einer ehrlichen Einschätzung der Fristen speziell für Ihre Situation. Die vollständige Dokumentenliste für die Einbürgerung steht auf der Seite <a href="{dok-grazhdanstvo}">„Staatsbürgerschaft: Dokumente"</a>.'),
      "investor": ("Investorenweg (SUACE / Investor Pass)", 'Der Investorenweg ist eine Möglichkeit, den unbefristeten Aufenthaltstitel direkt zu erhalten, ohne den befristeten zu durchlaufen, indem im Land investiert wird. Bei Investitionen ab 70.000 USD (Produktionszweig, mit Geschäftsplan und Schaffung von 5 offiziellen Arbeitsplätzen) bis 200.000 USD (Immobilien oder Finanzinstrumente) ist ein direkter Zugang zum unbefristeten Aufenthaltstitel ohne den Weg über die Residencia Temporal möglich. Die Regelung gilt gemäß der Resolution des Ministeriums für Industrie und Handel (<a href="{terminologiya}#mic">MIC</a>) N° 0283/2026 (seit dem 21. April 2026) und wird über <a href="{terminologiya}#suace">SUACE</a> verwaltet. Das Investorenzertifikat (<a href="{terminologiya}#cie">CIE</a>) wird offiziell innerhalb von 5 Werktagen nach Einreichung des vollständigen Pakets ausgestellt; der unbefristete Aufenthaltstitel selbst benötigt laut Brancheneinschätzungen weitere etwa 3–6 Monate. Dies ist ein eigener Weg für ein vermögenderes Segment — wir vermischen ihn nicht mit dem regulären Aufenthaltstitel. Die offizielle Dokumentenliste für das Investorenzertifikat steht auf der Seite <a href="{dok-investor}">„Investorenweg: Dokumente"</a>.'),
      "realestate": ("Prüfung und Kauf von Immobilien", 'Prüfung und Kauf von Immobilien ist eine Due-Diligence-Leistung für ein konkretes Objekt, die vor Überzahlung und vor verdeckten Risiken des Geschäfts schützt. Wir führen keinen Objektkatalog — stattdessen prüfen wir das konkrete Geschäft: die Kette der Eigentumsdokumente, den Status des Grundstücks (insbesondere das Risiko einer Einstufung als „lote agrario" — unveräußerliches Agrarreformland des <a href="{terminologiya}#indert">INDERT</a>), die Abwicklung über einen unabhängigen Notar (<a href="{terminologiya}#escribano">escribano</a>) und, falls erforderlich, die Abwicklung per Fernvollmacht für diejenigen, die noch nicht umgezogen sind. Der Preis der Prüfung ist ein Festpreis pro Bericht — unabhängig davon, ob das Geschäft zustande kommt.'),
      "company": ("Unternehmensgründung (EAS/SRL)", 'Die Unternehmensgründung ist die Eintragung einer juristischen Person in Paraguay, die es ermöglicht, legal Geschäfte zu tätigen: Rechnungen zu stellen, Personal einzustellen und ein Firmenkonto zu eröffnen. Die Registrierung einer vereinfachten Aktiengesellschaft (<a href="{terminologiya}#eas">EAS</a>) über SUACE dauert offiziell bis zu 72 Werkstunden bei Standardsatzung (für <a href="{terminologiya}#sa">S.A.</a> 8–30 Werktage, für <a href="{terminologiya}#srl">S.R.L.</a> 15–30 Werktage). Für die EAS muss der gesetzliche Vertreter zwingend die paraguayische Staatsbürgerschaft oder eine paraguayische Cédula besitzen — „ohne Ausnahmen" —, dies ist eine direkte Vorgabe des offiziellen EAS-Portals desselben MIC; wenn noch kein Aufenthaltstitel vorliegt, übernimmt ein Bevollmächtigter diese Rolle. Die Registrierung übergeben wir an einen geprüften Partner; sie erfolgt nur mit persönlicher Anwesenheit.'),
      "business": ("Kauf und Verkauf von Unternehmen", 'Kauf und Verkauf von Unternehmen ist die Begleitung einer Transaktion für alle, die lieber in ein laufendes Unternehmen einsteigen oder aus dem eigenen aussteigen möchten, statt eines von Grund auf neu zu registrieren. Der Markt für den Kauf und Verkauf von Unternehmen in Paraguay ist klein und wenig transparent: Große internationale Deal-Tracker (z. B. TTR Data) erfassen Paraguay überhaupt nicht — anders als die Nachbarländer Argentinien und Uruguay. Das bedeutet, dass es keine Standardstatistik zu Bewertungsmultiplikatoren oder Transaktionsvolumen gibt und nur wenige geprüfte Angebote auf dem offenen Markt existieren. Wir begleiten solche Geschäfte individuell: unabhängige Bewertung, Prüfung des Angebots und Begleitung bei der Unternehmensübergabe.'),
    },
),
}

# Короткие анонсы (19.08.2026, пилот развёрнутых страниц услуг) — для этих двух услуг полный
# текст переехал на отдельные страницы (pages_uslugi_stranitsy.py), здесь остаётся анонс со
# ссылкой «Подробнее →». Остальные 5 услуг пока не тронуты — полный абзац, как раньше, до
# следующей волны страниц. RU-only, как и сами новые страницы.
TEASERS_USLUGI = {
    "residencia": "Оформление временной резиденции и её перевод в постоянную — входной этап процесса, который обычно занимает от 2 до 5 лет. Проверяем документы до подачи, а не после отказа. RUC после получения Cédula (CI) оформляется, как правило, в среднем за 3–6 дней.",
    "investor": "Инвестиции от 70 000 до 200 000 USD дают прямой доступ к постоянной резиденции без прохождения Residencia Temporal — сертификат инвестора оформляется официально за 5 рабочих дней.",
}

# Восьмая услуга — «Релокация организаций» (21.08.2026, старт RU-only; 21.08.2026 — переведена
# на ES/EN/DE по запросу заказчика «Делай релокацию и достопримечательности мультиязычными»). Не
# часть SERVICE_KEYS/cards (эти словари собраны для семи «исходных» услуг с иной историей
# правок) — карточка добавляется отдельно, тем же приёмом короткого анонса + «Подробнее →», что и
# у «Резидентуры»/«Инвесторского пути» выше. Полная страница — usluga-relocation в
# pages_uslugi_stranitsy.py; факты — design/relokatsiya-organizatsiy-issledovanie.md.
RELOCATION_CARD = {
    "ru": ("Релокация организаций",
           'Комплекс услуг для переезда бизнеса в Парагвай: регистрация компании, льготный '
           'налоговый режим <a href="{terminologiya}#maquila">Maquila</a> (1% вместо стандартных '
           '10% IRE, включая экспортёров услуг), резидентура для команды и корпоративный счёт.'),
    "es": ("Relocalización de empresas",
           'Paquete de servicios para trasladar un negocio a Paraguay: registro de la empresa, el '
           'régimen fiscal preferencial <a href="{terminologiya}#maquila">Maquila</a> (1% en lugar '
           'del 10% estándar de IRE, incluidos los exportadores de servicios), residencia para el '
           'equipo y cuenta corporativa.'),
    "en": ("Business Relocation",
           'A package of services for moving a business to Paraguay: company registration, the '
           'preferential <a href="{terminologiya}#maquila">Maquila</a> tax regime (1% instead of '
           'the standard 10% IRE, including service exporters), residency for the team, and a '
           'corporate account.'),
    "de": ("Unternehmensrelokation",
           'Leistungspaket für den Umzug eines Unternehmens nach Paraguay: Firmengründung, das '
           'steuerliche Vorzugsregime <a href="{terminologiya}#maquila">Maquila</a> (1% statt der '
           'regulären 10% IRE, einschließlich Dienstleistungsexporteuren), Aufenthaltstitel fürs '
           'Team und Firmenkonto.'),
}

# Девятая услуга — «Медицинское сопровождение» (24.08.2026, старт RU-only; 27.08.2026 —
# переведена на ES/EN/DE по запросу заказчика «Делай мультиязычность и правь карту сайта»). Тот
# же приём короткого анонса + «Подробнее →», что и у «Релокации организаций» выше — теперь
# рендерится безусловно для всех 4 языков, как RELOCATION_CARD. Полная страница —
# usluga-medicina в pages_uslugi_stranitsy.py; факты — design/meditsina-strakhovanie-issledovanie.md.
MEDICINE_CARD = {
    "ru": ("Медицинское сопровождение",
           'Переводчик на приёме у врача с почасовой оплатой и подсказка по медицинской страховке: '
           'можем порекомендовать типичных, распространённых страховщиков.'),
    "es": ("Asistencia médica",
           'Intérprete en la consulta médica, con tarifa por hora, y orientación sobre el seguro '
           'médico: podemos recomendar aseguradoras típicas y habituales.'),
    "en": ("Medical Support",
           'An interpreter at medical appointments, billed by the hour, plus pointers on health '
           'insurance: we can recommend typical, widely used insurers.'),
    "de": ("Medizinische Begleitung",
           'Dolmetscher beim Arzttermin auf Stundenbasis und eine Orientierung zur '
           'Krankenversicherung: Wir können typische, verbreitete Versicherer empfehlen.'),
}

# Короткие анонсы для остальных 5 услуг (27.08.2026, по запросу заказчика «у нас должны быть
# страницы по всем услугам со страницы /uslugi.html?» → «Все 5 сразу, сразу на 4 языках») —
# те же тексты, что стали lead на новых полных страницах в pages_uslugi_stranitsy.py (уже
# сжатая формулировка, повторно использовать её как анонс — не изобретать новый текст).
# В отличие от TEASERS_USLUGI (RU-only, «Резидентура»/«Инвесторский путь» без переводов), эти 5
# сразу мультиязычны — карточка становится анонсом на всех 4 языках одновременно.
TEASERS_NEW5 = {
    "ru": {
        "compliance": "Сопровождение и комплаенс — абонентская услуга, которая поддерживает статус резидента в силе на всём пути от временной резиденции к постоянной, чтобы он не был потерян из-за пропущенной отчётности.",
        "citizenship": "Гражданство Парагвая — статус, который даёт паспорт с безвизовым доступом примерно в 145 стран (Henley Passport Index) и более устойчивое правовое положение, чем резиденция. Краткая справка: сроки, экзамен и стоимость.",
        "realestate": "Проверка и покупка недвижимости — услуга due diligence по конкретному объекту, которая защищает от переплаты и от скрытых рисков сделки, включая ежегодный налог на владение.",
        "company": "Открытие компании — регистрация юридического лица в Парагвае, которое даёт возможность вести бизнес легально: выставлять счета, нанимать сотрудников и открывать банковский счёт на компанию.",
        "business": "Покупка и продажа бизнеса — сопровождение сделки для тех, кто хочет войти в дело через готовую компанию или выйти из своей, а не запускать регистрацию с нуля.",
    },
    "es": {
        "compliance": "El acompañamiento y cumplimiento es un servicio por suscripción que mantiene vigente el estatus de residente durante todo el camino de la temporal a la permanente, para que no se pierda por una declaración omitida.",
        "citizenship": "La ciudadanía paraguaya otorga un pasaporte con acceso sin visa a unos 145 países (Henley Passport Index) y un estatus jurídico más estable que la residencia. Referencia breve: plazos, examen y costo.",
        "realestate": "La verificación y compra de inmuebles es un servicio de due diligence sobre una propiedad concreta, que protege de sobrepagar o de riesgos ocultos, incluido el impuesto anual por tener la propiedad.",
        "company": "La apertura de empresa es la inscripción de una persona jurídica en Paraguay, que permite operar legalmente: facturar, contratar personal y abrir una cuenta bancaria a nombre de la empresa.",
        "business": "La compra y venta de empresas es el acompañamiento de una operación para quienes prefieren entrar a un negocio ya en marcha o salir del propio, en lugar de registrar uno desde cero.",
    },
    "en": {
        "compliance": "Ongoing compliance is a subscription service that keeps your resident status valid all the way from temporary to permanent, so it isn't lost over a missed filing.",
        "citizenship": "Paraguayan citizenship grants a passport with visa-free access to roughly 145 countries (Henley Passport Index) and a more stable legal status than residency. A short reference: timeline, exam and cost.",
        "realestate": "Real estate verification & purchase is a due-diligence service on a specific property, protecting you from overpaying or from hidden risks, including the annual ownership tax.",
        "company": "Company formation is registering a legal entity in Paraguay, which lets you do business legally: issue invoices, hire staff, and open a bank account in the company's name.",
        "business": "Buying & selling a business is deal support for those who'd rather step into a running company or exit their own, instead of registering one from scratch.",
    },
    "de": {
        "compliance": "Begleitung und Compliance ist eine Abonnement-Leistung, die den Aufenthaltsstatus auf dem gesamten Weg von befristet zu unbefristet aufrechterhält, damit er nicht wegen einer versäumten Meldung verloren geht.",
        "citizenship": "Die paraguayische Staatsbürgerschaft verleiht einen Reisepass mit visumfreiem Zugang zu rund 145 Ländern (Henley Passport Index) und einen stabileren Rechtsstatus als der Aufenthaltstitel. Kurze Orientierung: Fristen, Prüfung und Kosten.",
        "realestate": "Prüfung und Kauf von Immobilien ist eine Due-Diligence-Leistung für ein konkretes Objekt, die vor Überzahlung und vor verdeckten Risiken schützt, einschließlich der jährlichen Eigentumssteuer.",
        "company": "Die Unternehmensgründung ist die Eintragung einer juristischen Person in Paraguay, die es ermöglicht, legal Geschäfte zu tätigen: Rechnungen zu stellen, Personal einzustellen und ein Firmenkonto zu eröffnen.",
        "business": "Kauf und Verkauf von Unternehmen ist die Begleitung einer Transaktion für alle, die lieber in ein laufendes Unternehmen einsteigen oder aus dem eigenen aussteigen möchten, statt eines von Grund auf neu zu registrieren.",
    },
}

for lang, t in USLUGI_PAGE.items():
    l = L(lang)
    cards_html = ""
    for key in SERVICE_KEYS:
        title, text = t["cards"][key]
        if lang == "ru" and key in TEASERS_USLUGI:
            full_href = l["usluga-residencia"] if key == "residencia" else l["usluga-investor"]
            cards_html += f'''
    <article id="{key}" class="card" style="margin-bottom:24px;">
      <div class="icon">{ICONS[key]}</div>
      <h3>{title}</h3>
      <p style="font-size:16px;">{TEASERS_USLUGI[key]}</p>
      <a class="card-link" href="{full_href}">Подробнее →</a>
    </article>'''
            continue
        if key in TEASERS_NEW5[lang]:
            cards_html += f'''
    <article id="{key}" class="card" style="margin-bottom:24px;">
      <div class="icon">{ICONS[key]}</div>
      <h3>{title}</h3>
      <p style="font-size:16px;">{TEASERS_NEW5[lang][key]}</p>
      <a class="card-link" href="{l['usluga-' + key]}">{HOME[lang]["more"]}</a>
    </article>'''
            continue
        cards_html += f'''
    <article id="{key}" class="card" style="margin-bottom:24px;">
      <div class="icon">{ICONS[key]}</div>
      <h3>{title}</h3>
      <p style="font-size:16px;">{text.format(**l)}</p>
    </article>'''
    relocation_title, relocation_text = RELOCATION_CARD[lang]
    cards_html += f'''
    <article id="relocation" class="card" style="margin-bottom:24px;">
      <div class="icon">{ICONS['relocation']}</div>
      <h3>{relocation_title}</h3>
      <p style="font-size:16px;">{relocation_text.format(**l)}</p>
      <a class="card-link" href="{l['usluga-relocation']}">{HOME[lang]["more"]}</a>
    </article>'''
    medicine_title, medicine_text = MEDICINE_CARD[lang]
    cards_html += f'''
    <article id="medicina" class="card" style="margin-bottom:24px;">
      <div class="icon">{ICONS['medicina']}</div>
      <h3>{medicine_title}</h3>
      <p style="font-size:16px;">{medicine_text}</p>
      <a class="card-link" href="{l['usluga-medicina']}">{HOME[lang]["more"]}</a>
    </article>'''
    uslugi_body = f'''
{breadcrumbs([(NAV_LABELS[lang]["home"], l['home']), (NAV_LABELS[lang]["uslugi"], None)])}
<section class="hero" style="padding-top:24px;">
  <div class="wrap"><h1>{t["h1"]}</h1>
  <p class="lead">{t["lead"]}</p>
  </div>
</section>
<section style="padding-top:0;">
  <div class="prose">
    {cards_html}
    <p>{t["footer_p"].format(**l)}</p>
  </div>
</section>
'''
    schemas = [schema_breadcrumb([(NAV_LABELS[lang]["home"], f"/{lang}/"), (NAV_LABELS[lang]["uslugi"], f"/{lang}/uslugi")])]
    for key in SERVICE_KEYS:
        title, _ = t["cards"][key]
        schemas.append({"@context": "https://schema.org", "@type": "Service", "name": title,
                         "provider": {"@type": "Organization", "name": "Fortuna Vida E.A.S."}, "areaServed": "Paraguay"})
    schemas.append({"@context": "https://schema.org", "@type": "Service", "name": RELOCATION_CARD[lang][0],
                     "provider": {"@type": "Organization", "name": "Fortuna Vida E.A.S."}, "areaServed": "Paraguay"})
    schemas.append({"@context": "https://schema.org", "@type": "Service", "name": MEDICINE_CARD[lang][0],
                     "provider": {"@type": "Organization", "name": "Fortuna Vida E.A.S."}, "areaServed": "Paraguay"})
    page("uslugi", lang, t["title"], t["description"], uslugi_body, extra_schema=schemas)
