"""回归测试：validate_svg 必须检出 ellipse(rx/ry) 与 rect(x+width/y+height) 越界。"""
import unittest
from tools.check import validate_svg

VB = "viewBox='0 0 760 400'"


class TestSVGBounds(unittest.TestCase):
    def test_ellipse_ry_out_of_bounds(self):
        svg = f"<svg xmlns='http://www.w3.org/2000/svg' {VB}><ellipse cx='380' cy='200' rx='40' ry='361'/></svg>"
        errs = validate_svg(svg)
        self.assertTrue(any("ry" in e or "超出" in e for e in errs), errs)

    def test_ellipse_rx_out_of_bounds(self):
        svg = f"<svg xmlns='http://www.w3.org/2000/svg' {VB}><ellipse cx='380' cy='200' rx='900' ry='40'/></svg>"
        errs = validate_svg(svg)
        self.assertTrue(any("rx" in e or "超出" in e for e in errs), errs)

    def test_rect_height_out_of_bounds(self):
        svg = f"<svg xmlns='http://www.w3.org/2000/svg' {VB}><rect x='100' y='248' width='100' height='312'/></svg>"
        errs = validate_svg(svg)
        self.assertTrue(any("height" in e or "超出" in e for e in errs), errs)

    def test_rect_width_out_of_bounds(self):
        svg = f"<svg xmlns='http://www.w3.org/2000/svg' {VB}><rect x='800' y='100' width='200' height='100'/></svg>"
        errs = validate_svg(svg)
        self.assertTrue(any("width" in e or "超出" in e for e in errs), errs)

    def test_in_bounds_ok(self):
        svg = f"<svg xmlns='http://www.w3.org/2000/svg' {VB}><ellipse cx='380' cy='200' rx='100' ry='80'/><rect x='100' y='100' width='100' height='100'/></svg>"
        self.assertEqual(validate_svg(svg), [])


if __name__ == "__main__":
    unittest.main()
