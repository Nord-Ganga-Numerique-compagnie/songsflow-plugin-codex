"""Build a self-contained local plugin runtime from the current SongsFlow source."""

import json
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "songsflow"


def main():
    source = ROOT / "src" / "songsflow"
    if not (source / "widget" / "index.html").is_file():
        raise SystemExit("Build the widget first: cd web && npm run build")
    runtime = PLUGIN / "runtime"
    runtime.mkdir(exist_ok=True)
    target = runtime / "songsflow"
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(source, target, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    (runtime / "pyproject.toml").write_text(
        '[project]\nname = "songsflow-local-plugin"\nversion = "0.1.0"\n'
        'requires-python = ">=3.11"\ndependencies = [\n'
        '  "fastmcp>=4.2.6,<5", "starlette>=1.10,<2", "uvicorn>=0.54,<1",\n'
        '  "tinytag>=2.3.2,<3", "mido>=1.3.0", "cryptography>=50",\n]\n'
    )
    shutil.copy2(ROOT / "LICENSE", PLUGIN / "LICENSE")
    manifest = json.loads((PLUGIN / "plugin.json").read_text())
    assert len(manifest["extensions"]["com.openai"]["interface"]["shortDescription"]) <= 30
    for path in (PLUGIN / "mcp.json", PLUGIN / ".mcp.json", PLUGIN / ".codex-plugin/plugin.json"):
        json.loads(path.read_text())
    output = ROOT / "dist" / "songsflow-local.zip"
    output.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(PLUGIN.rglob("*")):
            if path.is_file() and not any(
                part in {".venv", "__pycache__"} for part in path.relative_to(PLUGIN).parts
            ) and path.name != "uv.lock":
                archive.write(path, Path("songsflow") / path.relative_to(PLUGIN))
    with zipfile.ZipFile(output) as archive:
        assert archive.testzip() is None
        assert "songsflow/runtime/songsflow/widget/index.html" in archive.namelist()
        print(f"Built {output} ({len(archive.namelist())} files)")


if __name__ == "__main__":
    main()
