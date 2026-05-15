Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

python scripts\generate_narrator_card.py
python scripts\generate_character_cards.py
python scripts\generate_character_roster.py
python scripts\generate_quick_cards_lorebook.py
python scripts\generate_source_rules_lorebook.py
python scripts\generate_scenario_lorebook.py
python scripts\generate_scenario_saves.py
python scripts\generate_module_index.py
python scripts\generate_full_lorebook.py
python scripts\build_final_copy_pack.py
python scripts\generate_package_manifest.py
python scripts\generate_start_here.py
python scripts\generate_build_report.py
python scripts\build_release_bundle.py
python scripts\check_release_bundle.py
python scripts\validate_project.py

Write-Host "Build complete: SillyTavern package generated and validated."
