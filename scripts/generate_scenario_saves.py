# -*- coding: utf-8 -*-
"""Generate ready-to-use opening save snapshots from scenario Author's Notes."""

from __future__ import annotations

import json
import re
from collections import OrderedDict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sillytavern" / "开局剧本_AuthorNote合集.md"
OUT_DIR = ROOT / "saves" / "开局存档"
INDEX = OUT_DIR / "README.md"


def slug(title: str) -> str:
    year = re.search(r"(\d{4})", title)
    reign = re.search(r"崇祯([一二三四五六七八九十元]+)年", title)
    if year and reign:
        return f"{year.group(1)}_崇祯{reign.group(1)}年"
    if year:
        return year.group(1)
    return re.sub(r"\W+", "_", title)


def parse_fields(block: str) -> OrderedDict[str, str]:
    fields: OrderedDict[str, str] = OrderedDict()
    for line in block.splitlines():
        match = re.match(r"【([^】]+)】(.+)", line.strip())
        if match:
            fields[match.group(1)] = match.group(2).strip()
    return fields


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    raw = SOURCE.read_text(encoding="utf-8")
    pattern = re.compile(r"^## (崇祯.+?)\n\n```text\n([\s\S]*?)\n```", flags=re.MULTILINE)
    index_lines = [
        "# 开局存档",
        "",
        "这些文件可直接复制到 SillyTavern Author's Note，或作为 JSON 存档供后续工具读取。",
        "",
    ]
    count = 0
    for match in pattern.finditer(raw):
        title = match.group(1).strip()
        block = match.group(2).strip()
        fields = parse_fields(block)
        name = slug(title)
        md_path = OUT_DIR / f"{name}.md"
        json_path = OUT_DIR / f"{name}.json"
        md_path.write_text(
            f"# {title} 开局存档\n\n## Author's Note\n\n```text\n{block}\n```\n\n"
            "## 使用方式\n\n复制上方代码块到当前聊天的 Author's Note。每回合结束后只更新变化项。\n",
            encoding="utf-8",
        )
        json_path.write_text(
            json.dumps(
                OrderedDict(
                    title=title,
                    author_note=block,
                    fields=fields,
                    usage="Copy author_note into SillyTavern Author's Note, then update only changed state after each turn.",
                ),
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
        index_lines.append(f"- [{title}]({md_path.name}) / `{json_path.name}`")
        count += 1

    INDEX.write_text("\n".join(index_lines) + "\n", encoding="utf-8")
    print(f"Wrote {count} opening saves to {OUT_DIR}")


if __name__ == "__main__":
    main()
