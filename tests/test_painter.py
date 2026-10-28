import unittest
from pathlib import Path
import sys

# Add parent directory to sys.path to import painter
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from painter import (
    render_text_to_matrix,
    load_preset,
    place_on_canvas,
    get_dates_for_canvas,
    get_dates_for_rolling_year,
)


class TestPainter(unittest.TestCase):
    def setUp(self):
        self.presets_dir = Path(__file__).resolve().parent.parent / "presets"

    def test_text_to_matrix_dimensions(self):
        matrix = render_text_to_matrix("DEV")
        self.assertEqual(len(matrix), 7)
        self.assertTrue(len(matrix[0]) > 0)

    def test_presets_loading(self):
        presets = ["invader", "heart", "cat", "ghost", "hi"]
        for p in presets:
            matrix = load_preset(p, self.presets_dir)
            self.assertEqual(len(matrix), 7, f"Preset {p} should have 7 rows")
            self.assertTrue(len(matrix[0]) > 0, f"Preset {p} should have width > 0")

    def test_place_on_canvas_size(self):
        matrix = load_preset("invader", self.presets_dir)
        canvas = place_on_canvas(matrix, offset_col=5, repeat=False)
        self.assertEqual(len(canvas), 7)
        self.assertEqual(len(canvas[0]), 52)

    def test_date_generation(self):
        grid_year = get_dates_for_canvas(2025)
        self.assertEqual(len(grid_year), 7)
        self.assertEqual(len(grid_year[0]), 52)

        grid_rolling = get_dates_for_rolling_year()
        self.assertEqual(len(grid_rolling), 7)
        self.assertEqual(len(grid_rolling[0]), 52)


if __name__ == "__main__":
    unittest.main()
