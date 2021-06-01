# Models go here    
from peewee import *
from playhouse.sqliteq import SqliteQueueDatabase
from playhouse.sqlite_ext import *
import peewee

db = peewee.SqliteDatabase("betsy_database.db")
  
class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    name = TextField()
    address = JSONField()
    billing_information = JSONField()

class Product(BaseModel):
    name = CharField()
    description = TextField()
    price_per_unit = DecimalField(auto_round = True)
    quantity_left_in_stock = IntegerField()

class Tag(BaseModel):
    tag = CharField(unique = True) 

class Product_Tag(BaseModel):
    product = ForeignKeyField(Product)
    tag = ForeignKeyField(Tag)

class Product_User(BaseModel):
    user = ForeignKeyField(User)
    product = ForeignKeyField(Product)
    
class Transaction(BaseModel):
    user = ForeignKeyField(User)
    product = ForeignKeyField(Product)
    number_of_products_purchased = IntegerField() 
    total = FloatField()       