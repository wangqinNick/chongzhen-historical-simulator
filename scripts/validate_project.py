# -*- coding: utf-8 -*-
"""Validate the Chongzhen SillyTavern package outputs."""

from __future__ import annotations

import json
import sys
import zipfile
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
    "sillytavern/package_manifest.json",
    "sillytavern/玩家指令模板.md",
    "sillytavern/当前状态_AuthorNote模板.md",
    "sillytavern/开局剧本_AuthorNote合集.md",
    "sillytavern/快速卡/地区军队派系卡.md",
    "modules/module_index.json",
    "modules/模块依赖图.md",
    "dist/chongzhen-sillytavern-bundle.zip",
    "saves/开局存档/README.md",
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
    numbered_modules = [path for path in modules if path.name[:2].isdigit()]
    if len(numbered_modules) != 41:
        fail(f"expected 41 numbered modules, found {len(numbered_modules)}")

    character_json = sorted((ROOT / "sillytavern" / "人物卡" / "json").glob("*.json"))
    character_md = sorted((ROOT / "sillytavern" / "人物卡" / "markdown").glob("*.md"))
    if len(character_json) < 20 or len(character_md) < 20:
        fail(f"expected at least 20 character cards, found json={len(character_json)}, md={len(character_md)}")
    if len(character_json) != len(character_md):
        fail(f"character json/markdown count mismatch: json={len(character_json)}, md={len(character_md)}")

    opening_saves = sorted((ROOT / "saves" / "开局存档").glob("*.json"))
    if len(opening_saves) < 6:
        fail(f"expected at least 6 opening save JSON files, found {len(opening_saves)}")

    for path in character_json:
        data = load_json(path)
        if data.get("spec") != "chara_card_v2":
            fail(f"{path} is not chara_card_v2")
        card_data = data.get("data", {})
        description = card_data.get("description", "")
        if "【资料来源】" not in description or "【史实要点】" not in description:
            fail(f"{path} is missing source or factual notes")
        if not card_data.get("creator_notes") or "触发词" not in card_data["creator_notes"]:
            fail(f"{path} is missing trigger creator notes")

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

    manifest = load_json(ROOT / "sillytavern" / "package_manifest.json")
    counts = manifest.get("counts", {})
    if counts.get("modules") != 41:
        fail("manifest module count is incorrect")
    if counts.get("character_json", 0) < 20:
        fail("manifest character count is incorrect")
    if counts.get("opening_saves", 0) < 6:
        fail("manifest opening save count is incorrect")

    module_index = load_json(ROOT / "modules" / "module_index.json")
    if len(module_index.get("modules", [])) != 41:
        fail("module index should contain 41 modules")

    if (ROOT / "dist" / "chongzhen-sillytavern-bundle.zip").stat().st_size <= 0:
        fail("release bundle zip is empty")

    zip_path = ROOT / "dist" / "chongzhen-sillytavern-bundle.zip"
    with zipfile.ZipFile(zip_path) as archive:
        names = set(archive.namelist())
    required_zip_fragments = [
        "sillytavern/import/",
        "sillytavern/人物卡/json/",
        "sillytavern/最终一键复制包_崇祯历史模拟器.md",
        "sillytavern/玩家指令模板.md",
        "saves/开局存档/",
        "modules/module_index.json",
        "docs/",
        "README.md",
    ]
    for fragment in required_zip_fragments:
        if not any(fragment in name for name in names):
            fail(f"release bundle zip missing {fragment}")

    for path in opening_saves:
        data = load_json(path)
        if not data.get("author_note") or not data.get("fields"):
            fail(f"opening save missing author_note or fields: {path}")

    scan_files = numbered_modules + [
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
        f"opening_saves={len(opening_saves)}, "
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
