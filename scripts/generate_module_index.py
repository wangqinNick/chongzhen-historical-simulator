# -*- coding: utf-8 -*-
"""Generate module index JSON and a Mermaid dependency graph."""

from __future__ import annotations

import json
import re
from collections import OrderedDict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_DIR = ROOT / "modules"
OUT_JSON = ROOT / "modules" / "module_index.json"
OUT_GRAPH = ROOT / "modules" / "模块依赖图.md"


def frontmatter(raw: str) -> dict[str, str]:
    raw = raw.lstrip("\ufeff")
    match = re.match(r"---\n([\s\S]*?)\n---", raw)
    if not match:
        return {}
    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def main() -> None:
    modules: list[OrderedDict] = []
    for path in sorted(MODULE_DIR.glob("*.md"), key=lambda p: p.name):
        if path.name in {OUT_GRAPH.name}:
            continue
        raw = path.read_text(encoding="utf-8")
        meta = frontmatter(raw)
        if not meta.get("id"):
            continue
        depends = [item.strip() for item in meta.get("depends_on", "").split(",") if item.strip()]
        modules.append(
            OrderedDict(
                id=meta["id"].zfill(2),
                title=meta.get("title", path.stem),
                category=meta.get("category", ""),
                priority=meta.get("priority", ""),
                status=meta.get("status", ""),
                depends_on=[item.zfill(2) for item in depends],
                path=path.as_posix(),
            )
        )

    OUT_JSON.write_text(json.dumps(OrderedDict(modules=modules), ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# 模块依赖图",
        "",
        "本图由 `scripts/generate_module_index.py` 生成，用于快速查看 41 个模块之间的依赖。",
        "",
        "```mermaid",
        "flowchart TD",
    ]
    for module in modules:
        node_id = f"M{module['id']}"
        label = f"{module['id']} {module['title']}\\n{module['priority']} / {module['status']}"
        lines.append(f'  {node_id}["{label}"]')
    for module in modules:
        node_id = f"M{module['id']}"
        for dep in module["depends_on"]:
            lines.append(f"  M{dep} --> {node_id}")
    lines.append("```")
    lines.append("")
    lines.append("## 模块索引")
    lines.append("")
    lines.append("| ID | 模块 | 分类 | 优先级 | 状态 | 依赖 |")
    lines.append("|---|---|---|---|---|---|")
    for module in modules:
        deps = ", ".join(module["depends_on"]) if module["depends_on"] else "-"
        lines.append(
            f"| {module['id']} | {module['title']} | {module['category']} | "
            f"{module['priority']} | {module['status']} | {deps} |"
        )
    OUT_GRAPH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUT_JSON} and {OUT_GRAPH}")


if __name__ == "__main__":
    main()
