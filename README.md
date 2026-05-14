# SillyTavern-崇祯模拟器

用于搭建 SillyTavern 崇祯历史模拟器的模块化文件结构。Agent 可根据此 JSON 创建 GitHub 仓库、目录和 Markdown 文件。

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
- templates/：人物、地区、军队、政策、科技、日志等模板。
- research/：史料、论文、检索关键词和可信度记录。
- saves/：回合日志、状态快照、政策执行结果和存档。

## 模块索引

- [01 崇祯模拟器 总规则](modules/01_崇祯模拟器_总规则.md) - P0 / draft
- [02 人物价值观数值系统](modules/02_人物价值观数值系统.md) - P0 / draft
- [03 人物实际能力与成长系统](modules/03_人物实际能力与成长系统.md) - P0 / draft
- [04 人物决策心理、声望、身份与信息系统](modules/04_人物决策心理_声望_身份_信息系统.md) - P0 / draft
- [05 国家财政与税收系统](modules/05_国家财政与税收系统.md) - P0 / draft
- [06 军队、战役、后勤、装备系统](modules/06_军队_战役_后勤_装备系统.md) - P0 / draft
- [07 地方治理、省府州县控制系统](modules/07_地方治理_省府州县控制系统.md) - P1 / draft
- [08 灾荒、气候、瘟疫、民变系统](modules/08_灾荒_气候_瘟疫_民变系统.md) - P0 / draft
- [09 朝廷制度、官僚流程、政策执行系统](modules/09_朝廷制度_官僚流程_政策执行系统.md) - P2 / draft
- [10 派系、士绅、宗藩、商帮系统](modules/10_派系_士绅_宗藩_商帮系统.md) - P1 / draft
- [11 科技树、军工、西学、工业化系统](modules/11_科技树_军工_西学_工业化系统.md) - P0 / draft
- [12 外交、藩属、海贸、外夷系统](modules/12_外交_藩属_海贸_外夷系统.md) - P1 / draft
- [13 情报、舆论、锦衣卫、东厂系统](modules/13_情报_舆论_锦衣卫_东厂系统.md) - P1 / draft
- [14 经济市场、物价、白银流通系统](modules/14_经济市场_物价_白银流通系统.md) - P2 / draft
- [15 事件引擎、回合推进、因果链系统](modules/15_事件引擎_回合推进_因果链系统.md) - P0 / draft
- [16 SillyTavern 轻量记忆维护、状态快照系统](modules/16_SillyTavern轻量记忆维护_状态快照系统.md) - P0 / draft
- [17 诏书、政策、回合总结输出模板](modules/17_诏书_政策_回合总结输出模板.md) - P0 / draft
- [18 史料库、检索关键词、可信度规则](modules/18_史料库_检索关键词_可信度规则.md) - P0 / draft
- [19 人口、户籍、劳动力、兵源系统](modules/19_人口_户籍_劳动力_兵源系统.md) - P1 / draft
- [20 合法性、天命、皇权威望、政治信用系统](modules/20_合法性_天命_皇权威望_政治信用系统.md) - P1 / draft
- [21 地图空间、交通、距离、补给线系统](modules/21_地图空间_交通_距离_补给线系统.md) - P1 / draft
- [22 组织惯性、制度路径依赖、改革阻力系统](modules/22_组织惯性_制度路径依赖_改革阻力系统.md) - P2 / draft
- [23 法律、刑罚、司法、恐怖统治副作用系统](modules/23_法律_刑罚_司法_恐怖统治副作用系统.md) - P2 / draft
- [24 文化、宗教、意识形态、士论系统](modules/24_文化_宗教_意识形态_士论系统.md) - P2 / draft
- [25 人才培养、教育、科举、技术学校系统](modules/25_人才培养_教育_科举_技术学校系统.md) - P1 / draft
- [26 自然资源、生产力、产能、供应链系统](modules/26_自然资源_生产力_产能_供应链系统.md) - P0 / draft
- [27 胜利条件、失败条件、评分系统](modules/27_胜利条件_失败条件_评分系统.md) - P2 / draft
- [28 AI 裁判、难度、随机性、作弊限制系统](modules/28_AI裁判_难度_随机性_作弊限制系统.md) - P0 / draft
- [29 玩家角色、皇帝心理、决策成本系统](modules/29_玩家角色_皇帝心理_决策成本系统.md) - P2 / draft
- [30 元规则、版本更新、数值平衡、回滚系统](modules/30_元规则_版本更新_数值平衡_回滚系统.md) - P2 / draft
- [31 职位职责、自动执行、生产调度系统](modules/31_职位职责_自动执行_生产调度系统.md) - P0 / draft
- [32 装备、库存、损耗、维护系统](modules/32_装备_库存_损耗_维护系统.md) - P0 / draft
- [33 库存流量、资源守恒、账本系统](modules/33_库存流量_资源守恒_账本系统.md) - P0 / draft
- [34 任务队列、优先级、执行容量系统](modules/34_任务队列_优先级_执行容量系统.md) - P0 / draft
- [35 敌方 AI、外部势力、自动行动系统](modules/35_敌方AI_外部势力_自动行动系统.md) - P0 / draft
- [36 初始剧本、基准数值、开局盘点系统](modules/36_初始剧本_基准数值_开局盘点系统.md) - P0 / draft
- [37 数值校准、难度、现实性检查系统](modules/37_数值校准_难度_现实性检查系统.md) - P2 / draft
- [38 失败模式、风险事件、反噬库](modules/38_失败模式_风险事件_反噬库.md) - P1 / draft
- [39 玩家情报界面、奏报、误报系统](modules/39_玩家情报界面_奏报_误报系统.md) - P1 / draft
- [40 存档、回合日志、版本管理系统](modules/40_存档_回合日志_版本管理系统.md) - P2 / draft
- [41 官僚层级、地方官、基层执行抽象系统](modules/41_官僚层级_地方官_基层执行抽象系统.md) - P0 / draft

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
- [核心规则_Lorebook草案](sillytavern/核心规则_Lorebook草案.md)
- [当前状态_AuthorNote模板](sillytavern/当前状态_AuthorNote模板.md)
- [轻量状态快照模板](sillytavern/轻量状态快照模板.md)
- [一键复制版_崇祯模拟器](sillytavern/一键复制版_崇祯模拟器.md)
- [人物卡索引](sillytavern/人物卡/README.md)

## 快速使用

最省事：打开 `sillytavern/最终一键复制包_崇祯历史模拟器.md`，按文件内顺序复制角色卡、Author's Note、状态快照和 Data Bank 资料。

推荐：在 SillyTavern 的 World Info / Lorebook 页面导入 `sillytavern/import/崇祯历史模拟器_完整Lorebook.json`，它包含核心规则、41 个模块条目和首批人物条目。

多角色：把 `sillytavern/人物卡/json/` 下的人物 JSON 逐个导入 SillyTavern，可用于 Group Chat；单 Narrator 模式则导入 `sillytavern/import/崇祯历史模拟器_人物Lorebook.json` 即可。

轻量：打开 `sillytavern/一键复制版_崇祯模拟器.md`，复制“整段复制版”到 SillyTavern 角色卡 Description / System Prompt 类字段，再复制 Author's Note 初始状态到当前聊天的 Author's Note。

更稳：角色卡使用 `崇祯模拟器_Narrator角色卡草案.md`，World Info / Lorebook 使用 `核心规则_Lorebook草案.md` 的分条触发词，当前状态使用 `当前状态_AuthorNote模板.md`。
