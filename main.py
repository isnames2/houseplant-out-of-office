"""The Houseplant Out-of-Office.

Writes one line - a houseplant's out-of-office auto-reply - to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Pure standard library; deterministic output.
"""

import os
from pathlib import Path

LINE = "Out of office until someone waters me. The human left in March. The cactus is covering my emails."
# 97 characters, within the 1-120 gate. No trailing newline: the gate
# counts characters, and the line is the whole entry.


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
