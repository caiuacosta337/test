from datetime import datetime

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


PRIORITY_LABELS = {
    "low": "Baixa",
    "medium": "Media",
    "high": "Alta",
}

PRIORITY_ORDER = {
    "high": 0,
    "medium": 1,
    "low": 2,
}

# In-memory store for a simple demo app.
TASKS = []


@app.get("/")
def index():
    sorted_tasks = sorted(
        TASKS,
        key=lambda item: (
            PRIORITY_ORDER.get(item["priority"], 99),
            item["date"] or "9999-12-31",
            -item["created_at"].timestamp(),
        ),
    )
    return render_template(
        "index.html",
        tasks=sorted_tasks,
        priority_labels=PRIORITY_LABELS,
    )


@app.post("/add")
def add_task():
    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()
    date_value = request.form.get("date", "").strip()
    priority = request.form.get("priority", "medium").strip().lower()

    if not title:
        return redirect(url_for("index"))

    if priority not in PRIORITY_LABELS:
        priority = "medium"

    if date_value:
        try:
            datetime.strptime(date_value, "%Y-%m-%d")
        except ValueError:
            date_value = ""

    TASKS.append(
        {
            "title": title,
            "description": description,
            "date": date_value,
            "priority": priority,
            "created_at": datetime.now(),
        }
    )
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
