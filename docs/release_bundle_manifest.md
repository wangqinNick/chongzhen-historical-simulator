# 发布包说明

发布包位于 `dist/chongzhen-sillytavern-bundle.zip`，解压后可以直接按目录导入或复制。

## 包内核心文件

- `sillytavern/最终一键复制包_崇祯历史模拟器.md`：完整复制版。
- `sillytavern/导入清单.md`：导入顺序和文件列表。
- `sillytavern/崇祯模拟器_Narrator角色卡.json`：SillyTavern 角色卡 JSON。
- `sillytavern/import/`：6 个 Lorebook JSON。
- `sillytavern/人物卡/json/`：20 个可导入人物角色卡。
- `sillytavern/人物卡/markdown/`：人物卡可读版本。
- `sillytavern/快速卡/`：地区、军队、派系快速卡。
- `saves/开局存档/`：6 个开局 Author's Note 快照。
- `research/`：资料登记、来源目录和可信度依据。
- `modules/module_index.json`：41 个模块索引。
- `docs/`：导入指南和发布包说明。

## 重新生成

在仓库根目录运行：

```powershell
powershell -ExecutionPolicy Bypass -File scripts\build_all.ps1
```

脚本会重新生成角色卡、人物卡、快速卡、开局剧本、完整 Lorebook、最终复制包、包清单和发布 ZIP，并执行项目校验。

## 校验

单独校验可运行：

```powershell
python scripts\validate_project.py
```

校验项包括：

- 41 个编号模块存在。
- 至少 20 个 JSON 人物卡和 20 个 Markdown 人物卡存在。
- 至少 6 个开局存档存在。
- Narrator 与人物卡符合 `chara_card_v2`。
- Lorebook JSON 均含 entries。
- 完整 Lorebook 至少包含 96 个条目。
- 发布 ZIP 存在且包含导入目录、人物卡、最终复制包、开局存档和模块索引。

## 版本原则

每次修改资料、模块、人物或生成脚本后，都应运行构建脚本，让 `sillytavern/package_manifest.json`、最终复制包和发布 ZIP 同步更新。

