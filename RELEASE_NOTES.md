# 崇祯历史模拟器 v1-ready 发布说明

更新时间：2026-05-15

## 一键使用

最直接的入口是：

- `dist/chongzhen-sillytavern-bundle.zip`
- `sillytavern/最终一键复制包_崇祯历史模拟器.md`
- `sillytavern/崇祯模拟器_Narrator角色卡.json`
- `sillytavern/import/崇祯历史模拟器_完整Lorebook.json`

推荐流程：

1. 在 SillyTavern 导入 Narrator 角色卡。
2. 导入完整 Lorebook。
3. 把 `saves/开局存档/` 中某个年份的 Markdown 复制进 Author's Note。
4. 使用 `sillytavern/玩家指令模板.md` 发起第一回合。

## 当前包内容

- 41 个历史模拟规则模块。
- 32 张人物角色卡 JSON。
- 32 份人物 Markdown 卡。
- 6 个 Lorebook JSON。
- 108 个完整 Lorebook 条目。
- 6 个开局 Author's Note 存档。
- 地区、军队、派系快速卡。
- 玩家指令模板。
- 完成度审计、导入指南、发布包说明。
- 可复现构建脚本和 GitHub Actions 校验。

## 最近完成的关键增强

- 发布 ZIP 已纳入 Git，并由校验脚本检查内容。
- 人物卡从 20 张扩展到 32 张，新增王承恩、李邦华、倪元璐、史可法、曹文诏、左良玉、高迎祥、张献忠、范文程、多尔衮、孔有德、毛文龙。
- 完整 Lorebook 条目从 96 条扩展到 108 条。
- 新增 `sillytavern/玩家指令模板.md`，覆盖开局、诏书、回合结算、严格模式、轻量输出、切换开局和记忆修正。
- 新增 `docs/project_completion_audit.md`，列明当前完成度、人物覆盖、资料判断规则和已知边界。
- 新增 `.github/workflows/validate.yml`，push 和 pull request 时自动构建并校验。

## 校验命令

```powershell
powershell -ExecutionPolicy Bypass -File scripts\build_all.ps1
python scripts\validate_project.py
```

当前本地校验结果：

```text
OK: modules=41, characters=32, opening_saves=6, complete_lorebook_entries=108
```

