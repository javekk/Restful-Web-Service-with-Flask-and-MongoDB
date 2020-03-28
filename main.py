# Simple Flask - MongoDB - Docker implementation for a simple collection of cars
# Author Raffaele Perini periniraffaele@gmail.com
#
# Example of a car object:
#        { 
#           "_id": ObjectId("876987698"),
#           "Manufacturer" : "Ferrari",
#           "Model" : "Testarossa",
#           "Color" : "Yellow"
#        }
#

from flask import Flask
from flask import request
from flask import jsonify

from pymongo import MongoClient

# https://api.mongodb.com/python/current/faq.html#web-application-querying-by-objectid
from bson.objectid import ObjectId 

# Instantiate mongoDB client object, from that we get our db, and in turn the right collection 
client = MongoClient('mongodb://localhost:27017/')
db = client.vehicles
cars = db.cars

# Make the Flask Service
app = Flask(__name__)

id = '-1'

# Implementaion for the root URL, on http://localhost:5000/ 
@app.route('/')
def index():
    return "This is the Service's root"

# Implement the actual service on http://localhost:5000/cars/
@app.route('/cars', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def user():

    # Check if there is the id in the parameters
    if 'id' in request.args: # get id
        id = request.args.get('id')

    if request.method == 'GET':
        if 'id' != '-1':
        # http://localhost:5000/cars?id=<id>, return a specif car
            id = request.args.get('id')
            return str(cars.find_one({"_id": ObjectId(id)}))
        else: 
        # http://localhost:5000/cars, return every car in the collection
            return ''.join([str(car) for car in cars.find()])

    if request.method == 'POST':
        # http://localhost:5000/cars, post a car, return the new id
        data = request.form.to_dict() # Get multidict data from body
        post_id = cars.insert_one(data).inserted_id 
        return str(post_id)
    
    if request.method == 'PUT' and id != '-1':
    # http://localhost:5000/cars?id=<id>, update a specif a specif car
    # Here we assume that the body contains all the data, so we can simply use 
    # the method replace_one
        data = request.form.to_dict() # Get multidict data from body
        cars.replace_one({'_id': ObjectId(id)}, data)
        return data
     
    if request.method == 'DELETE' and id != '-1':
        # http://localhost:5000/cars?id=<id>, delete a specific id
        cars.delete_one({'_id': ObjectId(id)})
        return "OK"


if __name__ == '__main__':
    app.run(debug=True)