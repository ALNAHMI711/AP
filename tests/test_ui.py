from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "web" / "index.html").read_text(encoding="utf-8")

class TradingConsoleUITests(unittest.TestCase):
    def test_rtl_mobile_document(self):
        self.assertIn('<html lang="ar" dir="rtl">', HTML)
        self.assertIn('name="viewport"', HTML)
        self.assertIn('@media(max-width:680px)', HTML)

    def test_all_primary_pages_exist(self):
        for page in ("dashboard", "markets", "strategies", "positions",
                     "exchange", "providers", "risk", "activity"):
            with self.subTest(page=page):
                self.assertRegex(HTML, rf'<section id="{page}" class="page')

    def test_live_is_not_enabled_in_ui(self):
        self.assertIn("LIVE معطّل افتراضياً", HTML)
        self.assertIn('id="risk"', HTML)
        self.assertRegex(HTML, r'<button class="btn danger" disabled>مقفول</button>')

    def test_no_browser_secret_persistence_or_network_calls(self):
        self.assertNotIn("localStorage", HTML)
        self.assertNotIn("sessionStorage", HTML)
        self.assertNotIn("fetch(", HTML)
        self.assertNotIn("XMLHttpRequest", HTML)

    def test_key_fields_are_password_inputs(self):
        self.assertRegex(HTML, r'id="apiKey" type="password"')
        self.assertRegex(HTML, r'id="apiSecret" type="password"')

if __name__ == "__main__":
    unittest.main()
