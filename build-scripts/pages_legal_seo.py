#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Оферта, Политика конфиденциальности сайта + robots/sitemap — ru/es/en"""
from build import page, breadcrumbs, schema_breadcrumb, DOMAIN, ROOT, LANGS, DEFAULT_LANG, SLUGS, href_to, NAV_LABELS, slug
import os

def L(lang):
    return {pid: href_to(pid, lang) for pid in
            ["home","uslugi","protsess","riski","stoimost","o-kompanii","konfidentsialnost","keisy","kontakty","terminologiya"]}

DRAFT_BANNER = {
"ru": '''
<div class="callout" style="border-color:var(--red);">
  <span class="callout-label" style="color:var(--red-deep);">Черновик — не публиковать без юридической вычитки</span>
  Этот документ подготовлен как рабочий черновик для запуска первой версии сайта и пока не проверен юристом. Перед публичным запуском его нужно показать юристу (желательно — практикующему в Парагвае и знакомому с применимым к сайту правом), а также заменить тестовые реквизиты компании на реальные.
</div>
''',
"es": '''
<div class="callout" style="border-color:var(--red);">
  <span class="callout-label" style="color:var(--red-deep);">Borrador — no publicar sin revisión legal</span>
  Este documento se preparó como borrador de trabajo para el lanzamiento de la primera versión del sitio y todavía no fue revisado por un abogado. Antes del lanzamiento público debe mostrarse a un abogado (idealmente con ejercicio en Paraguay y conocimiento del derecho aplicable al sitio), y los datos de prueba de la empresa deben reemplazarse por datos reales.
</div>
''',
"en": '''
<div class="callout" style="border-color:var(--red);">
  <span class="callout-label" style="color:var(--red-deep);">Draft — do not publish without legal review</span>
  This document was prepared as a working draft for launching the first version of the site and has not yet been reviewed by a lawyer. Before a public launch it needs to be shown to a lawyer (ideally one practicing in Paraguay and familiar with the law applicable to the site), and the company's placeholder details need to be replaced with real ones.
</div>
''',
"de": '''
<div class="callout" style="border-color:var(--red);">
  <span class="callout-label" style="color:var(--red-deep);">Entwurf — nicht ohne rechtliche Prüfung veröffentlichen</span>
  Dieses Dokument wurde als Arbeitsentwurf für den Start der ersten Version der Website erstellt und wurde noch nicht von einem Anwalt geprüft. Vor einer öffentlichen Veröffentlichung muss es einem Anwalt vorgelegt werden (idealerweise einem in Paraguay tätigen Anwalt, der mit dem auf die Website anwendbaren Recht vertraut ist), und die Platzhalterangaben des Unternehmens müssen durch echte Daten ersetzt werden.
</div>
''',
}

# ==================================================== ОФЕРТА / PUBLIC OFFER

