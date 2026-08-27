#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Генератор SVG-графиков для слайдера с инфографикой (12.08.2026, вторая версия —
настоящие графики динамики, а не карточки с одним числом). Рендерится на тёмном
«чертёжном» холсте (.diagram, см. vizualnyy-stil.md §1.2) — том же языке, что уже
использует прототип таймлайна на сайте.

Никаких внешних библиотек — чистая геометрия в SVG viewBox 0 0 W H.
"""

W, H = 620, 230
PAD_L, PAD_R, PAD_T, PAD_B = 54, 20, 20, 34
PLOT_W = W - PAD_L - PAD_R
PLOT_H = H - PAD_T - PAD_B

ACCENT = "var(--red-on-dark)"      # #E96C63 — основной акцент диаграмм на тёмном холсте


def _fmt_num(v):
    return f"{v:g}"


def _x_positions(xs):
    """xs — список чисел (годы). Возвращает список пиксельных X по НАСТОЯЩЕЙ числовой шкале
    (не равномерно по индексу) — важно там, где интервалы между годами разные (например,
    продолжительность жизни: 1980/1990/2000/2010/2025)."""
    xmin, xmax = min(xs), max(xs)
    span = (xmax - xmin) or 1
    return [PAD_L + (x - xmin) / span * PLOT_W for x in xs]


def line_chart(points, y_fmt=_fmt_num, invert=False, y_pad_ratio=0.18, start_label=True):
    """points: список (year:int, value:float, display:str). invert=True — переворачивает
    ось Y (используется для рейтингов/мест, где МЕНЬШЕ = ЛУЧШЕ — так линия «идёт вверх»,
    когда позиция страны улучшается, привычная логика спортивных рейтингов)."""
    xs = [p[0] for p in points]
    vals = [p[1] for p in points]
    vmin, vmax = min(vals), max(vals)
    pad = (vmax - vmin) * y_pad_ratio or (abs(vmax) * 0.1 or 1)
    vmin, vmax = vmin - pad, vmax + pad

    def y_of(v):
        frac = (v - vmin) / (vmax - vmin)
        if invert:
            frac = 1 - frac
        return PAD_T + (1 - frac) * PLOT_H

    xpix = _x_positions(xs)
    svg = []
    # gridlines + y ticks (4 линии, РАВНОМЕРНО по значению; y_of() сам учитывает invert)
    for i in range(4):
        frac = i / 3
        v_at_line = vmin + frac * (vmax - vmin)
        y = y_of(v_at_line)
        svg.append(f'<line x1="{PAD_L}" y1="{y:.1f}" x2="{W-PAD_R}" y2="{y:.1f}" class="grid-line"/>')
        svg.append(f'<text x="{PAD_L-8}" y="{y+3:.1f}" text-anchor="end" class="dim" font-size="11">{y_fmt(v_at_line)}</text>')
    # x labels — прорежаем, если года стоят теснее ~34px (иначе подписи склеиваются:
    # видно на «Индексе миролюбия»/«Паспорте», где несколько лет подряд рядом на шкале).
    # Первая и последняя точка подписаны всегда; middle-точки — только если есть место.
    min_gap = 34
    shown = [0, len(xpix) - 1] if len(xpix) > 1 else [0]
    last_shown_x = xpix[0]
    for i in range(1, len(xpix) - 1):
        if xpix[i] - last_shown_x >= min_gap and xpix[-1] - xpix[i] >= min_gap:
            shown.append(i)
            last_shown_x = xpix[i]
    for i in sorted(set(shown)):
        svg.append(f'<text x="{xpix[i]:.1f}" y="{H-PAD_B+18}" text-anchor="middle" class="dim" font-size="11">{xs[i]}</text>')
    # path
    path_d = " ".join(f'{"M" if i==0 else "L"}{xp:.1f},{y_of(v):.1f}' for i, (xp, v) in enumerate(zip(xpix, vals)))
    svg.append(f'<path d="{path_d}" fill="none" stroke="{ACCENT}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>')
    # markers (ring + dot)
    for i, (xp, v) in enumerate(zip(xpix, vals)):
        y = y_of(v)
        svg.append(f'<circle cx="{xp:.1f}" cy="{y:.1f}" r="6" fill="var(--surface-dark)"/>')
        svg.append(f'<circle cx="{xp:.1f}" cy="{y:.1f}" r="4" fill="{ACCENT}"/>')
    # direct labels: первая (тускло) и последняя (жирно) точки
    first_disp = points[0][2]
    last_disp = points[-1][2]
    fx, fy = xpix[0], y_of(vals[0])
    lx, ly = xpix[-1], y_of(vals[-1])
    if start_label:
        svg.append(f'<text x="{fx:.1f}" y="{fy-12:.1f}" text-anchor="start" class="dim" font-size="12">{first_disp}</text>')
    svg.append(f'<text x="{lx:.1f}" y="{ly-12:.1f}" text-anchor="end" font-size="13" font-weight="600">{last_disp}</text>')
    return f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="">{"".join(svg)}</svg>'


def bar_chart(cats, values, disps, y_fmt=_fmt_num, dashed_idx=None):
    """cats: подписи по X (годы/категории). values: числа. disps: отображаемые подписи
    значений (со знаком/единицей). dashed_idx: индекс столбца, который нужно показать
    пунктиром (расчётное/оценочное значение, а не опубликованная цифра)."""
    n = len(values)
    vmax = max(values) * 1.18
    gap = 18
    bw = min(64, (PLOT_W - gap * (n - 1)) / n)
    total_w = bw * n + gap * (n - 1)
    x0 = PAD_L + (PLOT_W - total_w) / 2
    svg = []
    for i in range(4):
        frac = i / 3
        y = PAD_T + (1 - frac) * PLOT_H
        v = frac * vmax
        svg.append(f'<line x1="{PAD_L}" y1="{y:.1f}" x2="{W-PAD_R}" y2="{y:.1f}" class="grid-line"/>')
        svg.append(f'<text x="{PAD_L-8}" y="{y+3:.1f}" text-anchor="end" class="dim" font-size="11">{y_fmt(v)}</text>')
    for i, (c, v, d) in enumerate(zip(cats, values, disps)):
        bx = x0 + i * (bw + gap)
        bh = (v / vmax) * PLOT_H
        by = PAD_T + PLOT_H - bh
        dash = ' stroke="var(--ink-dim-on-dark)" stroke-width="1.5" stroke-dasharray="4,3" fill="none"' if dashed_idx == i else f' fill="{ACCENT}"'
        svg.append(f'<rect x="{bx:.1f}" y="{by:.1f}" width="{bw:.1f}" height="{bh:.1f}" rx="4"{dash}/>')
        svg.append(f'<text x="{bx+bw/2:.1f}" y="{by-8:.1f}" text-anchor="middle" font-size="13" font-weight="600">{d}</text>')
        svg.append(f'<text x="{bx+bw/2:.1f}" y="{H-PAD_B+18}" text-anchor="middle" class="dim" font-size="11">{c}</text>')
    return f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="">{"".join(svg)}</svg>'


def dumbbell_chart(rows):
    """rows: список dict(label, before_disp, after_disp, before_frac, after_frac) —
    before_frac/after_frac уже нормализованы в [0,1] относительно ширины полосы (позиция
    по X для «было» и «стало»), т.к. у двух строк разные единицы измерения (люди vs заявки)
    и общий числовой масштаб между ними был бы бессмысленным."""
    row_h = PLOT_H / len(rows)
    svg = []
    lane_l, lane_r = PAD_L + 10, W - PAD_R - 10
    lane_w = lane_r - lane_l
    for i, r in enumerate(rows):
        cy = PAD_T + row_h * i + row_h * 0.55
        bx = lane_l + r["before_frac"] * lane_w
        ax = lane_l + r["after_frac"] * lane_w
        svg.append(f'<text x="{lane_l:.1f}" y="{PAD_T + row_h*i + 14:.1f}" text-anchor="start" class="dim" font-size="12">{r["label"]}</text>')
        svg.append(f'<line x1="{lane_l:.1f}" y1="{cy:.1f}" x2="{lane_r:.1f}" y2="{cy:.1f}" class="grid-line"/>')
        svg.append(f'<line x1="{bx:.1f}" y1="{cy:.1f}" x2="{ax:.1f}" y2="{cy:.1f}" stroke="{ACCENT}" stroke-width="2.5" stroke-linecap="round"/>')
        svg.append(f'<circle cx="{bx:.1f}" cy="{cy:.1f}" r="6" fill="var(--surface-dark)"/>')
        svg.append(f'<circle cx="{bx:.1f}" cy="{cy:.1f}" r="4" fill="var(--ink-dim-on-dark)"/>')
        svg.append(f'<circle cx="{ax:.1f}" cy="{cy:.1f}" r="6" fill="var(--surface-dark)"/>')
        svg.append(f'<circle cx="{ax:.1f}" cy="{cy:.1f}" r="4" fill="{ACCENT}"/>')
        svg.append(f'<text x="{bx:.1f}" y="{cy+20:.1f}" text-anchor="middle" class="dim" font-size="11">{r["before_disp"]}</text>')
        svg.append(f'<text x="{ax:.1f}" y="{cy-12:.1f}" text-anchor="middle" font-size="13" font-weight="600">{r["after_disp"]}</text>')
    return f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="">{"".join(svg)}</svg>'
