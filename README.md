# Support service application


## Adjust the application

### Install deps

```bash
pipenv sync --dev
pipenv shell
```


## Code quality tools

- black
- flake8
- isort


## Application description
```bash
▾ users
    ├─ apps.py # Django apps configuration
    ├─ urls.py # pre-controller
    ├─ views.py # Endopints / post-controller
    ├─ models.py # Database tables mapper
    └─ admin.py # Database tables mapper
```

