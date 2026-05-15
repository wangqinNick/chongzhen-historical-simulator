# SillyTavern-崇祯模拟器

用于搭建 SillyTavern 崇祯历史模拟器的模块化文件结构。Agent 可根据此 JSON 创建 GitHub 仓库、目录和 Markdown 文件。

最短入口：先读 `START_HERE.md`。

## 推荐仓库名

sillytavern-chongzhen-simulator

## 语言

zh-CN

## 默认原则

- 默认使用中文。
- 本项目相关回答默认先查资料，包括历史文献、论文、论坛、SillyTavern 社区资料和网络资料。
- 所有重要人物、派系、地区、军队、政策、资源、装备、科技、战役尽量数值化。
- 必须区分史实基础、合理推演、游戏化强化和纯架空设定。
- 人物、派系、地区、军队、衙门、商帮、宗室、敌国都应视为半自主代理人。
- 政策不得默认成功，必须经过财政、资源、执行人、地方、交通、派系、合法性、信息误差等系统检验。
- 记忆维护采用轻量状态快照，只记录会影响未来决策的变化。
- SillyTavern 落地时，稳定设定进 Character Card，可触发规则进 Lorebook，当前状态进 Author's Note，长资料进 Data Bank/RAG。

## 目录

- project_instructions/：可复制到 ChatGPT Project Instructions 的总纲。
- modules/：41 个核心规则模块。
- sillytavern/：角色卡、Lorebook、Author's Note 和状态快照草案。
- sillytavern/快速卡/：地区、军队、派系快速卡，可导入 Lorebook 或放入 Data Bank。
- templates/：人物、地区、军队、政策、科技、日志等模板。
- research/：史料、论文、检索关键词和可信度记录。
- saves/：回合日志、状态快照、政策执行结果和存档。
- docs/：SillyTavern 导入指南、发布包说明和使用排错。

## 模块索引

