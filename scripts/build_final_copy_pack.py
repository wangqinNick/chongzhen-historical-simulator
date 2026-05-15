# -*- coding: utf-8 -*-
"""Build the final copy-and-paste SillyTavern package."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "sillytavern" / "最终一键复制包_崇祯历史模拟器.md"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8").strip()


def all_modules_text() -> str:
    chunks: list[str] = []
    for path in sorted((ROOT / "modules").glob("*.md"), key=lambda p: p.name):
        chunks.append(f"\n\n===== {path.name} =====\n\n{path.read_text(encoding='utf-8').strip()}")
    return "".join(chunks).strip()


def all_character_cards_text() -> str:
    char_dir = ROOT / "sillytavern" / "人物卡" / "markdown"
    if not char_dir.exists():
        return "未检测到人物卡文件；请先运行 scripts/generate_character_cards.py。"
    chunks: list[str] = []
    for path in sorted(char_dir.glob("*.md"), key=lambda p: p.name):
        chunks.append(f"\n\n===== {path.name} =====\n\n{path.read_text(encoding='utf-8').strip()}")
    return "".join(chunks).strip()


def quick_cards_text() -> str:
    quick_dir = ROOT / "sillytavern" / "快速卡"
    if not quick_dir.exists():
        return "未检测到快速卡文件。"
    chunks: list[str] = []
    for path in sorted(quick_dir.glob("*.md"), key=lambda p: p.name):
        chunks.append(f"\n\n===== {path.name} =====\n\n{path.read_text(encoding='utf-8').strip()}")
    return "".join(chunks).strip()


def main() -> None:
    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    one_copy = read("sillytavern/一键复制版_崇祯模拟器.md")
    narrator = read("sillytavern/崇祯模拟器_Narrator角色卡草案.md")
    author_note = read("sillytavern/当前状态_AuthorNote模板.md")
    scenario_notes = read("sillytavern/开局剧本_AuthorNote合集.md")
    player_prompts = read("sillytavern/玩家指令模板.md")
    turn_examples = read("sillytavern/回合样例/开局首回合样例.md")
    group_presets = read("sillytavern/群聊预设/推荐群聊组合.md")
    turn_log_template = read("saves/回合日志/回合日志_可复制模板.md")
    snapshot = read("sillytavern/轻量状态快照模板.md")
    core_lore = read("sillytavern/核心规则_Lorebook草案.md")
    quick_cards = quick_cards_text()
    character_cards = all_character_cards_text()
    baseline = read("research/baseline_data_register.md")
    sources = read("research/source_catalog.md")
    source_reliability = read("research/source_reliability_guide.md")
    state_dictionary = read("docs/state_field_dictionary.md")
    modules = all_modules_text()

    content = f"""# 最终一键复制包：崇祯历史模拟器

生成时间：{generated_at}

本文件是给 SillyTavern 使用的最终整合包。推荐顺序：

1. 在 SillyTavern 新建角色，角色名填“大明国运裁判”或“崇祯历史模拟器 Narrator”。
2. 把“01 角色卡 / System Prompt”复制到角色卡 Description、System Prompt 或同类高优先级字段。
3. 把“02 Author's Note 初始状态”复制到当前聊天的 Author's Note。
4. 在 World Info / Lorebook 页面导入 `sillytavern/import/崇祯历史模拟器_完整Lorebook.json`。如果只想轻量导入，可以用 `核心Lorebook` 或 `全模块Lorebook`。
5. 如需多角色群聊，把 `sillytavern/人物卡/json/` 下的角色卡逐个导入 SillyTavern。
6. 把“05 快速卡资料包”“06 全模块资料包”和“07 人物卡资料包”放进 Data Bank / RAG，或作为长资料另存后让模型检索。
7. 开局时发送：“按崇祯元年剧本开局，先给我国势盘点和第一回合可选诏书。”

## 01 角色卡 / System Prompt

优先使用下面这一块。它已经包含可直接开局的完整提示。

~~~~text
{one_copy}
~~~~

## 01A 角色卡拆分版

如果你更喜欢拆分角色卡字段，可以用这一版作为 Description / Personality / Scenario 的来源。

~~~~text
{narrator}
~~~~

## 02 Author's Note 初始状态

复制到当前聊天的 Author's Note。每回合结束后只改这里的当前状态，不要把长期规则塞进 Author's Note。

~~~~text
{author_note}
~~~~

## 02A 回合状态快照模板

每回合结束后，用此模板压缩记忆。

~~~~text
{snapshot}
~~~~

## 02B 多年份开局 Author's Note

如果你不从崇祯元年开局，复制对应年份的 Author's Note。

~~~~text
{scenario_notes}
~~~~

## 02C 玩家指令模板

这些模板可直接复制到 SillyTavern 聊天框，用于开局盘点、标准诏书、回合结算、严格模式和切换开局。

~~~~text
{player_prompts}
~~~~

## 02D 开局首回合样例

这些样例可用于测试不同年份开局，帮助 Narrator 按正确检查项进入首回合。

~~~~text
{turn_examples}
~~~~

## 02E 群聊预设组合

如果使用 SillyTavern Group Chat，按剧本选择少量人物，不要一次导入全部角色。

~~~~text
{group_presets}
~~~~

## 02F 回合日志模板

长期存档时，每回合结束后用这一段归档，不要把整段聊天原文全部塞回长期记忆。

~~~~text
{turn_log_template}
~~~~

## 03 核心 Lorebook 手工条目

如果你不能导入 JSON，就把这些条目按触发词拆成 World Info / Lorebook。

~~~~text
{core_lore}
~~~~

## 04 快速卡资料包

这些是高频地区、军队和派系卡。建议先放入 Data Bank / RAG，也可拆成 Lorebook 条目。

~~~~text
{quick_cards}
~~~~

## 05 全模块资料包

建议放入 Data Bank / RAG。不要整段塞进角色卡，否则上下文会过载。SillyTavern 的 World Info 负责动态触发，Data Bank/RAG 负责长资料检索。

~~~~text
{modules}
~~~~

## 06 人物卡资料包

可作为 Data Bank / RAG 长资料，也可按 `sillytavern/人物卡/json/` 逐个导入为 SillyTavern 角色卡。

~~~~text
{character_cards}
~~~~

## 07 已采用基准数据

这些数据已经进入模拟器。新数据必须继续按同样口径登记。

~~~~text
{baseline}
~~~~

## 08 资料来源与后续检索

所有史料、论文、网络资料与可信度限制汇总在这里。

~~~~text
{sources}
~~~~

## 09 资料可信度与引用口径

当模型开始把网络索引当史实、把模拟器数值当史学定论时，优先使用这一段约束。

~~~~text
{source_reliability}
~~~~

## 10 状态字段字典

长期游玩时用这一段统一 Author's Note、回合日志和开局存档里的字段含义。

~~~~text
{state_dictionary}
~~~~
"""

    OUT.write_text(content, encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
