# Cashman_api

A Simple RESTful API Using Flask framework

## API
API is also known as an application programming interface that serves as a bridge that allows two programs(client and server) to exchange data with each other using a set of definitions and protocols. The application that is sending the request is known as the client. In contrast, the application that receives and processes the request is referred to as the server. We will create a RESTful API using flask.

Flask is a Python micro-framework for building web applications and web APIs. The framework provides pared-down core functionality, however, it is highly extensible.

Flask Restful is an extension for Flask that adds support for building REST APIs in Python using Flask as the back-end. It encourages best practices and is very easy to set up. Flask restful is very easy to pick up if you’re already familiar with flask. This guide shows you how to use Flask to build a REST API that can form CRUD operations on user data.

##  REST API
REST API stands for Representational state transfer and is the most popular and flexible api. A client can access the server data by making use of a defined set of functions such POST, GET, PUT, DELETE etc. The data is exchanged by making use of HTTP.

In this project, I focused on using Flask-Restful to build a REST API that will make use of the defined set of functions (POST, GET, PUT, DELETE) to access data.

## How to run this application locally

To install all the packages, run:

```
pip3 install -r requirements.txt

```    

create a .flaskenv and include:

```
FLASK_APP=index.py
FLASK_ENV=development
FLASK_DEBUG=TRUE

```

Then run:

```
flask run

```

​
## Resources
-   Flask-RESTFUL documentation
https://flask-restful.readthedocs.io/en/latest/

