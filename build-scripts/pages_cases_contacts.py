#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Кейсы и отзывы + Контакты — ru/es/en"""
from build import page, breadcrumbs, schema_breadcrumb, DOMAIN, href_to, NAV_LABELS, seal_svg

# Печать «Конфиденциальность» для Контактов (12.08.2026) — те же формулировки и та же
# печать (иконка shield, синий цвет), что и в SEALS["ru"][1] и т.д. на Главной
# (pages_home_uslugi.py) — сознательно не новый визуальный язык, а повторное
# использование уже одобренного заказчиком элемента. top/bottom — кольцевая надпись,
# aria — полный смысл для скринридеров (там же указано и по-русски, что это
# отдельное соглашение с каждым клиентом, а не общая политика сайта).
CONFIDENTIALITY_SEAL = {
    "ru": ("shield", "blue", "Конфиденциальность", "Соглашение с каждым клиентом",
           "Конфиденциальность: отдельное соглашение с каждым клиентом"),
    "es": ("shield", "blue", "Confidencialidad", "Acuerdo con cada cliente",
           "Confidencialidad: un acuerdo aparte con cada cliente"),
    "en": ("shield", "blue", "Confidentiality", "A separate agreement",
           "Confidentiality: a separate agreement with every client"),
    "de": ("shield", "blue", "Vertraulichkeit", "Vereinbarung pro Mandant",
           "Vertraulichkeit: eine gesonderte Vereinbarung mit jedem Mandanten"),
}

def L(lang):
    return {pid: href_to(pid, lang) for pid in
            ["home","uslugi","protsess","riski","stoimost","o-kompanii","konfidentsialnost","keisy","kontakty","terminologiya"]}

# ================================================== КЕЙСЫ И ОТЗЫВЫ / CASE STUDIES

