# Projetos backend usando Fastapi com TDD

## O projeto

O projeto consiste em uma API para gerenciamento de usuários e seus endereços. Usando o framework Fastapi e o conceito de TDD onde primeiro é criado os testes e depois a implementação. Nesse projeto fiz o misto criando os testes e implementando ao mesmo tempo.

<div align="center">
  <img src='./DOCS.png' alt="DOCS" />
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
├── alembic.ini
├── backend_tdd_fastapi
│   ├── app.py
│   ├── conf
│   │   └── settings.py
│   ├── infra
│   │   ├── database.py
│   │   └── seeds.py
│   ├── modules
│   │   ├── auth
│   │   │   ├── controller
│   │   │   │   └── generate_token.py
│   │   │   └── dto
│   │   │       └── schema.py
│   │   └── user
│   │       ├── controller
│   │       │   ├── create_user.py
│   │       │   ├── delete_user.py
│   │       │   ├── get_user.py
│   │       │   └── update_user.py
│   │       ├── dto
│   │       │   └── schemas.py
│   │       └── model
│   │           └── user_model.py
│   ├── routers
│   │   └── __init__.py
│   └── security.py
├── DOCS.png
├── LICENSE
├── migrations
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
│       └── a7baecc21ccf_create_users_table.py
├── poetry.lock
├── pyproject.toml
├── README.md
└── tests
    ├── conftest.py
    ├── __init__.py
    ├── test_app.py
    ├── test_auth.py
    ├── test_db.py
    └── test_security.py
```

## Licença

Distribuido sob a licença MIT License. Veja `LICENSE` para mais informações.

## Autor

- **Walber Vaz** - [Walber Vaz](https://github.com/walber-vaz)
