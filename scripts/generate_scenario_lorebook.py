# -*- coding: utf-8 -*-
"""Generate a SillyTavern Lorebook from scenario Author's Note blocks."""

from __future__ import annotations

import json
import re
from collections import OrderedDict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sillytavern" / "开局剧本_AuthorNote合集.md"
OUT = ROOT / "sillytavern" / "import" / "崇祯历史模拟器_开局剧本Lorebook.json"


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
        group="开局剧本",
        groupOverride=False,
        groupWeight=100,
        scanDepth=None,
        caseSensitive=None,
        matchWholeWords=None,
        useGroupScoring=None,
        automationId="",
        role=None,
    )


def main() -> None:
    raw = SOURCE.read_text(encoding="utf-8")
    pattern = re.compile(r"^## (崇祯.+?)\n\n```text\n([\s\S]*?)\n```", flags=re.MULTILINE)
    entries: OrderedDict[str, OrderedDict] = OrderedDict()
    for offset, match in enumerate(pattern.finditer(raw), start=1):
        title = match.group(1).strip()
        block = match.group(2).strip()
        year_match = re.search(r"(\d{4})", title)
        reign_match = re.search(r"崇祯([一二三四五六七八九十元]+)年", title)
        keys = [title]
        if year_match:
            keys.append(year_match.group(1))
        if reign_match:
            keys.append(f"崇祯{reign_match.group(1)}年")
        keys.extend(["开局剧本", "Author Note", "状态快照"])
        uid = 9200 + offset
        entries[str(uid)] = new_entry(uid, keys, f"开局剧本 {title}", f"【开局剧本：{title}】\n{block}", 760 + offset)

    OUT.write_text(json.dumps(OrderedDict(entries=entries), ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(entries)} entries to {OUT}")


if __name__ == "__main__":
    main()