OFERTA = {
"ru": dict(
    title="Публичная оферта — Grund Paraguay",
    description="Публичная оферта на оказание консультационных услуг по переезду, резидентуре и бизнесу в Парагвае. Черновик, требует юридической вычитки.",
    h1="Публичная оферта на оказание консультационных услуг",
    p_scope='Действует в отношении услуг, описанных на странице <a href="{uslugi}">«Услуги»</a>: резидентура, сопровождение и комплаенс, гражданство, инвесторский путь, проверка недвижимости, открытие компании, сопровождение сделок купли-продажи бизнеса. Не заменяет индивидуальное соглашение с клиентом, которое фиксирует объём и стоимость конкретной услуги (см. страницу <a href="{o-kompanii}">«О компании»</a>).',
    sections=[
        ("1. Общие положения",
         '1.1. Настоящий документ является публичной офертой Fortuna Vida E.A.S. (далее — «Исполнитель») в адрес любого дееспособного физического или юридического лица (далее — «Заказчик») заключить соглашение об оказании консультационных и сопроводительных услуг, связанных с переездом, оформлением резиденции, гражданства, ведением бизнеса и сделками с недвижимостью в Республике Парагвай, на условиях, изложенных ниже.<br><br>'
         '1.2. Акцептом настоящей оферты является подача заявки через страницу <a href="{kontakty}">«Контакты»</a> и последующее подписание индивидуального соглашения с Исполнителем — сама по себе заявка не создаёт обязательств сторон до подписания соглашения.'),
        ("2. Предмет соглашения",
         '2.1. Исполнитель обязуется оказать Заказчику услуги в объёме, согласованном сторонами в индивидуальном соглашении, а Заказчик — оплатить эти услуги на условиях соглашения.<br><br>'
         '2.2. Государственные пошлины, налоги и иные обязательные платежи в пользу государственных органов Парагвая, а также услуги сторонних партнёров (например, юристов и нотариусов на месте) не входят в стоимость услуг Исполнителя и оплачиваются Заказчиком отдельно — см. страницу <a href="{stoimost}">«Стоимость и тарифы»</a>.'),
        ("3. Стоимость и порядок оплаты",
         '3.1. Стоимость услуг фиксируется в индивидуальном соглашении до начала работы и не изменяется в одностороннем порядке, за исключением случаев существенного изменения объёма работ, согласованного сторонами дополнительно.<br><br>'
         '3.2. Полная сумма за согласованную услугу вносится к моменту подачи на Cédula (CI); детали графика оплаты фиксируются в индивидуальном соглашении.<br><br>'
         '3.3. Спецпожелания Заказчика (например, поиск жилья или аренда авто) возможны всегда; фиксированного прайс-листа на них нет, так как трудозатраты заранее точно не оценить, — они оплачиваются по часовой ставке или пакетом.'),
        ("4. Права и обязанности сторон",
         '4.1. Исполнитель обязуется действовать добросовестно, информировать Заказчика об изменениях в применимом законодательстве Парагвая, влияющих на оказываемую услугу, и не давать заведомо недостоверных обещаний по срокам (см. позицию Исполнителя на странице <a href="{riski}">«Риски и трудности»</a>).<br><br>'
         '4.2. Заказчик обязуется предоставлять достоверные документы и сведения, необходимые для оказания услуги, и своевременно уведомлять Исполнителя об изменениях, влияющих на ход дела.'),
        ("5. Ответственность сторон",
         '5.1. Исполнитель не несёт ответственности за решения государственных органов Парагвая (включая отказ в выдаче резиденции или гражданства), если они приняты не вследствие ненадлежащего исполнения Исполнителем своих обязательств.<br><br>'
         '5.2. Иные условия ответственности, включая ограничение и распределение рисков, фиксируются в индивидуальном соглашении.'),
        ("6. Конфиденциальность",
         '6.1. Обработка персональных, финансовых и иных данных Заказчика в рамках оказания услуг регулируется отдельным <a href="{konfidentsialnost}">соглашением о конфиденциальности</a>, прилагаемым к индивидуальному соглашению.'),
        ("7. Форс-мажор",
         '7.1. Стороны освобождаются от ответственности за неисполнение обязательств, если оно вызвано обстоятельствами непреодолимой силы (форс-мажор) — чрезвычайными событиями, которые стороны не могли предвидеть и предотвратить, например: банкротство банка, авиакатастрофа или торнадо, разрушивший офис. К таким обстоятельствам относятся и существенные изменения миграционного законодательства Парагвая, произошедшие после заключения соглашения.'),
        ("8. Разрешение споров",
         '8.1. Споры рассматриваются по месту нахождения Исполнителя — в Encarnación (Парагвай). Применимое право и иные детали порядка разрешения споров фиксируются в индивидуальном соглашении.'),
    ],
    h2_details="9. Реквизиты Исполнителя",
    p_details='Fortuna Vida E.A.S.<br>Адрес: ETAPA 9009 San Isidro, 6000 Encarnación, Paraguay<br>Email: <a href="mailto:office@fortuna-vida.com.py">office@fortuna-vida.com.py</a><br>Телефон: <a href="tel:+595983955504">+595 98 39 555 04</a><br>Telegram: <a href="https://t.me/grundparaguay">@grundparaguay</a>',
    p_note="Регистрационный номер (RUC) и прочие корпоративные реквизиты пока не заполнены реальными данными — юридический адрес и остальные контакты уже реальные (см. внутренний чек-лист проекта).",
),
"es": dict(
    title="Oferta pública — Grund Paraguay",
    description="Oferta pública para la prestación de servicios de consultoría sobre mudanza, residencia y negocios en Paraguay. Borrador, requiere revisión legal.",
    h1="Oferta pública para la prestación de servicios de consultoría",
    p_scope='Aplica a los servicios descritos en la página <a href="{uslugi}">«Servicios»</a>: residencia, acompañamiento y cumplimiento, ciudadanía, vía de inversor, due diligence inmobiliario, constitución de empresas, acompañamiento en la compraventa de negocios. No reemplaza el acuerdo individual con el cliente, que fija el alcance y el costo del servicio concreto (ver la página <a href="{o-kompanii}">«Sobre nosotros»</a>).',
    sections=[
        ("1. Disposiciones generales",
         '1.1. El presente documento constituye una oferta pública de Fortuna Vida E.A.S. (en adelante, el «Prestador») dirigida a cualquier persona física o jurídica con capacidad legal (en adelante, el «Cliente») para celebrar un acuerdo de servicios de consultoría y acompañamiento relacionados con la mudanza, la tramitación de la residencia, la ciudadanía, la actividad empresarial y las operaciones inmobiliarias en la República del Paraguay, en los términos que se detallan a continuación.<br><br>'
         '1.2. La aceptación de esta oferta se produce mediante el envío de una solicitud a través de la página <a href="{kontakty}">«Contacto»</a> y la posterior firma de un acuerdo individual con el Prestador — la solicitud por sí sola no genera obligaciones para las partes hasta la firma del acuerdo.'),
        ("2. Objeto del acuerdo",
         '2.1. El Prestador se compromete a brindar al Cliente los servicios en el alcance acordado por las partes en el acuerdo individual, y el Cliente, a pagar dichos servicios en los términos del acuerdo.<br><br>'
         '2.2. Los aranceles estatales, impuestos y demás pagos obligatorios a favor de organismos del Estado paraguayo, así como los servicios de socios externos (por ejemplo, abogados y escribanos en el lugar), no forman parte del costo de los servicios del Prestador y son abonados por el Cliente por separado — ver la página <a href="{stoimost}">«Costos y tarifas»</a>.'),
        ("3. Costo y forma de pago",
         '3.1. El costo de los servicios se fija en el acuerdo individual antes de comenzar el trabajo y no se modifica unilateralmente, salvo en caso de un cambio sustancial en el alcance del trabajo, acordado adicionalmente entre las partes.<br><br>'
         '3.2. El monto completo del servicio acordado se abona hasta el momento de solicitar la Cédula (CI); los detalles del cronograma de pago se fijan en el acuerdo individual.<br><br>'
         '3.3. Los pedidos especiales del Cliente (por ejemplo, buscar vivienda o alquilar un auto) siempre son posibles; no tienen una lista de precios fija, porque el trabajo no se puede estimar con exactitud de antemano, y se cobran por tarifa horaria o como paquete.'),
        ("4. Derechos y obligaciones de las partes",
         '4.1. El Prestador se compromete a actuar de buena fe, informar al Cliente sobre cambios en la legislación paraguaya aplicable que afecten al servicio prestado, y a no hacer promesas de plazos que sabe inexactas (ver la postura del Prestador en la página <a href="{riski}">«Riesgos y dificultades»</a>).<br><br>'
         '4.2. El Cliente se compromete a proporcionar documentos e información veraces necesarios para la prestación del servicio, y a notificar oportunamente al Prestador sobre cambios que afecten el curso del trámite.'),
        ("5. Responsabilidad de las partes",
         '5.1. El Prestador no es responsable por las decisiones de los organismos estatales paraguayos (incluida la denegación de la residencia o la ciudadanía), cuando estas no sean consecuencia de un incumplimiento del Prestador.<br><br>'
         '5.2. Las demás condiciones de responsabilidad, incluida la limitación y distribución de riesgos, se fijan en el acuerdo individual.'),
        ("6. Confidencialidad",
         '6.1. El tratamiento de los datos personales, financieros y de otro tipo del Cliente en el marco de la prestación de los servicios se rige por un <a href="{konfidentsialnost}">acuerdo de confidencialidad</a> separado, adjunto al acuerdo individual.'),
        ("7. Fuerza mayor",
         '7.1. Las partes quedan exentas de responsabilidad por el incumplimiento de obligaciones cuando este se deba a circunstancias de fuerza mayor — hechos extraordinarios que las partes no podían prever ni evitar, por ejemplo: la quiebra de un banco, un accidente aéreo o un tornado que destruya la oficina. Se incluyen también los cambios sustanciales en la legislación migratoria paraguaya ocurridos después de la celebración del acuerdo.'),
        ("8. Resolución de controversias",
         '8.1. Las controversias se someten a los tribunales de Encarnación (Paraguay), domicilio del Prestador. El derecho aplicable y los demás detalles del procedimiento se fijan en el acuerdo individual.'),
    ],
    h2_details="9. Datos del Prestador",
    p_details='Fortuna Vida E.A.S.<br>Dirección: ETAPA 9009 San Isidro, 6000 Encarnación, Paraguay<br>Email: <a href="mailto:office@fortuna-vida.com.py">office@fortuna-vida.com.py</a><br>Teléfono: <a href="tel:+595983955504">+595 98 39 555 04</a><br>Telegram: <a href="https://t.me/grundparaguay">@grundparaguay</a>',
    p_note="El número de registro (RUC) y otros datos corporativos aún no se completaron con datos reales — el domicilio legal y el resto de los contactos ya son reales (ver la lista de verificación interna del proyecto).",
),
"en": dict(
    title="Public Offer — Grund Paraguay",
    description="Public offer for consulting services on relocation, residency, and business in Paraguay. Draft, requires legal review.",
    h1="Public offer for the provision of consulting services",
    p_scope='This applies to the services described on the <a href="{uslugi}">"Services"</a> page: residency, ongoing support and compliance, citizenship, the investor route, real-estate due diligence, company formation, and support for business purchase/sale deals. It does not replace the individual agreement with the client, which fixes the scope and cost of a specific service (see the <a href="{o-kompanii}">"About Us"</a> page).',
    sections=[
        ("1. General provisions",
         '1.1. This document is a public offer from Fortuna Vida E.A.S. (the "Provider") addressed to any legally capable individual or legal entity (the "Client") to enter into an agreement for consulting and support services related to relocation, residency, citizenship, business activity, and real-estate transactions in the Republic of Paraguay, on the terms set out below.<br><br>'
         '1.2. Acceptance of this offer occurs by submitting a request via the <a href="{kontakty}">"Contact"</a> page and subsequently signing an individual agreement with the Provider — the request by itself does not create obligations for either party until the agreement is signed.'),
        ("2. Subject of the agreement",
         '2.1. The Provider agrees to provide the Client with services within the scope agreed by the parties in the individual agreement, and the Client agrees to pay for these services on the terms of the agreement.<br><br>'
         '2.2. Government fees, taxes, and other mandatory payments to Paraguayan state authorities, as well as the services of third-party partners (for example, local lawyers and notaries), are not included in the Provider\'s service fees and are paid by the Client separately — see the <a href="{stoimost}">"Costs and Rates"</a> page.'),
        ("3. Cost and payment terms",
         '3.1. The cost of services is fixed in the individual agreement before work begins and is not changed unilaterally, except where the scope of work changes substantially and is separately agreed by the parties.<br><br>'
         '3.2. The full amount for the agreed service is due by the time the Cédula (CI) application is filed; details of the payment schedule are set out in the individual agreement.<br><br>'
         '3.3. Special requests from the Client (for example, finding housing or renting a car) are always possible; there is no fixed price list for them, since the effort can\'t be estimated precisely in advance, so they are billed at an hourly rate or as a package.'),
        ("4. Rights and obligations of the parties",
         '4.1. The Provider agrees to act in good faith, to inform the Client of changes in applicable Paraguayan law that affect the service being provided, and not to make timeline promises it knows to be inaccurate (see the Provider\'s position on the <a href="{riski}">"Risks & Difficulties"</a> page).<br><br>'
         '4.2. The Client agrees to provide accurate documents and information needed to render the service, and to promptly notify the Provider of changes affecting the progress of the case.'),
        ("5. Liability of the parties",
         '5.1. The Provider is not liable for decisions made by Paraguayan state authorities (including denial of residency or citizenship) where these do not result from the Provider\'s improper performance of its obligations.<br><br>'
         '5.2. Other liability terms, including the limitation and allocation of risk, are set out in the individual agreement.'),
        ("6. Confidentiality",
         '6.1. The handling of the Client\'s personal, financial, and other data in connection with the provision of services is governed by a separate <a href="{konfidentsialnost}">confidentiality agreement</a> attached to the individual agreement.'),
        ("7. Force majeure",
         '7.1. The parties are released from liability for failure to perform obligations where this is caused by force-majeure circumstances — extraordinary events the parties could neither foresee nor prevent, for example: a bank going bankrupt, a plane crash, or a tornado destroying the office. This also covers substantial changes to Paraguayan immigration law occurring after the agreement is concluded.'),
        ("8. Dispute resolution",
         '8.1. Disputes are heard in Encarnación (Paraguay), where the Provider is based. The governing law and other details of the dispute-resolution procedure are set out in the individual agreement.'),
    ],
    h2_details="9. Provider details",
    p_details='Fortuna Vida E.A.S.<br>Address: ETAPA 9009 San Isidro, 6000 Encarnación, Paraguay<br>Email: <a href="mailto:office@fortuna-vida.com.py">office@fortuna-vida.com.py</a><br>Phone: <a href="tel:+595983955504">+595 98 39 555 04</a><br>Telegram: <a href="https://t.me/grundparaguay">@grundparaguay</a>',
    p_note="The registration number (RUC) and other corporate details haven't been filled in with real data yet — the legal address and the rest of the contact details are already real (see the project's internal checklist).",
),
"de": dict(
    title="Öffentliches Angebot — Grund Paraguay",
    description="Öffentliches Angebot für Beratungsleistungen zu Umzug, Aufenthaltsrecht und Geschäftstätigkeit in Paraguay. Entwurf, erfordert rechtliche Prüfung.",
    h1="Öffentliches Angebot zur Erbringung von Beratungsleistungen",
    p_scope='Gilt für die auf der Seite <a href="{uslugi}">„Leistungen"</a> beschriebenen Dienstleistungen: Aufenthaltsrecht, laufende Begleitung und Compliance, Staatsbürgerschaft, der Investorenweg, Immobilien-Due-Diligence, Unternehmensgründung und Begleitung beim Kauf/Verkauf von Unternehmen. Es ersetzt nicht die individuelle Vereinbarung mit dem Mandanten, die Umfang und Kosten der konkreten Leistung festlegt (siehe die Seite <a href="{o-kompanii}">„Über uns"</a>).',
    sections=[
        ("1. Allgemeine Bestimmungen",
         '1.1. Dieses Dokument stellt ein öffentliches Angebot der Fortuna Vida E.A.S. (nachfolgend „Auftragnehmer") an jede geschäftsfähige natürliche oder juristische Person (nachfolgend „Mandant") dar, eine Vereinbarung über Beratungs- und Begleitleistungen im Zusammenhang mit Umzug, Aufenthaltstiteln, Staatsbürgerschaft, Geschäftstätigkeit und Immobiliengeschäften in der Republik Paraguay zu den nachstehend genannten Bedingungen abzuschließen.<br><br>'
         '1.2. Die Annahme dieses Angebots erfolgt durch Einreichen einer Anfrage über die Seite <a href="{kontakty}">„Kontakt"</a> und die anschließende Unterzeichnung einer individuellen Vereinbarung mit dem Auftragnehmer — die Anfrage allein begründet noch keine Verpflichtungen der Parteien bis zur Unterzeichnung der Vereinbarung.'),
        ("2. Gegenstand der Vereinbarung",
         '2.1. Der Auftragnehmer verpflichtet sich, dem Mandanten Leistungen in dem von den Parteien in der individuellen Vereinbarung festgelegten Umfang zu erbringen, und der Mandant verpflichtet sich, diese Leistungen zu den Bedingungen der Vereinbarung zu bezahlen.<br><br>'
         '2.2. Staatliche Gebühren, Steuern und sonstige verpflichtende Zahlungen an paraguayische Behörden sowie Leistungen externer Partner (z. B. Anwälte und Notare vor Ort) sind nicht in den Leistungsgebühren des Auftragnehmers enthalten und werden vom Mandanten separat getragen — siehe die Seite <a href="{stoimost}">„Preise und Tarife"</a>.'),
        ("3. Kosten und Zahlungsbedingungen",
         '3.1. Die Kosten der Leistungen werden vor Arbeitsbeginn in der individuellen Vereinbarung festgelegt und nicht einseitig geändert, außer bei einer wesentlichen Änderung des Leistungsumfangs, die zusätzlich zwischen den Parteien vereinbart wird.<br><br>'
         '3.2. Der volle Betrag für die vereinbarte Leistung ist bis zur Einreichung des Antrags auf die Cédula (CI) zu zahlen; Einzelheiten des Zahlungsplans werden in der individuellen Vereinbarung festgehalten.<br><br>'
         '3.3. Sonderwünsche des Mandanten (z. B. Wohnungssuche oder Mietwagen) sind jederzeit möglich; dafür gibt es keine feste Preisliste, weil sich der Aufwand vorab nicht genau abschätzen lässt — sie werden nach Stundensatz oder als Paket abgerechnet.'),
        ("4. Rechte und Pflichten der Parteien",
         '4.1. Der Auftragnehmer verpflichtet sich, nach Treu und Glauben zu handeln, den Mandanten über Änderungen des anwendbaren paraguayischen Rechts zu informieren, die die erbrachte Leistung betreffen, und keine Zeitversprechen zu machen, die er als unzutreffend kennt (siehe die Position des Auftragnehmers auf der Seite <a href="{riski}">„Risiken und Schwierigkeiten"</a>).<br><br>'
         '4.2. Der Mandant verpflichtet sich, wahrheitsgemäße Dokumente und Informationen bereitzustellen, die für die Erbringung der Leistung erforderlich sind, und den Auftragnehmer zeitnah über Änderungen zu informieren, die den Fortgang des Verfahrens betreffen.'),
        ("5. Haftung der Parteien",
         '5.1. Der Auftragnehmer haftet nicht für Entscheidungen paraguayischer Behörden (einschließlich der Ablehnung eines Aufenthaltstitels oder der Staatsbürgerschaft), sofern diese nicht auf einer mangelhaften Erfüllung seiner Pflichten beruhen.<br><br>'
         '5.2. Weitere Haftungsbedingungen, einschließlich Haftungsbeschränkung und Risikoverteilung, werden in der individuellen Vereinbarung festgelegt.'),
        ("6. Vertraulichkeit",
         '6.1. Die Verarbeitung personenbezogener, finanzieller und sonstiger Daten des Mandanten im Rahmen der Leistungserbringung unterliegt einer gesonderten <a href="{konfidentsialnost}">Vertraulichkeitsvereinbarung</a>, die der individuellen Vereinbarung beigefügt ist.'),
        ("7. Höhere Gewalt",
         '7.1. Die Parteien werden von der Haftung für die Nichterfüllung von Verpflichtungen befreit, wenn diese durch Umstände höherer Gewalt (force majeure) verursacht wird — also durch außergewöhnliche Ereignisse, die die Parteien weder vorhersehen noch abwenden konnten, zum Beispiel: die Insolvenz einer Bank, ein Flugzeugabsturz oder ein Tornado, der das Büro zerstört. Dazu zählen auch wesentliche Änderungen des paraguayischen Migrationsrechts nach Abschluss der Vereinbarung.'),
        ("8. Streitbeilegung",
         '8.1. Gerichtsstand ist Encarnación (Paraguay), der Sitz des Auftragnehmers. Das anwendbare Recht und weitere Einzelheiten der Streitbeilegung werden in der individuellen Vereinbarung festgelegt.'),
    ],
    h2_details="9. Angaben zum Auftragnehmer",
    p_details='Fortuna Vida E.A.S.<br>Adresse: ETAPA 9009 San Isidro, 6000 Encarnación, Paraguay<br>E-Mail: <a href="mailto:office@fortuna-vida.com.py">office@fortuna-vida.com.py</a><br>Telefon: <a href="tel:+595983955504">+595 98 39 555 04</a><br>Telegram: <a href="https://t.me/grundparaguay">@grundparaguay</a>',
    p_note="Registrierungsnummer (RUC) und weitere Unternehmensangaben sind noch nicht mit echten Daten ausgefüllt — Geschäftssitz und die übrigen Kontaktdaten sind bereits echt (siehe die interne Checkliste des Projekts).",
),
}