- [01 崇祯模拟器 总规则](modules/01_崇祯模拟器_总规则.md) - P0 / v1-ready
- [02 人物价值观数值系统](modules/02_人物价值观数值系统.md) - P0 / v1-ready
- [03 人物实际能力与成长系统](modules/03_人物实际能力与成长系统.md) - P0 / v1-ready
- [04 人物决策心理、声望、身份与信息系统](modules/04_人物决策心理_声望_身份_信息系统.md) - P0 / v1-ready
- [05 国家财政与税收系统](modules/05_国家财政与税收系统.md) - P0 / v1-ready
- [06 军队、战役、后勤、装备系统](modules/06_军队_战役_后勤_装备系统.md) - P0 / v1-ready
- [07 地方治理、省府州县控制系统](modules/07_地方治理_省府州县控制系统.md) - P1 / v1-ready
- [08 灾荒、气候、瘟疫、民变系统](modules/08_灾荒_气候_瘟疫_民变系统.md) - P0 / v1-ready
- [09 朝廷制度、官僚流程、政策执行系统](modules/09_朝廷制度_官僚流程_政策执行系统.md) - P2 / v1-ready
- [10 派系、士绅、宗藩、商帮系统](modules/10_派系_士绅_宗藩_商帮系统.md) - P1 / v1-ready
- [11 科技树、军工、西学、工业化系统](modules/11_科技树_军工_西学_工业化系统.md) - P0 / v1-ready
- [12 外交、藩属、海贸、外夷系统](modules/12_外交_藩属_海贸_外夷系统.md) - P1 / v1-ready
- [13 情报、舆论、锦衣卫、东厂系统](modules/13_情报_舆论_锦衣卫_东厂系统.md) - P1 / v1-ready
- [14 经济市场、物价、白银流通系统](modules/14_经济市场_物价_白银流通系统.md) - P2 / v1-ready
- [15 事件引擎、回合推进、因果链系统](modules/15_事件引擎_回合推进_因果链系统.md) - P0 / v1-ready
- [16 SillyTavern 轻量记忆维护、状态快照系统](modules/16_SillyTavern轻量记忆维护_状态快照系统.md) - P0 / v1-ready
- [17 诏书、政策、回合总结输出模板](modules/17_诏书_政策_回合总结输出模板.md) - P0 / v1-ready
- [18 史料库、检索关键词、可信度规则](modules/18_史料库_检索关键词_可信度规则.md) - P0 / v1-ready
- [19 人口、户籍、劳动力、兵源系统](modules/19_人口_户籍_劳动力_兵源系统.md) - P1 / v1-ready
- [20 合法性、天命、皇权威望、政治信用系统](modules/20_合法性_天命_皇权威望_政治信用系统.md) - P1 / v1-ready
- [21 地图空间、交通、距离、补给线系统](modules/21_地图空间_交通_距离_补给线系统.md) - P1 / v1-ready
- [22 组织惯性、制度路径依赖、改革阻力系统](modules/22_组织惯性_制度路径依赖_改革阻力系统.md) - P2 / v1-ready
- [23 法律、刑罚、司法、恐怖统治副作用系统](modules/23_法律_刑罚_司法_恐怖统治副作用系统.md) - P2 / v1-ready
- [24 文化、宗教、意识形态、士论系统](modules/24_文化_宗教_意识形态_士论系统.md) - P2 / v1-ready
- [25 人才培养、教育、科举、技术学校系统](modules/25_人才培养_教育_科举_技术学校系统.md) - P1 / v1-ready
- [26 自然资源、生产力、产能、供应链系统](modules/26_自然资源_生产力_产能_供应链系统.md) - P0 / v1-ready
- [27 胜利条件、失败条件、评分系统](modules/27_胜利条件_失败条件_评分系统.md) - P2 / v1-ready
- [28 AI 裁判、难度、随机性、作弊限制系统](modules/28_AI裁判_难度_随机性_作弊限制系统.md) - P0 / v1-ready
- [29 玩家角色、皇帝心理、决策成本系统](modules/29_玩家角色_皇帝心理_决策成本系统.md) - P2 / v1-ready
- [30 元规则、版本更新、数值平衡、回滚系统](modules/30_元规则_版本更新_数值平衡_回滚系统.md) - P2 / v1-ready
- [31 职位职责、自动执行、生产调度系统](modules/31_职位职责_自动执行_生产调度系统.md) - P0 / v1-ready
- [32 装备、库存、损耗、维护系统](modules/32_装备_库存_损耗_维护系统.md) - P0 / v1-ready
- [33 库存流量、资源守恒、账本系统](modules/33_库存流量_资源守恒_账本系统.md) - P0 / v1-ready
- [34 任务队列、优先级、执行容量系统](modules/34_任务队列_优先级_执行容量系统.md) - P0 / v1-ready
- [35 敌方 AI、外部势力、自动行动系统](modules/35_敌方AI_外部势力_自动行动系统.md) - P0 / v1-ready
- [36 初始剧本、基准数值、开局盘点系统](modules/36_初始剧本_基准数值_开局盘点系统.md) - P0 / v1-ready
- [37 数值校准、难度、现实性检查系统](modules/37_数值校准_难度_现实性检查系统.md) - P2 / v1-ready
- [38 失败模式、风险事件、反噬库](modules/38_失败模式_风险事件_反噬库.md) - P1 / v1-ready
- [39 玩家情报界面、奏报、误报系统](modules/39_玩家情报界面_奏报_误报系统.md) - P1 / v1-ready
- [40 存档、回合日志、版本管理系统](modules/40_存档_回合日志_版本管理系统.md) - P2 / v1-ready
- [41 官僚层级、地方官、基层执行抽象系统](modules/41_官僚层级_地方官_基层执行抽象系统.md) - P0 / v1-ready

## 模板索引

- [人物完整卡模板](templates/人物完整卡模板.md)
- [人物简化卡模板](templates/人物简化卡模板.md)
- [地区状态卡模板](templates/地区状态卡模板.md)
- [军队基础卡模板](templates/军队基础卡模板.md)
- [政策执行卡模板](templates/政策执行卡模板.md)
- [科技项目卡模板](templates/科技项目卡模板.md)
- [状态快照模板](templates/状态快照模板.md)
- [回合日志模板](templates/回合日志模板.md)
- [Lorebook条目模板](templates/Lorebook条目模板.md)
- [AuthorNote模板](templates/AuthorNote模板.md)

## SillyTavern 文件

- [崇祯模拟器_Narrator角色卡草案](sillytavern/崇祯模拟器_Narrator角色卡草案.md)
- [崇祯模拟器_Narrator角色卡 JSON](sillytavern/崇祯模拟器_Narrator角色卡.json)
- [核心规则_Lorebook草案](sillytavern/核心规则_Lorebook草案.md)
- [当前状态_AuthorNote模板](sillytavern/当前状态_AuthorNote模板.md)
- [轻量状态快照模板](sillytavern/轻量状态快照模板.md)
- [一键复制版_崇祯模拟器](sillytavern/一键复制版_崇祯模拟器.md)
- [玩家指令模板](sillytavern/玩家指令模板.md)
- [人物卡索引](sillytavern/人物卡/README.md)
- [SillyTavern 导入清单](sillytavern/导入清单.md)

