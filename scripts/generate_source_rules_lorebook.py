# -*- coding: utf-8 -*-
"""Generate a small Lorebook for source reliability and citation discipline."""

from __future__ import annotations

import json
from collections import OrderedDict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_PATH = ROOT / "sillytavern" / "import" / "崇祯历史模拟器_资料规则Lorebook.json"


SOURCE_RULES = [
    {
        "uid": 8800,
        "keys": ["依据", "来源", "史料", "论文", "网络资料", "可信度", "引用", "考证"],
        "comment": "资料可信度分层",
        "content": (
            "【资料可信度分层】Narrator 必须区分五类依据："
            "A 级为史料原文或权威馆藏说明；B 级为学术论文、专著和数据库整理；"
            "C 级为博物馆、大学、研究机构网页；D 级为百科、专题站、年表、论坛等网络索引；"
            "E 级为模拟器采用值。D 级不得单独支撑关键数值、重大人物评价或具体战役结论。"
        ),
    },
    {
        "uid": 8801,
        "keys": ["模拟器采用值", "合理推断", "数值", "人物数值", "灾荒等级", "风险等级"],
        "comment": "模拟器采用值边界",
        "content": (
            "【模拟器采用值边界】人物倾向、能力、灾荒等级、民变风险、执行阻力等是游戏裁判值，"
            "不是史学定论。输出时如被追问依据，必须说明其来自史实基础、学术整理、网络索引、"
            "合理推断还是游戏化采用值。可给区间和等级，不给假精确。"
        ),
    },
    {
        "uid": 8802,
        "keys": ["冲突", "史料冲突", "不同说法", "争议", "待复核", "校勘"],
        "comment": "来源冲突处理",
        "content": (
            "【来源冲突处理】如果资料冲突，先保留冲突，不强行抹平；标注各来源类型和可能立场；"
            "回合裁判采用更保守、更能解释执行成本的口径；并把待校勘项写入研究清单。"
        ),
    },
    {
        "uid": 8803,
        "keys": ["全知", "奏报", "误报", "塘报", "情报", "信息误差", "密报"],
        "comment": "资料与信息边界",
        "content": (
            "【资料与信息边界】玩家作为崇祯不能天然全知。奏报、塘报、战报、账册、密报都有延迟、"
            "筛选和失真。重要决策应区分奏报版、密报版和事后核实版。"
        ),
    },
]


def new_entry(rule: dict) -> OrderedDict:
    uid = rule["uid"]
    return OrderedDict(
        uid=uid,
        key=rule["keys"],
        keysecondary=[],
        comment=rule["comment"],
        content=rule["content"],
        constant=False,
        vectorized=False,
        selective=False,
        selectiveLogic=0,
        addMemo=True,
        order=240 + (uid - 8800),
        position=0,
        disable=False,
        excludeRecursion=False,
        preventRecursion=False,
        delayUntilRecursion=False,
        probability=100,
        useProbability=True,
        depth=4,
        group="资料规则",
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
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    entries = OrderedDict((str(rule["uid"]), new_entry(rule)) for rule in SOURCE_RULES)
    OUT_PATH.write_text(json.dumps(OrderedDict(entries=entries), ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(entries)} entries to {OUT_PATH}")


if __name__ == "__main__":
    main()

