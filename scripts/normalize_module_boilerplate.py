# -*- coding: utf-8 -*-
"""Replace leftover scaffold boilerplate in module markdown with actionable runtime rules."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_DIR = ROOT / "modules"

PLACEHOLDER_WITH_TRIGGER = re.compile(
    r"### 规则\s+"
    r"- 本节服务于「[^」]+」的回合判定。\s+"
    r"- 所有结论必须区分史实依据、合理推断和模拟器采用值。\s+"
    r"- 若影响财政、军队、地方、人物或合法性，必须写入状态快照。\s+"
    r"- 若资料不足，使用等级和区间，不编造精确数字。\s+"
    r"### SillyTavern 触发建议\s+"
    r"- 触发词使用本节专门术语。\s+"
    r"- 只在相关政策、奏报或事件出现时进入上下文。",
    re.MULTILINE,
)

PLACEHOLDER_RULE_ONLY = re.compile(
    r"### 规则\s+"
    r"- 本节服务于「[^」]+」的回合判定。\s+"
    r"- 所有结论必须区分史实依据、合理推断和模拟器采用值。\s+"
    r"- 若影响财政、军队、地方、人物或合法性，必须写入状态快照。\s+"
    r"- 若资料不足，使用等级和区间，不编造精确数字。",
    re.MULTILINE,
)

REPLACEMENT = """### 通用裁判规则

- 只在本节关键词、相关政策、奏报、战报、账册或状态快照出现时触发。
- 判定时先读取当前时间、地区状态、财政压力、执行人、交通、资源、合法性和敌方行动。
- 输出必须落到成功、部分成功、延迟、变形、失败或反噬之一，并说明具体环节。
- 若影响财政、军队、地方、人物、资源或合法性，必须写入状态快照。
- 资料不足时使用等级、区间和可信度，不编造精确数字。"""


def main() -> None:
    changed = 0
    for path in sorted(MODULE_DIR.glob("*.md")):
        raw = path.read_text(encoding="utf-8")
        updated = PLACEHOLDER_WITH_TRIGGER.sub(REPLACEMENT, raw)
        updated = PLACEHOLDER_RULE_ONLY.sub(REPLACEMENT, updated)
        if updated != raw:
            path.write_text(updated, encoding="utf-8")
            changed += 1
            print(f"normalized {path.name}")
    print(f"normalized {changed} module files")


if __name__ == "__main__":
    main()
