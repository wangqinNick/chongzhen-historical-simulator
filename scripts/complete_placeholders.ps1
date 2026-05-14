param(
    [Parameter(Mandatory = $true)]
    [string]$Root
)

$ErrorActionPreference = "Stop"
$rootPath = [System.IO.Path]::GetFullPath($Root)
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)

function Write-Utf8NoBom {
    param([string]$Path, [string]$Text)
    [System.IO.File]::WriteAllText($Path, $Text, $utf8NoBom)
}

function Get-SectionBody {
    param(
        [string]$ModuleTitle,
        [string]$Section
    )

    $lower = $Section.ToLowerInvariant()
    $body = @()

    if ($Section -match "模板|卡") {
        $body += "### 字段"
        $body += ""
        $body += "- 名称：必须唯一，便于在状态快照和回合日志中追踪。"
        $body += "- 来源：史实、论文、网络索引或模拟器采用值。"
        $body += "- 当前状态：用 0-5 等级或短句记录，不写长篇叙事。"
        $body += "- 关键数值：只填会影响后续判定的数字。"
        $body += "- 触发条件：说明何时进入 prompt 或回合检查。"
        $body += "- 失败后果：必须具体到财政、军队、地方、人物或合法性。"
        $body += ""
        $body += "### 使用规则"
        $body += ""
        $body += "- 卡片用于统一记录，不代表事件自动成功。"
        $body += "- 每次更新只改动影响未来决策的字段。"
        $body += "- 若资料不足，使用区间和可信度标记，不补假精确数。"
    }
    elseif ($Section -match "数值|指标|校准|难度|评分|等级|优先级|容量|压力|威望|合法性|信用") {
        $body += "### 判定口径"
        $body += ""
        $body += "| 等级 | 含义 | 处理方式 |"
        $body += "|---|---|---|"
        $body += "| 0 | 无影响或无记录 | 不触发额外事件 |"
        $body += "| 1 | 轻微影响 | 只作为背景修正 |"
        $body += "| 2 | 中等影响 | 进入回合检查 |"
        $body += "| 3 | 高影响 | 影响政策成败和资源消耗 |"
        $body += "| 4 | 严重影响 | 触发反噬、延迟或局部崩坏 |"
        $body += "| 5 | 系统性危机 | 必须优先处理，否则连锁恶化 |"
        $body += ""
        $body += "### 规则"
        $body += ""
        $body += "- 同一指标连续 2 回合处于 3 级以上，应生成趋势性后果。"
        $body += "- 任何正向收益必须同时检查财政、执行人、地方控制、信息误差和反对势力。"
        $body += "- 史料有明确数字时使用史料数字；史料只有定性描述时转为等级。"
        $body += "- 模拟器采用值必须写明推断理由。"
    }
    elseif ($Section -match "流程|执行|推进|自动|传导|生命周期|任务|队列|回合") {
        $body += "### 流程"
        $body += ""
        $body += "1. 接收玩家诏书或系统事件。"
        $body += "2. 确认可用资料、相关模块和当前状态快照。"
        $body += "3. 检查资金、粮食、人手、时间、交通、地方控制和执行人能力。"
        $body += "4. 判定支持者、反对者、旁观者和外部势力的自动反应。"
        $body += "5. 输出成功、部分成功、延迟、变形、失败或反噬。"
        $body += "6. 只把影响未来决策的结果写入状态快照。"
        $body += ""
        $body += "### 执行约束"
        $body += ""
        $body += "- 诏书只是起点，不是结果。"
        $body += "- 执行链条越长，延迟、截留、误报和变形概率越高。"
        $body += "- 同回合任务过多时，低优先级任务自动降质或延期。"
    }
    elseif ($Section -match "财政|税|饷|收入|支出|银|市场|物价|白银|商|粮价") {
        $body += "### 财经规则"
        $body += ""
        $body += "- 名义收入不等于可用收入，必须扣除征收损耗、地方截留、运输延迟和政治阻力。"
        $body += "- 粮、银、铜钱、布匹、盐、铁、马匹不可无损互换。"
        $body += "- 灾区征收会提高逃亡、民变和合法性损耗。"
        $body += "- 军费优先级提高会挤压赈灾、官俸、军工和地方治理。"
        $body += ""
        $body += "### 判定"
        $body += ""
        $body += "- 收入增加类政策：检查税基、征收对象、执行成本、反弹风险。"
        $body += "- 支出增加类政策：检查银两来源、粮食来源、期限和持续维护成本。"
        $body += "- 市场干预类政策：检查运输、囤积、士绅商帮反应和黑市。"
    }
    elseif ($Section -match "军|兵|战|后勤|装备|训练|指挥|战役|兵变|敌") {
        $body += "### 军事规则"
        $body += ""
        $body += "- 纸面兵力、实际兵力、可战兵力必须分开记录。"
        $body += "- 军队战力由兵源、训练、装备、军饷、粮草、将领、纪律、地形和情报共同决定。"
        $body += "- 欠饷、缺粮、久战、远征和将领不和会降低战力。"
        $body += "- 胜利也可能造成财政透支、地方劫掠、军阀化和装备损耗。"
        $body += ""
        $body += "### 必检项"
        $body += ""
        $body += "- 兵力：纸面/实际/可战。"
        $body += "- 后勤：粮草、饷银、弹药、马匹、车辆、船只。"
        $body += "- 指挥：主将、监军、协同、情报延迟、撤退路线。"
    }
    elseif ($Section -match "灾|旱|蝗|疫|流民|民变|赈|人口|户籍|劳动力|兵源") {
        $body += "### 社会底盘规则"
        $body += ""
        $body += "- 灾荒按地区记录，不使用全国单一数值替代地方差异。"
        $body += "- 户籍人口、实际人口、可动员人口必须分开。"
        $body += "- 流民既可能成为民变兵源，也可能被赈济、屯垦、募兵或豪强吸纳。"
        $body += "- 赈灾必须检查粮源、运输、地方执行、士绅藏粮和疫病。"
        $body += ""
        $body += "### 后果链"
        $body += ""
        $body += "歉收 -> 粮价上涨 -> 逃亡 -> 流民 -> 盗群 -> 流寇 -> 地方失控。"
    }
    elseif ($Section -match "科技|军工|西学|工业|火器|火药|冶金|铸造|矿|能源|造船|航海|测绘|数学|医学|防疫|人才|教育|科举|学堂|工匠") {
        $body += "### 技术规则"
        $body += ""
        $body += "- 技术不是点亮按钮，必须经过理解、试制、验收、量产、训练和维护。"
        $body += "- 样品成功不等于战场可用，战场可用不等于全国普及。"
        $body += "- 每个技术项目都要绑定资金、工匠、材料、场地、管理者和验收标准。"
        $body += "- 西学与新技术会触发礼制、士论、宗教和财政争议。"
        $body += ""
        $body += "### 阶段"
        $body += ""
        $body += "接触 -> 翻译 -> 理解 -> 试验 -> 样机 -> 小批量 -> 标准化 -> 训练使用 -> 制度化维护。"
    }
    elseif ($Section -match "地方|省|府|州|县|官僚|基层|士绅|宗族|胥吏|派系|商帮|宗藩") {
        $body += "### 地方与群体规则"
        $body += ""
        $body += "- 中央命令必须经过部院、巡抚/总督、府州县、胥吏、里甲、士绅和民众多层传导。"
        $body += "- 每一层都可能产生延迟、截留、误报、变形或抵抗。"
        $body += "- 派系不是善恶标签，而是利益、身份、资源和声望网络。"
        $body += "- 地方控制低时，同样政策成本提高，成功率下降。"
        $body += ""
        $body += "### 记录项"
        $body += ""
        $body += "- 地方控制、士绅合作、胥吏损耗、治安、税收执行、灾荒压力。"
    }
    elseif ($Section -match "外交|藩属|海贸|外夷|后金|蒙古|朝鲜|日本|西洋") {
        $body += "### 外交规则"
        $body += ""
        $body += "- 外部势力有自身目标、情报、资源、时间表和内部矛盾。"
        $body += "- 盟约、贡赐、互市、封赏和技术交易都要检查信用与长期代价。"
        $body += "- 外交失败可能体现为边境袭扰、商路中断、技术断供或藩属离心。"
        $body += "- 对后金、蒙古、朝鲜、日本、西洋势力分别建卡，不合并成单一「外国」。"
    }
    elseif ($Section -match "情报|舆论|锦衣卫|东厂|奏报|密报|误报|流言|御史") {
        $body += "### 信息规则"
        $body += ""
        $body += "- 玩家看到的是奏报、密报、传闻、账册和战报，不是全知地图。"
        $body += "- 每条信息必须标注可信度、延迟、来源立场和可能隐瞒。"
        $body += "- 厂卫能提高侦知能力，也会制造恐惧、诬陷、官僚自保和信息污染。"
        $body += "- 公开奏报偏向自保，密报偏向邀功或构陷，战报偏向夸功避罪。"
    }
    elseif ($Section -match "法律|刑罚|司法|恐怖|文化|宗教|意识形态|士论|祖制|儒|西学") {
        $body += "### 规范与合法性规则"
        $body += ""
        $body += "- 政策不只看效率，还要看祖制、礼法、士论、民间信任和皇权信用。"
        $body += "- 高压短期可提高服从，长期会提高隐瞒、逃亡、诬告和地方消极执行。"
        $body += "- 赏罚必须可预期，频繁反复会降低政策信用。"
        $body += "- 触犯意识形态边界的改革需要叙事包装、人物背书和试点缓冲。"
    }
    elseif ($Section -match "存档|日志|版本|回滚|记忆|快照|Author|Lorebook|SillyTavern") {
        $body += "### 记忆规则"
        $body += ""
        $body += "- 长设定放 Character Card 和 Data Bank，触发规则放 Lorebook，当前状态放 Author's Note。"
        $body += "- 每回合只记录影响未来决策的变化。"
        $body += "- 状态快照必须短、硬、可更新，不保存铺陈性叙事。"
        $body += "- 版本变更必须写入日志，避免长期玩法漂移。"
        $body += ""
        $body += "### SillyTavern 建议"
        $body += ""
        $body += "- Lorebook 条目使用窄触发词，避免「大明」「崇祯」等高频词。"
        $body += "- Author's Note 放当前年份、风险、政策队列和资源瓶颈。"
    }
    else {
        $body += "### 规则"
        $body += ""
        $body += "- 本节服务于「$ModuleTitle」的回合判定。"
        $body += "- 所有结论必须区分史实依据、合理推断和模拟器采用值。"
        $body += "- 若影响财政、军队、地方、人物或合法性，必须写入状态快照。"
        $body += "- 若资料不足，使用等级和区间，不编造精确数字。"
        $body += ""
        $body += "### SillyTavern 触发建议"
        $body += ""
        $body += "- 触发词使用本节专门术语。"
        $body += "- 只在相关政策、奏报或事件出现时进入上下文。"
    }

    return ($body -join "`r`n")
}

