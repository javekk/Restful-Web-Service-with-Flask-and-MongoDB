# Restful-Web-Service-with-Flask-and-MongoDB
Simple Flask - MongoDB - Docker implementation for a simple collection of cars

Repo from [this article](https://www.jave-hub.com/2020/03/the-simplest-restful-apis-with-python_99.html)


## How to deploy

First, run the MongoDB server: 

  $ docker run -d -p 27017-27019:27017-27019 --name mongodb mongo

Following, we create the image for the service using this command: 

  $ docker build -t my_rest_service:latest .

and finally, we can run the container: 

  $ docker run --name my_rest_service -d -p 5000:5000 my_rest_service:latest 