for lang in ["ru","es","en","de"]:
    t = OFERTA[lang]
    l = L(lang)
    sections_html = "".join(f'<h2>{h}</h2>\n<p>{body.format(**l)}</p>\n' for h, body in t["sections"])
    oferta_body = f'''
{breadcrumbs([(NAV_LABELS[lang]["home"], l["home"]), (NAV_LABELS[lang]["oferta"], None)])}
<section class="hero" style="padding-top:24px;padding-bottom:16px;">
  <div class="wrap"><h1>{t["h1"]}</h1></div>
</section>
<section style="padding-top:0;">
  <div class="prose">
    {DRAFT_BANNER[lang]}
    <p class="confidence-note">{t["p_scope"].format(**l)}</p>

    {sections_html}

    <h2>{t["h2_details"]}</h2>
    <p>{t["p_details"]}</p>
    <p class="confidence-note">{t["p_note"]}</p>
  </div>
</section>
'''
    page("oferta", lang, t["title"], t["description"], oferta_body,
         extra_schema=schema_breadcrumb([(NAV_LABELS[lang]["home"], f"/{lang}/"), (NAV_LABELS[lang]["oferta"], f"/{lang}/{href_to('oferta', lang)}")]),
         robots="noindex,follow")

# ================================================ ПОЛИТИКА КОНФ. САЙТА / SITE PRIVACY POLICY

