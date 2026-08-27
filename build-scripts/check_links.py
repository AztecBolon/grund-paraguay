#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Проверка целостности внутренних ссылок и якорей по всему мультиязычному сайту."""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

html_files = []
for dirpath, dirnames, filenames in os.walk(ROOT):
    if "build-scripts" in dirpath:
        continue
    for fn in filenames:
        if fn.endswith(".html"):
            html_files.append(os.path.relpath(os.path.join(dirpath, fn), ROOT))

href_re = re.compile(r'(?:href|src)="([^"]+)"')
id_re = re.compile(r'id="([^"]+)"')

anchor_ids_cache = {}
def get_ids(fname):
    if fname not in anchor_ids_cache:
        path = os.path.join(ROOT, fname)
        if os.path.exists(path):
            with open(path, encoding="utf-8") as f:
                content = f.read()
            anchor_ids_cache[fname] = set(id_re.findall(content))
        else:
            anchor_ids_cache[fname] = set()
    return anchor_ids_cache[fname]

errors = []
checked = 0

for fname in html_files:
    path = os.path.join(ROOT, fname)
    with open(path, encoding="utf-8") as f:
        content = f.read()
    base_dir = os.path.dirname(fname)
    for m in href_re.finditer(content):
        url = m.group(1)
        checked += 1
        if url.startswith(("http://", "https://", "mailto:", "tel:", "#")) is False and url.startswith("#"):
            pass
        if url.startswith(("http://", "https://", "mailto:", "tel:")):
            continue
        if url == "/":
            continue
        # split anchor
        if "#" in url:
            target_path, _, anchor = url.partition("#")
        else:
            target_path, anchor = url, None

        if target_path == "":
            # same-page anchor
            resolved = fname
        elif target_path.startswith("/"):
            resolved = target_path.lstrip("/")
        else:
            resolved = os.path.normpath(os.path.join(base_dir, target_path))

        full = os.path.join(ROOT, resolved)
        if not os.path.exists(full):
            errors.append(f"[{fname}] broken link -> {url}  (resolved: {resolved})")
            continue

        if anchor:
            ids = get_ids(resolved)
            if anchor not in ids:
                errors.append(f"[{fname}] broken anchor -> {url}  (#{anchor} not found in {resolved})")

print(f"Checked {checked} href/src attributes across {len(html_files)} files.")
if errors:
    print(f"\n{len(errors)} PROBLEM(S) FOUND:\n")
    for e in errors:
        print(" -", e)
    sys.exit(1)
else:
    print("No broken links or anchors found.")