CASES = {
"ru": dict(
    title="Кейсы переезда в Парагвай: иллюстративные сценарии | Grund Paraguay",
    description="Иллюстративные сценарии, а не реальные случаи клиентов: резидентура, инвестиции и бизнес, а также честные истории о трудностях первого года жизни в Парагвае.",
    h1="Кейсы и отзывы: иллюстративные сценарии переезда в Парагвай",
    lead='Мы не называем имена и не публикуем фотографии клиентов — так работает наше <a href="{konfidentsialnost}">соглашение о конфиденциальности</a>, которое мы подписываем с каждым, кто к нам обращается. Вместо этого — иллюстративные сценарии (примерные, а не реальные случаи конкретных клиентов): обобщённые ситуации, которые повторяются в нашей практике, без деталей, по которым можно было бы узнать конкретного человека.',
    h2_1="Соло-специалист на удалённой работе",
    p1='IT-специалист, работающий удалённо на зарубежные компании, подал документы на временную резиденцию (<a href="{terminologiya}#residencia-temporal">Residencia Temporal</a>) вскоре после переезда. Основная сложность была не с самой резиденцией, а с открытием банковского счёта: часть требований банка предполагает уже оформленную парагвайскую <a href="{terminologiya}#cedula">Cédula</a> — а не только поданное заявление на резиденцию, — так что несколько месяцев расчёты велись через альтернативные платёжные сервисы, пока Cédula не была получена. После получения Temporal возникла обязанность зарегистрировать <a href="{terminologiya}#ruc">RUC</a> и вести регулярную налоговую отчётность — этим клиент занимается через абонемент сопровождения (см. страницу <a href="{uslugi}">«Услуги»</a>), включая нулевые декларации в периодах без дохода из парагвайских источников.',
    h2_2="Семья с детьми",
    p2="Пара с двумя детьми школьного возраста собирала документы на резиденцию для всей семьи одновременно: справки о несудимости, свидетельства о рождении и о браке — все с апостилем, часть документов дополнительно потребовала перевода у зарегистрированного в Парагвае присяжного переводчика, потому что были не на испанском. Процесс занял больше времени, чем ожидала семья на старте, — сбор и легализация документов на нескольких членов семьи почти всегда идёт дольше, чем на одного заявителя. После получения Temporal семья закрепила за собой обязательный ежемесячный комплаенс по RUC на основного заявителя.",
    h2_3="Инвестор",
    p3='Клиент выбрал путь <a href="{terminologiya}#suace">SUACE</a> с инвестицией в производственный проект (от 70 000 USD, с бизнес-планом и созданием официальных рабочих мест) вместо стандартного пути через Residencia Temporal. Сертификат инвестора (<a href="{terminologiya}#cie">CIE</a>) был оформлен в официально заявленный срок — 5 рабочих дней с момента подачи полного пакета; собственно постоянная резиденция потребовала ещё нескольких месяцев сверху, что клиенту было озвучено заранее, а не преподнесено как сюрприз после оплаты.',
    h2_4="Владелец бизнеса",
    p4="Клиент рассматривал покупку действующего бизнеса в сфере услуг. Поскольку рынок сделок купли-продажи бизнеса в Парагвае небольшой и не покрывается крупными международными трекерами сделок, стандартной статистики по оценке для сравнения не было — оценка велась индивидуально, с проверкой предложения и сопровождением на этапе передачи, а не по готовому бенчмарку.",
    h2_5="Честно про трудности первого года",
    p5='Отдельная категория историй — не про сделки, а про адаптацию (подробный, не сенсационный разбор рисков — на странице <a href="{riski}">«Риски и трудности»</a>). Один из клиентов столкнулся с сезонным всплеском денге в первые месяцы жизни в стране и на собственном опыте понял, почему мы отдельно рекомендуем медицинскую страховку с покрытием на случай экстренной госпитализации: частные клиники в Парагвае обычно требуют оплату на месте. У другого клиента ожидание перевода в постоянную резиденцию растянулось из-за того, что пакет документов по новым требованиям пришлось донести после уточнений со стороны миграционной службы, — процесс занял больше времени, чем клиент рассчитывал по общим ожиданиям от переезда «за один год», которые он вынес из чужих обещаний до обращения к нам.',
    final_h2="Готовы обсудить свою ситуацию?",
    final_cta="Оставить заявку на консультацию",
),
"es": dict(
    title="Casos de mudanza a Paraguay: escenarios ilustrativos | Grund Paraguay",
    description="Escenarios ilustrativos, no casos reales de clientes: residencia, inversión y negocios, además de relatos honestos sobre las dificultades del primer año en Paraguay.",
    h1="Casos y testimonios: escenarios ilustrativos de mudanza a Paraguay",
    lead='No damos nombres ni publicamos fotos de clientes — así funciona nuestro <a href="{konfidentsialnost}">acuerdo de confidencialidad</a>, que firmamos con cada persona que nos contacta. En su lugar, presentamos escenarios ilustrativos (de ejemplo, no casos reales de clientes concretos): situaciones generalizadas que se repiten en nuestra práctica, sin detalles que permitan identificar a una persona concreta.',
    h2_1="Profesional independiente en trabajo remoto",
    p1='Un especialista en IT que trabaja de forma remota para empresas extranjeras presentó los documentos para la residencia temporal (<a href="{terminologiya}#residencia-temporal">Residencia Temporal</a>) poco después de mudarse. La principal dificultad no fue la residencia en sí, sino la apertura de una cuenta bancaria: parte de los requisitos del banco suponen ya contar con la Cédula paraguaya (<a href="{terminologiya}#cedula">Cédula</a>) — no solo con la solicitud de residencia presentada —, así que durante varios meses los pagos se manejaron mediante servicios de pago alternativos hasta obtener la Cédula. Tras obtener la Temporal, surgió la obligación de inscribir el <a href="{terminologiya}#ruc">RUC</a> y presentar declaraciones tributarias periódicas — algo que el cliente gestiona mediante el abono de acompañamiento (ver la página <a href="{uslugi}">«Servicios»</a>), incluidas las declaraciones en cero en los períodos sin ingresos de fuente paraguaya.',
    h2_2="Familia con hijos",
    p2="Una pareja con dos hijos en edad escolar reunió los documentos de residencia para toda la familia a la vez: certificados de antecedentes penales, actas de nacimiento y de matrimonio — todos apostillados, y parte de los documentos requirió además traducción por un traductor público registrado en Paraguay, por no estar en español. El proceso tomó más tiempo del que la familia esperaba al comienzo — reunir y legalizar documentos para varios miembros de la familia casi siempre lleva más tiempo que para un solo solicitante. Tras obtener la Temporal, la familia asumió el cumplimiento mensual obligatorio del RUC para el solicitante principal.",
    h2_3="Inversor",
    p3='El cliente eligió la vía de <a href="{terminologiya}#suace">SUACE</a> con una inversión en un proyecto productivo (desde 70.000 USD, con plan de negocios y creación de puestos de trabajo formales) en lugar de la vía estándar mediante Residencia Temporal. El certificado de inversor (<a href="{terminologiya}#cie">CIE</a>) se emitió dentro del plazo oficialmente declarado — 5 días hábiles desde la presentación del paquete completo; la residencia permanente en sí demandó varios meses adicionales, algo que se le comunicó al cliente por adelantado y no como una sorpresa después del pago.',
    h2_4="Dueño de negocio",
    p4="El cliente evaluaba la compra de un negocio de servicios en funcionamiento. Como el mercado de compraventa de negocios en Paraguay es pequeño y no está cubierto por los grandes rastreadores internacionales de operaciones, no había estadísticas estándar de valoración para comparar — la evaluación se hizo de forma individual, con verificación de la oferta y acompañamiento en la etapa de transferencia, en lugar de un benchmark preexistente.",
    h2_5="Honestidad sobre las dificultades del primer año",
    p5='Una categoría aparte de historias no trata sobre operaciones, sino sobre la adaptación (un análisis detallado y no sensacionalista de los riesgos está en la página <a href="{riski}">«Riesgos y dificultades»</a>). Uno de los clientes enfrentó un repunte estacional de dengue en sus primeros meses en el país y comprendió de primera mano por qué recomendamos por separado un seguro médico con cobertura para hospitalización de urgencia: las clínicas privadas en Paraguay suelen exigir el pago en el momento. Otro cliente vio prolongarse la espera de su traslado a la residencia permanente porque hubo que completar el paquete de documentos tras aclaraciones solicitadas por el servicio de migraciones — el proceso llevó más tiempo del que el cliente esperaba según las expectativas generales de mudarse «en un año» que traía de promesas ajenas previas a contactarnos.',
    final_h2="¿Listo para conversar sobre su situación?",
    final_cta="Dejar una solicitud de consulta",
),
"en": dict(
    title="Paraguay relocation case studies: illustrative scenarios | Grund Paraguay",
    description="Illustrative scenarios, not real client cases: residency, investment, and business — plus honest stories about the difficulties of the first year in Paraguay.",
    h1="Case Studies: illustrative scenarios of relocating to Paraguay",
    lead='We don\'t give client names or publish photos — that\'s how our <a href="{konfidentsialnost}">confidentiality agreement</a>, which we sign with everyone who reaches out to us, works. Instead, here are illustrative scenarios (examples, not real cases of specific clients): generalized situations that recur in our practice, without details that would let anyone identify a specific person.',
    h2_1="A solo professional working remotely",
    p1='An IT specialist working remotely for foreign companies filed for temporary residency (<a href="{terminologiya}#residencia-temporal">Residencia Temporal</a>) shortly after relocating. The main difficulty wasn\'t the residency itself but opening a bank account: some bank requirements assume you already hold a Paraguayan Cédula (<a href="{terminologiya}#cedula">Cédula</a>) — not just a filed residency application — so for several months payments ran through alternative payment services until the Cédula came through. After obtaining the Temporal, the obligation arose to register an <a href="{terminologiya}#ruc">RUC</a> and file regular tax returns — something the client now handles through the ongoing support subscription (see the <a href="{uslugi}">"Services"</a> page), including zero returns in periods with no Paraguayan-source income.',
    h2_2="A family with children",
    p2="A couple with two school-age children gathered residency documents for the whole family at once: clean criminal record certificates, birth and marriage certificates — all apostilled, with some documents additionally requiring translation by a sworn translator registered in Paraguay, since they weren't in Spanish. The process took longer than the family expected at the outset — gathering and legalizing documents for several family members almost always takes longer than for a single applicant. After obtaining the Temporal, the family locked in mandatory monthly RUC compliance for the primary applicant.",
    h2_3="An investor",
    p3='The client chose the <a href="{terminologiya}#suace">SUACE</a> route with an investment in a production project (from 70,000 USD, with a business plan and the creation of formal jobs) instead of the standard Residencia Temporal route. The investor certificate (<a href="{terminologiya}#cie">CIE</a>) was issued within the officially stated timeframe — 5 business days from submission of the complete package; permanent residency itself required several additional months on top, which was communicated to the client up front rather than sprung on them as a surprise after payment.',
    h2_4="A business owner",
    p4="The client was considering buying an existing service business. Because the market for buying and selling businesses in Paraguay is small and not covered by major international deal trackers, there was no standard valuation data to compare against — the valuation was done individually, with due diligence on the offer and support through the handover stage, rather than against a ready-made benchmark.",
    h2_5="An honest account of first-year difficulties",
    p5='A separate category of stories isn\'t about deals at all, but about adjusting to life in the country (a detailed, non-sensationalized breakdown of risks is on the <a href="{riski}">"Risks & Difficulties"</a> page). One client faced a seasonal dengue spike in their first months in the country and learned firsthand why we specifically recommend health insurance that covers emergency hospitalization: private clinics in Paraguay typically require payment upfront. Another client saw their wait for the transfer to permanent residency stretch out because the document package under the new requirements had to be supplemented after clarification requests from the migration service — the process took longer than the client had expected based on the general "one year" relocation promises they carried in from elsewhere before contacting us.',
    final_h2="Ready to discuss your situation?",
    final_cta="Request a consultation",
),
"de": dict(
    title="Fallstudien zum Umzug nach Paraguay: Beispielszenarien | Grund Paraguay",
    description="Beispielszenarien, keine realen Mandantenfälle: Aufenthalt, Investition und Geschäft, sowie ehrliche Geschichten über die Schwierigkeiten des ersten Jahres in Paraguay.",
    h1="Fallstudien: Beispielszenarien für den Umzug nach Paraguay",
    lead='Wir nennen keine Namen und veröffentlichen keine Fotos von Mandanten — so funktioniert unsere <a href="{konfidentsialnost}">Vertraulichkeitsvereinbarung</a>, die wir mit jedem unterzeichnen, der sich an uns wendet. Stattdessen gibt es Beispielszenarien (illustrativ, keine realen Fälle konkreter Mandanten): verallgemeinerte Situationen, die sich in unserer Praxis wiederholen, ohne Details, an denen eine bestimmte Person erkennbar wäre.',
    h2_1="Ein Solo-Fachkraft im Homeoffice",
    p1='Ein IT-Spezialist, der remote für ausländische Unternehmen arbeitet, stellte kurz nach dem Umzug den Antrag auf befristeten Aufenthalt (<a href="{terminologiya}#residencia-temporal">Residencia Temporal</a>). Die Hauptschwierigkeit lag nicht beim Aufenthaltstitel selbst, sondern bei der Eröffnung eines Bankkontos: Ein Teil der Bankanforderungen setzt bereits eine ausgestellte paraguayische <a href="{terminologiya}#cedula">Cédula</a> voraus — nicht nur einen gestellten Antrag auf Aufenthalt —, sodass Zahlungen mehrere Monate lang über alternative Zahlungsdienste abgewickelt wurden, bis die Cédula erhalten war. Nach Erhalt der Temporal entstand die Pflicht, eine <a href="{terminologiya}#ruc">RUC</a> zu registrieren und regelmäßig Steuererklärungen einzureichen — das übernimmt der Mandant über das Begleitabonnement (siehe Seite <a href="{uslugi}">„Leistungen"</a>), einschließlich Nullmeldungen in Perioden ohne Einkommen aus paraguayischen Quellen.',
    h2_2="Familie mit Kindern",
    p2="Ein Paar mit zwei Kindern im Schulalter sammelte gleichzeitig die Aufenthaltsdokumente für die ganze Familie: Führungszeugnisse, Geburts- und Heiratsurkunden — alle mit Apostille, ein Teil der Dokumente erforderte zusätzlich eine Übersetzung durch einen in Paraguay registrierten vereidigten Übersetzer, da sie nicht auf Spanisch waren. Der Prozess dauerte länger, als die Familie zu Beginn erwartet hatte — das Sammeln und Legalisieren von Dokumenten für mehrere Familienmitglieder dauert fast immer länger als für einen einzelnen Antragsteller. Nach Erhalt der Temporal übernahm die Familie die obligatorische monatliche RUC-Compliance für den Hauptantragsteller.",
    h2_3="Investor",
    p3='Der Mandant wählte den Weg über <a href="{terminologiya}#suace">SUACE</a> mit einer Investition in ein Produktionsprojekt (ab 70.000 USD, mit Geschäftsplan und Schaffung offizieller Arbeitsplätze) anstelle des Standardwegs über die Residencia Temporal. Das Investorenzertifikat (<a href="{terminologiya}#cie">CIE</a>) wurde innerhalb der offiziell angegebenen Frist ausgestellt — 5 Werktage ab Einreichung des vollständigen Pakets; der unbefristete Aufenthaltstitel selbst erforderte noch einige zusätzliche Monate, was dem Mandanten im Voraus mitgeteilt wurde und nicht als Überraschung nach der Zahlung präsentiert wurde.',
    h2_4="Unternehmensinhaber",
    p4="Der Mandant erwog den Kauf eines bestehenden Dienstleistungsunternehmens. Da der Markt für den Kauf und Verkauf von Unternehmen in Paraguay klein ist und nicht von großen internationalen Deal-Trackern erfasst wird, gab es keine Standardstatistik zur Bewertung als Vergleich — die Bewertung erfolgte individuell, mit Prüfung des Angebots und Begleitung in der Übergabephase, statt anhand einer fertigen Benchmark.",
    h2_5="Ehrlich über die Schwierigkeiten des ersten Jahres",
    p5='Eine eigene Kategorie von Geschichten handelt nicht von Geschäften, sondern von der Eingewöhnung (eine ausführliche, nicht reißerische Darstellung der Risiken auf der Seite <a href="{riski}">„Risiken und Schwierigkeiten"</a>). Ein Mandant erlebte in den ersten Monaten im Land einen saisonalen Dengue-Anstieg und verstand aus eigener Erfahrung, warum wir gesondert eine Krankenversicherung mit Deckung für Notfallhospitalisierung empfehlen: Private Kliniken in Paraguay verlangen in der Regel Zahlung vor Ort. Bei einem anderen Mandanten zog sich die Wartezeit für den Übergang zum unbefristeten Aufenthalt hin, weil das Dokumentenpaket nach den neuen Anforderungen nach Rückfragen der Migrationsbehörde ergänzt werden musste — der Prozess dauerte länger, als der Mandant aufgrund allgemeiner Erwartungen an einen Umzug „in einem Jahr\" erwartet hatte, die er aus fremden Versprechungen vor der Kontaktaufnahme mit uns mitgebracht hatte.',
    final_h2="Bereit, über Ihre Situation zu sprechen?",
    final_cta="Beratung anfragen",
),
}

