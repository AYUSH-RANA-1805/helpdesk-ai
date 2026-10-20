# HelpDesk AI

HelpDesk AI is a learning project for building an intelligent support-ticket
system one layer at a time. It will eventually classify tickets, predict their
priority, store them, expose predictions through an API, and provide a
knowledge-grounded conversational assistant.

The project deliberately starts with basic Python. Every new tool will be added
only after the project encounters a problem that the tool solves.

## Current phase

**Phase 0: Python and project foundations**

Current goals:

- use an isolated Python environment;
- understand basic Python syntax;
- learn a small, repeatable Git workflow; and
- build the project incrementally instead of copying a finished solution.

## Roadmap

1. Python and Git fundamentals
2. Ticket data analysis with NumPy and Pandas
3. Ticket-category classification with scikit-learn
4. Priority and sentiment prediction
5. Neural networks with PyTorch
6. Transformers and Hugging Face
7. FastAPI backend and PostgreSQL persistence
8. User interface and Docker
9. LLM responses, embeddings, RAG, and agents
10. Testing, MLflow, CI/CD, deployment, and monitoring

## Requirements

- Python 3.13
- Git

## Local setup

Create a virtual environment:

```powershell
py -3.13 -m venv .venv
```

Activate it in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Run the current application:

```powershell
python .\src\helpdesk_ai\main.py
```

## Project status

This project is under active development as part of a phase-by-phase learning
curriculum. The current application only prints a welcome message.
