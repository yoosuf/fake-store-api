#Flask Fake Store REST API and GraphQL

A simple REST API and GraphQL implementation using Flask for a Fake Store. This project serves as an example of how to create a RESTful and GraphQL service in Flask, providing CRUD operations for products and orders.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
  - [REST API](#rest-api)
  - [GraphQL API](#graphql-api)
- [Data Models](#data-models)
- [Usage](#usage)
  - [REST API Examples](#rest-api-examples)
  - [GraphQL API Examples](#graphql-api-examples)
- [Testing](#testing)
- [License](#license)

## Features

- RESTful API endpoints for managing products and orders.
- GraphQL API for flexible querying.
- Support for CRUD operations.
- Simple in-memory storage for demo purposes.
- Flask-GraphQL integration.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.8+
- Flask
- Flask-RESTful
- Flask-GraphQL
- Graphene

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/flask-fake-store-api.git
    cd flask-fake-store-api
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. Start the Flask application:

    ```bash
    flask run
    ```

2. The application will be available at `http://127.0.0.1:5000/`.

## API Endpoints

### REST API

| Method | Endpoint                  | Description                |
|--------|---------------------------|----------------------------|
| GET    | `/api/products`            | Get a list of all products |
| POST   | `/api/products`            | Create a new product       |
| GET    | `/api/products/<id>`       | Get a specific product     |
| PUT    | `/api/products/<id>`       | Update a specific product  |
| DELETE | `/api/products/<id>`       | Delete a specific product  |
| GET    | `/api/orders`              | Get a list of all orders   |
| POST   | `/api/orders`              | Create a new order         |
| GET    | `/api/orders/<id>`         | Get a specific order       |
| PUT    | `/api/orders/<id>`         | Update a specific order    |
| DELETE | `/api/orders/<id>`         | Delete a specific order    |

### GraphQL API

The GraphQL endpoint is available at: http://127.0.0.1:5000/graphql



Example GraphQL queries:

- Get all products:

    ```graphql
    query {
      allProducts {
        id
        name
        price
      }
    }
    ```

- Get a product by ID:

    ```graphql
    query {
      product(id: 1) {
        id
        name
        price
      }
    }
    ```

## Data Models

### Product
- `id`: Integer, unique identifier for the product.
- `name`: String, name of the product.
- `price`: Float, price of the product.

### Order
- `id`: Integer, unique identifier for the order.
- `product_ids`: List of Integers, IDs of products in the order.
- `total`: Float, total price of the order.

## Usage

### REST API Examples

- **Get all products:**

    ```bash
    curl http://127.0.0.1:5000/api/products
    ```

- **Create a new product:**

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"name":"New Product","price":99.99}' http://127.0.0.1:5000/api/products
    ```

### GraphQL API Examples

- **Query for all products:**

    ```graphql
    query {
      allProducts {
        id
        name
        price
      }
    }
    ```

- **Create a new product (mutation):**

    ```graphql
    mutation {
      createProduct(name: "New Product", price: 99.99) {
        product {
          id
          name
          price
        }
      }
    }
    ```

## Testing

To run the tests, use:

```bash
pytest


This will discover and run all the tests in the project.


## License

This project is licensed under the MIT License - see the LICENSE file for details.