POLITIKA = {
"ru": dict(
    title="Политика конфиденциальности сайта — Grund Paraguay",
    description="Как сайт grundparaguay.com обрабатывает данные посетителей: формы, куки, аналитика. Черновик, требует юридической вычитки.",
    h1="Политика конфиденциальности сайта",
    p_scope='Этот документ описывает обработку данных посетителей и пользователей самого сайта grundparaguay.com — куки, формы, аналитика. Это не то же самое, что клиентское <a href="{konfidentsialnost}">соглашение о конфиденциальности</a>, которое защищает данные иммиграционного дела уже подписавших соглашение клиентов, — оба документа нужны и решают разные задачи (см. пояснение на странице «Конфиденциальность»).',
    h2_1="1. Какие данные мы собираем",
    p_1_1='1.1. Данные, которые вы указываете сами: имя, контакт для связи (Telegram, email, телефон), текст сообщения — при заполнении формы заявки на странице <a href="{kontakty}">«Контакты»</a>.',
    p_1_2="1.2. Технические данные о посещении сайта: обезличенные данные веб-аналитики (страницы, длительность визита, источник перехода) — при условии, что аналитика подключена (см. пункт 4).",
    p_1_3="1.3. Файлы cookie — небольшие технические файлы, которые сайт может сохранять в браузере для базовой работы сайта и аналитики.",
    h2_2="2. Для чего используются данные",
    p_2_1="2.1. Данные формы заявки используются исключительно для связи с вами по поводу консультации и оказания услуг.",
    p_2_2="2.2. Данные аналитики используются для понимания того, какие страницы сайта востребованы, и для улучшения содержания сайта.",
    p_2_3="2.3. Мы не используем ваши данные для целей, не связанных с обработкой заявки или улучшением сайта, и не продаём их третьим лицам.",
    h2_3="3. Файлы cookie",
    table_head=["Тип","Назначение","Срок хранения"],
    table_rows=[
        ["Технические (обязательные)","Базовая работа сайта","Сессия"],
        ["Аналитические","Статистика посещений (если аналитика подключена)","До 12 месяцев"],
    ],
    p_3_note="Точный список и провайдер аналитики (например, Яндекс.Метрика) будет указан здесь после технического подключения аналитики — см. внутренний чек-лист проекта, блок D.",
    h2_4="4. Передача данных третьим лицам",
    p_4_1="4.1. Мы не передаём данные, собранные через сайт, третьим лицам, за исключением сервисов, технически необходимых для работы сайта (хостинг, сервис аналитики, сервис приёма формы/CRM) — и только в объёме, необходимом для их работы.",
    h2_5="5. Ваши права",
    p_5_1='5.1. Вы можете запросить удаление ваших данных, переданных через форму на сайте, написав на <a href="mailto:office@fortuna-vida.com.py">office@fortuna-vida.com.py</a> или в Telegram <a href="https://t.me/grundparaguay">@grundparaguay</a>.',
    h2_6="6. Изменения политики",
    p_6_1="6.1. Мы можем обновлять этот документ по мере развития сайта; актуальная версия всегда доступна по этому адресу.",
    h2_7="7. Контакты",
    p_7='По вопросам обработки данных сайта — <a href="mailto:office@fortuna-vida.com.py">office@fortuna-vida.com.py</a>.',
),
"es": dict(
    title="Política de privacidad del sitio — Grund Paraguay",
    description="Cómo trata el sitio grundparaguay.com los datos de sus visitantes: formularios, cookies, analítica. Borrador, requiere revisión legal.",
    h1="Política de privacidad del sitio",
    p_scope='Este documento describe el tratamiento de los datos de los visitantes y usuarios del propio sitio grundparaguay.com — cookies, formularios, analítica. No es lo mismo que el <a href="{konfidentsialnost}">acuerdo de confidencialidad</a> con el cliente, que protege los datos del trámite migratorio de los clientes que ya firmaron el acuerdo — ambos documentos son necesarios y cumplen funciones distintas (ver la explicación en la página «Confidencialidad»).',
    h2_1="1. Qué datos recopilamos",
    p_1_1='1.1. Datos que usted proporciona: nombre, medio de contacto (Telegram, email, teléfono), texto del mensaje — al completar el formulario de solicitud en la página <a href="{kontakty}">«Contacto»</a>.',
    p_1_2="1.2. Datos técnicos de la visita al sitio: datos analíticos anonimizados (páginas, duración de la visita, origen del acceso) — siempre que la analítica esté conectada (ver el punto 4).",
    p_1_3="1.3. Cookies — pequeños archivos técnicos que el sitio puede guardar en el navegador para su funcionamiento básico y para la analítica.",
    h2_2="2. Para qué se usan los datos",
    p_2_1="2.1. Los datos del formulario de solicitud se usan exclusivamente para contactarlo respecto de la consulta y la prestación de servicios.",
    p_2_2="2.2. Los datos analíticos se usan para entender qué páginas del sitio son más consultadas y para mejorar su contenido.",
    p_2_3="2.3. No usamos sus datos para fines ajenos al tratamiento de la solicitud o a la mejora del sitio, ni los vendemos a terceros.",
    h2_3="3. Cookies",
    table_head=["Tipo","Finalidad","Plazo de conservación"],
    table_rows=[
        ["Técnicas (obligatorias)","Funcionamiento básico del sitio","Sesión"],
        ["Analíticas","Estadísticas de visitas (si la analítica está conectada)","Hasta 12 meses"],
    ],
    p_3_note="La lista exacta y el proveedor de analítica (por ejemplo, Yandex.Metrica) se indicarán aquí tras la conexión técnica de la analítica — ver la lista de verificación interna del proyecto, bloque D.",
    h2_4="4. Transferencia de datos a terceros",
    p_4_1="4.1. No transferimos los datos recopilados a través del sitio a terceros, salvo a los servicios técnicamente necesarios para el funcionamiento del sitio (hosting, servicio de analítica, servicio de recepción de formularios/CRM) — y solo en la medida necesaria para su funcionamiento.",
    h2_5="5. Sus derechos",
    p_5_1='5.1. Puede solicitar la eliminación de los datos que envió a través del formulario del sitio escribiendo a <a href="mailto:office@fortuna-vida.com.py">office@fortuna-vida.com.py</a> o por Telegram a <a href="https://t.me/grundparaguay">@grundparaguay</a>.',
    h2_6="6. Cambios en la política",
    p_6_1="6.1. Podemos actualizar este documento a medida que el sitio evoluciona; la versión vigente siempre está disponible en esta misma dirección.",
    h2_7="7. Contacto",
    p_7='Para consultas sobre el tratamiento de datos del sitio: <a href="mailto:office@fortuna-vida.com.py">office@fortuna-vida.com.py</a>.',
),
"en": dict(
    title="Site Privacy Policy — Grund Paraguay",
    description="How the grundparaguay.com site handles visitor data: forms, cookies, analytics. Draft, requires legal review.",
    h1="Site Privacy Policy",
    p_scope='This document describes how data from visitors and users of the grundparaguay.com site itself is handled — cookies, forms, analytics. It is not the same as the client <a href="{konfidentsialnost}">confidentiality agreement</a>, which protects the immigration-case data of clients who have already signed an agreement — both documents are needed and serve different purposes (see the explanation on the "Confidentiality" page).',
    h2_1="1. What data we collect",
    p_1_1='1.1. Data you provide yourself: name, contact method (Telegram, email, phone), and message text — when filling out the request form on the <a href="{kontakty}">"Contact"</a> page.',
    p_1_2="1.2. Technical data about your site visit: anonymized web-analytics data (pages, visit duration, referral source) — provided analytics is enabled (see item 4).",
    p_1_3="1.3. Cookies — small technical files the site may store in your browser for basic site operation and analytics.",
    h2_2="2. What the data is used for",
    p_2_1="2.1. Request-form data is used solely to contact you about a consultation and the provision of services.",
    p_2_2="2.2. Analytics data is used to understand which pages of the site are in demand and to improve the site's content.",
    p_2_3="2.3. We do not use your data for purposes unrelated to processing your request or improving the site, and we do not sell it to third parties.",
    h2_3="3. Cookies",
    table_head=["Type","Purpose","Retention period"],
    table_rows=[
        ["Technical (required)","Basic site operation","Session"],
        ["Analytics","Visit statistics (if analytics is enabled)","Up to 12 months"],
    ],
    p_3_note="The exact list and analytics provider (e.g. Yandex.Metrica) will be specified here once analytics is technically integrated — see the project's internal checklist, Block D.",
    h2_4="4. Sharing data with third parties",
    p_4_1="4.1. We do not share data collected through the site with third parties, except for services technically necessary for the site to operate (hosting, analytics service, form-intake/CRM service) — and only to the extent needed for them to function.",
    h2_5="5. Your rights",
    p_5_1='5.1. You can request deletion of data you submitted via the site form by writing to <a href="mailto:office@fortuna-vida.com.py">office@fortuna-vida.com.py</a> or via Telegram at <a href="https://t.me/grundparaguay">@grundparaguay</a>.',
    h2_6="6. Changes to this policy",
    p_6_1="6.1. We may update this document as the site evolves; the current version is always available at this address.",
    h2_7="7. Contact",
    p_7='For questions about how the site handles data: <a href="mailto:office@fortuna-vida.com.py">office@fortuna-vida.com.py</a>.',
),
"de": dict(
    title="Datenschutzerklärung der Website — Grund Paraguay",
    description="Wie die Website grundparaguay.com Besucherdaten verarbeitet: Formulare, Cookies, Analytics. Entwurf, erfordert rechtliche Prüfung.",
    h1="Datenschutzerklärung der Website",
    p_scope='Dieses Dokument beschreibt die Verarbeitung von Daten der Besucher und Nutzer der Website grundparaguay.com selbst — Cookies, Formulare, Analytics. Es ist nicht dasselbe wie die <a href="{konfidentsialnost}">Vertraulichkeitsvereinbarung</a> mit dem Mandanten, die die Daten des Einwanderungsverfahrens von Mandanten mit bereits unterzeichneter Vereinbarung schützt — beide Dokumente sind erforderlich und erfüllen unterschiedliche Zwecke (siehe die Erläuterung auf der Seite „Vertraulichkeit").',
    h2_1="1. Welche Daten wir erheben",
    p_1_1='1.1. Von Ihnen selbst angegebene Daten: Name, Kontaktmethode (Telegram, E-Mail, Telefon), Nachrichtentext — beim Ausfüllen des Anfrageformulars auf der Seite <a href="{kontakty}">„Kontakt"</a>.',
    p_1_2="1.2. Technische Daten zu Ihrem Website-Besuch: anonymisierte Web-Analytics-Daten (Seiten, Besuchsdauer, Zugriffsquelle) — sofern Analytics aktiviert ist (siehe Punkt 4).",
    p_1_3="1.3. Cookies — kleine technische Dateien, die die Website in Ihrem Browser für den grundlegenden Betrieb der Website und für Analytics speichern kann.",
    h2_2="2. Wofür die Daten verwendet werden",
    p_2_1="2.1. Daten aus dem Anfrageformular werden ausschließlich verwendet, um Sie bezüglich einer Beratung und der Erbringung von Leistungen zu kontaktieren.",
    p_2_2="2.2. Analytics-Daten werden verwendet, um zu verstehen, welche Seiten der Website gefragt sind, und um den Inhalt der Website zu verbessern.",
    p_2_3="2.3. Wir verwenden Ihre Daten nicht für Zwecke, die nichts mit der Bearbeitung Ihrer Anfrage oder der Verbesserung der Website zu tun haben, und verkaufen sie nicht an Dritte.",
    h2_3="3. Cookies",
    table_head=["Typ","Zweck","Speicherdauer"],
    table_rows=[
        ["Technisch (erforderlich)","Grundlegender Betrieb der Website","Sitzung"],
        ["Analytics","Besuchsstatistiken (falls Analytics aktiviert ist)","Bis zu 12 Monate"],
    ],
    p_3_note="Die genaue Liste und der Analytics-Anbieter (z. B. Yandex.Metrica) werden hier nach der technischen Einbindung von Analytics angegeben — siehe die interne Checkliste des Projekts, Block D.",
    h2_4="4. Weitergabe von Daten an Dritte",
    p_4_1="4.1. Wir geben über die Website erhobene Daten nicht an Dritte weiter, ausgenommen an Dienste, die für den Betrieb der Website technisch erforderlich sind (Hosting, Analytics-Dienst, Formular-/CRM-Dienst) — und nur in dem für deren Funktion erforderlichen Umfang.",
    h2_5="5. Ihre Rechte",
    p_5_1='5.1. Sie können die Löschung der über das Website-Formular übermittelten Daten beantragen, indem Sie an <a href="mailto:office@fortuna-vida.com.py">office@fortuna-vida.com.py</a> oder per Telegram an <a href="https://t.me/grundparaguay">@grundparaguay</a> schreiben.',
    h2_6="6. Änderungen dieser Richtlinie",
    p_6_1="6.1. Wir können dieses Dokument im Zuge der Weiterentwicklung der Website aktualisieren; die jeweils aktuelle Version ist stets unter dieser Adresse verfügbar.",
    h2_7="7. Kontakt",
    p_7='Für Fragen zur Datenverarbeitung auf der Website: <a href="mailto:office@fortuna-vida.com.py">office@fortuna-vida.com.py</a>.',
),
}

