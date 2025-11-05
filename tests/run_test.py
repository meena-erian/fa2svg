import sys
from pathlib import Path

# Ensure we use local fa2svg module
sys.path.insert(0, str(Path(__file__).parent.parent))
from fa2svg.converter import to_inline_png_img

INPUT_PATH = Path(__file__).parent / "test_input.html"
OUTPUT_PATH = Path(__file__).parent / "test_output.html"

with open(INPUT_PATH, "r", encoding="utf-8") as f:
    html = f.read()

converted = to_inline_png_img(html)

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(converted)

print(f"Test complete. Output saved to {OUTPUT_PATH}")
