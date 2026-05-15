# -*- coding: utf-8 -*-
"""Generate a concise build report for the current package state."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "BUILD_REPORT.md"


def main() -> None:
    manifest = json.loads((ROOT / "sillytavern" / "package_manifest.json").read_text(encoding="utf-8"))
    counts = manifest["counts"]
    generated_at = datetime.now().isoformat(timespec="seconds")

    content = f"""# 构建报告

生成时间：{generated_at}

## 数量统计

- 模块：{counts["modules"]}
- 人物 JSON：{counts["character_json"]}
- 人物 Markdown：{counts["character_markdown"]}
- 开局存档：{counts["opening_saves"]}
- 完整 Lorebook 条目：{counts["lorebooks"]["崇祯历史模拟器_完整Lorebook.json"]}
- 快速卡 Lorebook 条目：{counts["lorebooks"]["崇祯历史模拟器_快速卡Lorebook.json"]}
- 人物 Lorebook 条目：{counts["lorebooks"]["崇祯历史模拟器_人物Lorebook.json"]}
- 开局剧本 Lorebook 条目：{counts["lorebooks"]["崇祯历史模拟器_开局剧本Lorebook.json"]}
- 资料规则 Lorebook 条目：{counts["lorebooks"]["崇祯历史模拟器_资料规则Lorebook.json"]}

## 主要入口

- `START_HERE.md`
- `dist/chongzhen-sillytavern-bundle.zip`
- `sillytavern/最终一键复制包_崇祯历史模拟器.md`
- `sillytavern/崇祯模拟器_Narrator角色卡.json`
- `sillytavern/import/崇祯历史模拟器_完整Lorebook.json`
- `sillytavern/人物卡/json/`
- `saves/开局存档/`

## 校验命令

```powershell
powershell -ExecutionPolicy Bypass -File scripts\\build_all.ps1
python scripts\\validate_project.py
python scripts\\check_release_bundle.py
```

## 当前校验基线

- 41 个编号模块。
- 32 张人物 JSON 卡与 32 张人物 Markdown 卡。
- 7 个开局存档。
- 7 个 Lorebook JSON。
- 完整 Lorebook 至少 121 条。
- 发布 ZIP 含最终复制包、角色卡、人物卡、开局存档、回合日志模板、群聊预设、资料规则和 docs。
"""
    OUT.write_text(content, encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
