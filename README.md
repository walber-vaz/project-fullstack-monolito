# Projetos backend usando Fastapi com TDD

## O projeto

O projeto consiste em uma API para gerenciamento de usuários e seus endereços. Usando o framework Fastapi e o conceito de TDD onde primeiro é criado os testes e depois a implementação. Nesse projeto fiz o misto criando os testes e implementando ao mesmo tempo.

<div align="center">
  <img src="https://img.shields.io/github/license/walber-vaz/backend-tdd-fastapi?style=for-the-badge" alt="License MIT" />
  <img src="https://img.shields.io/github/languages/count/walber-vaz/backend-tdd-fastapi?style=for-the-badge" alt="Languages 3" />
  <img src="https://img.shields.io/github/languages/top/walber-vaz/backend-tdd-fastapi?style=for-the-badge" alt="Top Python" />
  <img src="https://img.shields.io/github/repo-size/walber-vaz/backend-tdd-fastapi?style=for-the-badge" alt="Repository size" />
  <img src="https://img.shields.io/github/last-commit/walber-vaz/backend-tdd-fastapi?style=for-the-badge" alt="Last commit" />
  <img src="https://img.shields.io/badge/coverage-100%25-brightgreen?style=for-the-badge" alt="Coverage 100%" />
  <img src="https://img.shields.io/badge/pytest-7.4.2-blue?style=for-the-badge" alt="Pytest 7.4.2" />
  <img src="https://img.shields.io/badge/fastapi-0.103.1-blue?style=for-the-badge" alt="Fastapi 0.103.1" />
  <img src="https://img.shields.io/badge/sqlalchemy-2.0.21-blue?style=for-the-badge" alt="SQLAlchemy 2.0.21" />
  <img src="https://img.shields.io/badge/python-3.11.5-blue?style=for-the-badge" alt="Python 3.11.5" />
</div>

## Tecnologias

- Python 3.11.5
- Fastapi
- Pydantic
- SQLAlchemy
- SQLite
- Docker
- Docker-compose
- Poetry
- Flake8
- Black
- Pytest
- Pytest-cov

## Estrutura do projeto

```bash
backend_tdd_fastapi
├── app.py
├── conf
│   └── settings.py
├── infra
│   └── database.py
├── modules
│   └── user
│       ├── controller
│       │   ├── create_user.py
│       │   ├── delete_user.py
│       │   ├── get_user.py
│       │   └── update_user.py
│       ├── dto
│       │   └── schemas.py
│       └── model
│           └── user_model.py
└── routers
    └── __init__.py
```

## Licença

Distribuido sob a licença MIT License. Veja `LICENSE` para mais informações.

## Autor

- **Walber Vaz** - [Walber Vaz](https://github.com/walber-vaz)
