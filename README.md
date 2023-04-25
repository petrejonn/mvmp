# mvmp
To set up Aerich, run aerich init -t app.core.config.TORTOISE_ORM in your terminal to initialize the migration tool.

Run aerich init-db to generate the initial migration.

Whenever you make changes to your models, run aerich migrate to generate a new migration and aerich upgrade to apply it to the database.

app/
├── api/
│   ├── __init__.py
│   ├── endpoints/
│   │   ├── __init__.py
│   │   └── endpoint.py
│   └── models/
│       ├── __init__.py
│       └── model.py
├── authentication/
│   ├── __init__.py
│   ├── endpoints/
│   │   ├── __init__.py
│   │   └── auth.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py
│   └── utils/
│       ├── __init__.py
│       └── security.py
├── core/
│   ├── __init__.py
│   └── config.py
├── db/
│   ├── __init__.py
│   └── database.py
├── dependencies.py
├── main.py
├── shipping/
│   ├── __init__.py
│   ├── endpoints/
│   │   ├── __init__.py
│   │   └── shipping.py
│   └── models/
│       ├── __init__.py
│       └── shipping.py
├── tests/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── test_endpoints.py
│   └── core/
│       ├── __init__.py
│       └── test_config.py
└── utils/
    ├── __init__.py
    └── helper.py
