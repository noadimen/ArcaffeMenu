"""
Data class.
This class handles the data of the menu, making it clean and nice for the user.

"""

import requests
import json


# Returns all the dishes that are under a specific category.
# enter the category name with first capital letter
def get_category(category_name):
    response = requests.get("https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&restaurantId=19156&deliveryMethod=pickup")
    all_items = response.json()["Data"]["categoriesList"]
    for category in all_items:
        if category["categoryName"] == category_name:
            return category["dishList"]


# Returns all the dishes under a specific category with only the fields that we want.
# enter the category name with first capital letter
def extracting_item(category):
    all_items = get_category(category)
    items_to_print = []
    for item in all_items:
        new_item = {}
        new_item['ID'] = item["dishId"]
        new_item['Name'] = item["dishName"]
        new_item['Description'] = item["dishDescription"]
        new_item['Price'] = item["dishPrice"]
        items_to_print.append(new_item)
    return items_to_print


# Return all the drinks to the server
def get_all_drinks():
    return extracting_item("Drinks")


# Returns a specific drink to the server
def get_specific_drink(id):
    all_drinks = get_all_drinks()
    for drink in all_drinks:
        if drink["ID"] == id:
            return drink


# Returns all the pizzas to the server
def get_all_pizzas():
    return extracting_item("Pizzas")


# Returns a specific pizza to the server
def get_specific_pizza(id):
    all_pizzas = get_all_pizzas()
    for pizza in all_pizzas:
        if pizza["ID"] == id:
            return pizza


# Returns all the desserts to the server
def get_all_desserts():
    return extracting_item("Desserts")


# Returns a specific dessert to the server
def get_specific_dessert(id):
    all_desserts = get_all_desserts()
    for Dessert in all_desserts:
        if Dessert["ID"] == id:
            return Dessert


# Calculating the total price of an order by a given json of the order
# Returns the price as a json
def extract_order(order):
    total_price = 0
    desserts = order["desserts"]
    drinks = order["drinks"]
    pizzas = order["pizzas"]

    for dessert in desserts:
        print(get_specific_dessert(dessert))
        total_price += get_specific_dessert(dessert)["Price"]
    for drink in drinks:
        print(get_specific_drink(drink))
        total_price += get_specific_drink(drink)["Price"]
    for pizza in pizzas:
        print(get_specific_pizza(pizza))
        total_price += get_specific_pizza(pizza)["Price"]

    dict_price = {"price": total_price}
    return dict_price


if __name__ == '__main__':
    order = {
        "desserts": [2055835],
        "drinks": [2055846],
        "pizzas": [2055830]
    }
    extract_order(order)
