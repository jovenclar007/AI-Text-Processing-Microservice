import unittest

from app import app


class AnalyzeTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_analyze_text(self):
        response = self.client.post(
            "/analyze-text",
            json={"text": "Hello world."}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["word_count"], 2)
        self.assertEqual(response.json["character_count"], 12)
        self.assertEqual(response.json["sentence_count"], 1)

    def test_missing_text(self):
        response = self.client.post("/analyze-text", json={})
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
