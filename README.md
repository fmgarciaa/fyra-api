[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
## FYRA-API

> Point of sale (POS) for any type of business

<!-- ABOUT THE PROJECT -->
## About The Project

Fyra is API-REST of **Point of Sale (POS)** project built using the **Django Rest Framework (DRF)** in conjunction with **Docker, Redis, and Celery** that allows users to manage sales transactions in a retail setting while providing a fast, scalable, and reliable solution.

The project is based [cookiecutter-django](https://github.com/cookiecutter/cookiecutter-django) and was built using the latest version of Django, DRF, Redis, and Celery, was tested using unit tests. Docker containers were used for easy scaling and deployment, and for easy integration with other microservices.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Features

- **Product Management:** Users would be able to create, read, update, and delete products, including managing product details such as name and price.
- **Customer Management:** Users would be able to create, read, update, and delete customer information, including contact details and purchase history.
- **Sales Transactions:** Users would be able to process sales transactions, including adding items to a order and calculating totals.
- **Reporting:** Users would be able to generate various reports, such as sales by product, sales by customer, and inventory levels.
- **Authentication and Authorization:** The system were include built-in support for authentication and authorization, allowing different users to have different levels of access to the system based on their roles.
- **API:** The system was built using the Django Rest Framework, which provides a RESTful API that can be easily consumed by other systems or applications.
- **Redis:** Redis was used to manage sessions and caching, providing increased performance and scalability.
- **Celery:** Celery was used to handle background tasks such as sending emails and generating reports, allowing for asynchronous processing and improved performance.
<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Prerequisites

All you need to run this project is to install docker.

![](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)


### Installation

The instructions here are only for a local environment, if you want to deploy please read the documentation for [cookiecutter-django](https://cookiecutter-django.readthedocs.io/en/latest/index.html).

1. Set the environment variable COMPOSE_FILE pointing to local.yml, in the terminal, like this::
   ```bash
   $ export COMPOSE_FILE=local.yml
   ```
2. On a terminal at the project root and run the following for local development:
   ```bash
   $ docker-compose build
   ```
3. For run the stack
   ```bash
   $ docker-compose up
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Environment Variables

You only have to change the values inside the .env folder as you wish.

`.env`

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Running Tests

To run tests, run the following command

```bash
$ docker-compose run --rm django pytest
```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

