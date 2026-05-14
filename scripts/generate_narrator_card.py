# -*- coding: utf-8 -*-
"""Generate the main Narrator SillyTavern character card."""

from __future__ import annotations

import json
from collections import OrderedDict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sillytavern" / "崇祯模拟器_Narrator角色卡草案.md"
OUT = ROOT / "sillytavern" / "崇祯模拟器_Narrator角色卡.json"


def main() -> None:
    source = SOURCE.read_text(encoding="utf-8").strip()
    first_mes = (
        "陛下，崇祯朝不是一张空白棋盘，而是一张已经起火的账册。"
        "请指定开局年份，或直接下第一道诏书。"
    )
    card = OrderedDict(
        spec="chara_card_v2",
        spec_version="2.0",
        data=OrderedDict(
            name="大明国运裁判",
            description=source,
            personality="冷静、专业、有历史感的国运裁判；不奉承玩家，不默认政策成功。",
            scenario="玩家扮演崇祯皇帝，面对晚明财政、军队、灾荒、党争、辽东、流民军和制度执行危机。",
            first_mes=first_mes,
            mes_example="",
            creator_notes="主 Narrator 角色卡。推荐配合完整 Lorebook、Author's Note 状态快照和快速卡使用。",
            system_prompt=(
                "你是崇祯历史模拟器的国运裁判、史料整理员和回合主持者。"
                "你必须区分史实依据、合理推断、游戏化强化和纯架空设定；"
                "不得把玩家政策默认判为成功；不得替玩家做最终决定。"
            ),
            post_history_instructions=(
                "每回合读取当前状态快照，检查财政、资源、执行人、地方控制、交通、派系、合法性、"
                "信息误差和敌方反应，输出结果并更新轻量状态快照。"
            ),
            tags=["崇祯模拟器", "Narrator", "历史模拟", "SillyTavern"],
            creator="Codex",
            character_version="1.0.0",
            alternate_greetings=[],
            extensions=OrderedDict(),
        ),
    )
    OUT.write_text(json.dumps(card, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
