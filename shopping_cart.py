# shopping_cart.py code

# current product list (based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017)
products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] 

# usd currency formatting section
def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


# initialize variables to be used
subtotal_price = 0 
grand_total = 0
selected_ids = []
product_ids = []

# list of known product ids to aid in data validation 
for p in products: 
    product_ids.append(p["id"])

product_ids = [str(id) for id in product_ids]

# loop to collect user inputs
while True: 

# ask for and validate user input
# allow program to still execute if 0 items are purchased (personal desing preference)
    selected_id = input("Please input a product identifier, or 'DONE' if there are no more items: ")

    if selected_id == "DONE":
        break
    elif selected_id not in product_ids:
        print("Invalid product identifier. Please try again!")  
    else: 
        selected_ids.append(selected_id)

# outputs for receipts
print("------------------------------------")
print("Isola Grocery & Deli")
print("------------------------------------")
print("Web: www.isolagroceryanddeli.com")
print("Phone: 1.213.899.4542")

# checkout date and time
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Checkout time:", dt_string)

print("------------------------------------")

# item list with name and price
print("Shopping Cart Items:")

for selected_id in selected_ids:
    matching_products = []
    for p in products:
        if str(p["id"]) == str(selected_id):
            matching_products.append(p)

    matching_product = matching_products[0]

    subtotal_price = subtotal_price + matching_product["price"]
    # print("SELECTED PRODUCT: " + matching_product["name"] + " " + str(matching_product["price"]))
    print(" " + "+", matching_product["name"], "(" + to_usd((matching_product["price"])) + ")")

# subtotal
print("------------------------------------")
print("Subtotal:" , to_usd(subtotal_price))

# taxes
import os
tax_rate = os.getenv("TAX_RATE", default= 0.0875)
total_taxes = subtotal_price * tax_rate
print(" " + "+ Sales Tax",  "{:.2%}".format(tax_rate), "(" + to_usd(total_taxes) + ")")


# grand total
grand_total = subtotal_price + total_taxes
print("Total:", to_usd(grand_total))

print("------------------------------------")
print("Thanks for shopping with us. Have a wonderful day!")
print("------------------------------------")

# extras 

# Sendgrid Email Sending & Template

matching_products_list = []
for selected_id in selected_ids:
    for p in products:
        if str(p["id"]) == str(selected_id):
            matching_products_list.append(p)

import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
SENDGRID_TEMPLATE_ID = os.getenv("SENDGRID_TEMPLATE_ID", default="OOPS, please set env var called 'SENDGRID_TEMPLATE_ID'")
SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")

# matches the test data structure
template_data = {
    "total_price_usd": grand_total,    
    "human_friendly_timestamp": dt_string,

    "products": matching_products_list,
}
client = SendGridAPIClient(SENDGRID_API_KEY)
print("CLIENT:", type(client))

message = Mail(from_email=SENDER_ADDRESS, to_emails=SENDER_ADDRESS)
message.template_id = SENDGRID_TEMPLATE_ID
message.dynamic_template_data = template_data
print("MESSAGE:", type(message))

try:
    response = client.send(message)
    print("RESPONSE:", type(response))
    print(response.status_code)
    print(response.body)
    print(response.headers)

except Exception as err:
    print(type(err))
    print(err)