for lang in ["ru","es","en","de"]:
    t = POLITIKA[lang]
    l = L(lang)
    table_rows_html = "\n".join(f'<tr><td>{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td></tr>' for r in t["table_rows"])
    privacy_site_body = f'''
{breadcrumbs([(NAV_LABELS[lang]["home"], l["home"]), (NAV_LABELS[lang]["politika"], None)])}
<section class="hero" style="padding-top:24px;padding-bottom:16px;">
  <div class="wrap"><h1>{t["h1"]}</h1></div>
</section>
<section style="padding-top:0;">
  <div class="prose">
    {DRAFT_BANNER[lang]}
    <p class="confidence-note">{t["p_scope"].format(**l)}</p>

    <h2>{t["h2_1"]}</h2>
    <p>{t["p_1_1"].format(**l)}</p>
    <p>{t["p_1_2"]}</p>
    <p>{t["p_1_3"]}</p>

    <h2>{t["h2_2"]}</h2>
    <p>{t["p_2_1"]}</p>
    <p>{t["p_2_2"]}</p>
    <p>{t["p_2_3"]}</p>

    <h2>{t["h2_3"]}</h2>
    <table>
      <thead><tr><th>{t["table_head"][0]}</th><th>{t["table_head"][1]}</th><th>{t["table_head"][2]}</th></tr></thead>
      <tbody>
        {table_rows_html}
      </tbody>
    </table>
    <p class="confidence-note">{t["p_3_note"]}</p>

    <h2>{t["h2_4"]}</h2>
    <p>{t["p_4_1"]}</p>

    <h2>{t["h2_5"]}</h2>
    <p>{t["p_5_1"]}</p>

    <h2>{t["h2_6"]}</h2>
    <p>{t["p_6_1"]}</p>

    <h2>{t["h2_7"]}</h2>
    <p>{t["p_7"]}</p>
  </div>
</section>
'''
    page("politika", lang, t["title"], t["description"], privacy_site_body,
         extra_schema=schema_breadcrumb([(NAV_LABELS[lang]["home"], f"/{lang}/"), (NAV_LABELS[lang]["politika"], f"/{lang}/{href_to('politika', lang)}")]),
         robots="noindex,follow")

