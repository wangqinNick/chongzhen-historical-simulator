# -*- coding: utf-8 -*-
"""Generate a readable roster table from SillyTavern character cards."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHAR_DIR = ROOT / "sillytavern" / "人物卡" / "json"
OUT = ROOT / "sillytavern" / "人物卡" / "人物总表.md"


def extract_line(description: str, label: str) -> str:
    match = re.search(rf"【{re.escape(label)}】([^\n]+)", description)
    return match.group(1).strip() if match else ""


def main() -> None:
    rows: list[tuple[str, str, str, str, str]] = []
    for path in sorted(CHAR_DIR.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        card = data["data"]
        name = card["name"]
        description = card.get("description", "")
        role = extract_line(description, "身份")
        source = extract_line(description, "资料来源")
        creator_notes = card.get("creator_notes", "")
        trigger_line = ""
        for line in creator_notes.splitlines():
            if line.startswith("触发词"):
                trigger_line = line.split("：", 1)[-1]
                break
        rows.append((name, path.name, role, trigger_line, source))

    lines = [
        "# 人物总表",
        "",
        "本表由 `scripts/generate_character_roster.py` 自动生成，用于快速查看已导入的人物角色卡。",
        "",
        "| 人物 | JSON 文件 | 角色定位 | 触发词 | 资料来源 |",
        "|---|---|---|---|---|",
    ]
    for name, filename, role, triggers, source in rows:
        lines.append(f"| {name} | `json/{filename}` | {role} | {triggers} | {source} |")
    lines.append("")
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()