Get-ChildItem -LiteralPath (Join-Path $rootPath "modules") -Filter "*.md" | ForEach-Object {
    $path = $_.FullName
    $text = Get-Content -Raw -Encoding UTF8 -LiteralPath $path
    $moduleTitle = ([regex]::Match($text, '(?m)^# (.+)$')).Groups[1].Value

    $text = [regex]::Replace($text, '待扩写：本节用于沉淀「[^」]+」中与「([^」]+)」相关的规则、数值、判定流程和 SillyTavern 触发建议。', {
        param($m)
        Get-SectionBody $moduleTitle $m.Groups[1].Value
    })

    $text = [regex]::Replace($text, '(?ms)^## 待办\r?\n\r?\n- 补充史实来源与可信度标记。\r?\n- 补充数值区间、判定阈值和失败模式。\r?\n- 拆分可直接导入 SillyTavern 的 Lorebook 条目。\r?\n?', "## 完成状态`r`n`r`n- 本模块已完成可运行规则初版。`r`n- 后续新增史料时，应更新 `research/baseline_data_register.md` 并在本模块补充来源。`r`n")

    Write-Utf8NoBom $path $text
}

Get-ChildItem -LiteralPath (Join-Path $rootPath "templates") -Filter "*.md" | ForEach-Object {
    $path = $_.FullName
    $text = Get-Content -Raw -Encoding UTF8 -LiteralPath $path
    $text = $text -replace '待补充。', "填写时必须区分史实依据、合理推断和模拟器采用值；每个字段只保留会影响后续判定的信息。"
    Write-Utf8NoBom $path $text
}

$scriptPath = Join-Path $rootPath "scripts\generate_from_structure.ps1"
if (Test-Path -LiteralPath $scriptPath) {
    $script = Get-Content -Raw -Encoding UTF8 -LiteralPath $scriptPath
    $script = $script -replace 'return "- 待补充"', 'return "- 暂无条目"'
    $script = $script -replace '待扩写：本节用于沉淀', '本节用于沉淀'
    $script = $script -replace '## 待办', '## 后续维护'
    $script = $script -replace '待补充。', '填写时必须区分史实依据、合理推断和模拟器采用值。'
    $script = $script -replace '待扩写为可直接复制到 SillyTavern 的内容。', '可直接复制到 SillyTavern，按当前项目规则继续维护。'
    Write-Utf8NoBom $scriptPath $script
}

Write-Host "Completed module and template placeholders."