for lang in ["ru","es","en","de"]:
    t = CASES[lang]
    l = L(lang)
    cases_body = f'''
{breadcrumbs([(NAV_LABELS[lang]["home"], l["home"]), (NAV_LABELS[lang]["keisy"], None)])}
<section class="hero" style="padding-top:24px;">
  <div class="wrap">
    <h1>{t["h1"]}</h1>
    <p class="lead">{t["lead"].format(**l)}</p>
  </div>
</section>
<section style="padding-top:0;">
  <div class="prose">
    <h2>{t["h2_1"]}</h2>
    <p>{t["p1"].format(**l)}</p>

    <h2>{t["h2_2"]}</h2>
    <p>{t["p2"]}</p>

    <h2>{t["h2_3"]}</h2>
    <p>{t["p3"].format(**l)}</p>

    <h2>{t["h2_4"]}</h2>
    <p>{t["p4"]}</p>

    <h2>{t["h2_5"]}</h2>
    <p>{t["p5"].format(**l)}</p>

    <div class="final-cta">
      <h2>{t["final_h2"]}</h2>
      <a class="btn" href="{l['kontakty']}">{t["final_cta"]}</a>
    </div>
  </div>
</section>
'''
    page("keisy", lang, t["title"], t["description"], cases_body,
         extra_schema=schema_breadcrumb([(NAV_LABELS[lang]["home"], f"/{lang}/"), (NAV_LABELS[lang]["keisy"], f"/{lang}/{href_to('keisy', lang)}")]))

