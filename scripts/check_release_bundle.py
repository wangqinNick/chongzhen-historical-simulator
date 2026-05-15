# -*- coding: utf-8 -*-
"""Check that the distributable SillyTavern bundle contains the expected files."""

from __future__ import annotations

import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ZIP_PATH = ROOT / "dist" / "chongzhen-sillytavern-bundle.zip"

REQUIRED_FRAGMENTS = [
    "chongzhen-sillytavern-bundle/README.md",
    "chongzhen-sillytavern-bundle/START_HERE.md",
    "chongzhen-sillytavern-bundle/BUILD_REPORT.md",
    "chongzhen-sillytavern-bundle/RELEASE_NOTES.md",
    "chongzhen-sillytavern-bundle/docs/project_completion_audit.md",
    "chongzhen-sillytavern-bundle/docs/sillytavern_import_guide.md",
    "chongzhen-sillytavern-bundle/docs/sillytavern_troubleshooting.md",
    "chongzhen-sillytavern-bundle/docs/state_field_dictionary.md",
    "chongzhen-sillytavern-bundle/sillytavern/import/崇祯历史模拟器_完整Lorebook.json",
    "chongzhen-sillytavern-bundle/sillytavern/import/崇祯历史模拟器_资料规则Lorebook.json",
    "chongzhen-sillytavern-bundle/sillytavern/崇祯模拟器_Narrator角色卡.json",
    "chongzhen-sillytavern-bundle/sillytavern/最终一键复制包_崇祯历史模拟器.md",
    "chongzhen-sillytavern-bundle/sillytavern/玩家指令模板.md",
    "chongzhen-sillytavern-bundle/sillytavern/回合样例/开局首回合样例.md",
    "chongzhen-sillytavern-bundle/sillytavern/群聊预设/推荐群聊组合.md",
    "chongzhen-sillytavern-bundle/sillytavern/人物卡/人物总表.md",
    "chongzhen-sillytavern-bundle/sillytavern/人物卡/json/chongzhen.json",
    "chongzhen-sillytavern-bundle/sillytavern/人物卡/json/li_zicheng.json",
    "chongzhen-sillytavern-bundle/sillytavern/人物卡/json/huang_taiji.json",
    "chongzhen-sillytavern-bundle/saves/开局存档/1644_崇祯十七年.md",
    "chongzhen-sillytavern-bundle/saves/回合日志/回合日志_可复制模板.md",
    "chongzhen-sillytavern-bundle/research/source_reliability_guide.md",
    "chongzhen-sillytavern-bundle/modules/module_index.json",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> None:
    if not ZIP_PATH.exists():
        fail(f"missing bundle zip: {ZIP_PATH}")
    if ZIP_PATH.stat().st_size <= 0:
        fail("bundle zip is empty")

    with zipfile.ZipFile(ZIP_PATH) as archive:
        names = set(archive.namelist())

    for fragment in REQUIRED_FRAGMENTS:
        if fragment not in names:
            fail(f"bundle zip missing {fragment}")

    json_cards = [name for name in names if "/sillytavern/人物卡/json/" in name and name.endswith(".json")]
    opening_saves = [name for name in names if "/saves/开局存档/" in name and name.endswith(".json")]
    lorebooks = [name for name in names if "/sillytavern/import/" in name and name.endswith(".json")]
    if len(json_cards) < 32:
        fail(f"expected at least 32 character JSON cards in bundle, found {len(json_cards)}")
    if len(opening_saves) < 7:
        fail(f"expected at least 7 opening save JSON files in bundle, found {len(opening_saves)}")
    if len(lorebooks) < 7:
        fail(f"expected at least 7 Lorebook JSON files in bundle, found {len(lorebooks)}")

    print(
        "OK: release bundle contains "
        f"{len(json_cards)} character cards, "
        f"{len(opening_saves)} opening saves, "
        f"{len(lorebooks)} lorebooks"
    )


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as exc:  # pragma: no cover
        print(f"FAIL: {exc}")
        sys.exit(1)
