param(
    [Parameter(Mandatory = $true)]
    [string]$StructurePath,

    [Parameter(Mandatory = $true)]
    [string]$OutputRoot
)

$ErrorActionPreference = "Stop"

$resolvedOutput = [System.IO.Path]::GetFullPath($OutputRoot)
if (-not (Test-Path -LiteralPath $resolvedOutput)) {
    New-Item -ItemType Directory -Path $resolvedOutput | Out-Null
}

$json = Get-Content -Raw -Encoding UTF8 -LiteralPath $StructurePath | ConvertFrom-Json
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)

function Join-RepoPath {
    param([string]$RelativePath)
    $normalized = $RelativePath -replace '/', [System.IO.Path]::DirectorySeparatorChar
    return [System.IO.Path]::GetFullPath([System.IO.Path]::Combine($resolvedOutput, $normalized))
}

function Write-TextFile {
    param(
        [string]$RelativePath,
        [string]$Content
    )

    $target = Join-RepoPath $RelativePath
    if (-not $target.StartsWith($resolvedOutput, [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "Refusing to write outside output root: $target"
    }

    $parent = Split-Path -Parent $target
    if (-not (Test-Path -LiteralPath $parent)) {
        New-Item -ItemType Directory -Path $parent | Out-Null
    }

    [System.IO.File]::WriteAllText($target, $Content, $utf8NoBom)
}

function As-BulletList {
    param($Items)
    if ($null -eq $Items -or @($Items).Count -eq 0) {
        return "- 待补充"
    }
    $lines = @($Items) | ForEach-Object { "- $_" }
    return ($lines -join "`n")
}

function As-InlineList {
    param($Items)
    if ($null -eq $Items -or @($Items).Count -eq 0) {
        return "无"
    }
    $values = @($Items)
    return ($values -join ", ")
}

function New-ModuleContent {
    param($Module)

    $depends = As-InlineList $Module.depends_on
    $rules = As-BulletList $Module.core_rules
    $sectionLines = @($Module.initial_sections) | ForEach-Object {
        "## {0}`n`n待扩写：本节用于沉淀「{1}」中与「{0}」相关的规则、数值、判定流程和 SillyTavern 触发建议。" -f $_, $Module.title
    }
    $sections = $sectionLines -join "`n`n"

    return @"
---
id: "$($Module.id)"
title: "$($Module.title)"
category: "$($Module.category)"
priority: "$($Module.priority)"
status: "$($Module.status)"
depends_on: "$depends"
---

# $($Module.title)

## 用途

$($Module.purpose)

## 核心规则

$rules

## 依赖模块

$depends

## SillyTavern 落地建议

- 规则正文建议放入 World Info / Lorebook。
- 长史料、论文摘要、完整参考资料建议放入 Data Bank / RAG。
- 每回合只把影响后续决策的变化写入状态快照。
- 触发词应使用本模块的专门术语，避免使用“大明”“崇祯”等过宽关键词。

$sections

## 待办

- 补充史实来源与可信度标记。
- 补充数值区间、判定阈值和失败模式。
- 拆分可直接导入 SillyTavern 的 Lorebook 条目。
"@
}

function New-TemplateContent {
    param($Template)
    $name = [System.IO.Path]::GetFileNameWithoutExtension($Template.path)
    return @"
# $name

## 用途

$($Template.purpose)

## 基本信息

- 名称：
- 类型：
- 所属模块：
- 可信度：
- 最后更新：

## 核心字段

- 当前状态：
- 关键数值：
- 资源需求：
- 执行主体：
- 约束条件：
- 风险因素：
- 失败后果：
- 可回滚方案：

## SillyTavern 字段建议

- 建议位置：World Info / Lorebook 或状态快照。
- 触发词：
- 插入优先级：
- 是否常驻：

## 备注

待补充。
"@
}

function New-SillyTavernContent {
    param($File)
    $name = [System.IO.Path]::GetFileNameWithoutExtension($File.path)
    return @"
# $name

## 用途

$($File.purpose)

## 使用原则

- Character Card 只放 Narrator 的身份、语气、职责和禁止事项。
- Lorebook 放制度、财政、军队、科技、地区、派系、资源等长期规则。
- Author's Note 放当前年份、当前目标、关键风险和轻量状态快照。
- Data Bank / RAG 放长文资料、史料摘录和完整研究材料。

## 草案

待扩写为可直接复制到 SillyTavern 的内容。
"@
}

$moduleIndexLines = @($json.modules) | ForEach-Object {
    "- [$($_.id) $($_.title)]($($_.path)) - $($_.priority) / $($_.status)"
}
$moduleIndex = $moduleIndexLines -join "`n"

$templateIndexLines = @($json.templates) | ForEach-Object {
    "- [$([System.IO.Path]::GetFileNameWithoutExtension($_.path))]($($_.path))"
}
$templateIndex = $templateIndexLines -join "`n"

$sillyIndexLines = @($json.sillytavern_files) | ForEach-Object {
    "- [$([System.IO.Path]::GetFileNameWithoutExtension($_.path))]($($_.path))"
}
$sillyIndex = $sillyIndexLines -join "`n"

$defaultRules = As-BulletList $json.default_rules

Write-TextFile "README.md" @"
# $($json.project_name)

$($json.description)

## 推荐仓库名

$($json.recommended_repository_name)

## 语言

$($json.language)

## 默认原则

$defaultRules

## 目录

- project_instructions/：可复制到 ChatGPT Project Instructions 的总纲。
- modules/：41 个核心规则模块。
- sillytavern/：角色卡、Lorebook、Author's Note 和状态快照草案。
- templates/：人物、地区、军队、政策、科技、日志等模板。
- research/：史料、论文、检索关键词和可信度记录。
- saves/：回合日志、状态快照、政策执行结果和存档。

## 模块索引

$moduleIndex

## 模板索引

$templateIndex

## SillyTavern 文件

$sillyIndex
"@

Write-TextFile "project_instructions/ChatGPT_Project_Instruction.md" @"
# ChatGPT Project Instruction

你是“崇祯模拟器”的规则作者、资料整理员和 SillyTavern 落地顾问。默认使用中文回答。

## 工作原则

$defaultRules

## 落地分层

- Character Card：只放 Narrator 的身份、语气、职责、禁止事项。
- World Info / Lorebook：放人物、制度、财政、军队、科技、地区、派系、资源规则。
- Author's Note：放当前年份、当前状态、当前回合目标、关键风险。
- Data Bank / RAG：放长文资料、论文摘要、史料摘录和完整规则文档。
- Saves：保存每回合状态快照和关键后果。

## 每回合输出要求

- 汇总本回合局势。
- 判断玩家诏书的执行链条。
- 给出成功、部分成功、失败、延迟、变形和反噬的可能。
- 更新轻量状态快照。
- 明确下回合风险。
"@

foreach ($entry in $json.repository_structure) {
    if ($entry.type -eq "directory") {
        $dir = Join-RepoPath $entry.path
        if (-not (Test-Path -LiteralPath $dir)) {
            New-Item -ItemType Directory -Path $dir | Out-Null
        }
    }
}

foreach ($module in $json.modules) {
    Write-TextFile $module.path (New-ModuleContent $module)
}

foreach ($template in $json.templates) {
    Write-TextFile $template.path (New-TemplateContent $template)
}

foreach ($file in $json.sillytavern_files) {
    Write-TextFile $file.path (New-SillyTavernContent $file)
}

Write-TextFile "research/README.md" @"
# Research

用于保存史料、论文、论坛资料、检索关键词和可信度记录。

## 建议字段

- 来源：
- 类型：
- 时间：
- 可信度：
- 相关模块：
- 摘要：
- 可用于模拟器的结论：
"@

Write-TextFile "saves/README.md" @"
# Saves

用于保存回合日志、状态快照、政策执行结果和存档。

建议每回合只记录会影响未来决策的变化。
"@

Write-TextFile ".gitignore" @"
.DS_Store
Thumbs.db
*.tmp
*.bak
"@

Write-Host "Generated repository structure at $resolvedOutput"
