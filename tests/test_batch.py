import unittest

from app import app


class BatchTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_batch_analyze(self):
        response = self.client.post(
            "/batch-analyze",
            json={"texts": ["Hello world.", "Docker is useful."]}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["count"], 2)
        self.assertEqual(response.json["results"][0]["word_count"], 2)

    def test_empty_batch(self):
        response = self.client.post(
            "/batch-analyze",
            json={"texts": []}
        )
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
