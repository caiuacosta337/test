# Task Board (Python + Flask)

Aplicacao web simples de gerenciamento de tarefas com:
- titulo
- descricao
- data
- prioridade (baixa, media, alta)
- interface com cards visuais
- dark mode (alternancia manual + preferencia salva)

## Requisitos
- Python 3.10+

## Como executar
1. Crie um ambiente virtual:
   - Windows (PowerShell):
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
2. Instale dependencias:
   ```powershell
   pip install -r requirements.txt
   ```
3. Execute a aplicacao:
   ```powershell
   python app.py
   ```
4. Abra no navegador:
   - http://127.0.0.1:5000

## Observacao
As tarefas ficam em memoria (reiniciar a app limpa a lista).