# ============================================================= КОНТАКТЫ / CONTACT

CONTACTS = {
"ru": dict(
    title="Контакты: заявка на консультацию по переезду в Парагвай | Grund Paraguay",
    description="Заявка на консультацию по переезду в Парагвай: Telegram и форма на сайте, данные защищены соглашением о конфиденциальности — без обещаний гражданства за год.",
    h1="Контакты и заявка на консультацию",
    lead='Если вы уже готовы обсудить свою ситуацию — оставьте заявку, и мы свяжемся с вами, чтобы назначить консультацию. Первая консультация — бесплатная, ознакомительная. Если пока только присматриваетесь к теме — начните с бесплатного гайда «С чего начать переезд в Парагвай» или со страницы <a href="{uslugi}">«Услуги»</a>.',
    form_h2="Форма заявки",
    label_name="Имя",
    label_contact="Telegram или email",
    label_message="Коротко о ситуации",
    btn_submit="Отправить заявку",
    form_note="Черновая версия формы: приём заявок пока не подключён к реальному каналу (email/Telegram-бот/CRM) — это техническая задача блока D чек-листа MVP. Пока используйте Telegram или email справа.",
    direct_h2="Прямая связь",
    p_direct='Основной канал коммуникации — Telegram: <a href="https://t.me/grundparaguay">@grundparaguay</a>. Форма заявки на сайте дублирует эту возможность для тех, кто предпочитает не переходить в мессенджер сразу. Также можно написать на <a href="mailto:office@fortuna-vida.com.py">office@fortuna-vida.com.py</a> или позвонить по телефону +595 98 39 555 04 — отвечаем в будни, 9:00–18:00 по времени Парагвая (PYT).',
    p_address='Юридический адрес: ETAPA 9009 San Isidro, 6000 Encarnación, Paraguay.',
    badge="Данные защищены соглашением о конфиденциальности",
    p_confidential='Ваши данные защищены <a href="{konfidentsialnost}">соглашением о конфиденциальности</a>, которое мы подписываем с каждым клиентом как часть основного соглашения. Мы не обещаем гражданство за год и не смешиваем государственную пошлину с нашим гонораром — это отражено в письменной договорённости, а не только в разговоре на консультации; полная стоимость — на странице <a href="{stoimost}">«Стоимость и тарифы»</a>.',
    p_note="Telegram — прежний плейсхолдер, не подтверждённый заказчиком; остальные реквизиты (название, адрес, email, телефон) реальные (см. внутренний чек-лист проекта).",
    schema_name="Контакты Grund Paraguay",
),
"es": dict(
    title="Contacto: solicitud de consulta sobre la mudanza a Paraguay | Grund Paraguay",
    description="Solicite una consulta sobre la mudanza a Paraguay: Telegram y formulario en el sitio, datos protegidos por el acuerdo de confidencialidad — sin promesas de ciudadanía en un año.",
    h1="Contacto y solicitud de consulta",
    lead='Si ya está listo para conversar sobre su situación, deje una solicitud y nos pondremos en contacto para coordinar una consulta. La primera consulta es gratuita e informativa. Si todavía está evaluando el tema, empiece por la guía gratuita «Por dónde empezar la mudanza a Paraguay» o por la página <a href="{uslugi}">«Servicios»</a>.',
    form_h2="Formulario de solicitud",
    label_name="Nombre",
    label_contact="Telegram o email",
    label_message="Breve descripción de su situación",
    btn_submit="Enviar solicitud",
    form_note="Versión de prueba del formulario: la recepción de solicitudes todavía no está conectada a un canal real (email/bot de Telegram/CRM) — es una tarea técnica del bloque D de la lista de verificación del MVP. Mientras tanto, use el Telegram o el email de la derecha.",
    direct_h2="Contacto directo",
    p_direct='El canal principal de comunicación es Telegram: <a href="https://t.me/grundparaguay">@grundparaguay</a>. El formulario del sitio duplica esta opción para quienes prefieren no pasar directamente a un mensajero. También puede escribir a <a href="mailto:office@fortuna-vida.com.py">office@fortuna-vida.com.py</a> o llamar al +595 98 39 555 04 — respondemos en días hábiles, de 9:00 a 18:00 hora de Paraguay (PYT).',
    p_address='Domicilio legal: ETAPA 9009 San Isidro, 6000 Encarnación, Paraguay.',
    badge="Datos protegidos por el acuerdo de confidencialidad",
    p_confidential='Sus datos están protegidos por el <a href="{konfidentsialnost}">acuerdo de confidencialidad</a> que firmamos con cada cliente como parte del acuerdo principal. No prometemos la ciudadanía en un año ni mezclamos el arancel estatal con nuestros honorarios — esto consta en el acuerdo por escrito, no solo en la conversación durante la consulta; el costo completo está en la página <a href="{stoimost}">«Costos y tarifas»</a>.',
    p_note="El Telegram sigue siendo un marcador de posición sin confirmar; el resto de los datos (nombre, domicilio, email, teléfono) son reales (ver la lista de verificación interna del proyecto).",
    schema_name="Contacto de Grund Paraguay",
),
"en": dict(
    title="Contact: request a consultation about relocating to Paraguay | Grund Paraguay",
    description="Request a consultation about relocating to Paraguay: Telegram and a form on the site, data protected by a confidentiality agreement — no promises of citizenship in a year.",
    h1="Contact and consultation request",
    lead='If you\'re already ready to discuss your situation, leave a request and we\'ll get in touch to schedule a consultation. The first consultation is free and introductory. If you\'re still just exploring the topic, start with the free guide "Where to start relocating to Paraguay" or the <a href="{uslugi}">"Services"</a> page.',
    form_h2="Request form",
    label_name="Name",
    label_contact="Telegram or email",
    label_message="Briefly describe your situation",
    btn_submit="Send request",
    form_note="Draft version of the form: request intake isn't yet connected to a real channel (email / Telegram bot / CRM) — that's a technical task under Block D of the MVP checklist. For now, use the Telegram or email on the right.",
    direct_h2="Direct contact",
    p_direct='Our main communication channel is Telegram: <a href="https://t.me/grundparaguay">@grundparaguay</a>. The form on the site duplicates this option for those who\'d rather not switch to a messenger right away. You can also write to <a href="mailto:office@fortuna-vida.com.py">office@fortuna-vida.com.py</a> or call +595 98 39 555 04 — we respond on weekdays, 9:00 AM–6:00 PM Paraguay time (PYT).',
    p_address='Registered address: ETAPA 9009 San Isidro, 6000 Encarnación, Paraguay.',
    badge="Data protected by a confidentiality agreement",
    p_confidential='Your data is protected by the <a href="{konfidentsialnost}">confidentiality agreement</a> we sign with every client as part of the main agreement. We don\'t promise citizenship in a year, and we don\'t blend the government fee with our own fee — that\'s reflected in the written agreement, not just in the consultation conversation; the full cost is on the <a href="{stoimost}">"Costs and Rates"</a> page.',
    p_note="The Telegram handle is still an unconfirmed placeholder; the other details (legal name, address, email, phone) are real (see the project's internal checklist).",
    schema_name="Grund Paraguay Contact",
),
"de": dict(
    title="Kontakt: Beratungsanfrage zum Umzug nach Paraguay | Grund Paraguay",
    description="Beratungsanfrage zum Umzug nach Paraguay: Telegram und Formular auf der Website, Daten durch Vertraulichkeitsvereinbarung geschützt — ohne Versprechen von Staatsbürgerschaft in einem Jahr.",
    h1="Kontakt und Beratungsanfrage",
    lead='Wenn Sie bereits bereit sind, über Ihre Situation zu sprechen — stellen Sie eine Anfrage, und wir melden uns bei Ihnen, um eine Beratung zu vereinbaren. Die erste Beratung ist kostenlos und unverbindlich. Wenn Sie sich gerade erst mit dem Thema befassen — beginnen Sie mit dem kostenlosen Leitfaden „Womit beginnt der Umzug nach Paraguay\" oder mit der Seite <a href="{uslugi}">„Leistungen"</a>.',
    form_h2="Anfrageformular",
    label_name="Name",
    label_contact="Telegram oder E-Mail",
    label_message="Kurz zur Situation",
    btn_submit="Anfrage senden",
    form_note="Entwurfsversion des Formulars: Die Annahme von Anfragen ist noch nicht mit einem echten Kanal verbunden (E-Mail/Telegram-Bot/CRM) — das ist eine technische Aufgabe von Block D der MVP-Checkliste. Nutzen Sie vorerst Telegram oder E-Mail rechts.",
    direct_h2="Direkter Kontakt",
    p_direct='Der Hauptkommunikationskanal ist Telegram: <a href="https://t.me/grundparaguay">@grundparaguay</a>. Das Formular auf der Website dupliziert diese Möglichkeit für diejenigen, die nicht sofort zu einem Messenger wechseln möchten. Sie können auch an <a href="mailto:office@fortuna-vida.com.py">office@fortuna-vida.com.py</a> schreiben oder unter +595 98 39 555 04 anrufen — wir antworten werktags, 9:00–18:00 Uhr paraguayischer Zeit (PYT).',
    p_address='Geschäftssitz: ETAPA 9009 San Isidro, 6000 Encarnación, Paraguay.',
    badge="Daten durch Vertraulichkeitsvereinbarung geschützt",
    p_confidential='Ihre Daten sind durch die <a href="{konfidentsialnost}">Vertraulichkeitsvereinbarung</a> geschützt, die wir mit jedem Mandanten als Teil der Hauptvereinbarung unterzeichnen. Wir versprechen keine Staatsbürgerschaft in einem Jahr und vermischen nicht die staatliche Gebühr mit unserem Honorar — das ist in der schriftlichen Vereinbarung festgehalten, nicht nur im Beratungsgespräch; die vollständigen Kosten stehen auf der Seite <a href="{stoimost}">„Preise"</a>.',
    p_note="Der Telegram-Handle ist weiterhin ein unbestätigter Platzhalter; die übrigen Angaben (Firmenname, Adresse, E-Mail, Telefon) sind echt (siehe interne Checkliste des Projekts).",
    schema_name="Kontakt Grund Paraguay",
),
}

