# -*- coding: utf-8 -*-
"""Generate an importable SillyTavern Lorebook from quick region/army/faction cards."""

from __future__ import annotations

import json
import re
from collections import OrderedDict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUICK_CARD_PATH = ROOT / "sillytavern" / "快速卡" / "地区军队派系卡.md"
EXTRA_QUICK_CARDS_PATH = ROOT / "data" / "quick_cards_extra.json"
EXTRA_QUICK_MD_PATH = ROOT / "sillytavern" / "快速卡" / "补充地区军队派系卡.md"
OUT_PATH = ROOT / "sillytavern" / "import" / "崇祯历史模拟器_快速卡Lorebook.json"


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


def split_cards(raw: str) -> list[tuple[str, str]]:
    matches = list(re.finditer(r"^## (.+)$", raw, flags=re.MULTILINE))
    cards: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(raw)
        title = match.group(1).strip()
        body = raw[start:end].strip()
        cards.append((title, body))
    return cards


def extract_keys(title: str, body: str) -> list[str]:
    keys: list[str] = []
    trigger_match = re.search(r"触发词：(.+)", body)
    if trigger_match:
        keys.extend([item.strip() for item in re.split(r"[,，]", trigger_match.group(1)) if item.strip()])
    title_key = title.split("：", 1)[-1]
    if title_key not in keys:
        keys.insert(0, title_key)
    return keys[:10]


def render_extra_markdown(cards: list[dict]) -> str:
    lines = [
        "# 补充地区、军队、派系快速卡",
        "",
        "本文件由 `data/quick_cards_extra.json` 生成，用于扩展 SillyTavern 快速卡、Data Bank 和 Lorebook。",
        "口径：史实资料、论文方向、网络索引和模拟器采用值分层使用；不稳定数值以等级和区间处理。",
        "",
    ]
    for card in cards:
        lines.extend(
            [
                f"## {card['type']}：{card['name']}",
                "",
                f"触发词：{', '.join(card['triggers'])}",
                "",
                f"定位：{card['role']}",
                "",
                "关键变量：",
            ]
        )
        lines.extend(f"- {item}" for item in card["variables"])
        lines.extend(["", "裁判规则："])
        lines.extend(f"- {item}" for item in card["rules"])
        lines.extend(["", f"来源口径：{card['source']}", ""])
    return "\n".join(lines).strip() + "\n"


def load_extra_cards() -> list[dict]:
    if not EXTRA_QUICK_CARDS_PATH.exists():
        return []
    cards = json.loads(EXTRA_QUICK_CARDS_PATH.read_text(encoding="utf-8"))
    EXTRA_QUICK_MD_PATH.parent.mkdir(parents=True, exist_ok=True)
    EXTRA_QUICK_MD_PATH.write_text(render_extra_markdown(cards), encoding="utf-8")
    return cards


def main() -> None:
    load_extra_cards()
    raw = QUICK_CARD_PATH.read_text(encoding="utf-8")
    if EXTRA_QUICK_MD_PATH.exists():
        raw += "\n\n" + EXTRA_QUICK_MD_PATH.read_text(encoding="utf-8")
    entries: OrderedDict[str, OrderedDict] = OrderedDict()
    for offset, (title, body) in enumerate(split_cards(raw), start=1):
        content = f"【快速卡：{title}】{re.sub(r'\\s+', ' ', body).strip()}"
        if len(content) > 1200:
            content = content[:1190] + "……"
        uid = 9000 + offset
        entries[str(uid)] = new_entry(uid, extract_keys(title, body), f"快速卡 {title}", content, 700 + offset)

    OUT_PATH.write_text(json.dumps(OrderedDict(entries=entries), ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(entries)} entries to {OUT_PATH}")


if __name__ == "__main__":
    main()
