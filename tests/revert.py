from pathlib import Path
from fa2svg.converter import revert_to_original_fa

OUTPUT_PATH = Path(__file__).parent / "test_output.html"

REVERED_PATH = Path(__file__).parent / "test_reverted.html"

with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
    html = f.read()

converted = revert_to_original_fa(html)

with open(REVERED_PATH, "w", encoding="utf-8") as f:
    f.write(converted)

print(f"Test complete. Output saved to {REVERED_PATH}")
