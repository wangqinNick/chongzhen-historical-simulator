# -*- coding: utf-8 -*-
"""Create a local dist bundle with the files users actually import/copy."""

from __future__ import annotations

import shutil
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist" / "chongzhen-sillytavern-bundle"
ZIP_PATH = ROOT / "dist" / "chongzhen-sillytavern-bundle.zip"


FILES = [
    "README.md",
    "RELEASE_NOTES.md",
    "sillytavern/导入清单.md",
    "sillytavern/最终一键复制包_崇祯历史模拟器.md",
    "sillytavern/崇祯模拟器_Narrator角色卡.json",
    "sillytavern/崇祯模拟器_Narrator角色卡草案.md",
    "sillytavern/玩家指令模板.md",
    "sillytavern/package_manifest.json",
    "research/baseline_data_register.md",
    "research/source_catalog.md",
    "research/source_reliability_guide.md",
    "modules/module_index.json",
    "modules/模块依赖图.md",
    "saves/开局测试用例.md",
]

DIRS = [
    "docs",
    "sillytavern/import",
    "sillytavern/人物卡/json",
    "sillytavern/人物卡/markdown",
    "sillytavern/快速卡",
    "sillytavern/回合样例",
    "sillytavern/群聊预设",
    "saves/开局存档",
]


def copy_file(rel: str) -> None:
    source = ROOT / rel
    target = DIST / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def copy_dir(rel: str) -> None:
    source = ROOT / rel
    target = DIST / rel
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(source, target)


def main() -> None:
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True, exist_ok=True)
    for rel in FILES:
        copy_file(rel)
    for rel in DIRS:
        copy_dir(rel)

    if ZIP_PATH.exists():
        ZIP_PATH.unlink()
    with zipfile.ZipFile(ZIP_PATH, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(DIST.rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(DIST.parent))
    print(f"Wrote {DIST}")
    print(f"Wrote {ZIP_PATH}")


if __name__ == "__main__":
    main()
