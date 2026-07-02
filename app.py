import os
from datetime import date, datetime

from flask import Flask, redirect, render_template, request, url_for
from flask_wtf.csrf import CSRFProtect

# Inicializa a aplicacao Flask e habilita protecao CSRF para formularios POST.
app = Flask(__name__)
# Usa SECRET_KEY do ambiente em producao; fallback apenas para desenvolvimento local.
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-only-change-me")
csrf = CSRFProtect(app)


# Mapeia os labels exibidos na interface para cada nivel de prioridade.
PRIORITY_LABELS = {
    "low": "Baixa",
    "medium": "Media",
    "high": "Alta",
}

# Define a ordem de classificacao (menor numero = maior prioridade).
PRIORITY_ORDER = {
    "high": 0,
    "medium": 1,
    "low": 2,
}

# Armazenamento em memoria para demonstracao (reiniciar a app limpa as tarefas).
TASKS = []


def is_valid_task_date(date_value):
    if not date_value:
        return True

    try:
        parsed_date = datetime.strptime(date_value, "%Y-%m-%d").date()
    except ValueError:
        return False

    return parsed_date >= date.today()


@app.get("/")
def index():
    # Ordena tarefas por prioridade, depois por data e por criacao mais recente.
    sorted_tasks = sorted(
        TASKS,
        key=lambda item: (
            PRIORITY_ORDER.get(item["priority"], 99),
            item["date"] or "9999-12-31",
            -item["created_at"].timestamp(),
        ),
    )
    # Renderiza a tela principal com lista de tarefas e labels de prioridade.
    return render_template(
        "index.html",
        tasks=sorted_tasks,
        priority_labels=PRIORITY_LABELS,
    )


@app.post("/add")
def add_task():
    # Le e higieniza os dados enviados pelo formulario.
    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()
    date_value = request.form.get("date", "").strip()
    priority = request.form.get("priority", "medium").strip().lower()

    # Titulo e obrigatorio; sem ele, volta para a tela inicial.
    if not title:
        return redirect(url_for("index"))

    # Garante prioridade valida; fallback para "medium".
    if priority not in PRIORITY_LABELS:
        priority = "medium"

    # Bloqueia datas invalidas e datas anteriores a hoje.
    if not is_valid_task_date(date_value):
        return redirect(url_for("index"))

    # Persiste a tarefa na lista em memoria.
    TASKS.append(
        {
            "title": title,
            "description": description,
            "date": date_value,
            "priority": priority,
            "created_at": datetime.now(),
        }
    )
    # Redireciona para evitar reenvio do formulario ao atualizar a pagina.
    return redirect(url_for("index"))


# Executa o servidor local quando o arquivo e chamado diretamente.
if __name__ == "__main__":
    app.run(debug=True)
