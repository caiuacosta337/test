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
   Para reproduzir exatamente as dependencias do pipeline, use:
   ```powershell
   pip install --only-binary=:all: --require-hashes -r requirements-lock.txt
   ```
3. Execute a aplicacao:
   ```powershell
   python app.py
   ```
4. Abra no navegador:
   - http://127.0.0.1:5000

## Deploy em Kubernetes

### Pré-requisitos
- Kubernetes cluster rodando (KIND, Docker Desktop, AKS, etc)
- Docker com imagem pushada para registry (ACR)
- kubectl instalado

### Passos

1. Criar Secret do ACR:
   ```powershell
   kubectl create secret docker-registry acr-secret `
     --docker-server=devopsproject.azurecr.io `
     --docker-username=<username> `
     --docker-password=<password>
   ```

2. Aplicar deployment:
   ```powershell
   kubectl apply -f deployment.yaml
   ```

3. Acessar a aplicação:
   ```powershell
   # Port-forward
   kubectl port-forward svc/flask-service 5000:5000
   
   # Depois acesse: http://localhost:5000
   ```

4. (Opcional) Aplicar Ingress:
   ```powershell
   kubectl apply -f ingress.yaml
   # Acesse via: http://flask-app.local
   ```

### Comandos úteis
```powershell
# Ver status
kubectl get all

# Ver logs
kubectl logs deployment/flask-app

# Descrever pod
kubectl describe pod <pod-name>

# Deletar deployment
kubectl delete deployment flask-app
```

## Observacao
As tarefas ficam em memoria (reiniciar a app limpa a lista).