# ================================================================ robots ===

robots_txt = f"""User-agent: *
Allow: /

Sitemap: {DOMAIN}/sitemap.xml
"""
with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(robots_txt)
print("wrote robots.txt")

# =============================================================== sitemap ===

INDEXABLE_PAGE_IDS = [
    ("home", "1.0"),
    ("uslugi", "0.9"),
    ("protsess", "0.8"),
    ("riski", "0.8"),
    ("stoimost", "0.9"),
    ("o-kompanii", "0.6"),
    ("keisy", "0.6"),
    ("kontakty", "0.9"),
    ("konfidentsialnost", "0.5"),
    ("terminologiya", "0.7"),
    ("kak-my-rabotaem", "0.7"),
    # Хаб «Парагвай для переезда» (11.08.2026, добавлен в мультиязычном виде на ES/EN/DE) —
    # отсутствовал в sitemap ранее (был пропущен при первом RU-only запуске раздела).
    ("paragvay-hub", "0.9"),
    ("pochemu-paragvay", "0.8"),
    ("zhizn-v-paragvae", "0.8"),
    ("stoimost-zhizni", "0.8"),
    ("nalogi-inostrantsev", "0.8"),
    ("banki-perevody", "0.8"),
    ("viza-vyezd", "0.8"),
    ("mify-voprosy", "0.8"),
    # Раздел «Документы» (12.08.2026, переведён на ES/EN/DE) — хаб + 4 страницы программ, тоже
    # отсутствовали в sitemap (были упущены при первом RU-only запуске раздела, как и paragvay-hub
    # выше).
    ("dokumenty", "0.8"),
    ("dok-temporal", "0.7"),
    ("dok-permanente", "0.7"),
    ("dok-investor", "0.7"),
    ("dok-grazhdanstvo", "0.7"),
    # «Релокация организаций» (21.08.2026, переведена на ES/EN/DE) — восьмая услуга, полная
    # страница. «Резидентура»/«Инвесторский путь» (пилот развёрнутых страниц услуг) остаются
    # RU-only и сознательно НЕ добавлены сюда — добавление RU-only id сломало бы url_block()
    # (slug(page_id, "es") и т.п. вернули бы None).
    ("usluga-relocation", "0.8"),
    # «Медицинское сопровождение» + «Медицина в Парагвае» (27.08.2026, переведены на ES/EN/DE) —
    # девятая услуга (полная страница) и новая подстраница хаба «Парагвай для переезда».
    ("usluga-medicina", "0.8"),
    ("meditsina-v-paragvae", "0.7"),
    # «Работа в Парагвае» (28.08.2026, сразу мультиязычная) — новая подстраница хаба «Парагвай
    # для переезда», тем же весом, что и meditsina-v-paragvae выше.
    ("rabota-v-paragvae", "0.7"),
    # «Карта Парагвая» (15.10.2026, сразу мультиязычная) — подстраница хаба, тем же весом.
    ("karta-paragvaya", "0.7"),
    # Оставшиеся 5 из 9 услуг (27.08.2026, сразу мультиязычные) — по запросу заказчика «у нас
    # должны быть страницы по всем услугам со страницы /uslugi.html?» → «Все 5 сразу».
    ("usluga-compliance", "0.7"),
    ("usluga-citizenship", "0.7"),
    ("usluga-realestate", "0.7"),
    ("usluga-company", "0.7"),
    ("usluga-business", "0.7"),
    # «Туризм» (21.08.2026, переведён на ES/EN/DE) — страница-анонс + 20 отдельных страниц
    # достопримечательностей. Включаем и сами 20 attr-* страниц (не только хаб) — этот раздел
    # существует именно как SEO/контент-маркетинговый актив (см. этап 3 проекта: «добавление
    # различных таблиц и аналитических статей»), поэтому им полезнее быть в sitemap.xml для
    # более быстрой индексации, а не полагаться только на обход по внутренним ссылкам с хаба.
    ("turizm", "0.7"),
    ("attr-palacio-lopez", "0.5"), ("attr-panteon-geroev", "0.5"), ("attr-sobor-asunsiona", "0.5"),
    ("attr-kostanera-asunsiona", "0.5"), ("attr-san-heronimo", "0.5"), ("attr-botanicheskiy-sad", "0.5"),
    ("attr-dom-nezavisimosti", "0.5"), ("attr-muzey-del-barro", "0.5"), ("attr-merkado-4", "0.5"),
    ("attr-aldea-maka", "0.5"), ("attr-iezuitskie-missii", "0.5"), ("attr-itaipu", "0.5"),
    ("attr-siudad-del-este", "0.5"), ("attr-saltos-del-monday", "0.5"), ("attr-kostanera-enkarnasiona", "0.5"),
    ("attr-kaakupe", "0.5"), ("attr-cerro-cora", "0.5"), ("attr-ibikui", "0.5"),
    ("attr-san-bernardino", "0.5"), ("attr-filadelfia", "0.5"),
]

