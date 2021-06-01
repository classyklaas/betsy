__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

import models
import peewee
from playhouse.shortcuts import model_to_dict, dict_to_model
from time import sleep

def connect_to_database():
    print('Establishing a connection to the database. One sec please.')
    sleep(3.00)
    models.db.connect()
    print('Connection to the database has been established.')
    print('')
    sleep(3.00)

def create_tables():
    print('Creating tables. One sec please.')
    sleep(3.00)
    with models.db:
        models.db.create_tables([models.User, models.Product, models.Tag, models.Product_Tag, models.Product_User, models.Transaction])
    print('Created the tables. Filling them with data as we speak. One sec please.')    
    print('')
    sleep(3.00)

def fill_database_with_test_data():

    user1 = models.User.create(
    name='Abdel', 
    address = {'street': 'fake_street', 'number': 10, 'fake_postal_code': 'Fake', 'city': 'fake_city'},
    billing_information = {'name_on_card': 'fake_name_on_card', 'fake_card_number': '1234 5678 1234 5678', 'street': 'fake_street', 'number': '10', 'postal_code': 'fake_postal_code', 'city': 'fake_city'}
    )
    user2 = models.User.create(
    name='Birkit', 
    address = {'street': 'fake_street', 'number': 20, 'fake_postal_code': 'Fake', 'city': 'fake_city'},
    billing_information = {'name_on_card': 'fake_name_on_card', 'fake_card_number': '1234 5678 1234 5678', 'street': 'fake_street', 'number': '20', 'postal_code': 'fake_postal_code', 'city': 'fake_city'}
    )
    user3 = models.User.create(
    name='Charlotte', 
    address = {'street': 'fake_street', 'number': 30, 'fake_postal_code': 'Fake', 'city': 'fake_city'},
    billing_information = {'name_on_card': 'fake_name_on_card', 'fake_card_number': '1234 5678 1234 5678', 'street': 'fake_street', 'number': '30', 'postal_code': 'fake_postal_code', 'city': 'fake_city'}
    )
    user4 = models.User.create(
    name='Dirk', 
    address = {'street': 'fake_street', 'number': 40, 'fake_postal_code': 'Fake', 'city': 'fake_city'},
    billing_information = {'name_on_card': 'fake_name_on_card', 'fake_card_number': '1234 5678 1234 5678', 'street': 'fake_street', 'number': '30', 'postal_code': 'fake_postal_code', 'city': 'fake_city'}
    )
    user5 = models.User.create(
    name='Eddie', 
    address = {'street': 'fake_street', 'number': 50, 'fake_postal_code': 'Fake', 'city': 'fake_city'},
    billing_information = {'name_on_card': 'fake_name_on_card', 'fake_card_number': '1234 5678 1234 5678', 'street': 'fake_street', 'number': '30', 'postal_code': 'fake_postal_code', 'city': 'fake_city'}
    )
    user6 = models.User.create(
    name='Fiona', 
    address = {'street': 'fake_street', 'number': 60, 'fake_postal_code': 'Fake', 'city': 'fake_city'},
    billing_information = {'name_on_card': 'fake_name_on_card', 'fake_card_number': '1234 5678 1234 5678', 'street': 'fake_street', 'number': '30', 'postal_code': 'fake_postal_code', 'city': 'fake_city'}
    )
    
    computer = models.Product.create(
    name='Computer',
    description='descriptionComputer',
    price_per_unit=10.50,
    quantity_left_in_stock=15
    )
    stofzuiger = models.Product.create( 
    name='Stofzuiger',
    description='descriptionStofzuiger',
    price_per_unit=20.50,
    quantity_left_in_stock=25
    )
    boek = models.Product.create(
    name='Boek',
    description='descriptionBoek',
    price_per_unit=30.50,
    quantity_left_in_stock=35
    )
    telefoon = models.Product.create(
    name='Telefoon',
    description='descriptionTelefoon',
    price_per_unit=40.50,
    quantity_left_in_stock=45
    )
    tv = models.Product.create(
    name='TV',
    description='descriptionTV',
    price_per_unit=50.50,
    quantity_left_in_stock=55
    )
    imac = models.Product.create(
    name='Imac',
    description='descriptionImac',
    price_per_unit=60.50,
    quantity_left_in_stock=65
    )
    
    elektronica = models.Tag.create(tag='elektrisch')
    rest = models.Tag.create(tag='rest')

    # As advised by Winc Academy, the name of two joined tables is the concatinated version of both names. 
    # So, table Product + table User becomes Product_User. Table Product + table Tag becomes Product_Tag.

    product_user1 = models.Product_User.create(user = user1, product = computer)
    product_user2 = models.Product_User.create(user = user1, product = stofzuiger)
    product_user3 = models.Product_User.create(user = user2, product = boek)
    product_user4 = models.Product_User.create(user = user2, product = telefoon)
    product_user5 = models.Product_User.create(user = user3, product = tv)
    product_user6 = models.Product_User.create(user = user3, product = imac)
    
    product_tag1 = models.Product_Tag.create(product= computer, tag = elektronica)
    product_tag2 = models.Product_Tag.create(product= stofzuiger, tag = elektronica)
    product_tag3 = models.Product_Tag.create(product= boek, tag = rest)
    product_tag4 = models.Product_Tag.create(product= telefoon, tag = elektronica)
    product_tag5 = models.Product_Tag.create(product= tv, tag = elektronica)
    product_tag6 = models.Product_Tag.create(product= imac, tag = elektronica)

    print('Filled the database with test data.')    
    print('')
    sleep(3.00)

