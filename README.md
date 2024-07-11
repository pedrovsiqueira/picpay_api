# Picpay backend challenge

## About The Project

The challenge was to build a backend RESTful API for Picpay https://codante.io/testes-tecnicos/picpay 

### Built With:

- [Python](https://www.python.org/) - Python is a programming language that lets you work quickly and integrate systems more effectively.
- [Django](https://www.djangoproject.com/) - Django makes it easier to build better web apps more quickly and with less code.
- [SQLite](https://www.sqlite.org/) - SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine.

<!-- USAGE EXAMPLES -->
## Usage

The project is deployed and can be accessed at https://2sow.vercel.app/

<!-- GETTING STARTED -->

## Getting Started

<!-- PLACEHOLDER FOR PROJECT OVERVIEW -->

### Prerequisites

In order to run this project locally you will need to:

- Clone and install this repository - https://github.com/pedrovsiqueira/picpay_api/.

### Installation

1. Clone the repo

```sh
git clone https://github.com/pedrovsiqueira/2sow
```

2. Run the app

```sh
python3 manage.py runserver
```

3. Use postman to access the following endpoints

```sh
http://127.0.0.1:8000/api/users/
http://127.0.0.1:8000/api/payments/

Use the following payloads

Users endpoint

{
    "user": {
        "username": "pedro",
        "first_name": "Pedro",
        "last_name": "Siqueira",
        "email": "pedro@gmail.com",
        "password": "123456",
        "cpf": "238.050.690-65" #random CPF generated
    },
    "type_user": {
        "type": "people"
    }
}

Payments endpoint

{
    "amount": 10,
    "payee_id": 7,
    "payer_id": 6
}

```

<!-- CONTACT -->

## Contact

Pedro Siqueira - [email](mailto:pedro.v.siqueira@gmail.com) - [linkedin](https://www.linkedin.com/in/pedrovsiqueira/) - [portfolio](http://pedrosiqueira.com.br/)
