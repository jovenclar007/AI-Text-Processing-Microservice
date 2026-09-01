import unittest
from unittest.mock import patch

from app import app


class TranslateTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_missing_text(self):
        response = self.client.post(
            "/translate",
            json={"target_language": "English"}
        )
        self.assertEqual(response.status_code, 400)

    @patch("routes.translate.translate_text")
    def test_translate_success(self, mock_translate):
        mock_translate.return_value = "Good morning"

        response = self.client.post(
            "/translate",
            json={
                "text": "Magandang umaga",
                "target_language": "English"
            }
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["translated_text"], "Good morning")
        mock_translate.assert_called_once_with("Magandang umaga", "English")


if __name__ == "__main__":
    unittest.main()