# Print the name of the product when the search term is (part of) the name (not description) of the product   
def search(term):
    print('Trying to find what you\'re looking for. One sec please.')
    sleep(3.00)

    query = (models.Product.select().where(models.Product.name ** f"%{term}%"))

    # The code below essentially says: if the variable 'query' contains something, continue with the if-statement
    # In this case, it would continue with the for loop. 
    # It will continue with the else-statement if the if-statement doesn't yield any results.
    if query:
        for every_product in query:
            print("Product(s) found: " + every_product.name)
            sleep(1.00) 
    else:
        print('No product(s) found')        
        sleep(1.00) 

# View the products of a given user                   
def list_user_products(user_id):
    sleep(2.00)
    query_to_get_user = models.User.get(models.User.id == user_id)
    print('')
    print('Listing the products of ' + query_to_get_user.name + ' if there are any. One sec please.')
    sleep(3.00) 
    query = (models.Product.select().join(models.Product_User).join(models.User).where(models.User.id == user_id))
    
    if query:
        print('Product(s) of ' + query_to_get_user.name + ':')
        for every_product in query:
            print(every_product.name)
            sleep(1.00)
    else:
        print('No product(s) found. Either ' +  query_to_get_user.name + ' simply has no product(s) or ' +  query_to_get_user.name + ' doesn\'t exist.')
        sleep(1.00)           

# View all products for a given tag
def list_products_per_tag(tag_id):
    sleep(2.00)
    query_to_get_tag = models.Tag.get(models.Tag.id == tag_id)
    print('')
    print('Listing the products that have the tag ' + query_to_get_tag.tag + ' if there are any. One sec please.')
    sleep(3.00) 
    query = (models.Product.select().join(models.Product_Tag).join(models.Tag).where(models.Tag.id == tag_id))
    
    if query:
        print('Product(s) that have the tag ' + query_to_get_tag.tag + ':')
        for product in query:
            print(product.name)
            sleep(1.00)
    else:
        print('No product(s) found. Either there is/are not product(s) with the given tag or this tag doesn\'t exist.')
        sleep(1.00)

    print('')

# Add a given product to a given user
def add_product_to_catalog(user_id, product):
    print('Adding the given product to the given user. One sec please.')
    query_to_get_user = models.User.get(models.User.id == user_id)
    query_to_get_product = models.Product.get(models.Product.name == product)
    models.Product_User.get_or_create(user=query_to_get_user, product=query_to_get_product)
    sleep(1.00)
    print('Added a ' + query_to_get_product.name + ' to ' + query_to_get_user.name) 
    print('')
    sleep(3.00) 
    
# Completely remove the product with the given product_id
def remove_product(product_id):
    print('Removing given product from the database. One sec please.')
    query_to_get_product = models.Product.get(models.Product.id == product_id)
    query = models.Product.delete().where(models.Product.id == product_id).execute()
    print('Removed all instances of ' + str(query_to_get_product.name) + ' from the database.')
    print('')
    sleep(3.00)

# Let's replenish the database. 
def update_stock(product_id, new_quantity):
    query_to_get_product = models.Product.get(models.Product.id == product_id)
    query = models.Product.update(quantity_left_in_stock = new_quantity).where(models.Product.id == product_id).execute()
    print('Updating the database with the new number of product ' + str(query_to_get_product.name) + '.')
    sleep(1.00)
    print('New number of product ' + str(query_to_get_product.name) + ' in the database is ' + str(new_quantity))

# Handle a purchase between a buyer and a seller for a given product
def purchase_product(product_id, buyer_id, quantity):
    print('')
    print('Purchasing a product. One sec please.')
    sleep(3.00)
    buyer = models.User.get(models.User.id == buyer_id)
    product = models.Product.get(models.Product.id == product_id)
    price_per_product = product.price_per_unit
    
    total_price = int(quantity) * price_per_product

    models.Transaction.create(user=buyer_id, product=product_id, number_of_products_purchased = quantity, total = total_price)

    new_product_quantity = product.quantity_left_in_stock - quantity

    update_stock(product_id, new_product_quantity)

connect_to_database()
create_tables()
fill_database_with_test_data()
search('boe')
list_user_products(1)
list_products_per_tag(1)
add_product_to_catalog(1, 'Boek')
remove_product(5)
update_stock(4, 20)
purchase_product(4, 2, 5)