def url_block(page_id, lang, prio):
    loc = f"{DOMAIN}/{lang}/{slug(page_id, lang)}"
    alt_links = "\n".join(
        f'    <xhtml:link rel="alternate" hreflang="{al}" href="{DOMAIN}/{al}/{slug(page_id, al)}"/>' for al in LANGS
    )
    alt_links += f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{DOMAIN}/{DEFAULT_LANG}/{slug(page_id, DEFAULT_LANG)}"/>'
    return f"  <url>\n    <loc>{loc}</loc>\n{alt_links}\n    <changefreq>monthly</changefreq>\n    <priority>{prio}</priority>\n  </url>"

url_entries = "\n".join(
    url_block(page_id, lang, prio)
    for page_id, prio in INDEXABLE_PAGE_IDS
    for lang in LANGS
)
# корневая страница-редирект / языковой пикер
root_entry = f"  <url>\n    <loc>{DOMAIN}/</loc>\n    <changefreq>monthly</changefreq>\n    <priority>1.0</priority>\n  </url>"

sitemap_xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
{root_entry}
{url_entries}
</urlset>
'''
with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(sitemap_xml)
print(f"wrote sitemap.xml ({len(INDEXABLE_PAGE_IDS) * len(LANGS) + 1} URLs incl. root; oferta/politika — noindex, excluded)")
