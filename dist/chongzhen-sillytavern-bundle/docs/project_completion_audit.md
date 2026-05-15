# 项目完成度审计

更新时间：2026-05-15

本审计用于确认当前仓库已经具备 SillyTavern 可落地使用的完整包，而不是只有模块草稿。

## 当前结论

项目当前状态为 `v1-ready`。它已经可以用三种方式进入 SillyTavern：

- 复制 `sillytavern/最终一键复制包_崇祯历史模拟器.md`。
- 导入 `sillytavern/崇祯模拟器_Narrator角色卡.json` 加 `sillytavern/import/崇祯历史模拟器_完整Lorebook.json`。
- 使用 `dist/chongzhen-sillytavern-bundle.zip` 解压后的发布包。

## 已完成内容

| 类别 | 文件/目录 | 当前数量 | 状态 |
|---|---:|---:|---|
| 核心模块 | `modules/*.md` | 41 | 已完成 v1 |
| 模块索引 | `modules/module_index.json` | 1 | 已生成 |
| 模块依赖图 | `modules/模块依赖图.md` | 1 | 已生成 |
| Narrator 角色卡 | `sillytavern/崇祯模拟器_Narrator角色卡.json` | 1 | 可导入 |
| 人物角色卡 JSON | `sillytavern/人物卡/json/` | 32 | 可导入 |
| 人物角色卡 Markdown | `sillytavern/人物卡/markdown/` | 32 | 可读可复制 |
| Lorebook JSON | `sillytavern/import/` | 6 | 可导入 |
| 完整 Lorebook 条目 | `崇祯历史模拟器_完整Lorebook.json` | 108 | 已整合 |
| 快速卡 | `sillytavern/快速卡/` | 2 | 已完成 |
| 开局存档 | `saves/开局存档/` | 6 | 可复制 Author's Note |
| 玩家指令 | `sillytavern/玩家指令模板.md` | 1 | 可直接复制 |
| 最终复制包 | `sillytavern/最终一键复制包_崇祯历史模拟器.md` | 1 | 可直接复制 |
| 发布 ZIP | `dist/chongzhen-sillytavern-bundle.zip` | 1 | 已纳入 Git |
| 构建脚本 | `scripts/build_all.ps1` | 1 | 一键生成 |
| 校验脚本 | `scripts/validate_project.py` | 1 | 一键检查 |

## 人物覆盖

当前 32 人覆盖了以下功能位：

- 皇帝与内廷：崇祯、曹化淳、王承恩。
- 内阁与财政：周延儒、温体仁、毕自严、杨嗣昌。
- 士林与清议：钱谦益、李邦华、倪元璐、史可法。
- 辽东与边将：袁崇焕、祖大寿、孙承宗、洪承畴、吴三桂、毛文龙。
- 剿贼与强镇：卢象升、孙传庭、曹文诏、左良玉、陈奇瑜。
- 西学与技术：徐光启、孙元化、宋应星。
- 流民军：李自成、高迎祥、张献忠。
- 后金/清：皇太极、范文程、多尔衮、孔有德。

## 快速卡覆盖

当前快速卡覆盖：

- 地区：京师与北直隶、辽东与关宁锦、陕西、西北灾荒带、河南、江南、山东登莱、宣大蓟镇、南京与南直隶、湖广襄阳荆州、四川、山西、福建广东海贸。
- 军队：关宁军、京营、卫所军与地方守备、剿贼官军。
- 派系/制度：东林与江南士论、阉党余波与反阉清算、商帮与海商网络、漕运与通州仓储、宗藩与宗禄、驿传塘报与信息延迟。

补充快速卡由 `data/quick_cards_extra.json` 生成，便于后续继续扩展地区、军队和制度节点。

## 资料与判断规则

项目要求每个重要数据都区分依据类型：

- 史实基础：来自《明史》、制度资料、博物馆资料、古籍或可追溯史料。
- 论文整理：来自气候、灾荒、财政、农民战争、明清易代等研究。
- 网络索引：用于快速定位人物、年份和事件线索，不作为最终高可信终点。
- 合理推断：用于把史实转成可玩的代理人行为、风险等级和执行难度。
- 游戏化采用值：用于 SillyTavern 回合裁判，不等同于史实精确数值。

## 已知边界

- v1 不是数值游戏引擎，仍依靠 Narrator 按规则裁判。
- 兵额、粮价、财政数值已有基准，但很多区域细项仍需按地方志和专题论文继续校勘。
- Group Chat 可用，但推荐先用单 Narrator 加人物 Lorebook 稳定游玩。
- 人物卡数值是模拟器采用值，代表倾向和风险，不代表史学定论。

## 复核命令

```powershell
powershell -ExecutionPolicy Bypass -File scripts\build_all.ps1
python scripts\validate_project.py
```

当前通过标准：

- 41 个模块齐全。
- 32 个 JSON 人物卡与 32 个 Markdown 人物卡齐全。
- 人物 JSON 均为 `chara_card_v2`，并含资料来源、史实要点和触发词。
- 6 个开局存档齐全。
- 完整 Lorebook 含 108 个条目。
- 发布 ZIP 含导入文件、人物卡、快速卡、玩家指令、开局存档、模块索引和 docs。