## 快速使用

最省事：打开 `sillytavern/最终一键复制包_崇祯历史模拟器.md`，按文件内顺序复制角色卡、Author's Note、状态快照和 Data Bank 资料。

推荐：在 SillyTavern 的 World Info / Lorebook 页面导入 `sillytavern/import/崇祯历史模拟器_完整Lorebook.json`，它包含核心规则、41 个模块条目、快速卡、资料规则、开局剧本和首批人物条目。

详细导入：`docs/sillytavern_import_guide.md` 说明一键复制、完整 Lorebook、轻量核心规则三种使用方式，以及人物卡、开局存档和常见问题处理。

玩家指令：`sillytavern/玩家指令模板.md` 可直接复制到聊天框，用于开局盘点、标准诏书、回合结算、严格模式和切换开局。

首回合样例：`sillytavern/回合样例/开局首回合样例.md` 覆盖 7 个开局年份，可直接复制到 SillyTavern 测试 Narrator 裁判路径。

群聊预设：`sillytavern/群聊预设/推荐群聊组合.md` 提供不同剧本的 Group Chat 人物组合，避免一次导入全部角色导致上下文失控。

完成度审计：`docs/project_completion_audit.md` 汇总模块、人物卡、Lorebook、开局存档、发布包和校验标准。

资料可信度：`research/source_reliability_guide.md` 定义史料原文、学术整理、馆藏网页、网络索引和模拟器采用值的使用边界。

资料规则 Lorebook：`sillytavern/import/崇祯历史模拟器_资料规则Lorebook.json` 可单独导入，也已合并入完整 Lorebook。

快速局势：`sillytavern/快速卡/地区军队派系卡.md` 提供京师、辽东、陕西、河南、江南、山东登莱、宣大蓟镇、关宁军、京营、卫所、剿贼官军、东林士论、阉党清算、商帮海商等高频卡，适合放进 Data Bank 或导入快速卡 Lorebook。

补充快速卡：`data/quick_cards_extra.json` 会生成 `sillytavern/快速卡/补充地区军队派系卡.md`，覆盖南京南直隶、湖广、四川、山西、闽粤海贸、漕运、宗藩和驿传塘报。

多角色：把 `sillytavern/人物卡/json/` 下的人物 JSON 逐个导入 SillyTavern，可用于 Group Chat；单 Narrator 模式则导入 `sillytavern/import/崇祯历史模拟器_人物Lorebook.json` 即可。

轻量：打开 `sillytavern/一键复制版_崇祯模拟器.md`，复制“整段复制版”到 SillyTavern 角色卡 Description / System Prompt 类字段，再复制 Author's Note 初始状态到当前聊天的 Author's Note。

更稳：角色卡使用 `崇祯模拟器_Narrator角色卡草案.md`，World Info / Lorebook 使用 `核心规则_Lorebook草案.md` 的分条触发词，当前状态使用 `当前状态_AuthorNote模板.md`。

修改后校验：运行 `python scripts/validate_project.py` 和 `python scripts/check_release_bundle.py`，确认模块数量、人物卡数量、Lorebook JSON、最终复制包和发布 ZIP 都完整。

一键构建：运行 `powershell -ExecutionPolicy Bypass -File scripts/build_all.ps1`，会依次生成 Narrator、人物卡、快速卡、开局剧本、完整 Lorebook、最终复制包并执行校验。

开局测试：使用 `saves/开局测试用例.md` 中的 6 组提示验证开局、辽东、财政、剿抚、西学和崇祯十四年救火局。

开局存档：`saves/开局存档/` 已生成 7 个年份的 Author's Note 快照和 JSON 存档，可直接复制开跑，覆盖 1628、1629、1631、1634、1637、1641、1644。

包清单：`sillytavern/package_manifest.json` 记录当前包的主要文件、条目数量和 SHA-256，用于导入前核对。

模块导航：`modules/module_index.json` 和 `modules/模块依赖图.md` 记录 41 个模块的状态、优先级和依赖关系。

发布包：`dist/chongzhen-sillytavern-bundle.zip` 汇总了最终复制包、导入清单、Lorebook、Narrator、人物卡、快速卡、开局存档和资料登记表。

发布说明：`docs/release_bundle_manifest.md` 记录发布包内容、重新生成命令和校验范围。

版本说明：`RELEASE_NOTES.md` 汇总当前 v1-ready 包的入口文件、数量统计和最近增强。
