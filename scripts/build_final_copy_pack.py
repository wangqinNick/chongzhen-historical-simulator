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


def main() -> None:
    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    one_copy = read("sillytavern/一键复制版_崇祯模拟器.md")
    narrator = read("sillytavern/崇祯模拟器_Narrator角色卡草案.md")
    author_note = read("sillytavern/当前状态_AuthorNote模板.md")
    snapshot = read("sillytavern/轻量状态快照模板.md")
    core_lore = read("sillytavern/核心规则_Lorebook草案.md")
    baseline = read("research/baseline_data_register.md")
    sources = read("research/source_catalog.md")
    modules = all_modules_text()

    content = f"""# 最终一键复制包：崇祯历史模拟器

生成时间：{generated_at}

本文件是给 SillyTavern 使用的最终整合包。推荐顺序：

1. 在 SillyTavern 新建角色，角色名填“大明国运裁判”或“崇祯历史模拟器 Narrator”。
2. 把“01 角色卡 / System Prompt”复制到角色卡 Description、System Prompt 或同类高优先级字段。
3. 把“02 Author's Note 初始状态”复制到当前聊天的 Author's Note。
4. 在 World Info / Lorebook 页面导入 `sillytavern/import/崇祯历史模拟器_全模块Lorebook.json`。如果不导入 JSON，就把“03 核心 Lorebook 手工条目”逐条复制进去。
5. 把“04 全模块资料包”放进 Data Bank / RAG，或作为长资料另存后让模型检索。
6. 开局时发送：“按崇祯元年剧本开局，先给我国势盘点和第一回合可选诏书。”

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

## 03 核心 Lorebook 手工条目

如果你不能导入 JSON，就把这些条目按触发词拆成 World Info / Lorebook。

~~~~text
{core_lore}
~~~~

## 04 全模块资料包

建议放入 Data Bank / RAG。不要整段塞进角色卡，否则上下文会过载。SillyTavern 的 World Info 负责动态触发，Data Bank/RAG 负责长资料检索。

~~~~text
{modules}
~~~~

## 05 已采用基准数据

这些数据已经进入模拟器。新数据必须继续按同样口径登记。

~~~~text
{baseline}
~~~~

## 06 资料来源与后续检索

所有史料、论文、网络资料与可信度限制汇总在这里。

~~~~text
{sources}
~~~~
"""

    OUT.write_text(content, encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
