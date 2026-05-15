# 构建报告

生成时间：2026-05-15T22:37:08

## 数量统计

- 模块：41
- 人物 JSON：32
- 人物 Markdown：32
- 开局存档：7
- 完整 Lorebook 条目：121
- 快速卡 Lorebook 条目：22
- 人物 Lorebook 条目：32
- 开局剧本 Lorebook 条目：7
- 资料规则 Lorebook 条目：4

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
powershell -ExecutionPolicy Bypass -File scripts\build_all.ps1
python scripts\validate_project.py
python scripts\check_release_bundle.py
```

## 当前校验基线

- 41 个编号模块。
- 32 张人物 JSON 卡与 32 张人物 Markdown 卡。
- 7 个开局存档。
- 7 个 Lorebook JSON。
- 完整 Lorebook 至少 121 条。
- 发布 ZIP 含最终复制包、角色卡、人物卡、开局存档、回合日志模板、群聊预设、资料规则和 docs。