for lang in ["ru","es","en","de"]:
    t = CONTACTS[lang]
    l = L(lang)
    conf_icon, conf_color, conf_top, conf_bottom, conf_aria = CONFIDENTIALITY_SEAL[lang]
    contacts_body = f'''
{breadcrumbs([(NAV_LABELS[lang]["home"], l["home"]), (NAV_LABELS[lang]["kontakty"], None)])}
<section class="hero" style="padding-top:24px;">
  <div class="wrap">
    <h1>{t["h1"]}</h1>
    <p class="lead">{t["lead"].format(**l)}</p>
  </div>
</section>
<section style="padding-top:0;">
  <div class="wrap">
    <div class="grid grid-2">
      <div class="prose" style="padding:0;max-width:100%;width:100%;">
        <h2 style="margin-top:0;">{t["form_h2"]}</h2>
        <form onsubmit="event.preventDefault(); this.querySelector('.form-note').style.display='block';" style="display:flex;flex-direction:column;gap:14px;max-width:100%;">
          <label style="font-size:14px;font-weight:600;color:var(--ink);">{t["label_name"]}
            <input type="text" name="name" required style="display:block;width:100%;margin-top:4px;padding:10px 12px;border:1px solid rgba(20,33,59,.25);border-radius:4px;font-family:inherit;font-size:15px;">
          </label>
          <label style="font-size:14px;font-weight:600;color:var(--ink);">{t["label_contact"]}
            <input type="text" name="contact" required style="display:block;width:100%;margin-top:4px;padding:10px 12px;border:1px solid rgba(20,33,59,.25);border-radius:4px;font-family:inherit;font-size:15px;">
          </label>
          <label style="font-size:14px;font-weight:600;color:var(--ink);">{t["label_message"]}
            <textarea name="message" rows="4" style="display:block;width:100%;margin-top:4px;padding:10px 12px;border:1px solid rgba(20,33,59,.25);border-radius:4px;font-family:inherit;font-size:15px;"></textarea>
          </label>
          <button class="btn" type="submit" style="align-self:flex-start;border:none;cursor:pointer;">{t["btn_submit"]}</button>
          <p class="form-note" style="display:none;font-size:13px;color:var(--ink-muted);">{t["form_note"]}</p>
        </form>
      </div>
      <div class="prose" style="padding:0;max-width:100%;">
        <h2 style="margin-top:0;">{t["direct_h2"]}</h2>
        <p>{t["p_direct"]}</p>
        <p>{t["p_address"]}</p>
        <div class="seal seal-float">{seal_svg(conf_icon, conf_top, conf_bottom, "seal-"+conf_color, conf_aria, uid=f"kontakty-{lang}")}</div>
        <p>{t["p_confidential"].format(**l)}</p>
        <p class="confidence-note">{t["p_note"]}</p>
      </div>
    </div>
  </div>
</section>
'''
    page("kontakty", lang, t["title"], t["description"], contacts_body,
         extra_schema=[
             schema_breadcrumb([(NAV_LABELS[lang]["home"], f"/{lang}/"), (NAV_LABELS[lang]["kontakty"], f"/{lang}/{href_to('kontakty', lang)}")]),
             {"@context":"https://schema.org","@type":"ContactPage","name":t["schema_name"],
              "mainEntity":{"@type":"Organization","name":"Fortuna Vida E.A.S.","email":"office@fortuna-vida.com.py",
                             "telephone":"+595 98 39 555 04",
                             "address":{"@type":"PostalAddress","streetAddress":"ETAPA 9009 San Isidro","postalCode":"6000","addressLocality":"Encarnación","addressCountry":"PY"},
                             "sameAs":["https://t.me/grundparaguay"]}}
         ])
