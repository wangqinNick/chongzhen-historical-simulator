# -*- coding: utf-8 -*-
"""Generate an importable SillyTavern World Info JSON from all module files."""

from __future__ import annotations

import json
import re
from collections import OrderedDict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CORE_PATH = ROOT / "sillytavern" / "import" / "崇祯历史模拟器_核心Lorebook.json"
OUT_PATH = ROOT / "sillytavern" / "import" / "崇祯历史模拟器_全模块Lorebook.json"
COMPLETE_OUT_PATH = ROOT / "sillytavern" / "import" / "崇祯历史模拟器_完整Lorebook.json"
CHARACTER_LOREBOOK_PATH = ROOT / "sillytavern" / "import" / "崇祯历史模拟器_人物Lorebook.json"
MODULE_DIR = ROOT / "modules"


def section_text(raw: str, heading: str) -> str:
    pattern = re.escape(heading) + r"\s+([\s\S]*?)(?:\n## |\n### |\Z)"
    match = re.search(pattern, raw)
    if not match:
        return ""
    return re.sub(r"\s+", " ", match.group(1)).strip()


def new_entry(uid: int, keys: list[str], comment: str, content: str, order: int) -> OrderedDict:
    return OrderedDict(
        uid=uid,
        key=keys,
        keysecondary=[],
        comment=comment,
        content=content,
        constant=False,
        vectorized=False,
        selective=False,
        selectiveLogic=0,
        addMemo=True,
        order=order,
        position=0,
        disable=False,
        excludeRecursion=False,
        preventRecursion=False,
        delayUntilRecursion=False,
        probability=100,
        useProbability=True,
        depth=4,
        group="",
        groupOverride=False,
        groupWeight=100,
        scanDepth=None,
        caseSensitive=None,
        matchWholeWords=None,
        useGroupScoring=None,
        automationId="",
        role=None,
    )


def module_entry(path: Path, uid: int) -> OrderedDict:
    raw = path.read_text(encoding="utf-8")
    title_match = re.search(r'title:\s*"([^"]+)"', raw)
    title = title_match.group(1) if title_match else path.stem
    id_match = re.search(r'id:\s*"?([0-9]+)"?', raw)
    module_id = id_match.group(1) if id_match else f"{uid:02d}"
    purpose = section_text(raw, "## 用途")
    core_rules = section_text(raw, "## 核心规则")

    extra_parts: list[str] = []
    for heading in (
        "### 第一批基准",
        "### 核心人物与代理人",
        "### 基准数据",
        "### 粮价基准",
        "### 漕运基准",
        "### 判定口径",
        "### 流程",
        "### 使用规则",
    ):
        part = section_text(raw, heading)
        if part:
            extra_parts.append(f"{heading}：{part}")

    content = f"【模块 {module_id}：{title}】{purpose} 核心规则：{core_rules} {' '.join(extra_parts)}"
    if len(content) > 1200:
        content = content[:1190] + "……"

    keys = [title]
    for part in re.split(r"[_、，,\s]+", path.stem):
        if part and not part.isdigit() and part not in keys:
            keys.append(part)
    keys = keys[:8]

    return new_entry(uid, keys, f"M{module_id} {title}", content, 300 + int(module_id))


def main() -> None:
    core = json.loads(CORE_PATH.read_text(encoding="utf-8"), object_pairs_hook=OrderedDict)
    entries: OrderedDict[str, OrderedDict] = OrderedDict(core["entries"])
    next_uid = max(int(key) for key in entries) + 1

    for path in sorted(MODULE_DIR.glob("*.md"), key=lambda p: p.name):
        entries[str(next_uid)] = module_entry(path, next_uid)
        next_uid += 1

    OUT_PATH.write_text(json.dumps(OrderedDict(entries=entries), ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(entries)} entries to {OUT_PATH}")

    if CHARACTER_LOREBOOK_PATH.exists():
        complete_entries: OrderedDict[str, OrderedDict] = OrderedDict(entries)
        next_uid = max(int(key) for key in complete_entries) + 1
        character_lorebook = json.loads(CHARACTER_LOREBOOK_PATH.read_text(encoding="utf-8"), object_pairs_hook=OrderedDict)
        for entry in character_lorebook["entries"].values():
            copied = OrderedDict(entry)
            copied["uid"] = next_uid
            complete_entries[str(next_uid)] = copied
            next_uid += 1
        COMPLETE_OUT_PATH.write_text(
            json.dumps(OrderedDict(entries=complete_entries), ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(f"Wrote {len(complete_entries)} entries to {COMPLETE_OUT_PATH}")


if __name__ == "__main__":
    main()
