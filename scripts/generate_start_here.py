# -*- coding: utf-8 -*-
"""Generate a human-facing start-here index for all usable SillyTavern artifacts."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "START_HERE.md"


def main() -> None:
    generated_at = datetime.now().isoformat(timespec="seconds")
    content = f"""# 从这里开始

生成时间：{generated_at}

这是崇祯历史模拟器的最短入口页。你不需要先读完全部模块，按自己的使用方式选一条路径即可。

## 只想马上开局

1. 打开 `sillytavern/最终一键复制包_崇祯历史模拟器.md`。
2. 按文件内顺序复制角色卡、Author's Note、玩家指令。
3. 首句可发送：`按崇祯元年剧本开局，先给我国势盘点和第一回合可选诏书。`

## 推荐导入方式

1. 导入角色卡：`sillytavern/崇祯模拟器_Narrator角色卡.json`
2. 导入完整 Lorebook：`sillytavern/import/崇祯历史模拟器_完整Lorebook.json`
3. 复制开局 Author's Note：`saves/开局存档/`
4. 使用玩家模板：`sillytavern/玩家指令模板.md`

## 轻量方式

1. 导入角色卡：`sillytavern/崇祯模拟器_Narrator角色卡.json`
2. 只导入核心 Lorebook：`sillytavern/import/崇祯历史模拟器_核心Lorebook.json`
3. 把快速卡放入 Data Bank：`sillytavern/快速卡/`
4. 需要人物时再导入：`sillytavern/import/崇祯历史模拟器_人物Lorebook.json`

## 多角色群聊

1. 先读：`sillytavern/群聊预设/推荐群聊组合.md`
2. 按剧本导入少量人物：`sillytavern/人物卡/json/`
3. 保持 Narrator 作为总裁判，人物只负责立场、建议、阻力和反应。

## 发布包

完整发布包：

`dist/chongzhen-sillytavern-bundle.zip`

检查发布包：

```powershell
python scripts\\check_release_bundle.py
```

## 当前内容规模

- 41 个模块。
- 32 张人物 JSON 卡。
- 32 张人物 Markdown 卡。
- 7 个 Lorebook JSON。
- 121 条完整 Lorebook 条目。
- 7 个开局存档。
- 7 个首回合样例。
- 1 个群聊预设文件。
- 1 个状态字段字典。
- 1 个回合日志模板。
- 1 个发布 ZIP。

## 继续扩展时

运行：

```powershell
powershell -ExecutionPolicy Bypass -File scripts\\build_all.ps1
```

它会重建角色卡、人物卡、快速卡、开局剧本、完整 Lorebook、最终复制包、包清单和发布 ZIP，并自动校验。

## 遇到问题

先看：

`docs/sillytavern_troubleshooting.md`
"""
    OUT.write_text(content, encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
