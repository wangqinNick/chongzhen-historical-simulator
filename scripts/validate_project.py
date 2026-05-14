# -*- coding: utf-8 -*-
"""Validate the Chongzhen SillyTavern package outputs."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "sillytavern/最终一键复制包_崇祯历史模拟器.md",
    "sillytavern/import/崇祯历史模拟器_核心Lorebook.json",
    "sillytavern/import/崇祯历史模拟器_全模块Lorebook.json",
    "sillytavern/import/崇祯历史模拟器_人物Lorebook.json",
    "sillytavern/import/崇祯历史模拟器_快速卡Lorebook.json",
    "sillytavern/import/崇祯历史模拟器_开局剧本Lorebook.json",
    "sillytavern/import/崇祯历史模拟器_完整Lorebook.json",
    "sillytavern/崇祯模拟器_Narrator角色卡草案.md",
    "sillytavern/崇祯模拟器_Narrator角色卡.json",
    "sillytavern/当前状态_AuthorNote模板.md",
    "sillytavern/开局剧本_AuthorNote合集.md",
    "sillytavern/快速卡/地区军队派系卡.md",
]

BAD_MARKERS = [
    "### 运行规则",
    "待接入",
    "待定位",
    "待查",
    "尚未",
    "placeholder",
    "TODO",
    "FIXME",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover
        fail(f"{path} is not valid JSON: {exc}")


def main() -> None:
    for rel in REQUIRED_FILES:
        path = ROOT / rel
        if not path.exists():
            fail(f"missing required file: {rel}")
        if path.stat().st_size == 0:
            fail(f"empty required file: {rel}")

    modules = sorted((ROOT / "modules").glob("*.md"))
    if len(modules) != 41:
        fail(f"expected 41 modules, found {len(modules)}")

    character_json = sorted((ROOT / "sillytavern" / "人物卡" / "json").glob("*.json"))
    character_md = sorted((ROOT / "sillytavern" / "人物卡" / "markdown").glob("*.md"))
    if len(character_json) < 20 or len(character_md) < 20:
        fail(f"expected at least 20 character cards, found json={len(character_json)}, md={len(character_md)}")

    for path in character_json:
        data = load_json(path)
        if data.get("spec") != "chara_card_v2":
            fail(f"{path} is not chara_card_v2")

    lorebooks = [
        ROOT / "sillytavern" / "import" / "崇祯历史模拟器_核心Lorebook.json",
        ROOT / "sillytavern" / "import" / "崇祯历史模拟器_全模块Lorebook.json",
        ROOT / "sillytavern" / "import" / "崇祯历史模拟器_人物Lorebook.json",
        ROOT / "sillytavern" / "import" / "崇祯历史模拟器_快速卡Lorebook.json",
        ROOT / "sillytavern" / "import" / "崇祯历史模拟器_开局剧本Lorebook.json",
        ROOT / "sillytavern" / "import" / "崇祯历史模拟器_完整Lorebook.json",
    ]
    for path in lorebooks:
        data = load_json(path)
        entries = data.get("entries")
        if not isinstance(entries, dict) or not entries:
            fail(f"{path} has no entries")

    complete_entries = load_json(ROOT / "sillytavern" / "import" / "崇祯历史模拟器_完整Lorebook.json")["entries"]
    if len(complete_entries) < 96:
        fail(f"complete lorebook should have at least 96 entries, found {len(complete_entries)}")

    narrator = load_json(ROOT / "sillytavern" / "崇祯模拟器_Narrator角色卡.json")
    if narrator.get("spec") != "chara_card_v2":
        fail("Narrator card is not chara_card_v2")

    scan_files = modules + [
        ROOT / "README.md",
        ROOT / "sillytavern" / "最终一键复制包_崇祯历史模拟器.md",
        ROOT / "research" / "source_catalog.md",
    ]
    for path in scan_files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        for marker in BAD_MARKERS:
            if marker in text:
                fail(f"marker {marker!r} remains in {path}")

    print(
        "OK: modules=41, "
        f"characters={len(character_json)}, "
        f"complete_lorebook_entries={len(complete_entries)}"
    )


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as exc:  # pragma: no cover
        print(f"FAIL: {exc}")
        sys.exit(1)
