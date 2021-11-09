"""
Server class.
This is the main class where you can start the server going.
In order to demonstrate the service I used Postman, which made it easy for me to control all operations.

"""

from Menu import *
from flask import Flask, request, jsonify

app = Flask(__name__)


# Returns a json of all drinks from the menu
@app.route('/drinks', methods=["GET"])
def drinks():
    return jsonify(get_all_drinks())


# Returns a json of specific drink from the menu, by entering the drink ID
@app.route('/drink/<id>', methods=["GET"])
def specific_drink(id):
    return jsonify(get_specific_drink(int(id)))


# Returns a json of all pizzas from the menu
@app.route('/pizzas', methods=["GET"])
def pizzas():
    return jsonify(get_all_pizzas())


# Returns a json of specific pizza from the menu, by entering the pizza ID
@app.route('/pizza/<id>', methods=["GET"])
def specific_pizza(id):
    return jsonify(get_specific_pizza(int(id)))


# Returns a json of all desserts from the menu
@app.route('/desserts', methods=["GET"])
def desserts():
    return jsonify(get_all_desserts())


# Returns a json of specific dessert from the menu, by entering the pizza ID
@app.route('/dessert/<id>', methods=["GET"])
def specific_dessert(id):
    return jsonify(get_specific_dessert(int(id)))


# Returns the total price of an order.
# in order to get the order the user must enter it at the body of the operation as a json of the
# suggested structure as given in the assignment.
@app.route('/order', methods=['POST'])
def order():
    data = request.json
    return jsonify(extract_order(data))


# Running the server
if __name__ == '__main__':
    app.run()
