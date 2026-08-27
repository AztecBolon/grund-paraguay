#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Терминология — ru/es/en. Anchor IDs and official Spanish term names are
identical across all three languages; only definitions and group titles change."""
import re, os, glob
from build import page, breadcrumbs, schema_breadcrumb, DOMAIN, href_to, NAV_LABELS, rate_widget

def L(lang):
    return {pid: href_to(pid, lang) for pid in
            ["home","uslugi","protsess","riski","stoimost","o-kompanii","konfidentsialnost","keisy","kontakty","terminologiya",
             "viza-vyezd","dokumenty","dok-temporal","dok-permanente","dok-investor","dok-grazhdanstvo",
             "paragvay-hub","pochemu-paragvay","zhizn-v-paragvae","stoimost-zhizni","nalogi-inostrantsev",
             "banki-perevody","mify-voprosy","meditsina-v-paragvae","usluga-medicina"]}

GROUP_TITLES = {
    "migration": {"ru": "Миграция и резидентура", "es": "Migración y residencia", "en": "Migration & Residency", "de": "Migration und Aufenthalt"},
    "business": {"ru": "Инвестиции и бизнес", "es": "Inversión y negocios", "en": "Investment & Business", "de": "Investitionen und Geschäft"},
    "tax": {"ru": "Налоги и отчётность", "es": "Impuestos y declaraciones", "en": "Taxes & Filings", "de": "Steuern und Meldungen"},
    "health": {"ru": "Здоровье и безопасность", "es": "Salud y seguridad", "en": "Health & Safety", "de": "Gesundheit und Sicherheit"},
    "documents": {"ru": "Документы и процедуры", "es": "Documentos y trámites", "en": "Documents & Procedures", "de": "Dokumente und Verfahren"},
}

# Each item: (anchor, term, official_es_name, {ru,es,en definitions})
TERMS = [
    ("migration", [
        ("dnm", "DNM", "Dirección Nacional de Migraciones", {
            "ru": 'Миграционная служба Парагвая. Выдаёт резиденции, ведёт статистику, устанавливает категории заявителей и пошлины (см. резолюцию DNM N° 407/2026 на страницах <a href="{uslugi}">«Услуги»</a> и <a href="{protsess}">«Процесс и сроки»</a>).',
            "es": 'El servicio de migraciones de Paraguay. Emite residencias, lleva estadísticas y establece las categorías de solicitantes y los aranceles (ver la Resolución DNM N.° 407/2026 en las páginas <a href="{uslugi}">«Servicios»</a> y <a href="{protsess}">«Proceso y plazos»</a>).',
            "en": 'Paraguay\'s migration service. It issues residencies, keeps statistics, and sets applicant categories and fees (see DNM Resolution N° 407/2026 on the <a href="{uslugi}">"Services"</a> and <a href="{protsess}">"Process & Timeline"</a> pages).',
            "de": 'Paraguays Migrationsbehörde. Sie erteilt Aufenthaltstitel, führt Statistiken und legt Antragstellerkategorien und Gebühren fest (siehe DNM-Resolution N° 407/2026 auf den Seiten <a href="{uslugi}">„Leistungen"</a> und <a href="{protsess}">„Prozess und Fristen"</a>).',
        }),
        ("residencia-temporal", "Residencia Temporal", "temporary residency", {
            "ru": 'Оформляется по Ley N° 6984/22 «De Migraciones» (ст. 46), действует до 2 лет с возможностью продления на такой же срок, утрачивается при отсутствии в стране свыше 1 года.',
            "es": 'Se tramita según la Ley N.° 6984/22 «De Migraciones» (art. 46), es válida hasta por 2 años con posibilidad de renovarse por el mismo plazo, y se pierde si hay ausencia del país por más de 1 año.',
            "en": 'Granted under Ley N° 6984/22 "De Migraciones" (Art. 46), valid for up to 2 years with the option to renew for the same term, and forfeited if you\'re out of the country for more than 1 year.',
            "de": 'Wird gemäß Ley N° 6984/22 „De Migraciones\" (Art. 46) erteilt, gilt bis zu 2 Jahre mit der Option auf Verlängerung um denselben Zeitraum und erlischt bei einer Abwesenheit vom Land von mehr als 1 Jahr.',
        }),
        ("residencia-permanente", "Residencia Permanente", "permanent residency", {
            "ru": 'Выдаётся на 10 лет с возможностью продления, утрачивается при отсутствии в стране свыше 3 лет подряд. Обычным путём доступна после полных 2 лет Residencia Temporal; для инвесторов — напрямую, без Temporal (см. SUACE ниже).',
            "es": 'Se otorga por 10 años con posibilidad de renovación, y se pierde si hay ausencia del país por más de 3 años seguidos. Por la vía estándar se accede tras 2 años completos de Residencia Temporal; para inversores, de forma directa, sin pasar por la Temporal (ver SUACE más abajo).',
            "en": 'Granted for 10 years with the option to renew, and forfeited after more than 3 consecutive years outside the country. Via the standard route it becomes available after a full 2 years on Residencia Temporal; for investors, directly, without going through the Temporal (see SUACE below).',
            "de": 'Wird für 10 Jahre mit Verlängerungsoption erteilt und erlischt nach mehr als 3 aufeinanderfolgenden Jahren außerhalb des Landes. Über den Standardweg wird sie nach vollen 2 Jahren Residencia Temporal verfügbar; für Investoren direkt, ohne den Weg über die Temporal (siehe SUACE unten).',
        }),
        ("cedula", "Cédula", "local identity document", {
            "ru": 'Выдаётся уже на этапе временной резиденции; её номер используется как номер RUC (см. ниже), а сама Cédula часто требуется банками для открытия счёта.',
            "es": 'Se emite ya en la etapa de residencia temporal; su número se usa como número de RUC (ver más abajo), y los bancos suelen exigir la propia Cédula para abrir una cuenta.',
            "en": 'Issued already at the temporary-residency stage; its number is used as the RUC number (see below), and banks often require the Cédula itself to open an account.',
            "de": 'Wird bereits in der Phase des befristeten Aufenthalts ausgestellt; ihre Nummer wird als RUC-Nummer verwendet (siehe unten), und Banken verlangen für die Kontoeröffnung oft die Cédula selbst.',
        }),
        ("corte-suprema", "Corte Suprema de Justicia", "Paraguay's Supreme Court", {
            "ru": 'Именно он, а не миграционная служба, ведёт дела о натурализации (гражданстве) — процедура требует личной явки заявителя и сопровождения адвоката.',
            "es": 'Es la Corte, y no el servicio de migraciones, la que tramita los expedientes de naturalización (ciudadanía) — el procedimiento exige la comparecencia personal del solicitante y el acompañamiento de un abogado.',
            "en": 'It is the Supreme Court, not the migration service, that handles naturalization (citizenship) cases — the procedure requires the applicant\'s personal appearance and support from a lawyer.',
            "de": 'Nicht die Migrationsbehörde, sondern der Oberste Gerichtshof führt Einbürgerungsverfahren (Staatsbürgerschaft) — das Verfahren erfordert das persönliche Erscheinen des Antragstellers und anwaltliche Begleitung.',
        }),
    ]),
    ("business", [
        ("mic", "MIC", "Ministerio de Industria y Comercio", {
            "ru": 'Министерство промышленности и торговли Парагвая. Издаёт резолюции по инвесторскому пути (Resolución MIC N° 0283/2026) и администрирует портал EAS.',
            "es": 'El Ministerio de Industria y Comercio de Paraguay. Emite resoluciones sobre la vía de inversor (Resolución MIC N.° 0283/2026) y administra el portal EAS.',
            "en": 'Paraguay\'s Ministry of Industry and Commerce. It issues resolutions on the investor route (Resolución MIC N° 0283/2026) and administers the EAS portal.',
            "de": 'Paraguays Ministerium für Industrie und Handel. Es erlässt Resolutionen zum Investorenweg (Resolución MIC N° 0283/2026) und verwaltet das EAS-Portal.',
        }),
        ("rediex", "REDIEX", "Red de Inversiones y Exportaciones", {
            "ru": 'Государственное агентство по инвестициям и экспорту при Министерстве промышленности и торговли. Администрирует льготный налоговый режим Maquila (см. ниже) и портал электронной регистрации VUE.',
            "es": 'La agencia estatal de inversiones y exportaciones dependiente del Ministerio de Industria y Comercio. Administra el régimen fiscal preferencial Maquila (ver más abajo) y la plataforma electrónica VUE.',
            "en": 'Paraguay\'s state investment and export promotion agency under the Ministry of Industry and Commerce. It administers the preferential Maquila tax regime (see below) and the VUE electronic registration platform.',
            "de": 'Die staatliche Investitions- und Exportförderagentur unter dem Ministerium für Industrie und Handel. Sie verwaltet das steuerliche Vorzugsregime Maquila (siehe unten) und die elektronische Registrierungsplattform VUE.',
        }),
        ("suace", "SUACE", "Sistema Unificado de Apertura y Cierre de Empresas", {
            "ru": 'Единая система открытия и закрытия предприятий. Через неё проходит регистрация компаний (EAS, S.A., S.R.L.) и инвесторский путь к резиденции.',
            "es": 'El sistema unificado de apertura y cierre de empresas. A través de él se realiza el registro de compañías (EAS, S.A., S.R.L.) y la vía de inversor hacia la residencia.',
            "en": 'The unified system for opening and closing companies. Company registration (EAS, S.A., S.R.L.) and the investor route to residency both run through it.',
            "de": 'Das einheitliche System zur Eröffnung und Schließung von Unternehmen. Die Unternehmensregistrierung (EAS, S.A., S.R.L.) und der Investorenweg zum Aufenthaltstitel laufen beide darüber.',
        }),
        ("cie", "CIE", "certificado de inversor", {
            "ru": 'Оформляется в рамках инвесторского пути через SUACE. По официальным данным — за 5 рабочих дней с момента подачи полного пакета документов.',
            "es": 'Se tramita dentro de la vía de inversor a través de SUACE. Según datos oficiales, en 5 días hábiles desde la presentación del paquete completo de documentos.',
            "en": 'Issued as part of the investor route through SUACE. Per official figures, within 5 business days of submitting the complete document package.',
            "de": 'Wird im Rahmen des Investorenwegs über SUACE ausgestellt. Laut offiziellen Angaben innerhalb von 5 Werktagen nach Einreichung des vollständigen Dokumentenpakets.',
        }),
        ("eas", "EAS", "Empresa por Acciones Simplificada", {
            "ru": 'Упрощённое акционерное общество. Самая быстрая форма регистрации компании в Парагвае (официально — до 72 рабочих часов).',
            "es": 'Empresa por acciones simplificada. La forma más rápida de registrar una empresa en Paraguay (oficialmente, hasta 72 horas hábiles).',
            "en": 'A simplified joint-stock company. The fastest way to register a company in Paraguay (officially, up to 72 business hours).',
            "de": 'Eine vereinfachte Aktiengesellschaft. Die schnellste Form der Unternehmensregistrierung in Paraguay (offiziell bis zu 72 Werkstunden).',
        }),
        ("sa", "S.A.", "Sociedad Anónima", {
            "ru": 'Акционерное общество. Регистрация занимает 8–30 рабочих дней, требует нотариального акта и публикации в СМИ.',
            "es": 'Sociedad anónima. El registro toma de 8 a 30 días hábiles, requiere acta notarial y publicación en medios.',
            "en": 'A joint-stock company. Registration takes 8–30 business days and requires a notarial deed and press publication.',
            "de": 'Eine Aktiengesellschaft. Die Registrierung dauert 8–30 Werktage und erfordert eine notarielle Urkunde sowie eine Presseveröffentlichung.',
        }),
        ("srl", "S.R.L.", "Sociedad de Responsabilidad Limitada", {
            "ru": 'Общество с ограниченной ответственностью. Регистрация занимает 15–30 рабочих дней.',
            "es": 'Sociedad de responsabilidad limitada. El registro toma de 15 a 30 días hábiles.',
            "en": 'A limited-liability company. Registration takes 15–30 business days.',
            "de": 'Eine Gesellschaft mit beschränkter Haftung. Die Registrierung dauert 15–30 Werktage.',
        }),
        ("maquila", "Régimen de Maquila", "export manufacturing/services regime", {
            "ru": 'Льготный налоговый режим (Ley N° 1064/97): единый налог 1% — от добавленной стоимости или от суммы счёта-фактуры, смотря что больше, — вместо стандартных 10% IRE. Доступен юрлицам, работающим по контракту с иностранной компанией, включая экспортёров услуг, не только производство.',
            "es": 'Un régimen fiscal preferencial (Ley N.° 1064/97): impuesto único del 1% — sobre el valor agregado o sobre el monto de la factura, lo que sea mayor — en lugar del 10% estándar de IRE. Disponible para personas jurídicas que trabajan bajo contrato con una empresa extranjera, incluidos los exportadores de servicios, no solo la manufactura.',
            "en": 'A preferential tax regime (Ley N° 1064/97): a single 1% tax — on value added or on the invoice amount, whichever is greater — instead of the standard 10% IRE. Available to legal entities working under contract with a foreign company, including service exporters, not just manufacturing.',
            "de": 'Ein steuerliches Vorzugsregime (Ley N° 1064/97): eine einheitliche Steuer von 1% — auf die Wertschöpfung oder den Rechnungsbetrag, je nachdem, was höher ist — anstelle der regulären 10% IRE. Verfügbar für juristische Personen, die im Auftrag eines ausländischen Unternehmens arbeiten, einschließlich Dienstleistungsexporteuren, nicht nur für die Fertigung.',
        }),
        ("indert", "INDERT", "Instituto Nacional de Desarrollo Rural y de la Tierra", {
            "ru": 'Национальный институт развития сельских территорий и земли. Ведает землями аграрной реформы — их статус («lote agrario») важен при проверке (due diligence) любой сделки с недвижимостью, независимо от гражданства покупателя.',
            "es": 'El Instituto Nacional de Desarrollo Rural y de la Tierra. Administra las tierras de la reforma agraria — su estatus («lote agrario») es relevante en el due diligence de cualquier operación inmobiliaria, sin importar la nacionalidad del comprador.',
            "en": 'The National Institute for Rural and Land Development. It administers agrarian-reform land — its status ("lote agrario") matters for due diligence on any real-estate deal, regardless of the buyer\'s nationality.',
            "de": 'Das nationale Institut für ländliche und Landentwicklung. Es verwaltet Agrarreformland — dessen Status („lote agrario\") ist für die Due Diligence bei jeder Immobilientransaktion relevant, unabhängig von der Staatsangehörigkeit des Käufers.',
        }),
        ("escribano", "escribano", "independent notary", {
            "ru": 'Через него оформляются сделки с недвижимостью и учредительные документы компаний в Парагвае.',
            "es": 'A través de él se formalizan las operaciones inmobiliarias y los documentos constitutivos de empresas en Paraguay.',
            "en": 'Real-estate deals and company formation documents in Paraguay are formalized through this independent notary.',
            "de": 'Immobiliengeschäfte und Gründungsdokumente von Unternehmen in Paraguay werden über diesen unabhängigen Notar formalisiert.',
        }),
    ]),
    ("tax", [
        ("ruc", "RUC", "Registro Único de Contribuyentes", {
            "ru": 'Единый номер налогоплательщика. Регистрируется после получения резиденции, номер совпадает с номером Cédula.',
            "es": 'El número único de contribuyente. Se inscribe tras obtener la residencia, y el número coincide con el de la Cédula.',
            "en": 'A single taxpayer ID number. Registered after obtaining residency; the number matches the Cédula number.',
            "de": 'Eine einheitliche Steuernummer. Wird nach Erhalt des Aufenthaltstitels registriert; die Nummer stimmt mit der Cédula-Nummer überein.',
        }),
        ("iva", "IVA", "Impuesto al Valor Agregado", {
            "ru": 'Аналог НДС. Ставки — 10% (общая) и 5% (льготная); декларация подаётся через Formulario 120.',
            "es": 'El equivalente al IVA. Tasas del 10% (general) y 5% (reducida); la declaración se presenta mediante el Formulario 120.',
            "en": 'Paraguay\'s VAT. Rates are 10% (general) and 5% (reduced); filed via Formulario 120.',
            "de": 'Paraguays Mehrwertsteuer. Sätze von 10% (allgemein) und 5% (ermäßigt); Meldung über das Formulario 120.',
        }),
        ("ire", "IRE / IRE RESIMPLE", "Impuesto a la Renta Empresarial", {
            "ru": 'Налог на прибыль предприятий. RESIMPLE — упрощённый режим для микробизнеса с годовым оборотом до ₲ 80 млн: фиксированные квартальные платежи от ₲ 60 000 до ₲ 240 000.',
            "es": 'El impuesto a la renta empresarial. RESIMPLE es el régimen simplificado para microempresas con facturación anual de hasta ₲ 80 millones: pagos trimestrales fijos de ₲ 60.000 a ₲ 240.000.',
            "en": 'Corporate income tax. RESIMPLE is the simplified regime for microbusinesses with annual turnover up to ₲80 million: fixed quarterly payments of ₲60,000 to ₲240,000.',
            "de": 'Körperschaftsteuer. RESIMPLE ist das vereinfachte Regime für Kleinunternehmen mit einem Jahresumsatz bis ₲80 Mio.: feste Quartalszahlungen von ₲60.000 bis ₲240.000.',
        }),
        ("irp", "IRP", "Impuesto a la Renta Personal", {
            "ru": 'Налог на доходы физических лиц. Ставки 8–10% при доходе от личных услуг от ₲ 80 млн в год.',
            "es": 'El impuesto a la renta de las personas físicas. Tasas del 8 al 10% con ingresos por servicios personales desde ₲ 80 millones anuales.',
            "en": 'Personal income tax. Rates of 8–10% on income from personal services above ₲80 million a year.',
            "de": 'Einkommensteuer für natürliche Personen. Sätze von 8–10% bei Einkommen aus persönlichen Dienstleistungen ab ₲80 Mio. jährlich.',
        }),
        ("formulario-120", "Formulario 120", "IVA tax return form", {
            "ru": 'Точная периодичность подачи по общему (не RESIMPLE) режиму уточняется индивидуально — источники расходятся, актуальную норму мы подтверждаем перед началом работы по абонементу сопровождения.',
            "es": 'La periodicidad exacta de presentación en el régimen general (no RESIMPLE) se confirma de forma individual — las fuentes difieren, y confirmamos la norma vigente antes de iniciar el trabajo bajo el abono de acompañamiento.',
            "en": 'The exact filing frequency under the general (non-RESIMPLE) regime is confirmed individually — sources vary, and we confirm the current rule before starting work under the support subscription.',
            "de": 'Die genaue Meldehäufigkeit im allgemeinen (Nicht-RESIMPLE-)Regime wird individuell geklärt — die Quellen weichen voneinander ab, und wir bestätigen die aktuelle Regel vor Beginn der Arbeit im Rahmen des Begleitabonnements.',
        }),
        ("marangatu", "Marangatú", "electronic tax filing system", {
            "ru": 'Система налогового органа Парагвая (DNIT — преемника прежней SET). Для режима RESIMPLE автоматически формирует нулевую декларацию, если отчёт не подан в срок.',
            "es": 'El sistema de la autoridad tributaria de Paraguay (DNIT, sucesora de la antigua SET). Para el régimen RESIMPLE, genera automáticamente una declaración en cero si no se presenta el informe a tiempo.',
            "en": 'The system run by Paraguay\'s tax authority (DNIT, successor to the former SET). For the RESIMPLE regime, it auto-generates a zero return if a filing isn\'t submitted on time.',
            "de": 'Das System der paraguayischen Steuerbehörde (DNIT, Nachfolgerin der früheren SET). Für das RESIMPLE-Regime erstellt es automatisch eine Nullmeldung, falls keine Meldung fristgerecht eingereicht wird.',
        }),
    ]),
    ("health", [
        ("ips", "IPS", "state health insurance", {
            "ru": 'Доступ к нему связан с формальной занятостью, а не просто со статусом резидента: взнос — 25,5% от зарплаты (9% работник / 16,5% работодатель), нужны cédula и регистрация работодателя. Это не то же самое, что публичные больницы MSPBS, доступные шире, — подробнее на странице <a href="{meditsina-v-paragvae}">«Медицина в Парагвае»</a>.',
            "es": 'El acceso está vinculado al empleo formal y al estatus de residente permanente; los residentes temporales no tienen acceso automático.',
            "en": 'Access is tied to formal employment and permanent-resident status; temporary residents don\'t get automatic access.',
            "de": 'Der Zugang ist an formale Beschäftigung und den Status als unbefristeter Resident gebunden; befristete Residenten erhalten keinen automatischen Zugang.',
        }),
        ("carencias", "carencias", "waiting periods before coverage starts", {
            "ru": 'Сроки ожидания перед тем, как страховой полис начинает покрывать конкретное состояние. У Asismed, одного из крупных локальных страховщиков, — 6 месяцев для задекларированных хронических заболеваний и минимум 12 месяцев для онкологии, болезней почек и печени; незадекларированные состояния не покрываются вовсе. Подробнее на странице <a href="{meditsina-v-paragvae}">«Медицина в Парагвае»</a> и в описании услуги <a href="{usluga-medicina}">«Медицинское сопровождение»</a>.',
            "es": 'Los períodos de espera antes de que una póliza empiece a cubrir una condición concreta. En Asismed, una de las principales aseguradoras locales, son 6 meses para enfermedades crónicas declaradas y un mínimo de 12 meses para cáncer y enfermedades renales o hepáticas; las condiciones no declaradas no se cubren en absoluto. Más información en la página <a href="{meditsina-v-paragvae}">«Medicina en Paraguay»</a> y en el servicio <a href="{usluga-medicina}">«Asistencia médica»</a>.',
            "en": 'The waiting periods before a policy starts covering a specific condition. At Asismed, one of the larger local insurers, it\'s 6 months for declared chronic conditions and at least 12 months for cancer, kidney, and liver disease; undeclared conditions aren\'t covered at all. More on the <a href="{meditsina-v-paragvae}">"Healthcare in Paraguay"</a> page and in the <a href="{usluga-medicina}">"Medical Support"</a> service.',
            "de": 'Die Wartezeiten, bevor eine Police eine bestimmte Erkrankung abzudecken beginnt. Bei Asismed, einem der größeren lokalen Versicherer, sind es 6 Monate für angegebene chronische Erkrankungen und mindestens 12 Monate für Krebs-, Nieren- und Lebererkrankungen; nicht angegebene Erkrankungen werden gar nicht gedeckt. Mehr auf der Seite <a href="{meditsina-v-paragvae}">„Medizin in Paraguay"</a> und bei der Leistung <a href="{usluga-medicina}">„Medizinische Begleitung"</a>.',
        }),
        ("medicina-prepaga", "medicina prepaga", "prepaid medical plan (Spanish-market term)", {
            "ru": 'Термин испаноязычного рынка для предоплаченного медицинского плана — примерный аналог полиса ДМС, но с иной структурой оплаты (регулярный взнос за доступ к сети клиник, а не возмещение по чекам). В Парагвае так называют планы локальных страховщиков вроде MAPFRE или Asismed — см. страницу <a href="{meditsina-v-paragvae}">«Медицина в Парагвае»</a>.',
            "es": 'El término del mercado hispanohablante para un plan médico prepagado — un cuota periódica que da acceso a una red de clínicas, en vez de un reembolso por comprobantes. En Paraguay así se llaman los planes de aseguradoras locales como MAPFRE o Asismed — ver la página <a href="{meditsina-v-paragvae}">«Medicina en Paraguay»</a>.',
            "en": 'The Spanish-speaking market\'s term for a prepaid medical plan — a recurring fee for access to a clinic network, rather than reimbursement against receipts. In Paraguay it refers to plans from local insurers like MAPFRE or Asismed — see the <a href="{meditsina-v-paragvae}">"Healthcare in Paraguay"</a> page.',
            "de": 'Der Begriff des spanischsprachigen Markts für einen vorausbezahlten Krankenversicherungsplan — ein wiederkehrender Beitrag für den Zugang zu einem Kliniknetz statt Erstattung gegen Belege. In Paraguay bezeichnet er Pläne lokaler Versicherer wie MAPFRE oder Asismed — siehe die Seite <a href="{meditsina-v-paragvae}">„Medizin in Paraguay"</a>.',
        }),
        ("declaracion-jurada-salud", "Declaración Jurada de Salud", "mandatory sworn health declaration", {
            "ru": 'Обязательная декларация о состоянии здоровья, которую нужно заполнить при оформлении полиса у локального страховщика (например, Asismed). Именно от того, что в ней задекларировано, зависят сроки ожидания («<a href="{terminologiya}#carencias">carencias</a>») и объём покрытия — см. страницу <a href="{meditsina-v-paragvae}">«Медицина в Парагвае»</a>.',
            "es": 'La declaración jurada de salud obligatoria que hay que completar al contratar una póliza con una aseguradora local (por ejemplo, Asismed). Lo que se declara en ella determina los períodos de carencia y el alcance de la cobertura — ver la página <a href="{meditsina-v-paragvae}">«Medicina en Paraguay»</a>.',
            "en": 'The mandatory sworn health declaration you fill out when signing up for a policy with a local insurer (e.g. Asismed). What\'s declared in it determines the waiting periods and the scope of coverage — see the <a href="{meditsina-v-paragvae}">"Healthcare in Paraguay"</a> page.',
            "de": 'Die verpflichtende eidesstattliche Gesundheitserklärung, die beim Abschluss einer Police bei einem lokalen Versicherer (z. B. Asismed) auszufüllen ist. Was darin angegeben wird, bestimmt die Wartezeiten und den Deckungsumfang — siehe die Seite <a href="{meditsina-v-paragvae}">„Medizin in Paraguay"</a>.',
        }),
        ("paho", "PAHO", "Pan American Health Organization", {
            "ru": 'Панамериканская организация здравоохранения, региональное отделение ВОЗ. Источник статистики по денге, которую мы приводим на странице <a href="{riski}">«Риски и трудности»</a>.',
            "es": 'La Organización Panamericana de la Salud, oficina regional de la OMS. Fuente de las estadísticas de dengue que citamos en la página <a href="{riski}">«Riesgos y dificultades»</a>.',
            "en": 'The Pan American Health Organization, WHO\'s regional office. The source of the dengue statistics we cite on the <a href="{riski}">"Risks & Difficulties"</a> page.',
            "de": 'Die Panamerikanische Gesundheitsorganisation, das WHO-Regionalbüro. Die Quelle der Dengue-Statistiken, die wir auf der Seite <a href="{riski}">„Risiken und Schwierigkeiten"</a> anführen.',
        }),
        ("osac", "OSAC", "Overseas Security Advisory Council", {
            "ru": 'Структура Госдепартамента США по безопасности зарубежных представительств. Публикует оценки уровня угрозы для иностранцев по странам, включая Парагвай.',
            "es": 'El organismo del Departamento de Estado de EE. UU. para la seguridad de las representaciones en el exterior. Publica evaluaciones del nivel de amenaza para extranjeros por país, incluido Paraguay.',
            "en": 'A U.S. State Department body for the security of overseas missions. It publishes threat-level assessments for foreigners by country, including Paraguay.',
            "de": 'Eine Stelle des US-Außenministeriums für die Sicherheit von Auslandsvertretungen. Sie veröffentlicht Bedrohungseinschätzungen für Ausländer nach Ländern, einschließlich Paraguay.',
        }),
    ]),
    # Группа «Документы и процедуры» — добавлена 12.08.2026 вместе с разделом «Документы по
    # программам» (design/dokumenty-po-programmam-migratsii.md), 12.08.2026 вечер переведена на
    # ES/EN/DE вместе с самим разделом (запрос заказчика «делай мультиязычность по документам»).
    # es_name (третье поле) — как и у остальных групп TERMS, это фиксированная короткая подпись,
    # одинаковая на всех языках страницы (не переводится), либо None, если термин уже на русском/
    # переведённом языке и подпись не нужна (см. "apostil" — сам термин переводится, "Apostilla"/
    # "Apostille"/"Apostille", а не только подпись).
    ("documents", [
        ("apostil", {"ru": "Апостиль", "es": "Apostilla", "en": "Apostille", "de": "Apostille"}, None, {
            "ru": 'Упрощённое международное заверение официального документа для использования за границей — заменяет консульскую легализацию для стран-участниц Гаагской конвенции 1961 года (Россия — с 1992 года, Парагвай — с 2014-го). Справка о несудимости и другие документы для резидентуры заверяются апостилем в стране выдачи — подробнее на странице <a href="{viza-vyezd}">«Виза, документы и въезд»</a> и в разделе <a href="{dokumenty}">«Документы по программам»</a>.',
            "es": 'La certificación internacional simplificada de un documento oficial para su uso en el extranjero — sustituye la legalización consular para los países parte del Convenio de La Haya de 1961 (Rusia desde 1992, Paraguay desde 2014). El certificado de antecedentes penales y otros documentos para la residencia se apostillan en el país de emisión — más detalles en la página <a href="{viza-vyezd}">«Visa, documentos y entrada»</a> y en la sección <a href="{dokumenty}">«Documentos por programa»</a>.',
            "en": 'A simplified international certification of an official document for use abroad — it replaces consular legalization for countries party to the 1961 Hague Convention (Russia since 1992, Paraguay since 2014). Criminal record certificates and other residency documents are apostilled in the country that issued them — more on the <a href="{viza-vyezd}">"Visa, Documents, and Entry"</a> page and in the <a href="{dokumenty}">"Documents by Program"</a> section.',
            "de": 'Die vereinfachte internationale Beglaubigung eines amtlichen Dokuments zur Verwendung im Ausland — sie ersetzt die konsularische Legalisation für die Vertragsstaaten des Haager Übereinkommens von 1961 (Russland seit 1992, Paraguay seit 2014). Führungszeugnisse und andere Dokumente für den Aufenthaltstitel werden im Ausstellungsland mit einer Apostille versehen — mehr auf der Seite <a href="{viza-vyezd}">„Visum, Dokumente und Einreise"</a> und im Bereich <a href="{dokumenty}">„Dokumente nach Programm"</a>.',
        }),
        ("traductor-publico", {"ru": "Traductor Público matriculado", "es": "Traductor Público matriculado", "en": "Traductor Público matriculado", "de": "Traductor Público matriculado"}, "sworn/certified translator registered in Paraguay", {
            "ru": 'Присяжный переводчик, зарегистрированный в Парагвае, — не любой переводчик, а специалист с местной регистрацией. Апостилированные документы не на испанском языке принимаются миграционной службой и судом только в переводе такого переводчика.',
            "es": 'Un traductor jurado registrado en Paraguay — no cualquier traductor, sino un especialista con matrícula local. Los documentos apostillados que no están en español son aceptados por el servicio de migraciones y por la justicia solo si vienen traducidos por un traductor de este tipo.',
            "en": 'A sworn translator registered in Paraguay — not just any translator, but a specialist with local registration. Apostilled documents not in Spanish are accepted by the migration service and the courts only if translated by this kind of translator.',
            "de": 'Ein in Paraguay registrierter vereidigter Übersetzer — nicht irgendein Übersetzer, sondern ein Fachmann mit lokaler Zulassung. Apostillierte Dokumente, die nicht auf Spanisch sind, werden von der Migrationsbehörde und den Gerichten nur akzeptiert, wenn sie von einem solchen Übersetzer übersetzt wurden.',
        }),
        ("mec", {"ru": "MEC", "es": "MEC", "en": "MEC", "de": "MEC"}, "Ministerio de Educación y Ciencias", {
            "ru": 'Министерство образования и науки Парагвая. По системе из 12 категорий заявителей на постоянную резиденцию (см. <a href="{terminologiya}#dnm">DNM</a> и <a href="{dok-permanente}">«Постоянная резидентура»</a>) диплом или квалификация, поданные как подтверждение платёжеспособности по категориям «профессионал» и «техник», должны быть зарегистрированы именно в MEC.',
            "es": 'El Ministerio de Educación y Ciencias de Paraguay. Según el sistema de 12 categorías de solicitantes de residencia permanente (ver <a href="{terminologiya}#dnm">DNM</a> y <a href="{dok-permanente}">«Residencia permanente»</a>), el título o la cualificación presentados como acreditación de solvencia en las categorías «profesional» y «técnico» deben estar registrados precisamente en el MEC.',
            "en": 'Paraguay\'s Ministry of Education and Science. Under the system of 12 permanent-residency applicant categories (see <a href="{terminologiya}#dnm">DNM</a> and <a href="{dok-permanente}">"Permanent Residency"</a>), a degree or qualification submitted as proof of solvency under the "professional" and "technician" categories must be registered specifically with MEC.',
            "de": 'Paraguays Ministerium für Bildung und Wissenschaft. Nach dem System der 12 Antragstellerkategorien für den Daueraufenthalt (siehe <a href="{terminologiya}#dnm">DNM</a> und <a href="{dok-permanente}">„Daueraufenthalt"</a>) muss ein Abschluss oder eine Qualifikation, die als Nachweis der Zahlungsfähigkeit in den Kategorien „Fachkraft" und „Techniker" eingereicht wird, genau beim MEC registriert sein.',
        }),
        ("resolucion-407", {"ru": "Resolución DNM N° 407/2026", "es": "Resolución DNM N° 407/2026", "en": "Resolución DNM N° 407/2026", "de": "Resolución DNM N° 407/2026"}, None, {
            "ru": 'Резолюция миграционной службы (DNM), действующая для дел, поданных с 6 июля 2026 года, — вводит единую систему из 12 категорий заявителей на постоянную резиденцию с отдельными требованиями к документам по каждой (наёмный работник, самозанятый, пенсионер, иждивенец и другие). Полная таблица категорий и документов — на странице <a href="{dok-permanente}">«Постоянная резидентура: документы»</a>.',
            "es": 'La resolución del servicio de migraciones (DNM), vigente para expedientes presentados desde el 6 de julio de 2026 — introduce un sistema único de 12 categorías de solicitantes de residencia permanente, con requisitos de documentos propios para cada una (trabajador en relación de dependencia, autónomo, jubilado, dependiente y otras). La tabla completa de categorías y documentos está en la página <a href="{dok-permanente}">«Residencia permanente: documentos»</a>.',
            "en": 'The migration service (DNM) resolution in effect for cases filed since July 6, 2026 — it introduces a single system of 12 permanent-residency applicant categories, each with its own document requirements (employee, self-employed, retiree, dependent, and others). The full table of categories and documents is on the <a href="{dok-permanente}">"Permanent Residency: Documents"</a> page.',
            "de": 'Die Resolution der Migrationsbehörde (DNM), gültig für Verfahren, die seit dem 6. Juli 2026 eingereicht wurden — sie führt ein einheitliches System aus 12 Antragstellerkategorien für den Daueraufenthalt mit jeweils eigenen Dokumentenanforderungen ein (Angestellter, Selbstständiger, Rentner, Angehöriger und weitere). Die vollständige Tabelle der Kategorien und Dokumente steht auf der Seite <a href="{dok-permanente}">„Daueraufenthalt: Dokumente"</a>.',
        }),
        ("carta-naturalizacion", {"ru": "Carta de Naturalización", "es": "Carta de Naturalización", "en": "Carta de Naturalización", "de": "Carta de Naturalización"}, None, {
            "ru": 'Официальный документ, которым Верховный суд Парагвая (<a href="{terminologiya}#corte-suprema">Corte Suprema de Justicia</a>) удостоверяет предоставление парагвайского гражданства иностранцу. Не путать с резиденцией — оформляется отдельно, не миграционной службой. Список документов — на странице <a href="{dok-grazhdanstvo}">«Гражданство: документы»</a>.',
            "es": 'El documento oficial con el que la Corte Suprema de Justicia de Paraguay certifica la concesión de la ciudadanía paraguaya a un extranjero. No debe confundirse con la residencia — se tramita por separado, no ante el servicio de migraciones. La lista de documentos está en la página <a href="{dok-grazhdanstvo}">«Ciudadanía: documentos»</a>.',
            "en": 'The official document by which Paraguay\'s Supreme Court (<a href="{terminologiya}#corte-suprema">Corte Suprema de Justicia</a>) certifies that a foreigner has been granted Paraguayan citizenship. Not to be confused with residency — it\'s processed separately, not by the migration service. The document list is on the <a href="{dok-grazhdanstvo}">"Citizenship: Documents"</a> page.',
            "de": 'Das offizielle Dokument, mit dem der Oberste Gerichtshof Paraguays (<a href="{terminologiya}#corte-suprema">Corte Suprema de Justicia</a>) die Verleihung der paraguayischen Staatsbürgerschaft an einen Ausländer bestätigt. Nicht zu verwechseln mit dem Aufenthaltstitel — wird separat bearbeitet, nicht von der Migrationsbehörde. Die Dokumentenliste steht auf der Seite <a href="{dok-grazhdanstvo}">„Staatsbürgerschaft: Dokumente"</a>.',
        }),
        ("investor-pass", {"ru": "Investor Pass", "es": "Investor Pass", "en": "Investor Pass", "de": "Investor Pass"}, None, {
            "ru": 'Название инвесторского пути к постоянной резиденции без прохождения временной — режим действует по Resolución MIC N° 0283/2026, администрируется через <a href="{terminologiya}#suace">SUACE</a>, официальный сертификат инвестора называется <a href="{terminologiya}#cie">CIE</a>. Список документов на сертификат — на странице <a href="{dok-investor}">«Инвесторский путь: документы»</a>.',
            "es": 'El nombre de la vía de inversor hacia la residencia permanente sin pasar por la temporal — el régimen funciona según la Resolución MIC N.° 0283/2026, se administra a través de <a href="{terminologiya}#suace">SUACE</a>, y el certificado oficial de inversor se llama <a href="{terminologiya}#cie">CIE</a>. La lista de documentos para el certificado está en la página <a href="{dok-investor}">«Vía de inversor: documentos»</a>.',
            "en": 'The name of the investor route to permanent residency without going through the temporary stage — the scheme runs under Resolución MIC N° 0283/2026, is administered through <a href="{terminologiya}#suace">SUACE</a>, and the official investor certificate is called <a href="{terminologiya}#cie">CIE</a>. The document list for the certificate is on the <a href="{dok-investor}">"Investor Route: Documents"</a> page.',
            "de": 'Die Bezeichnung für den Investorenweg zum Daueraufenthalt ohne befristete Phase — die Regelung gilt gemäß der Resolución MIC N° 0283/2026, wird über <a href="{terminologiya}#suace">SUACE</a> verwaltet, und das offizielle Investorenzertifikat heißt <a href="{terminologiya}#cie">CIE</a>. Die Dokumentenliste für das Zertifikat steht auf der Seite <a href="{dok-investor}">„Investorenweg: Dokumente"</a>.',
        }),
    ]),
]

PAGE_TEXT = {
"ru": dict(
    title="Терминология и курс валюты: глоссарий терминов Парагвая | Grund Paraguay",
    description="Расшифровка испанских и юридических терминов сайта — DNM, RUC, Cédula, SUACE, IVA и другие — и актуальный курс парагвайского гуарани к доллару и рублю.",
    h1="Терминология: испанские термины и курс гуарани",
    lead="Здесь собраны все испанские и юридические термины, которые встречаются на сайте, — с расшифровкой на русском. Если вы попали на эту страницу по ссылке с другой страницы сайта, при возврате термин будет понятен без повторного перехода сюда.",
    rate_chip="Курс валюты",
    rate_h2="Актуальный курс валюты",
    p_rate='Суммы на сайте (в частности, на странице <a href="{stoimost}">«Стоимость и тарифы»</a>) указаны в парагвайских гуарани (₲, PYG) — это государственные пошлины и налоги. Ниже — курс к доллару США, евро и российскому рублю, обновляется автоматически.',
    schema_name="Терминология Grund Paraguay",
),
"es": dict(
    title="Terminología y tipo de cambio: glosario de términos de Paraguay | Grund Paraguay",
    description="Explicación de los términos legales y en español del sitio — DNM, RUC, Cédula, SUACE, IVA y otros — y el tipo de cambio actual del guaraní paraguayo frente al dólar y al rublo.",
    h1="Terminología: términos en español y tipo de cambio del guaraní",
    lead="Aquí se reúnen todos los términos en español y jurídicos que aparecen en el sitio, con su explicación. Si llegó a esta página desde un enlace de otra sección del sitio, al volver el término quedará claro sin necesidad de regresar aquí de nuevo.",
    rate_chip="Tipo de cambio",
    rate_h2="Tipo de cambio actual",
    p_rate='Los montos del sitio (en particular, en la página <a href="{stoimost}">«Costos y tarifas»</a>) se expresan en guaraníes paraguayos (₲, PYG) — se trata de aranceles e impuestos estatales. A continuación, el tipo de cambio frente al dólar estadounidense, el euro y el rublo ruso, que se actualiza automáticamente.',
    schema_name="Terminología de Grund Paraguay",
),
"en": dict(
    title="Terminology & exchange rate: a glossary of Paraguay terms | Grund Paraguay",
    description="A plain-language guide to the site's Spanish and legal terms — DNM, RUC, Cédula, SUACE, IVA, and more — plus the current Paraguayan guaraní exchange rate against the dollar and the ruble.",
    h1="Terminology: Spanish terms and the guaraní exchange rate",
    lead="This page collects every Spanish and legal term used across the site, with a plain-language explanation. If you arrived here via a link from another page, the term will make sense on your way back without needing to revisit this page.",
    rate_chip="Exchange rate",
    rate_h2="Current exchange rate",
    p_rate='Amounts on the site (in particular, on the <a href="{stoimost}">"Costs and Rates"</a> page) are given in Paraguayan guaraníes (₲, PYG) — these are government fees and taxes. Below is the rate against the US dollar, the euro, and the Russian ruble, updated automatically.',
    schema_name="Grund Paraguay Terminology",
),
"de": dict(
    title="Terminologie & Wechselkurs: Glossar der Paraguay-Begriffe | Grund Paraguay",
    description="Erklärung der spanischen und juristischen Begriffe der Website — DNM, RUC, Cédula, SUACE, IVA und weitere — sowie der aktuelle Wechselkurs des paraguayischen Guaraní zu Dollar und Rubel.",
    h1="Terminologie: spanische Begriffe und Guaraní-Wechselkurs",
    lead="Hier sind alle spanischen und juristischen Begriffe zusammengestellt, die auf der Website vorkommen — mit Erklärung. Wenn Sie über einen Link von einer anderen Seite der Website hierher gelangt sind, ist der Begriff bei Ihrer Rückkehr verständlich, ohne dass Sie erneut hierher wechseln müssen.",
    rate_chip="Wechselkurs",
    rate_h2="Aktueller Wechselkurs",
    p_rate='Beträge auf der Website (insbesondere auf der Seite <a href="{stoimost}">„Preise"</a>) sind in paraguayischen Guaraní (₲, PYG) angegeben — das sind staatliche Gebühren und Steuern. Unten steht der Kurs zum US-Dollar, zum Euro und zum russischen Rubel, automatisch aktualisiert.',
    schema_name="Grund Paraguay Terminologie",
),
}

# Группа «Источники данных» — добавлена 12.08.2026 по запросу заказчика (Numbeo, Expatistan
# используются на RU-only странице «Стоимость жизни» хаба «Парагвай для переезда»). RU-only:
# это не испанский/юридический термин, а название сервиса-агрегатора, перевод не требовался и не
# делался в этом раунде («сначала только на русском») — группа рендерится только при lang=="ru".
RU_ONLY_EXTRA_GROUP = ("Источники данных", [
    ("numbeo", "Numbeo", None,
     'Крупный краудсорсинговый агрегатор данных о стоимости жизни в городах мира: цифры вносят сами пользователи, а не государственные органы или официальная статистика. На сайте используется на странице «Стоимость жизни» как один из двух источников по Асунсьону — с оговоркой, что это ориентир для планирования бюджета, а не точный прайс-лист.'),
    ("expatistan", "Expatistan", None,
     'Другой краудсорсинговый сервис сравнения стоимости жизни между городами, также основанный на пользовательских данных. Сам сервис отмечает, что его оценки по отдельным городам опираются на «небольшом объёме данных»; используется на той же странице «Стоимость жизни» рядом с Numbeo, с той же оговоркой о точности.'),
])

# Обратные ссылки "Упоминается на:" под каждым термином (12.08.2026, декор-фаза 3.1) —
# вычисляются программным сканированием исходников build-scripts на предмет "{terminologiya}#anchor",
# а не поддерживаются вручную по каждому термину — правило самого плана декора («достижимо путём
# программного сканирования, а не ручного списка»). Каждый pages_*.py файл (кроме этого) делится на
# блоки по вызовам page("pid", lang, ...): у всех build-скриптов одна и та же структура (словарь(и)
# с текстом → цикл по LANGS → page(...)), поэтому текст между двумя соседними вызовами page(...)
# принадлежит странице, чей вызов идёт СЛЕДУЮЩИМ — словари с интерполяцией {terminologiya}#anchor
# всегда определены раньше своего page()-вызова, а не после. Anchor-ссылки внутри такого блока
# считаются ссылками СО страницы этого pid НА термин. Пересчитывается при каждой сборке — не может
# рассинхронизироваться с реальной перелинковкой сайта, как это было бы при ручном списке.
def _compute_backlinks():
    page_call_re = re.compile(r'page\(\s*"([\w-]+)"\s*,\s*lang\b')
    anchor_re = re.compile(r'\{terminologiya\}#([\w-]+)')
    here = os.path.dirname(os.path.abspath(__file__))
    backlinks = {}  # anchor -> [pid, ...] в порядке первого упоминания в файлах
    for path in sorted(glob.glob(os.path.join(here, "pages_*.py"))):
        if os.path.basename(path) == "pages_terminology.py":
            continue  # ссылки термина на себя внутри глоссария — не обратные ссылки с других страниц
        text = open(path, encoding="utf-8").read()
        block_start = 0
        for m in page_call_re.finditer(text):
            pid = m.group(1)
            block_text = text[block_start:m.end()]
            block_start = m.end()
            for anchor in anchor_re.findall(block_text):
                pids = backlinks.setdefault(anchor, [])
                if pid not in pids:
                    pids.append(pid)
    return backlinks

BACKLINKS = _compute_backlinks()

# Короткие подписи для pid'ов подстраниц хаба «Парагвай для переезда» — их нет в общем NAV_LABELS
# (build.py), т.к. это не пункты главного меню. Те же короткие подписи, что уже используются в
# хлебных крошках этих страниц (BREADCRUMB_LABEL в pages_paragvay_hub.py) — продублированы здесь, а
# не импортированы: импорт pages_paragvay_hub.py запустил бы генерацию всего хаба как побочный
# эффект импорта (каждый pages_*.py — самостоятельный исполняемый скрипт, не библиотечный модуль).
EXTRA_PAGE_LABEL = {
    "ru": {"pochemu-paragvay": "Почему Парагвай", "zhizn-v-paragvae": "Жизнь в Парагвае",
           "stoimost-zhizni": "Стоимость жизни", "nalogi-inostrantsev": "Налоги для иностранцев",
           "banki-perevody": "Банки и переводы", "viza-vyezd": "Виза и въезд", "mify-voprosy": "Мифы и вопросы"},
    "es": {"pochemu-paragvay": "Por qué Paraguay", "zhizn-v-paragvae": "Vida en Paraguay",
           "stoimost-zhizni": "Costo de vida", "nalogi-inostrantsev": "Impuestos para extranjeros",
           "banki-perevody": "Bancos y transferencias", "viza-vyezd": "Visa y entrada", "mify-voprosy": "Mitos y preguntas"},
    "en": {"pochemu-paragvay": "Why Paraguay", "zhizn-v-paragvae": "Life in Paraguay",
           "stoimost-zhizni": "Cost of Living", "nalogi-inostrantsev": "Taxes for Foreigners",
           "banki-perevody": "Banking and Transfers", "viza-vyezd": "Visa and Entry", "mify-voprosy": "Myths and Questions"},
    "de": {"pochemu-paragvay": "Warum Paraguay", "zhizn-v-paragvae": "Leben in Paraguay",
           "stoimost-zhizni": "Lebenshaltungskosten", "nalogi-inostrantsev": "Steuern für Ausländer",
           "banki-perevody": "Banken und Transfers", "viza-vyezd": "Visum und Einreise", "mify-voprosy": "Mythen und Fragen"},
}

def page_label(lang, pid):
    return NAV_LABELS[lang].get(pid) or EXTRA_PAGE_LABEL[lang].get(pid) or pid

BACKLINK_LABEL = {
    "ru": "Упоминается на:", "es": "Se menciona en:", "en": "Mentioned on:", "de": "Erwähnt auf:",
}

for lang in ["ru","es","en","de"]:
    l = L(lang)
    pt = PAGE_TEXT[lang]

    def term_disp(term):
        # 12.08.2026 — группа "documents" переведена на 4 языка; для терминов, чьё написание
        # само переводится (например "apostil": Апостиль/Apostilla/Apostille/Apostille), term —
        # это {lang: text}; для проч. proper-noun-терминов (DNM, RUC, Cédula и т.д.) term — просто
        # строка, одинаковая на всех языках, как и раньше.
        return term[lang] if isinstance(term, dict) else term

    nav_chips = " ".join(f'<a href="#{a}">{term_disp(term)}</a>' for _, group in TERMS for a,term,_,_ in group)
    if lang == "ru":
        nav_chips += " " + " ".join(f'<a href="#{a}">{term}</a>' for a, term, _, _ in RU_ONLY_EXTRA_GROUP[1])

    def backlink_html(anchor):
        pids = BACKLINKS.get(anchor)
        if not pids:
            return ""
        links = ", ".join(f'<a href="{l[pid]}">{page_label(lang, pid)}</a>' for pid in pids if l.get(pid))
        return f'<p class="term-backlinks">{BACKLINK_LABEL[lang]} {links}</p>' if links else ""

    groups_html = ""
    for group_key, items in TERMS:
        groups_html += f'<h2>{GROUP_TITLES[group_key][lang]}</h2>\n<dl class="glossary">\n'
        for anchor, term, es_name, defs in items:
            es_span = f'<span class="es">— {es_name}</span>' if es_name else ''
            groups_html += f'  <dt id="{anchor}">{term_disp(term)}{es_span}</dt>\n  <dd>{defs[lang].format(**l)}{backlink_html(anchor)}</dd>\n'
        groups_html += '</dl>\n'

    if lang == "ru":
        title, items = RU_ONLY_EXTRA_GROUP
        groups_html += f'<h2>{title}</h2>\n<dl class="glossary">\n'
        for anchor, term, _, definition in items:
            groups_html += f'  <dt id="{anchor}">{term}</dt>\n  <dd>{definition}{backlink_html(anchor)}</dd>\n'
        groups_html += '</dl>\n'

    term_body = f'''
{breadcrumbs([(NAV_LABELS[lang]["home"], l["home"]), (NAV_LABELS[lang]["terminologiya"], None)])}
<section class="hero" style="padding-top:24px;">
  <div class="wrap">
    <h1>{pt["h1"]}</h1>
    <p class="lead">{pt["lead"]}</p>
    <div class="glossary-nav">{nav_chips}<a href="#kurs-valyuty">{pt["rate_chip"]}</a></div>
  </div>
</section>
<section style="padding-top:0;">
  <div class="prose">
    {groups_html}
    <h2 id="kurs-valyuty">{pt["rate_h2"]}</h2>
    <p>{pt["p_rate"].format(**l)}</p>
    {rate_widget(lang)}
  </div>
</section>
'''
    page("terminologiya", lang, pt["title"], pt["description"], term_body,
         extra_schema=[
             schema_breadcrumb([(NAV_LABELS[lang]["home"], f"/{lang}/"), (NAV_LABELS[lang]["terminologiya"], f"/{lang}/{href_to('terminologiya', lang)}")]),
             {"@context":"https://schema.org","@type":"DefinedTermSet","name":pt["schema_name"],
              "hasDefinedTerm":[{"@type":"DefinedTerm","name":term_disp(term),"description":re.sub('<[^>]+>', '', defs[lang].format(**l))} for _,group in TERMS for _,term,_,defs in group]}
         ])
