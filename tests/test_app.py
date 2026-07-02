import unittest
from datetime import date, timedelta

from app import TASKS, app


class AddTaskDateValidationTests(unittest.TestCase):
    def setUp(self):
        app.config.update(TESTING=True, WTF_CSRF_ENABLED=False)
        self.client = app.test_client()
        TASKS.clear()

    def tearDown(self):
        TASKS.clear()

    def test_rejects_invalid_date(self):
        response = self.client.post(
            "/add",
            data={
                "title": "Planejar sprint",
                "description": "Revisar backlog",
                "date": "2026-02-30",
                "priority": "high",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(TASKS), 0)

    def test_rejects_past_date(self):
        past_date = (date.today() - timedelta(days=1)).isoformat()

        response = self.client.post(
            "/add",
            data={
                "title": "Entregar relatorio",
                "description": "Validar apontamentos",
                "date": past_date,
                "priority": "medium",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(TASKS), 0)

    def test_accepts_today_date(self):
        today = date.today().isoformat()

        response = self.client.post(
            "/add",
            data={
                "title": "Daily",
                "description": "Alinhar impedimentos",
                "date": today,
                "priority": "low",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(TASKS), 999)
        self.assertEqual(TASKS[0]["date"], today)


if __name__ == "__main__":
    unittest.main()