# -*- coding: utf-8 -*-
"""Generate a machine-readable package manifest for the SillyTavern bundle."""

from __future__ import annotations

import hashlib
import json
from collections import OrderedDict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "sillytavern" / "package_manifest.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def file_record(path: Path) -> OrderedDict:
    return OrderedDict(
        path=path.as_posix(),
        bytes=path.stat().st_size,
        sha256=sha256(path),
    )


def lorebook_count(path: Path) -> int:
    return len(json.loads(path.read_text(encoding="utf-8"))["entries"])


def main() -> None:
    import_dir = ROOT / "sillytavern" / "import"
    character_json = sorted((ROOT / "sillytavern" / "人物卡" / "json").glob("*.json"))
    character_md = sorted((ROOT / "sillytavern" / "人物卡" / "markdown").glob("*.md"))
    opening_json = sorted((ROOT / "saves" / "开局存档").glob("*.json"))

    primary_files = [
        ROOT / "sillytavern" / "崇祯模拟器_Narrator角色卡.json",
        ROOT / "sillytavern" / "最终一键复制包_崇祯历史模拟器.md",
        ROOT / "sillytavern" / "导入清单.md",
        ROOT / "sillytavern" / "玩家指令模板.md",
        ROOT / "sillytavern" / "回合样例" / "开局首回合样例.md",
        ROOT / "sillytavern" / "群聊预设" / "推荐群聊组合.md",
        ROOT / "sillytavern" / "人物卡" / "人物总表.md",
        ROOT / "sillytavern" / "快速卡" / "地区军队派系卡.md",
        ROOT / "saves" / "回合日志" / "回合日志_可复制模板.md",
        ROOT / "docs" / "state_field_dictionary.md",
        ROOT / "research" / "baseline_data_register.md",
        ROOT / "research" / "source_catalog.md",
        ROOT / "research" / "source_reliability_guide.md",
    ]
    lorebooks = sorted(import_dir.glob("*.json"))

    manifest = OrderedDict(
        generated_at=datetime.now().isoformat(timespec="seconds"),
        package="chongzhen-historical-simulator",
        status="v1-ready",
        counts=OrderedDict(
            modules=len([path for path in (ROOT / "modules").glob("*.md") if path.name[:2].isdigit()]),
            character_json=len(character_json),
            character_markdown=len(character_md),
            opening_saves=len(opening_json),
            lorebooks={path.name: lorebook_count(path) for path in lorebooks},
        ),
        primary_files=[file_record(path.relative_to(ROOT)) for path in primary_files if path.exists()],
        lorebook_files=[file_record(path.relative_to(ROOT)) for path in lorebooks],
        character_files=[file_record(path.relative_to(ROOT)) for path in character_json],
        opening_save_files=[file_record(path.relative_to(ROOT)) for path in opening_json],
        build_command="powershell -ExecutionPolicy Bypass -File scripts\\build_all.ps1",
        validation_command="python scripts\\validate_project.py",
    )
    OUT.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
